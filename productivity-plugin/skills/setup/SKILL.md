---
name: setup
description: "Run the first-time onboarding flow for the Ripple Ventures Cowork plugin marketplace. Walks the user through 8 phases: role and industry discovery, plugin recommendations, skill explanations, MCP and connector setup, tech stack capture, template and example collection, calibration mechanism explanation, and a first-skill recommendation. Writes calibration entries to each installed skill so they personalize from day one. Use whenever the user just installed the plugins, says 'set up', 'onboarding', 'first run', 'configure plugin', 'walk me through this', 'how do I start', or asks how to get started."
---

# Setup — Onboarding Flow

The first-time onboarding for the Cowork plugin marketplace. Runs through 8 phases and produces a fully calibrated environment so the skills work for the user from day one.

Run after install. Re-run anytime the user's role, tech stack, or team changes.

## Goals

By the end of this flow:

1. The user understands which plugins are installed and what they do
2. The user has connected the right MCPs / connectors for their tech stack
3. The skills have enough calibration to produce useful output on the first invocation
4. The user knows how calibration works and how to feed examples / templates to the skills

## Tone

- Conversational, not bureaucratic. This is supposed to feel like onboarding a new teammate, not filling out a form.
- Don't dump all questions at once. Use AskUserQuestion in groups of 2-5 questions per form. Walk through the phases one at a time.
- Save progressively — if the user bails mid-flow, what's been answered is preserved.
- Always offer skip. Some answers can come later.

---

## Phase 1: Role, industry, and company

Open with a brief welcome, then ask:

> "Welcome. I'll walk you through setting up the plugins so they're customized to your work. About 10-15 minutes. We can stop and pick up any time.
>
> First, three questions about you:"

Use AskUserQuestion:

```
1. Role:
   - Venture capital investor (early-stage)
   - Venture capital investor (growth-stage / multi-stage)
   - Private equity investor (buyout)
   - Private equity investor (growth)
   - Fund of funds / LP
   - Investment banking analyst or associate
   - Equity research analyst
   - Corporate development / M&A
   - Family office investor
   - Operating company executive (founder, CFO, COO)
   - Financial advisor / wealth management
   - Other (free text)

2. Industry / sector focus:
   - SaaS / B2B software
   - Consumer / B2C
   - Fintech
   - Healthcare / biotech
   - Climate / energy
   - Industrials / manufacturing
   - Multi-sector / generalist
   - Other (free text)

3. Company / firm:
   - [Free text — fund name, firm, or "independent"]
```

Save the answers to `productivity-plugin/skills/setup/calibration/profile.md`. The role drives plugin recommendations and the "why it matters for you" framing in news-brief and email-draft.

## Phase 2: Plugin recommendations

Based on the role from Phase 1, recommend which plugins the user should install. Show what each plugin does in a scannable form.

### Recommendations by role

| Role | Recommended plugins |
|---|---|
| VC investor (any stage) | productivity + deals + microsoft-office |
| PE investor (buyout / growth) | productivity + deals + microsoft-office |
| Fund of funds / LP | productivity + deals + microsoft-office (heavy use of `valuation-reviewer`) |
| Investment banking analyst | productivity + deals + microsoft-office (heavy use of `pitch-deck-creator`) |
| Equity research analyst | productivity + deals + microsoft-office (heavy use of `earnings-reviewer`) |
| Corporate development | productivity + deals + microsoft-office |
| Family office | productivity + deals + microsoft-office |
| Operating company exec | productivity only (deals plugins are over-built for this use case) |
| Financial advisor | productivity (deals plugin if doing investment due diligence on behalf of clients) |

### What each plugin does

Show this once the recommendations are set:

> **`productivity-plugin`** (5 skills)
>
> Day-to-day knowledge work — anyone uses these regardless of role:
> - `weekly-review` — gathers calendar / email / chat items, renders an HTML overview of the week, drafts the team recap email
> - `email-draft` — drafts emails in your voice
> - `meeting-prep` — research one person or many before a meeting
> - `news-brief` — daily curated news, "why it matters for you" customized to your role
> - `setup` — what you're running right now

> **`deals-plugin`** (24 skills, organized in three layers)
>
> Investment / banking workflows. Three flavors:
> - **Orchestration skills** — entry points that chain other skills. Examples: `pitch-deck-creator` chains comps + LBO + DCF + deck QC. `model-builder` chains the right model skill plus audit. `earnings-reviewer` chains read + update + audit + note draft.
> - **Custom workflow skills** — `investment-memo-drafter` (IC memo), `vc-general-counsel` (term sheets, SAFEs, side letters)
> - **Component skills** — comps, DCF, LBO, sector overview, etc., adapted from Anthropic's financial-services repo

> **`microsoft-office-plugin`** (3 skills + slash commands + scripts)
>
> Foundation for producing Excel and PowerPoint files. Required by the deals plugin's modeling and deck workflows. Includes `/audit`, `/format-xls`, `/build-deck`, `/check-deck` slash commands.

Ask:

> "Want to install the recommended plugins now, or pick a subset?"

If a plugin needs installing that the user doesn't have, give them the install command and pause for them to confirm before continuing. If they already have everything, move to Phase 3.

## Phase 3: Skill explanations

Walk through what each installed skill does, with trigger phrases. Group by plugin. Don't dump all 30+ skills at once — group sensibly.

For productivity:

> "In the productivity plugin, you have 5 skills. Here's what triggers each one:
> - `weekly-review`: 'plan my week', 'weekly review', 'what's my week', 'weekly email'
> - `email-draft`: 'draft an email', 'help me respond', 'write a follow-up'
> - `meeting-prep`: 'background check on X', 'who's coming to this event', 'research these people'
> - `news-brief`: 'morning brief', 'daily news', 'catch me up on today'
> - `setup`: this — re-run anytime your stack changes"

For deals (if installed), show the orchestration skills first since they're the entry points:

> "In the deals plugin, the 5 high-level skills are:
> - `pitch-deck-creator`: end-to-end IB pitch deck
> - `market-researcher`: sector or thematic primer
> - `model-builder`: DCF / LBO / 3-statement / comps from scratch
> - `earnings-reviewer`: process an earnings event end-to-end
> - `valuation-reviewer`: quarter-end portfolio valuation review
>
> Plus `investment-memo-drafter` for IC memos and `vc-general-counsel` for term sheet review.
>
> Component skills (comps-analysis, dcf-model, lbo-model, sector-overview, earnings-analysis, etc.) can also be invoked directly if you want, but the orchestration skills are usually the way in."

For microsoft-office, briefly note the slash commands.

## Phase 4: MCP / connector setup

This is the most important part. The skills need access to the user's tools to work.

Ask which connectors the user has installed in Cowork. Use AskUserQuestion. For each, if the answer is "not installed, but I want to," walk them through installing it via Cowork's connector marketplace.

```
1. Calendar:
   - Google Calendar (already connected)
   - Outlook Calendar (already connected)
   - Apple Calendar
   - Need to install — which one?
   - Don't use a calendar tool

2. Email:
   - Gmail (already connected)
   - Outlook (already connected)
   - Need to install — which one?
   - Don't use email through Cowork

3. Chat / team comms:
   - Slack (already connected)
   - Microsoft Teams (already connected)
   - Discord
   - Need to install — which one?
   - Don't use chat through Cowork

4. CRM:
   - Attio (already connected)
   - HubSpot (already connected)
   - Salesforce (already connected)
   - Notion as CRM
   - Airtable as CRM
   - Need to install — which one?
   - No CRM

5. Meeting notes:
   - Granola (already connected)
   - Fireflies
   - Otter
   - Notion
   - Obsidian
   - Need to install — which one?
   - No meeting notes tool

6. Knowledge base / wiki:
   - Notion (already connected)
   - Confluence
   - Obsidian
   - Need to install — which one?
   - No knowledge base
```

For each "need to install" answer, surface the install path:

> "To install [X], open Cowork → Settings → Connectors → search for [X] → Install. Come back here once it's connected and tell me you're ready."

Wait for the user to confirm before continuing. Don't try to install connectors programmatically — they require user-facing OAuth.

Save tech stack answers to `productivity-plugin/skills/setup/calibration/profile.md` (append to Phase 1's profile).

Then propagate to per-skill calibration files:

- Write `productivity-plugin/skills/weekly-review/calibration/setup.md` with the tools chosen
- Write `productivity-plugin/skills/meeting-prep/calibration/setup.md` (if installed)
- Other skills that need tool context

## Phase 5: Tech stack and team

Ask team-related questions:

```
1. Team size:
   - Just me
   - 2-5
   - 5-15
   - 15+

2. Who's on your team? (Optional — used for the weekly recap email recipient list)
   - [Free text — names + emails, one per line]

3. What format does your weekly recap email use? (subject template)
   - "Recap W[X] [Month] [Year]"
   - "Weekly update — [date]"
   - Other (free text)
   - Skip this one
```

Save to `productivity-plugin/skills/weekly-review/calibration/setup.md`.

## Phase 6: Templates and examples

This phase is what unlocks calibration. Different skills want different inputs.

For each installed skill, ask the skill-specific deep questions:

### `email-draft`

> "Email-draft works best when grounded in your actual writing. Two questions:
>
> 1. Who do you email regularly? Group them by relationship type (e.g., 'co-investors', 'internal team', 'founders we're talking to', 'LPs', 'service providers'). Free text — just list the groups.
>
> 2. Want to share 3-5 example emails right now? Paste them as plain text, one per message. I'll save them as canonical voice references and the skill will match your tone. Or skip and I'll learn from your edits as you use the skill."

Save the recipient groups to `productivity-plugin/skills/email-draft/references/voice-guide.md`.
Save examples to `productivity-plugin/skills/email-draft/references/examples/example-1.md`, `example-2.md`, etc.

### `news-brief`

> "News-brief needs to know what to read and what you care about:
>
> 1. Which sources should I pull from? (e.g., FT, Bloomberg, The Information, Stratechery, Axios, TechCrunch, Reuters)
> 2. Which categories should I organize stories into? (e.g., AI/ML, Tech & Markets, Global Politics, Climate)
> 3. Format preference: markdown in chat / HTML file / email-ready text"

Save to `productivity-plugin/skills/news-brief/references/profile.md`.

### `investment-memo-drafter` (if deals plugin installed)

> "IC memos work best when they match your firm's template:
>
> 1. Do you have a memo template? Paste it (section headers + length per section + any firm-specific sections like 'Sourcing Fit' or 'Pro-rata Plan'). Or skip and I'll use a generic seed/Series A template as the starting point.
>
> 2. Want to share 1-2 example memos right now? Paste them as plain text. They become canonical voice references."

Save template to `deals-plugin/skills/investment-memo-drafter/references/template.md`.
Save examples to `deals-plugin/skills/investment-memo-drafter/references/sample-memos/`.

### `vc-general-counsel` (if deals plugin installed)

> "VC general counsel is most useful when grounded in your firm's actual closed deals rather than abstract framework defaults.
>
> Want to share 2-5 precedent docs from past deals? Useful: a recent term sheet, a SAFE you've signed or led, a side letter showing your standard pro-rata / info rights / board observer / ROFR / co-sale / MFN provisions, a closing book index. Strip counterparty info if you want.
>
> Or skip and I'll work from generic CVCA / NVCA / YC standards. Framework defaults are stricter than what most funds actually accept, so calibrating to your precedent makes the analysis sharper."

Save to `deals-plugin/skills/vc-general-counsel/references/{descriptive-name}.md`.

## Phase 7: How calibration works

Explain the learning mechanism so the user understands what to do when a skill misses something.

> "Quick explainer on how the skills get better over time.
>
> Each skill has two folders alongside its SKILL.md:
>
> - **`references/`** — files the skill consults on every run. Templates, examples, your voice guide. We just populated some of these in Phase 6. You can add more anytime by dropping files in.
>
> - **`calibration/`** — log of corrections. After a skill produces output, if it missed something or got something wrong, you can ask me to log a calibration entry. Future runs read recent entries (newest first) and apply the lessons.
>
> The pattern: when a skill output isn't right, tell me what was wrong and I'll save it to `calibration/YYYY-MM-DD-short-slug.md` with the context, what the skill produced, what was wrong, and a one-line lesson. Next time the skill runs, it picks up the lesson.
>
> All this lives on your machine. None of it travels with the plugin source — when you redistribute an updated plugin to coworkers, your calibration stays with you and they start fresh."

Show the file paths so users know where to look:

```
productivity-plugin/skills/<skill-name>/references/
productivity-plugin/skills/<skill-name>/calibration/
deals-plugin/skills/<skill-name>/references/
deals-plugin/skills/<skill-name>/calibration/
microsoft-office-plugin/skills/<skill-name>/references/
microsoft-office-plugin/skills/<skill-name>/calibration/
```

## Phase 8: Try a skill

End on action. Recommend a first skill to try based on role and what's installed.

For VC / PE / IB roles with deals + productivity installed:

> "Setup done. Three good first skills to try:
>
> - **`weekly-review`** — say 'plan my week' to see the calendar overview + task list rendered as HTML
> - **`news-brief`** — say 'morning brief' to get your first daily news rundown
> - **`vc-general-counsel`** — paste a term sheet and say 'review this term sheet, is this market?'
>
> Pick one. The skills will reference what we set up here and give you customized output."

For productivity-only users:

> "Setup done. Try `weekly-review` first — say 'plan my week'. The HTML overview pulls from the tools we connected, and the tasks bucket your week's open items so you can see what's actually on your plate."

## Re-running setup

Setup is idempotent. Re-run anytime:

- The user's tech stack changes (e.g., switched from Slack to Teams)
- A team member joins or leaves
- The user's role evolves
- New plugins get installed
- Calibration feels stale and needs a refresh

When re-running, read the existing values from each calibration file and offer "Keep, change, or skip?" for each phase. Don't blow away existing files without asking.

## Rules

- **Never auto-install connectors.** OAuth flows require the user. Always show the install path and wait for confirmation.
- **Never overwrite calibration without asking.** If the file exists, show current value and ask first.
- **Save progressively.** If the user bails after Phase 3, Phases 1-3 are saved. Don't lose progress.
- **Don't ask too much in one form.** AskUserQuestion in groups of 2-5 questions max. Break across phases.
- **Match the user's pace.** Some users want to power through; others want to do it over a few sessions. Honor stop / pick-up-later signals.
- **Be honest about scope.** If the user asks "is this all I need to do?" — yes. After setup the skills work. They get sharper with use, but they're not blocked on more setup.

## Troubleshooting

**User has only one plugin installed (e.g., productivity only).**
Cause: They didn't install all recommended plugins.
Solution: Skip the questions for plugins they don't have. Note in the chat that they can re-run setup if they install more later.

**User picks a role that maps to "no plugins recommended" (e.g., a non-target role).**
Cause: Edge case — role doesn't fit the typical user profile.
Solution: Recommend productivity by default. Note that deals plugins are designed for investment / banking work and may not be useful for their role.

**MCP connector doesn't exist for the user's tool.**
Cause: User uses a tool not yet supported by Cowork (e.g., a niche CRM).
Solution: Note the gap. Skip that source. The skills will work without it but will mention "[tool] not connected" in outputs that would have used it.

**User skips all examples in Phase 6.**
Cause: Examples not at hand or user wants to onboard fast.
Solution: Save the answers from earlier phases and finish setup. Note that skills will ask for examples on first invocation as a fallback.

**Calibration files already exist (re-run scenario).**
Cause: User is updating their setup.
Solution: For each file, show current value and ask "Keep, change, or skip?" Don't silently overwrite.

## References

- **`references/`** — Optional. If you want a customized onboarding script (different role categories, different question ordering, role-specific deep questions), save it here.
- **`calibration/`** — Past setup runs and feedback on the onboarding flow itself.

## Summary of files this skill writes

| Path | Purpose |
|---|---|
| `productivity-plugin/skills/setup/calibration/profile.md` | User's role, industry, company, team |
| `productivity-plugin/skills/<skill>/calibration/setup.md` | Per-skill tech stack + tool config |
| `productivity-plugin/skills/email-draft/references/voice-guide.md` | Recipient groups and email types |
| `productivity-plugin/skills/email-draft/references/examples/*.md` | Example emails for voice grounding |
| `productivity-plugin/skills/news-brief/references/profile.md` | Sources, categories, format preferences |
| `deals-plugin/skills/investment-memo-drafter/references/template.md` | Firm's memo template |
| `deals-plugin/skills/investment-memo-drafter/references/sample-memos/*.md` | Example IC memos |
| `deals-plugin/skills/vc-general-counsel/references/*.md` | Precedent docs (term sheets, SAFEs, side letters) |
