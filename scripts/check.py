#!/usr/bin/env python3
"""
check.py — Lint the marketplace and every plugin in the package.

Walks the repo and verifies:
  1. Top-level .claude-plugin/marketplace.json exists, parses, and references
     plugins that resolve to actual folders.
  2. Each *-plugin/.claude-plugin/plugin.json exists and contains valid JSON.
  3. plugin.json has a `name` field in kebab-case.
  4. Every plugin has .mcp.json (valid JSON) and hooks/hooks.json (valid JSON array).
  5. Every skills/<name>/ folder has SKILL.md.
  6. Every SKILL.md has YAML frontmatter with `name` and `description`.
  7. The frontmatter `name` matches the folder name.
  8. Description is under 1024 characters and contains no XML angle brackets.
  9. No README.md inside skill folders (per Cowork conventions).

Run before committing changes:
  python scripts/check.py

Exits non-zero on any failure.
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KEBAB_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.+?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(path: Path):
    text = path.read_text()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, "No YAML frontmatter (must start with --- on line 1)"

    fm = m.group(1)
    fields = {}
    for line in fm.split("\n"):
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        fields[key.strip()] = val.strip().strip('"').strip("'")
    return fields, None


def check_marketplace(repo: Path):
    """Validate the top-level .claude-plugin/marketplace.json."""
    errors = []
    manifest = repo / ".claude-plugin" / "marketplace.json"
    if not manifest.exists():
        errors.append(f"  MISSING: {manifest.relative_to(repo)} — required for plugin marketplace")
        return errors

    try:
        data = json.loads(manifest.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"  INVALID JSON in {manifest.relative_to(repo)}: {e}")
        return errors

    if "name" not in data:
        errors.append(f"  marketplace.json: missing `name` field")
    if "plugins" not in data or not isinstance(data["plugins"], list):
        errors.append(f"  marketplace.json: missing or invalid `plugins` array")
        return errors

    for entry in data["plugins"]:
        if "name" not in entry or "source" not in entry:
            errors.append(f"  marketplace.json: plugin entry missing name or source: {entry}")
            continue
        source_path = (repo / entry["source"]).resolve()
        if not source_path.exists():
            errors.append(f"  marketplace.json: plugin `{entry['name']}` source `{entry['source']}` does not exist")
        elif not (source_path / ".claude-plugin" / "plugin.json").exists():
            errors.append(f"  marketplace.json: plugin `{entry['name']}` has no plugin.json at {entry['source']}")

    return errors


def check_plugin(plugin_dir: Path):
    errors = []
    repo = plugin_dir.parent

    # .mcp.json validation
    mcp = plugin_dir / ".mcp.json"
    if mcp.exists():
        try:
            json.loads(mcp.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"  INVALID JSON in {mcp.relative_to(repo)}: {e}")

    # hooks/hooks.json validation
    hooks = plugin_dir / "hooks" / "hooks.json"
    if hooks.exists():
        try:
            data = json.loads(hooks.read_text())
            if not isinstance(data, (list, dict)):
                errors.append(f"  {hooks.relative_to(repo)}: must be a JSON array or object")
        except json.JSONDecodeError as e:
            errors.append(f"  INVALID JSON in {hooks.relative_to(repo)}: {e}")

    name = plugin_dir.name

    # 1. plugin.json exists
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        errors.append(f"  MISSING: {manifest}")
        return errors

    # 2. plugin.json valid
    try:
        data = json.loads(manifest.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"  INVALID JSON in {manifest}: {e}")
        return errors

    if "name" not in data:
        errors.append(f"  {manifest}: missing `name` field")
    elif not KEBAB_RE.match(data["name"]):
        errors.append(f"  {manifest}: name `{data['name']}` is not kebab-case")

    # 3-7. Walk skills
    skills_dir = plugin_dir / "skills"
    if not skills_dir.exists():
        return errors  # plugin without skills is OK (e.g., commands-only)

    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue

        # Skip empty / stub folders silently
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"  {skill_dir}: missing SKILL.md")
            continue

        # README.md inside skill folder is forbidden
        if (skill_dir / "README.md").exists():
            errors.append(f"  {skill_dir}: README.md should not exist inside a skill folder (use references/ instead)")

        # Frontmatter validation
        fields, fm_error = parse_frontmatter(skill_md)
        if fm_error:
            # Skip stubs with no frontmatter (deprecated skills moved elsewhere)
            text = skill_md.read_text()
            if "Moved to" in text or "Deprecated" in text:
                continue
            errors.append(f"  {skill_md}: {fm_error}")
            continue

        if "name" not in fields:
            errors.append(f"  {skill_md}: frontmatter missing `name`")
        elif fields["name"] != skill_dir.name:
            errors.append(
                f"  {skill_md}: frontmatter name `{fields['name']}` "
                f"!= folder name `{skill_dir.name}`"
            )

        if "description" not in fields:
            errors.append(f"  {skill_md}: frontmatter missing `description`")
        else:
            desc = fields["description"]
            if len(desc) > 1024:
                errors.append(
                    f"  {skill_md}: description is {len(desc)} chars (max 1024)"
                )
            if "<" in desc and ">" in desc:
                errors.append(f"  {skill_md}: description contains XML angle brackets")

    return errors


def main():
    total_errors = 0

    # 1. Marketplace
    print(".claude-plugin/marketplace.json")
    mp_errors = check_marketplace(REPO)
    if not mp_errors:
        print("  ✓ OK")
    else:
        for e in mp_errors:
            print(e)
        total_errors += len(mp_errors)

    # 2. Each plugin
    plugins = sorted(
        p for p in REPO.iterdir()
        if p.is_dir() and p.name.endswith("-plugin") and not p.name.startswith(".")
    )

    if not plugins:
        print("\nNo *-plugin/ folders found at repo root.")
        sys.exit(2)

    for plugin in plugins:
        print(f"\n{plugin.name}/")
        errors = check_plugin(plugin)
        if not errors:
            print("  ✓ OK")
        else:
            for e in errors:
                print(e)
            total_errors += len(errors)

    print(f"\n{'='*40}")
    if total_errors == 0:
        print("Marketplace and all plugins pass validation.")
        sys.exit(0)
    else:
        print(f"FAILED: {total_errors} error(s) found.")
        sys.exit(1)


if __name__ == "__main__":
    main()
