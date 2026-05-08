---
name: weekly-review
description: "Run a work-only weekly review: gather work items from the user's calendar, email, chat, and meeting-notes tools; render an interactive HTML overview with a calendar week grid (in-person + virtual meetings) and a grouped task list; then draft the weekly team email after user approval. Triggers on: weekly review, weekly summary, what's my week, weekly email, week overview, plan my week, what do I need to do this week."
---

# Weekly Review

Gather work items from the user's connected tools, render an interactive HTML overview, then draft the weekly team email after the user approves the open items. Personal items are never gathered or shown.

## Step 0: Check setup and calibration

Read these in order before doing anything:

1. **`calibration/setup.md`** — captures which tools the user uses and how to address them. If missing, run the setup flow below.
2. **`calibration/`** entries (newest first) — past misses, mis-classifications, edge cases.
3. **`references/task-buckets.md`** — the 6 task buckets and how to classify items.

### If `calibration/setup.md` is missing (first-time setup)

Pause and run the setup interview before gathering any data:

> "Before I run a weekly review, I need to know which tools to pull from. Quick questions:
>
> 1. **Calendar** — Google Calendar, Outlook, Apple, none?
> 2. **Email** — Gmail, Outlook, none?
> 3. **Chat / team comms** — Slack, Microsoft Teams, none?
> 4. **CRM** — Attio, HubSpot, Salesforce, Notion, none? (Optional — used for context on people you're meeting.)
> 5. **Meeting notes** — Granola, Fireflies, Otter, Notion, none?
> 6. **Who's on your team?** (Names + emails of people you'd email a weekly recap to.)
> 7. **What email goes to the team recap?** (e.g., 'Recap WX [Month] [Year]' or your own format.)"

Save the answers to `calibration/setup.md` using the template in `references/setup-template.md`. Subsequent runs read from there and skip the interview.

If the user declines to set up some tools, mark them as "skip" — those sources will be ignored.

## Step 1: Compute date range

Calculate:

- `WEEK_START` = upcoming Monday (YYYY-MM-DD)
- `WEEK_END` = upcoming Sunday (YYYY-MM-DD)
- `LOOKBACK_DATE` = today minus 14 days (YYYY-MM-DD)

The week grid uses `WEEK_START` to `WEEK_END`. The task gathering uses `LOOKBACK_DATE` to today.

## Step 2: Set up the task list

Use TaskCreate to create the checklist:

1. Gather calendar events
2. Gather email items
3. Gather chat items
4. Gather meeting-notes items
5. Classify and group items into the buckets
6. Build interactive HTML file
7. Open HTML for review
8. Draft weekly team email (after user approval)
9. Create email draft (after user approval)

Mark steps 1-4 as `in_progress` together when launching parallel searches. Mark each `completed` as results arrive. Steps 8-9 stay pending until the user explicitly approves.

## Step 3: Gather data (PARALLEL)

Launch ALL searches simultaneously using the user's connected tools as listed in `calibration/setup.md`.

### 3a. Calendar (primary source for the grid)

Use the user's calendar tool. Pull events for `WEEK_START` to `WEEK_END`. For each event extract: title, date, start/end, location (in-person vs virtual), attendees, description.

Classify each event into one of two grid rows:

- **In-person meetings**: physical address in location, OR title indicates in-person (office visit, coffee, lunch, dinner, summit, etc.)
- **Virtual meetings**: has a Zoom/Meet/conferenceUrl, OR is a remote 1:1 / sync without a physical location

**Drop these from the grid:**

- Self-created calendar blocks (Emails, Drive, Focus, Prep, Run-Through, time-blocked work without other attendees) — actionable work they represent is captured in tasks below
- Personal items (haircut, doctor, family, errands) — work-only skill
- OOO/holidays (note them but don't render)
- Declined events

Calendar is the PRIMARY source for the grid. Other sources supplement with tasks that aren't on the calendar.

If calendar is not connected: skip silently, rely on email calendar invites + meeting-notes tool.

### 3b. Email

Run these searches in parallel using the user's email tool:

1. Starred items after `LOOKBACK_DATE` — needs action
2. Unread items after `LOOKBACK_DATE`, excluding promotions/social
3. From the user (sent items) after `LOOKBACK_DATE` — promises made, drafts not sent
4. From each teammate (one search per email in `calibration/setup.md`) — assignments, forwards, CC'd items
5. Targeted keyword searches based on calibration history (e.g., "canva", "1-pager", "booking", "travel" — extend the list as patterns emerge)

For every actionable email, read the full message body. Snippets are not enough. Watch for:

- Comment notifications from collaborative tools (Canva, Figma, Notion) containing task assignments
- Draft emails not yet sent
- Travel bookings teammates have made but the user hasn't (compare who's booked vs. not)
- Calendar invites with descriptions containing prep instructions
- CC'd emails where teammates loop the user in on something needing follow-up

### 3c. Chat (Slack / Teams)

Look up the user's own user ID first (via the chat tool's profile API — don't hardcode IDs). Then run in parallel:

1. Messages from the user after `LOOKBACK_DATE` — commitments, "I'll do X"
2. Messages mentioning or DMing the user after `LOOKBACK_DATE` — things others asked of them
3. Messages with reactions in user DMs — reacted to but maybe not actioned
4. Keyword search after `LOOKBACK_DATE`: deadline, reminder, follow up, need to

PAGINATE: if any search returns a cursor, fetch page 2. 2-week lookbacks often blow past 20 results.

For each result, extract: what was the commitment or request, was it fulfilled (look for follow-up messages), who's involved, permalink.

### 3d. Meeting notes (Granola / Fireflies / etc.)

1. List meetings for `this_week` and `last_week`
2. For each, get notes/transcripts
3. Extract action items, follow-ups, commitments made during calls
4. Also run a semantic query for "action items and follow-ups from this week" for broader coverage

### 3e. Source attribution

For every item, capture:

- **Source type**: calendar / email / chat / meeting-notes
- **Source link**: permalink/URL from the tool result. Never construct or guess URLs.
- **Grid row** (for calendar events): `in-person` or `virtual`
- **Task group** (for non-calendar tasks): one of the 6 buckets in `references/task-buckets.md`

## Step 4: Classify items

### 4a. Week grid items

Calendar events for the week → grid, classified into in-person or virtual per Step 3a. Filter out self-created blocks, personal, declined, and OOO.

### 4b. Task groups

All non-calendar work items → one of the 6 task buckets defined in `references/task-buckets.md`. Don't invent new buckets.

When a task could fit two buckets, prefer the bucket that matches the primary stakeholder (see the conflict-resolution rules in the task-buckets reference).

### 4c. Deduplicate

If the same task appears in multiple sources (Slack message about an email thread), merge into one item. List all sources.

### 4d. Filter completed

Remove items clearly completed:

- Chat threads where the user confirmed completion
- Email threads with a sent reply that fulfilled the ask

Keep ambiguous items (no confirmation).

### 4e. Filter personal

Drop ANY item that looks personal regardless of source. If unsure whether work or personal, INCLUDE it — the user can uncheck.

## Step 5: Build interactive HTML

Generate a single self-contained HTML file at `outputs/weekly-review-{YYYY-MM-DD}.html`.

Read `references/html-design-system.md` for the design system (palette, layout rules, interaction model). Implement the layout exactly as specified there — don't improvise colors or fonts.

Layout summary (full spec in the reference):

- **Section 1**: Calendar week grid (Mon-Sun), two rows (in-person, virtual). Cards show item name + time + source badge only.
- **Section 2**: Tasks grouped by the 6 buckets in fixed order. Each task shows title, context, next step, source link.
- **Interactive**: checkboxes (checked = done), floating summary panel, copy-summary button.

Open the file in the default browser:

```bash
open outputs/weekly-review-{YYYY-MM-DD}.html
```

## Step 6: User review (APPROVAL GATE)

After opening, ask:

> "The weekly review is open in your browser. Review the grid and task list, check off anything that's already done, then let me know:
>
> 1. Any items to add, remove, or edit?
> 2. Ready to draft the weekly email with the open (unchecked) items?"

**DO NOT proceed until the user explicitly approves.**

## Step 7: Draft weekly team email

Using ONLY the unchecked (still-open) items, draft the email to the user's team (recipients from `calibration/setup.md`).

Read `references/email-format.md` for the exact format. Summary:

- Subject: `Recap W[X] [Month] [Year]`
- Sections in fixed order matching the task buckets (use only sections with content)
- Bold topic names, bulleted list of what got done, italicized "Next Step" only when there's a concrete one
- End with "Best, [Name]"
- No em dashes
- No tree/code-block formatting

Present a "Bucket B" review list separately — items the skill is unsure about including. Get user picks before finalizing.

Show the final draft in chat. Wait for explicit approval before any write action.

## Step 8: Create email draft (write action — APPROVAL REQUIRED)

Only after the user explicitly approves the final draft:

1. Create the email draft using the user's email tool
2. Confirm draft was created
3. The user sends manually

**Email creation is FORBIDDEN without explicit approval.** Never auto-send.

## Rules

- Parallelize ALL data gathering in Step 3. This is the most expensive step.
- Every source link must come from a tool result in this conversation. Don't construct or guess URLs.
- No filler, no sycophancy. Straight to the work.
- No em dashes.
- If a source returns no data, skip it silently. Don't pad with "no items found."
- When in doubt about whether something is done, INCLUDE it. Better to list a completed task than miss an open one.
- Break big tasks into their smallest actionable next step. "Plan Toronto Tech Week" becomes "Reply to [name] with finalized event details and collab proposal."
- Every action item must be concrete enough to start immediately.
- This skill is WORK-ONLY. Never gather, query, render, or include personal items.
- HTML file must be fully self-contained (inline CSS, inline JS, no external dependencies).
- Reads are automatic. Writes (email draft, calendar updates, etc.) are FORBIDDEN without explicit approval.

## Troubleshooting

**Calendar tool not connected.**
Cause: Setup skipped calendar, or auth expired.
Solution: Skip the grid silently. Rely on email calendar invites + meeting-notes for week-of context. Tell the user the grid will be sparse until calendar is connected.

**Chat search hits pagination limit.**
Cause: 2-week lookback returns more than 20 results in a busy workspace.
Solution: Always paginate. Fetch page 2 minimum on the user-from and user-to searches. If still capped, reduce the lookback to 7 days for those specific searches.

**Meeting-notes tool returns no transcripts.**
Cause: Tool not connected, meetings recorded under a different account, or transcripts haven't generated yet.
Solution: Skip silently and rely on the calendar attendee list + email follow-ups for meeting context.

**Teammate detection from calibration is stale (someone joined or left).**
Cause: `calibration/setup.md` has the old roster.
Solution: At the start of each run, ask once: "Anyone new on the team I should add to the email recap, or anyone to drop?" If yes, update `calibration/setup.md` before proceeding.

**Task lands in two buckets.**
Cause: Item spans LP and Fund Software, or Portfolio Support and Deal/Investments.
Solution: See the conflict-resolution rules in `references/task-buckets.md`. Default to the bucket that matches the primary stakeholder.

## References

- **`calibration/setup.md`** — Per-user setup: tools, teammates, email format. Created during first-run interview.
- **`references/setup-template.md`** — Template structure for `calibration/setup.md`.
- **`references/task-buckets.md`** — The 6 task buckets, definitions, and conflict-resolution rules.
- **`references/html-design-system.md`** — Color palette, layout, interaction model for the HTML file.
- **`references/email-format.md`** — Exact format for the weekly team email.
- **`calibration/`** — Past mis-classifications and edge cases logged for self-improvement.
