# Productivity Plugin

5 skills for the day-to-day work of a knowledge worker, venture investor, or operator. Install via Cowork to get all of them at once.

## First-run setup

Before anything else, run the `setup` skill. It asks about your tech stack (calendar, email, chat, CRM, meeting notes), industry, and role, then writes the answers to each other skill's calibration so they personalize from day one.

Without setup, the skills still work but each one will ask you their own setup questions individually. Running `setup` once up front saves the back-and-forth.

## Skills

The order below is roughly the order you'd encounter them in a normal week — start of the week (`weekly-review`), throughout the week (`email-draft`, `news-brief`, `meeting-prep`).

### 0. `setup` — run once after install

Walks the user through onboarding: tech stack, industry, role, team. Writes calibration entries for the other skills so they personalize from day one.

**Trigger phrases:** "set up", "onboarding", "first run", "configure plugin", "set this up"

Re-run anytime your tech stack changes (e.g., switched from Slack to Teams).

### 1. `weekly-review` — start of the week

Gathers work items from across your tools and renders an interactive HTML overview to plan the week.

**What it does:**

- Pulls events from your calendar (next Mon–Sun)
- Scans email, chat, and meeting notes for unfinished tasks and commitments
- Classifies tasks into 6 default buckets (LP, Portfolio Support, Deals/Investments, Fund Operations, Events, Software). Buckets are customizable in `references/task-buckets.md` if your role looks different.
- Renders a self-contained HTML file: week grid (in-person + virtual) + grouped task list with checkboxes
- After you review, drafts the weekly team recap email and creates a draft in your email tool (you send manually)

**Trigger phrases:** "weekly review", "what's my week", "weekly email", "plan my week"

### 2. `email-draft` — composing email throughout the week

Drafts emails in your voice — replies, cold outreach, follow-ups, intros, declines.

**What it does:**

- Reads your recipient context (who they are, prior thread)
- Drafts in your voice using examples from `references/` and patterns from `calibration/`
- Offers iterations ("punchier", "more formal", "shorter")

**First-run setup:** asks who you email regularly (grouped by relationship type), what types of emails you send, and ideally 3-5 example emails to learn from.

**Trigger phrases:** "draft an email", "help me respond", "write a reply", "follow up with X"

### 3. `meeting-prep` — before any 1:1, event, or list of intros

Research a person before meeting them. Single-person → chat brief. Multi-person list → sorted table.

**What it does:**

- **Single person:** pulls past interaction from CRM / email / chat / meeting notes; researches recent activity on the open web; suggests 2-3 specific conversation topics.
- **Multi-person list (e.g., event RSVP CSV):** same research per person, plus categorization by relevance (Talent / Founder / LP / Co-investor / Partner / Community), Priority (H/M/L), and CRM membership. Outputs as markdown table or HTML file.

**Replaces:** the older separate `background-check` and `scrape` skills — merged into one.

**Trigger phrases:** "background check on X", "research this person", "I'm meeting X tomorrow", "who's coming to this event", "research these people"

### 4. `news-brief` — morning catch-up

Daily curated news brief from your chosen sources, categorized by topic.

**What it does:**

- Pulls top stories from each source you've configured
- Organizes into your chosen categories (Tech, Markets, Politics, etc.)
- For each story: source, title, working URL, one-line summary, one-line "why it matters for you" customized to your industry and role
- Output format you pick: markdown in chat, HTML file, or email-ready text

**First-run setup:** asks for sources, categories, your industry, your role, and format preferences.

**Trigger phrases:** "morning brief", "daily news", "what's new today", "catch me up", "today's headlines"

**Pairs well with `schedule`** — automate the brief to run every weekday at 6am.

## How they work together

A representative week:

- **Day 1 after install:** Run `setup` to onboard.
- **Monday morning:** Run `weekly-review` to plan the week. Review the HTML, check off completed items, approve the team recap email.
- **Throughout the week:** `email-draft` for replies. `news-brief` daily (or scheduled). `meeting-prep` before any 1:1 or event you don't already know the people at.
- **Friday evening:** Re-run `weekly-review` if you want a retrospective view (the same skill works for "this week's tasks" and "what got done").

## Calibration

All skills improve over time as you use them. When a skill misses something or you edit a draft, log a calibration entry — the next run reads it and applies the lesson.

Calibration entries live in each skill's `calibration/` folder on your local machine. They never travel with the plugin source, so updating the plugin doesn't wipe your personalization.

## What's not in this plugin

- Anything deal-specific (memos, term sheets, valuation models) — see `deals-plugin/` for those.
- Excel / PowerPoint foundation skills — see `microsoft-office-plugin/`.
