# Cowork Plugin Package — Productivity, Deals, MS Office

A Cowork plugin marketplace built by the **Ripple Ventures Team**, with three plugins for knowledge workers, venture investors, and analysts. Install one, two, or all three depending on what you do.

> [!IMPORTANT]
> Many of the deal and Office skills in this package are adapted from Anthropic's public [`financial-services`](https://github.com/anthropics/financial-services) repository. We've added our own productivity skills, two custom deal skills (`investment-memo-drafter`, `vc-general-counsel`), five orchestration skills, and a setup flow on top of that foundation. See the per-plugin READMEs for the exact list of what's custom vs. adapted.
>
> **All logins, personal data, and individual calibration have been removed from this package.** When you install, the skills won't have your team's emails, your CRM, your firm's term sheet templates, or your voice. You'll need to run the `setup` skill once after install (and answer first-run prompts as the skills load) to get full functionality. This typically takes 5–10 minutes.

## Install via the marketplace

This package is structured as a Cowork plugin marketplace. Add it once and you can install any of the three plugins from inside Cowork:

```bash
# Add the marketplace (point at this folder, or a Git URL once it's hosted)
claude plugin marketplace add /path/to/ripple-ventures-claude-package

# Install plugins (any combination)
claude plugin install productivity@ripple-ventures-cowork-plugins
claude plugin install deals@ripple-ventures-cowork-plugins
claude plugin install microsoft-office@ripple-ventures-cowork-plugins
```

Or install a single plugin without adding the marketplace:

```bash
# Via Cowork: Settings → Plugins → Install plugin → point at productivity-plugin/ (or another)
# Or zip and share:
cd productivity-plugin && zip -r /tmp/productivity.plugin . -x "*.DS_Store"
```

## What's in this repo

```
.
├── README.md                    ← you are here
├── CLAUDE.md                    ← context file for Claude when reading this repo
├── LICENSE                      ← MIT
├── .claude-plugin/
│   └── marketplace.json         ← marketplace manifest registering all 3 plugins
├── productivity-plugin/         ← daily-driver workflows for any knowledge worker
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   ├── .mcp.json                ← MCP server declarations (empty by default)
│   ├── hooks/hooks.json         ← event hooks (empty by default)
│   └── skills/                  ← setup, email-draft, weekly-review, meeting-prep, news-brief
├── deals-plugin/                ← deal evaluation and execution workflows (VC + IB)
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   ├── .mcp.json
│   ├── hooks/hooks.json
│   └── skills/                  ← orchestration + custom workflow + Anthropic workflow skills
├── microsoft-office-plugin/     ← foundation Excel + PowerPoint skills (deals depends on this)
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   ├── .mcp.json
│   ├── hooks/hooks.json
│   ├── skills/                  ← xlsx-author, pptx-author, audit-xls
│   ├── commands/                ← /audit, /format-xls, /build-deck, /check-deck slash commands
│   ├── scripts/                 ← validate_xls.py, check_deck.py, extract_named_ranges.py, etc.
│   └── examples/                ← example reference structures (3-statement, pitch deck, color coding)
└── scripts/                     ← repo-level tooling
    ├── README.md
    ├── check.py                 ← lint marketplace + every plugin
    ├── package.sh               ← zip every plugin into a .plugin file
    └── sync-anthropic.sh        ← pull skill updates from anthropics/financial-services
```

Run `python3 scripts/check.py` before committing or packaging.

## Three plugins

### `productivity-plugin/`

Day-to-day knowledge work. The kind of stuff anyone uses every week regardless of role.

**Skills:**

- `setup` — first-run onboarding flow. Asks about your tech stack (calendar, email, chat, CRM, meeting notes), industry, role. Writes answers to each other skill's calibration so they personalize from day one. **Run this before anything else.**
- `email-draft` — drafts emails in your voice. First-run setup captures recipient groups (co-investors, internal team, founders, customers, partners) and email types. Calibrates as you edit drafts.
- `weekly-review` — gathers work items from calendar / email / chat / meeting notes; renders an interactive HTML week grid with grouped task list; drafts the weekly team email after approval.
- `meeting-prep` — research one person (chat brief) or many (sorted markdown / HTML table). Pulls past interaction history from CRM / email / chat / meeting notes before going to the open web. Categorizes lists by relevance.
- `news-brief` — daily curated news brief from sources you pick, organized by category, with a one-line "why it matters for you" customized to your industry and role.

**Source:** All five skills are custom-built by the Ripple Ventures Team for general productivity workflows.

### `deals-plugin/`

Anything to do with evaluating, structuring, or executing a venture deal.

**Three skill flavors:**

**Orchestration skills (the high-level entry points):** `pitch-deck-creator`, `market-researcher`, `model-builder`, `earnings-reviewer`, `valuation-reviewer` — each chains several component skills together so you ask for a deliverable and the orchestration handles sequencing.

**Custom workflow skills (Ripple Ventures Team):**

- `investment-memo-drafter` — IC memo from a pitch deck, founder calls, and external research. Adapts to your firm's template.
- `vc-general-counsel` — in-house counsel voice for term sheets, SAFEs, side letters. Traffic-light review. Grounded in your firm's actual closed-deal precedent.

**Anthropic workflow skills** (sourced from [`anthropics/financial-services`](https://github.com/anthropics/financial-services)):

`competitive-analysis`, `comps-analysis`, `idea-generation`, `sector-overview`, `earnings-analysis`, `earnings-preview`, `model-update`, `morning-note`, `3-statement-model`, `dcf-model`, `lbo-model`, `ic-memo`, `portfolio-monitoring`, `returns-analysis`, `pitch-deck`, `deck-refresh`, `ib-check-deck`

### `microsoft-office-plugin/`

Foundation skills for producing Excel and PowerPoint files. Used by most deals skills under the hood. **If you install `deals-plugin`, install this too.**

**Skills:** `xlsx-author`, `pptx-author`, `audit-xls` — all sourced from [`anthropics/financial-services`](https://github.com/anthropics/financial-services).

**Plus:**

- `commands/` — 4 slash commands (`/audit`, `/format-xls`, `/build-deck`, `/check-deck`)
- `scripts/` — 4 Python utilities for deterministic Excel/PowerPoint QC (`validate_xls.py`, `check_deck.py`, `extract_named_ranges.py`, `validate_color_coding.py`)
- `examples/` — reference structures for 3-statement models, IB pitch decks, and the institutional color-coding standard

## Skills overview

### Productivity plugin (5 skills, ordered by typical use)

| Order | Skill | What it does | Setup needed |
|---|---|---|---|
| 0 | `setup` | One-time onboarding — asks role / industry / tech stack, recommends plugins, walks through MCP connections, calibrates the other skills | Run once after install |
| 1 | `weekly-review` | Gathers calendar / email / chat / meeting items, renders interactive HTML week grid + grouped task list, drafts team recap email | Tools + team email list |
| 2 | `email-draft` | Drafts emails in the user's voice (replies, intros, follow-ups, declines) | Recipient groups + email types + 3-5 example emails |
| 3 | `meeting-prep` | Single-person chat brief OR multi-person table; pulls past interaction from CRM / email / chat / notes before web research | None (uses connected tools) |
| 4 | `news-brief` | Daily curated news from chosen sources, "why it matters for you" customized to industry / role | Sources + categories + role |

### Deals plugin (24 active skills, organized by flavor)

| Type | Skills |
|---|---|
| **Orchestration** (entry points — chain other skills) | `pitch-deck-creator`, `market-researcher`, `model-builder`, `earnings-reviewer`, `valuation-reviewer` |
| **Custom workflow** (Ripple Ventures Team) | `investment-memo-drafter`, `vc-general-counsel` |
| **Anthropic workflow** (sourced from `anthropics/financial-services`) | `competitive-analysis`, `comps-analysis`, `idea-generation`, `sector-overview`, `earnings-analysis`, `earnings-preview`, `model-update`, `morning-note`, `3-statement-model`, `dcf-model`, `lbo-model`, `ic-memo`, `portfolio-monitoring`, `returns-analysis`, `pitch-deck`, `deck-refresh`, `ib-check-deck` |

### Microsoft Office plugin (3 skills + scaffolding)

| Component | Items |
|---|---|
| **Skills** | `xlsx-author`, `pptx-author`, `audit-xls` |
| **Slash commands** | `/audit`, `/format-xls`, `/build-deck`, `/check-deck` |
| **Scripts (Python)** | `validate_xls.py`, `extract_named_ranges.py`, `check_deck.py`, `validate_color_coding.py` |
| **Examples** | `example-three-statement-structure.md`, `example-pitch-deck-structure.md`, `example-color-coding.md` |

## How orchestration skills chain

The 5 skills in `deals-plugin` flagged as **orchestration** don't do work themselves — they sequence other skills end-to-end. When the user asks for a deliverable, the orchestration skill picks the right components and runs them in order.

| Orchestration skill | Trigger | Chain (in order) |
|---|---|---|
| `pitch-deck-creator` | "create a pitch deck for [target]" | `sector-overview` → `comps-analysis` → `lbo-model` → `dcf-model` → `3-statement-model` → `audit-xls` → football-field summary → `pitch-deck` → `ib-check-deck` |
| `market-researcher` | "sector primer on X" / "research the [sector] space" | `sector-overview` → `competitive-analysis` → `comps-analysis` → `idea-generation` → optional `pptx-author` |
| `model-builder` | "build a DCF on [company]" / "fresh LBO model" | (picks one) `dcf-model` OR `lbo-model` OR `3-statement-model` OR `comps-analysis` → `audit-xls` → standard sensitivity tables |
| `earnings-reviewer` | "[ticker] just reported, write it up" | optional `earnings-preview` → pull print + filings → `earnings-analysis` → `model-update` → `audit-xls` → variance table → `morning-note` |
| `valuation-reviewer` | "quarter-end valuations" / "NAV review" | ingest GP packages → `portfolio-monitoring` → `returns-analysis` → fund-level waterfall → optional `ic-memo` → `xlsx-author` for LP pack |

The component skills can also be invoked directly (e.g., "build a DCF" → `dcf-model` runs alone). Orchestration is the convenience layer.

The productivity-plugin's `setup` skill follows the same pattern but for first-run calibration: it walks the user through tech stack, role, plugin recommendations, MCP connections, and calibration setup, then writes config for each skill it detects installed so the user gets personalized output from day one.

## First time using these plugins (important)

Skills in this package don't ship with anyone's team data or voice. Two things make them work:

1. **`references/` folders** — pre-bundled with general-purpose templates and standards. The skill consults them on every run.
2. **`calibration/` folders** — empty by default. Populates as you use the skills and log corrections.

For the skills to actually feel like *your* tools, you need to feed them your context. The fastest way:

1. Install the plugins (start with productivity at minimum)
2. Run the `setup` skill once
3. It walks you through 8 phases over 10–15 minutes covering: role / industry / company → plugin recommendations → skill explanations → MCP / connector setup → tech stack → templates and examples → calibration mechanism → first skill to try
4. The setup writes calibration entries for each skill so they personalize from day one

If you skip `setup`, each individual skill will ask you its own setup questions on first invocation. That works too — `setup` just batches the questions so you do them once instead of one-at-a-time.

## How the skills learn

- **`references/`** holds reference material the skill consults on every run. Some references are populated during first-run setup; others come pre-bundled.
- **`calibration/`** holds entries logged when the skill misses something or when your edits reveal a pattern. Each entry is read on subsequent runs and the lessons get applied.

This means each user's skills personalize over time without any of their data leaking into the shared plugin source. Calibration is local to each machine — when you redistribute an updated plugin to coworkers, their existing calibration is left untouched.

## Privacy

- Skills are read-only by default. Any write action (sending an email, creating a CRM record, posting to chat) requires explicit user approval at run time.
- Personal data lives in each user's local `calibration/` and `references/` folders, never in the plugin source.
- No logins, API keys, or credentials are bundled. Each user connects their own tools through Cowork's connector setup.

## Reference and attribution

This package is built on top of Anthropic's [`financial-services`](https://github.com/anthropics/financial-services) reference repo, which is also MIT-licensed. The `cookbook/` directory in their repo has Managed Agent API templates for the same workflows if you want to deploy server-side via `/v1/agents` instead of through Cowork.

What's adapted vs. custom:

- **Adapted from Anthropic** (with calibration/references scaffolding added by us): `xlsx-author`, `pptx-author`, `audit-xls`, `competitive-analysis`, `comps-analysis`, `idea-generation`, `sector-overview`, `earnings-analysis`, `earnings-preview`, `model-update`, `morning-note`, `3-statement-model`, `dcf-model`, `lbo-model`, `ic-memo`, `portfolio-monitoring`, `returns-analysis`, `pitch-deck`, `deck-refresh`, `ib-check-deck`
- **Custom-built by Ripple Ventures Team**: `setup`, `email-draft`, `weekly-review`, `meeting-prep`, `news-brief`, `investment-memo-drafter`, `vc-general-counsel`, plus the 5 orchestration skills (`pitch-deck-creator`, `market-researcher`, `model-builder`, `earnings-reviewer`, `valuation-reviewer`) which we rewrote from Anthropic's agent definitions into Cowork-native skills

The microsoft-office-plugin's slash commands, Python scripts, and example reference docs are also custom additions on top of the foundation skills.

## License

MIT — see `LICENSE` file. Skills adapted from Anthropic's repo retain their original MIT license; the LICENSE file documents the dual attribution.

Nothing in this package constitutes investment, legal, tax, or accounting advice. The skills draft analyst work product (models, memos, research notes, emails, summaries) for review by a qualified professional — not final outputs. Every action that affects external systems (email send, CRM write, document publication) is staged for human sign-off.
