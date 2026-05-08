---
name: meeting-prep
description: "Research a person or list of people before a meeting. Handles both single-person briefs (1:1 prep, cold outreach, podcast guest research) and multi-person lists (event attendee rosters, intro batches, RSVP CSVs). Pulls past interaction history from the user's CRM, email, chat, and meeting notes before going to the open web. Categorizes multi-person lists by relevance (talent / founder / LP / co-investor / partner / community). Use when the user shares names, emails, LinkedIn URLs, or CSVs and asks for context, or says 'background check on [name]', 'research these people', 'I'm meeting [name] tomorrow', 'who's coming to this event', 'prep me for this meeting', 'who are these people'. Outputs a chat brief for one person or a sorted markdown/HTML table for many."
---

# Meeting Prep

Research the people the user is about to meet — one person or many — and produce the right kind of output for each case. Walk into a 1:1 already knowing what's been discussed before. Walk into an event already knowing who to seek out.

This skill is read-only. It does not write to the CRM, email, or any other system.

## Step 0: Check calibration

List files in `calibration/` and read entries newest first. Each entry captures past briefs that missed something the user needed. Apply those lessons before answering.

## Step 1: Parse the input and pick the mode

The user will give you one of:

- **A single name, URL, or LinkedIn profile** → single-person mode (chat brief output)
- **A CSV, paste of names, multi-row list, or 4+ names mentioned** → list mode (table output)

If unclear, ask: "Single brief on [name] in chat, or a table for the full list?"

For each person, extract whatever's available: name, email, LinkedIn URL, Twitter handle, company, title.

If the input is a CSV, read it with the workspace bash tool and present back the count and a sample row so the user can confirm parsing.

## Step 2: Ask the clarifying questions you actually need

Use AskUserQuestion if available. Most important question first:

**Always ask:** What's the purpose?

1. **Cold outreach / general research** — worth reaching out to? find a hook, find mutual connections.
2. **Upcoming call or 1:1** — call already booked, tailor the brief to the topic.
3. **Event prep** — attending an event, want to know who to seek out.
4. **List enrichment** — RSVP roster from an event, intros batch, attendee list — need each person categorized by relevance.

Tailored follow-ups by purpose:

**Upcoming call:** When is the call? Who set it up? Look at CRM and email for the original thread that booked it.

**Event prep:** What's the event? When? Specific themes or sectors of interest?

**Cold outreach:** What's the angle? (portfolio fit, deal flow, recruiting, partnership)

**List enrichment:** What's the source? (event name, intro batch label) — drives the table title.

Skip questions the input already answers. Two or three sharp questions beats a wall of clarification.

## Step 3: Past interaction check (always do this first)

Before going to the open web, see if the user has already met or interacted with each person. Order matters: internal sources first, web second.

For each person, run these in parallel where possible across the user's connected tools:

### 3a. CRM (Attio, HubSpot, Salesforce, Notion, etc.)

- Search for the person by name and by email
- Search for their company by name
- If a person record exists, capture the CRM URL for hyperlinking
- If a company record exists, capture the CRM URL
- For person records: list notes, search emails by metadata, search meetings/call recordings, note who on the team interacted with them

Logic for the "In CRM" attribute (list mode): "Yes" if EITHER person OR company exists; "No" only if neither exists.

### 3b. Email (Gmail, Outlook)

- Search threads with the person's email or name
- For substantive threads, read the full message body — snippets are not enough
- Note: who emailed them, when, last topic, open follow-ups

### 3c. Chat (Slack, Microsoft Teams)

- Search users in shared workspaces
- Search public/private channels for their name (deal channels, intro channels, portfolio channels)

### 3d. Meeting notes (Granola, Fireflies, Otter, Notion)

- Query the meeting tool for the name
- Get transcripts for hits
- Search the user's knowledge base for the name (deal memos, portfolio updates)

### 3e. Synthesize past interaction

For each person:

- **Met before?** (yes / no / unclear)
- **Who from the team?**
- **When and what for?**
- **Open follow-ups?** (anything unanswered, anything the user promised)

If "no, we haven't met them," say that plainly. Don't invent context.

## Step 4: Open web research

Run at least two searches per person. Parallelize across subagents when the list has 5+ people (each subagent researches one person and returns a structured profile).

### 4a. LinkedIn

- WebFetch the LinkedIn URL if provided. LinkedIn often returns JS-rendered noise — if so, extract from search snippets only and note "unverified (LinkedIn blocked)".
- WebSearch `"[name]" "[company if known]" linkedin` for role and recent activity.

### 4b. Recent activity

- WebSearch `"[name]" 2025 OR 2026` for press, podcasts, fundraises, launches
- If a founder: search company name + funding, traction, recent news
- If they post publicly: scan their last 3-5 LinkedIn or Twitter posts for what they're thinking about

### 4c. Mutual connections and overlapping context

- Search for shared connections (recent posts together, common companies on their LinkedIn vs. user's network)
- School overlap with the user's network
- Company overlap with the user's portfolio or focus areas

### 4d. Don't fabricate

Every factual claim must come from a search done in this conversation. If you cannot verify, say so. Do not invent titles, funding amounts, or backgrounds.

## Step 5: Categorize (list mode only)

For multi-person output, assign each person two attributes.

### Person Type

- **Talent** — strong candidate for hiring at portfolio companies
- **Founder** — building something the user could invest in
- **LP** — potential limited partner
- **Co-investor / VC** — co-investment or deal sharing relationship
- **Corp Dev Partner** — strategic partner for the user or portfolio companies
- **Service Provider** — lawyer, accountant, recruiter, etc.
- **Community** — event organizer, content creator, ecosystem builder
- **Unknown** — insufficient information

### Priority (H / M / L)

- **High** — direct, actionable opportunity (pipeline deal, key co-investor, elite talent, key connector)
- **Medium** — worth a conversation, some signal but needs more info or is early stage
- **Low** — general community, no immediate relevance, or insufficient information

Research depth rules:

- **Student** at a school → don't deep-dive the school. Focus on what they're building, projects, hackathon wins, side ventures.
- **Founder** → go deep on the company: stage, sector, funding, traction, team size.
- **Executive or senior professional** → look for LP / partnership signals: past fund investments, board seats, family office ties.
- **VC / investor** → fund, stage focus, co-investment overlap.

## Step 6: Suggest conversation topics (single-person mode only)

Propose 2 to 3 specific conversation topics. Specific is the operative word.

Bad: "their work in AI"
Good: "the teardown they posted last week about how their team uses Claude Code at the API layer"

Good topics ground in something concrete: a recent post, a launch, a hire, a market they're in that overlaps with the user's thesis, a mutual connection.

If purpose is "upcoming call," at least one topic should tie to the booked agenda.

If we've met them before, at least one topic should reference an open thread from the prior interaction.

## Step 7: Output

### 7a. Single-person → chat brief

Format directly in the chat:

```
## [Name]
[Title @ Company] · [LinkedIn URL] · [Twitter handle if found]

### Past interaction
[Have we met? Who, when, what for. Open follow-ups. Or: "First time meeting."]

### Current information
[Role, company, what they're working on, recent activity that's actually relevant. Specific over general.]

### Suggested topics
1. [Specific topic grounded in evidence]
2. [Specific topic]
3. [Specific topic — optional]

### Caveats
[Anything you couldn't verify, anything LinkedIn-blocked, anything to double-check.]
```

### 7b. List → markdown table or HTML

Sort by Priority (High → Medium → Low), then alphabetically within each priority tier. Include everyone — for first-name-only attendees, mark Unknown / Low with "First name only, insufficient information."

**Markdown table** (≤10 people, or user requested chat output):

```
| Person | Company / Org | In CRM | Person Type | Priority | Comments |
|--------|---------------|--------|-------------|----------|----------|
| [Name](crm-url) | [Company](crm-url) | Yes | Founder | High | Background, reasoning, next step. |
```

**HTML file** (>10 people, or user requested file output):

Use `scripts/render_html.py` to generate. Build a JSON like:

```json
{
  "title": "Meeting prep — [event or context]",
  "purpose": "list_enrichment | event_prep | upcoming_call | cold_outreach",
  "people": [
    {
      "name": "Jane Doe",
      "subtitle": "Co-founder @ Acme",
      "linkedin": "https://linkedin.com/in/janedoe",
      "twitter": "@janedoe",
      "in_crm": "Yes",
      "person_type": "Founder",
      "priority": "High",
      "past_interaction": "Met [teammate] at Toronto Tech Week 2025. Discussed her seed raise.",
      "current_info": "Raised $4M seed in March 2026. Hiring engineering #1.",
      "comments": "Pipeline deal candidate. Founder Type, High Priority because [reasoning].",
      "topics": ["Open follow-up", "Recent LinkedIn post on scaling on-call"],
      "caveats": "LinkedIn was blocked, role pulled from Crunchbase."
    }
  ]
}
```

Then run:

```bash
python scripts/render_html.py --input brief.json --output meeting-prep-{source-slug}-{YYYY-MM-DD}.html
```

Save the HTML to the outputs folder and present with a `computer://` link.

## Step 8: Offer to log calibration

After delivering, ask once:

> If I missed something or got something wrong, want me to log it in calibration so I do better next time?

If the user shares the miss, copy `calibration/_template.md`, fill in, save as `calibration/YYYY-MM-DD-short-slug.md`. Otherwise skip.

## Tone

- Direct. No filler. No "I'd be happy to help."
- No em dashes. Use commas, parentheses, or new sentences.
- Specific over general everywhere. Names, dates, quotes from posts.
- If you don't know something, say "couldn't find" or "unverified" — don't paper over it.
- If past interaction shows the team ghosted them, flag it. That's exactly what the user needs to know before the call.

## Things to avoid

- Don't write to the user's CRM, email, or any other system. This skill is read-only.
- Don't fabricate. Every claim ties to a search or an internal source.
- Don't pad the brief. If past interaction is "first time meeting," say that in one line.
- Don't suggest generic conversation topics. Topics must be grounded in evidence.
- Don't conflate people with similar names without disambiguating first.

## Troubleshooting

**LinkedIn returns JS-rendered noise instead of profile data.**
Cause: LinkedIn aggressively blocks scraping.
Solution: Skip the WebFetch. Use WebSearch with name + company + "linkedin" and pull from search snippets. Note "unverified (LinkedIn blocked)" in caveats.

**Person not found in CRM, email, chat, or meeting notes.**
Cause: First-time contact, or different email/spelling than what the team has.
Solution: Try a name-only search across CRM and chat (no email filter). If still nothing, plainly say "first time meeting" and move to web research.

**Ambiguous name with multiple matches (e.g., "John Smith").**
Cause: Common name, no disambiguating info.
Solution: Single-person mode → ask the user to disambiguate before researching, with top 2-3 candidates and one-line distinguishers. List mode → list candidates in Comments column with distinguishing features and mark Priority Low.

**Source blocks scraping (LinkedIn, some company sites).**
Cause: JS-rendered content, 403 responses.
Solution: Extract from search snippets. Note "unverified (source blocked)" in caveats/comments. Include the URL so the user can check manually.

**CRM search returns false positives.**
Cause: Duplicate or near-duplicate names in the CRM.
Solution: Verify by company match before attributing the CRM record. If unclear, mark "In CRM" as No and note ambiguity in comments.

**List has more than 20 people — research is slow.**
Cause: Sequential research across many subjects.
Solution: Parallelize via subagents. Each subagent researches one person and returns a structured profile. Aggregate at the end.

## References

- **`scripts/render_html.py`** — Renders multi-person briefs as a styled HTML table.
- **`references/`** — Optional. If the user wants briefs in a specific format or has a custom Person Type taxonomy, save it here.
- **`calibration/`** — Past misses logged for self-improvement.
