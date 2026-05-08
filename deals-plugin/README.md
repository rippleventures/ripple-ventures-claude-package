# Deals Plugin

Skills for evaluating, structuring, and executing venture deals. Built on top of Anthropic's [financial-services reference repo](https://github.com/anthropics/financial-services) with custom additions and orchestration skills.

## Dependency: install `microsoft-office-plugin` alongside this one

Most deal skills produce Excel or PowerPoint files. The foundation skills that create those files (`xlsx-author`, `pptx-author`, `audit-xls`) live in `microsoft-office-plugin/` so they can be reused by other workflows. Install both plugins together for full functionality.

## How this plugin is structured

Everything is a skill — Cowork picks the right one based on what you ask for. Three flavors:

1. **Orchestration skills** — handle end-to-end workflows by coordinating other skills. Examples: `pitch-deck-creator`, `model-builder`, `market-researcher`. You ask for a deliverable; the orchestration skill sequences the right component skills in the right order.
2. **Workflow skills** — focused capabilities that handle one task on their own. Examples: `investment-memo-drafter`, `vc-general-counsel`, `earnings-analysis`.
3. **Foundation skills** — shared utilities used by other skills (Excel + PowerPoint authoring, audit checks). These live in `microsoft-office-plugin/`, not here.

## Orchestration skills (start here)

These are the high-level capabilities. Each chains several component skills together.

### `pitch-deck-creator`

End-to-end IB pitch deck. Given a target and strategic situation, pulls comps and precedents, builds DCF + LBO + 3-statement valuations, generates the football-field summary, populates the deck on the firm's template, and runs deck QC.

**Trigger phrases:** "create a pitch deck for [target]", "build a pitch on [name]", "first-draft pitch", "pitch deck on [target] exploring strategic alternatives"

**Orchestrates:** `sector-overview` · `comps-analysis` · `lbo-model` · `dcf-model` · `3-statement-model` · `audit-xls` · `pitch-deck` · `ib-check-deck` · `deck-refresh`

### `market-researcher`

Sector or thematic primer. Industry overview, competitive landscape, peer comps spread, ideas shortlist, packaged as a research note + optional slides.

**Trigger phrases:** "do a sector primer on X", "research the [sector] space", "thematic research", "what's interesting in [theme]"

**Orchestrates:** `sector-overview` · `competitive-analysis` · `comps-analysis` · `idea-generation` · `pptx-author`

### `model-builder`

Build DCF, LBO, 3-statement, or comps models from scratch. Pulls inputs, builds with formatting standards, audits, and applies sensitivity tables.

**Trigger phrases:** "build a DCF on [company]", "put together an LBO model", "fresh model on [company]", "comps spread on [sector]"

**Orchestrates:** `dcf-model` · `lbo-model` · `3-statement-model` · `comps-analysis` · `audit-xls`

### `earnings-reviewer`

Process an earnings event end-to-end. Reads call transcript and filings, updates the coverage model, drafts the post-earnings note.

**Trigger phrases:** "cover [company] earnings", "[ticker] just reported, write it up", "post-earnings note", "process Q[X] for [company]"

**Orchestrates:** `earnings-analysis` · `model-update` · `audit-xls` · `morning-note` · `earnings-preview`

### `valuation-reviewer`

Quarter-end portfolio valuation review. Ingests GP packages, runs the valuation template, computes NAV and waterfall, stages the LP reporting pack.

**Trigger phrases:** "quarter-end valuations", "NAV review", "LP report prep", "review portfolio marks"

**Orchestrates:** `portfolio-monitoring` · `returns-analysis` · `ic-memo` · `xlsx-author`

## Workflow skills (custom)

Standalone skills written for venture investors directly.

### `investment-memo-drafter`

Drafts an IC memo from a pitch deck, founder calls, and external research. Adapts to your firm's template via examples.

**First-run setup:** asks for your firm's memo template (paste once) and ideally 1-2 example memos.

**Trigger phrases:** "draft an IC memo", "memo this deal", "deal writeup on [company]", "investment memo"

### `vc-general-counsel`

In-house counsel voice for term sheets, SAFEs, side letters, closing books. Traffic-light review (RED / YELLOW / GREEN). Grounded in your firm's actual closed-deal precedent.

**First-run setup:** asks for 2-5 example precedent docs from past deals.

**Trigger phrases:** "review this term sheet", "is this market", "redline this SAFE", "draft a side letter"

## Workflow skills (from Anthropic's repo)

Each is bundled here so the deals plugin is self-contained for the analytical work. The Office foundation skills they use live in `microsoft-office-plugin/`.

#### Sourcing and screening

- **`competitive-analysis`** — competitor landscape and positioning
- **`comps-analysis`** — public comps with consistent metrics, outlier flags
- **`idea-generation`** — sector-driven idea shortlist
- **`sector-overview`** — industry overview, market position, why now

#### Earnings and ongoing diligence

- **`earnings-analysis`** — quarterly print analysis, surprises, guidance
- **`earnings-preview`** — pre-print expectations, key numbers to watch
- **`model-update`** — update the model after earnings
- **`morning-note`** — analyst note draft based on earnings + filings

#### Modeling

- **`3-statement-model`** — full integrated income statement / balance sheet / cash flow
- **`dcf-model`** — discounted cash flow valuation
- **`lbo-model`** — leveraged buyout model with sensitivity

#### Portfolio monitoring (LP / fund admin side)

- **`ic-memo`** — IC memo for an existing portfolio company
- **`portfolio-monitoring`** — quarterly portfolio update analysis
- **`returns-analysis`** — IRR / MOIC / DPI calculation and sensitivity tables

#### Pitch deck creation

- **`pitch-deck`** — populates IB pitch deck templates from source files
- **`deck-refresh`** — update an existing deck with new data
- **`ib-check-deck`** — QC pass on a finished deck

## How they work together

A typical deal lifecycle:

1. **Sourcing:** `market-researcher` for sector context. `competitive-analysis` and `idea-generation` to identify targets.
2. **Initial diligence:** `meeting-prep` from the productivity plugin for founder background.
3. **Deeper diligence:** `model-builder` for the financial picture (DCF / LBO / 3-statement).
4. **Memo:** `investment-memo-drafter` for the IC draft. Includes `[CHECK]` flags for the analyst to chase.
5. **Term sheet / closing:** `vc-general-counsel` for traffic-light review of incoming docs and drafting outgoing ones.
6. **Post-investment monitoring:** `valuation-reviewer` for quarterly LP-facing reports. `earnings-reviewer` if portfolio companies disclose publicly.
7. **Sponsor pitches / strategic-alternatives mandates:** `pitch-deck-creator` for end-to-end deck builds.

## Calibration

The custom skills (`investment-memo-drafter`, `vc-general-counsel`) and all 5 orchestration skills get better with use. Each has a `calibration/` folder where you log misses or framing mistakes — the next run applies the lessons.

The Anthropic-built workflow skills also have calibration patterns built in; check each skill's `references/` folder for what they consult.

## Note on the agents/ folder

You'll see a `deals-plugin/agents/` folder with deprecated stub files. Anthropic's original repo used these as agent definitions for their Managed Agents API deployment path. For Cowork, agents aren't the primary entry point — skills are — so we converted those agent definitions into the orchestration skills above. The deprecated stubs are kept only because the workspace doesn't allow file deletion. They have no functional effect on Cowork.

## What's not in this plugin

- General productivity work (`weekly-review`, `email-draft`, `meeting-prep`, `news-brief`) — see `productivity-plugin/`
- MS Office foundation skills (`xlsx-author`, `pptx-author`, `audit-xls`) — see `microsoft-office-plugin/`
- Operations / fund admin agents (`gl-reconciler`, `month-end-closer`, `statement-auditor`, `kyc-screener`) from Anthropic's repo — not bundled here, install separately if needed

## Reference

For the original Anthropic financial-services repo this plugin builds on, see https://github.com/anthropics/financial-services. Their `cookbook/` directory has Managed Agent API templates for the same workflows if you want to deploy server-side via `/v1/agents` instead of Cowork.
