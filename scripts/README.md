# Scripts

Repo-level tooling for validating, packaging, and syncing the plugins. Run from the repo root.

## `check.py`

Lint every plugin in the package.

```bash
python3 scripts/check.py
```

Walks each `*-plugin/` folder at the repo root and verifies:

- `.claude-plugin/plugin.json` exists and contains valid JSON
- `plugin.json` has a `name` field in kebab-case
- Every `skills/<name>/` folder has `SKILL.md`
- Every `SKILL.md` has YAML frontmatter with `name` and `description`
- The frontmatter `name` matches the folder name
- Description is under 1024 characters and contains no XML angle brackets
- No `README.md` inside skill folders (use `references/` instead)

Exits non-zero on any failure. Stub files (deprecated skills moved elsewhere) are skipped silently.

Run before committing changes or packaging.

## `package.sh`

Zip every `*-plugin/` folder into a `.plugin` file in `/tmp/`.

```bash
./scripts/package.sh                 # all plugins
./scripts/package.sh productivity    # one plugin (matched by prefix)
```

Runs `check.py` first; aborts if validation fails. Output filenames use the `name` from each plugin's `plugin.json` (e.g., `productivity.plugin`, `deals.plugin`, `microsoft-office.plugin`).

## `sync-anthropic.sh`

Pull updates to bundled Anthropic skills from a local clone of [`anthropics/financial-services`](https://github.com/anthropics/financial-services).

```bash
./scripts/sync-anthropic.sh /path/to/anthropic-financial-services
```

Walks the source repo's `plugins/agent-plugins/` and updates matching skill folders in `deals-plugin/skills/` and `microsoft-office-plugin/skills/`. Does NOT overwrite our custom skills (`vc-general-counsel`, `investment-memo-drafter`, the orchestration skills).

Use this when Anthropic publishes updates upstream and you want to pick up improvements to skills like `dcf-model`, `comps-analysis`, etc. without touching the custom skills you've written.

After syncing, always re-run `check.py`.

## Typical workflow

```bash
# After making changes:
python3 scripts/check.py

# When ready to share:
./scripts/package.sh

# Periodically:
./scripts/sync-anthropic.sh ~/Desktop/anthropic-financial-services
python3 scripts/check.py
```
