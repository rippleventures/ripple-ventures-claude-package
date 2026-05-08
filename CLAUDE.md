# Cowork Plugin Package

Three Cowork plugins for knowledge workers, venture investors, and analysts. This file is project context for Claude (and any other AI tool) reading the repo to do development work on the plugins themselves. End users don't need to read this — they install the plugins via Cowork.

## Repository structure

```
.
├── README.md                    User-facing intro to the package
├── CLAUDE.md                    This file — project context for Claude
├── productivity-plugin/         General-purpose productivity skills
├── deals-plugin/                Venture deal evaluation and execution skills
└── microsoft-office-plugin/     Foundation Office (Excel, PowerPoint) skills
```

Each plugin folder follows Anthropic's Cowork plugin convention:

```
<plugin-name>/
├── .claude-plugin/
│   └── plugin.json              Plugin manifest (name, version, description)
├── README.md                    User-facing description of the plugin
└── skills/
    └── <skill-name>/
        ├── SKILL.md             Required — name + description in YAML frontmatter, instructions in body
        ├── references/          Optional — files the skill consults on every run
        │   └── README.md
        └── calibration/         Optional — log of corrections / misses for self-improvement
            ├── README.md
            └── _template.md
```

## Plugins at a glance

| Plugin | Skills | Audience |
|---|---|---|
| productivity | `setup`, `weekly-review`, `email-draft`, `meeting-prep`, `news-brief` | Knowledge workers — install for general workflows |
| deals | 5 orchestration + 2 custom workflow + 17 from Anthropic | VCs, IB analysts, PE associates |
| microsoft-office | `xlsx-author`, `pptx-author`, `audit-xls` | Anyone producing Office files; deals plugin depends on this |

## Skill conventions used in this repo

### YAML frontmatter (required)

Every `SKILL.md` starts with:

```yaml
---
name: skill-name-in-kebab-case
description: "What it does + when to trigger. Includes specific phrases users would say. Mentions file types if relevant."
---
```

Description must be under 1024 characters, no XML tags, no `claude` or `anthropic` in the name.

### First-run setup pattern

Skills that need user-specific calibration (voice, tools, examples) follow this pattern:

1. **Step 0** in `SKILL.md` checks `references/` and `calibration/` for existing config
2. If missing, the skill asks the user a small set of setup questions
3. Saves answers to `references/<config-file>.md` (durable) or `calibration/setup.md` (per-instance)
4. On subsequent runs, reads the saved config — no re-prompt

The `setup` skill in productivity-plugin orchestrates these per-skill setups in one flow so the user runs it once after install instead of getting prompted by each skill individually.

### Calibration pattern

Skills improve over time as users correct them. After the skill produces output:

1. Skill asks once: "Want me to log a calibration entry?"
2. If yes, copy `calibration/_template.md`, fill in, save as `YYYY-MM-DD-short-slug.md`
3. On every subsequent run, the skill reads recent calibration entries (newest first) and applies the lessons

Calibration is local to each user's machine. It never travels with the plugin source.

### Orchestration skills

5 skills in `deals-plugin/` orchestrate other skills end-to-end: `pitch-deck-creator`, `market-researcher`, `model-builder`, `earnings-reviewer`, `valuation-reviewer`.

Each orchestration skill's `SKILL.md` has a "Skills this skill orchestrates" section at the bottom listing the component skills it invokes. When updating the orchestration skill or adding new component skills, keep this list in sync.

### Foundation skills

`microsoft-office-plugin/` contains foundation skills (`xlsx-author`, `pptx-author`, `audit-xls`) that other plugins depend on. These have no domain logic of their own — they're pure utilities for producing Office files.

When a deals-plugin skill calls `audit-xls` or `xlsx-author`, the user must have `microsoft-office-plugin` installed for it to resolve.

## Development conventions

### Editing a skill

1. Edit `<plugin>/skills/<skill>/SKILL.md` directly.
2. Keep YAML frontmatter intact (the `---` delimiters are required).
3. Keep the body under ~500 lines. If approaching the limit, move detail to `references/` and link to it.
4. After editing, update the README at the plugin root if the skill's behavior changed.

### Adding a new skill

1. Create `<plugin>/skills/<new-skill-name>/`.
2. Write `SKILL.md` with proper YAML frontmatter (name + description with trigger phrases).
3. Add `calibration/_template.md` and `calibration/README.md` if the skill should learn from corrections.
4. Add `references/README.md` describing what optional reference files the skill can consult.
5. Update the plugin's `README.md` to list the new skill.

### Adding a new plugin

1. Create `<new-plugin>/.claude-plugin/plugin.json` with `name`, `version`, `description`.
2. Create `<new-plugin>/README.md` describing the plugin's purpose, skills, and audience.
3. Add the plugin to the top-level `README.md` and this `CLAUDE.md`.

### Removing a skill

If the workspace allows file deletion, just remove the folder. If not (some sandboxed environments block delete operations):

1. Overwrite the `SKILL.md` with a deprecation note (no YAML frontmatter so it doesn't register).
2. Document the removal in the plugin's `README.md`.

This is what we did for the legacy `agents/` folders in `deals-plugin/` — the files are stubs with deprecation notes.

## Source attribution

This package draws from Anthropic's [financial-services reference repo](https://github.com/anthropics/financial-services).

Mappings to the original:

- **Custom skills (written here):** `email-draft`, `weekly-review`, `meeting-prep`, `news-brief`, `setup`, `investment-memo-drafter`, `vc-general-counsel`, plus the 5 orchestration skills (rewritten from Anthropic's agent definitions into Cowork-native skills)
- **Anthropic skills (bundled):** `xlsx-author`, `pptx-author`, `audit-xls`, `competitive-analysis`, `comps-analysis`, `idea-generation`, `sector-overview`, `earnings-analysis`, `earnings-preview`, `model-update`, `morning-note`, `3-statement-model`, `dcf-model`, `lbo-model`, `ic-memo`, `portfolio-monitoring`, `returns-analysis`, `pitch-deck`, `deck-refresh`, `ib-check-deck`

When updating Anthropic skills upstream, sync via:

```bash
SRC=~/Desktop/anthropic-finance-skills/plugins/agent-plugins
DST=~/Desktop/<your-package-folder>/deals-plugin/skills

# For each agent-plugin you want to sync from:
for skill in $SRC/<agent>/skills/*/; do
  cp -rn "$skill" "$DST/"  # -n: don't overwrite existing
done
```

## Onboarding the user

The `setup` skill in `productivity-plugin` handles user onboarding:

1. Detects which plugins are installed
2. Explains what's in each
3. Asks tech stack questions (calendar, email, chat, CRM, meeting notes)
4. Asks role/industry questions
5. For each installed skill, asks the skill-specific setup questions
6. Writes calibration entries so the skills personalize from day one

Users should run `setup` once after install. Re-run when their tech stack or role changes.

## Distribution

To package and share:

```bash
cd <plugin-folder> && zip -r /tmp/<plugin-name>.plugin . -x "*.DS_Store"
```

The resulting `.plugin` file installs in Cowork via the plugin install flow.

## Limitations to be aware of

- The Cowork workspace where this package was built blocks file deletion. Some folders (`deals-plugin/agents/`, `deals-plugin/skills/xlsx-author|pptx-author|audit-xls/`) contain deprecated stub files that couldn't be removed in-process. They're harmless (no YAML frontmatter, so they don't register), but you may want to delete them manually for cleanliness.
- Cowork's plugin loader expects `.md` files in `agents/` to have YAML frontmatter to register. The deprecation stubs in `deals-plugin/agents/` lack frontmatter, so they're ignored.
