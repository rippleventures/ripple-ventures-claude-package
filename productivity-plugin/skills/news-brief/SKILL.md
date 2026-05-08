---
name: news-brief
description: "Generate a curated daily news brief from the user's chosen sources, categorized by topic, with one-line summaries and a 'why it matters for you' note customized to the user's industry and role. Triggers on phrases like 'morning brief', 'daily news', 'news brief', 'what's new today', 'catch me up', 'news summary', 'today in tech', 'today's headlines', or whenever the user asks for a curated rundown of news. First-run setup captures the user's sources, industry, and role; subsequent runs deliver the brief in their preferred format."
---

# News Brief

Generate a daily news brief from the user's chosen sources, organized by category, with a one-line summary and a one-line "why it matters for you" customized to their industry and role.

## Step 0: Check personalization and calibration

Read these in order:

1. **`references/profile.md`** — captures the user's sources, categories, industry, and role. Drives every brief.
2. **`calibration/`** entries (newest first) — past briefs that missed something or included noise.

### If `references/profile.md` is missing (first-time setup)

Pause and run the setup interview:

> "Before I run news briefs, I need to know what you actually care about. Quick questions:
>
> 1. **Sources** — which publications do you want me to pull from? (Examples: Bloomberg, FT, WSJ, The Information, Stratechery, Axios, Politico, TechCrunch, Reuters, AP, The Globe and Mail, Bloomberg Crypto. Pick as many as you want.)
> 2. **Categories** — which topic buckets should the brief organize into? (Examples: Tech, AI/ML, Global Politics, Domestic Politics, Markets, Crypto, Climate, Healthcare, Canada-specific. Pick the ones relevant to your work and life.)
> 3. **Industry** — what sector or industry are you in? (Used for the 'why it matters' line.)
> 4. **Role** — what's your role within that industry? (e.g., venture investor at an early-stage Canadian fund; product manager at a fintech; founder of a healthtech startup. The more specific, the sharper the 'why it matters' will be.)
> 5. **Format preferences** — Markdown in chat, HTML file, or email-ready text? Length cap (e.g., 5 stories per category)?"

Save the answers to `references/profile.md` using the template in `references/profile-template.md`. Subsequent runs read from there and skip the interview.

If the user wants to change sources or focus later, they can edit the file directly or just tell the skill in chat ("add Stratechery, drop TechCrunch") and the skill will update the file.

## Step 1: Compute the date range

Default: news from the last 24 hours, ending today. The user can override ("yesterday's news", "this week's news").

## Step 2: Gather news

For each source in `references/profile.md`, search for the most recent stories in the date range. Use WebSearch with site-restricted queries:

```
site:[source-domain] [optional category keyword] after:[YYYY-MM-DD]
```

Examples:

- `site:ft.com after:2026-05-07`
- `site:bloomberg.com climate after:2026-05-07`
- `site:theinformation.com AI after:2026-05-07`

For each result, capture:

- **Title** (verbatim from the source)
- **URL** (must work — verify by WebFetch if unsure)
- **Publish date / time**
- **Snippet** — what happened, in the source's own words

Run searches in parallel across sources to keep latency low.

## Step 3: Filter and categorize

For each story:

1. **Filter** — drop:
   - Stories older than the date range
   - Pure opinion / op-eds (unless the user explicitly listed an opinion source like Stratechery)
   - Listicles, "best of" roundups
   - Stories the source labels as "sponsored" or "promoted"

2. **Categorize** — assign each story to one of the user's categories from `references/profile.md`. If a story spans multiple, pick the primary one (the angle most relevant to the user's industry).

3. **Deduplicate** — if multiple sources cover the same story (which they usually do), pick the most authoritative source for the user's needs. Default rule: prefer the source closest to the original reporting (e.g., Bloomberg for markets news, FT for European business, Reuters for breaking news). Note in the "why it matters" line if other major outlets are also covering it.

4. **Cap** — apply the user's per-category cap (default: 5 stories per category). If more remain, keep the highest-signal ones.

## Step 4: Write the "why it matters for you" line

For each story, write one sentence — under 25 words — that connects the story to the user's industry and role from `references/profile.md`.

The line answers: *given my role and what I work on, why should I care about this story?*

Examples (industry: VC, role: early-stage Canadian fund focused on enterprise AI):

> Story: "Anthropic raises $5B at $200B valuation"
> Why it matters: Reset on what AI infra valuations look like at the top of the market — your portfolio's enterprise-AI startups will get questions on multiples.

> Story: "Bank of Canada cuts rates 25 bps"
> Why it matters: Slightly easier financing environment for portfolio companies raising bridge or extension rounds; LPs may revisit allocation models.

> Story: "OpenAI launches GPT-5.5"
> Why it matters: Capability bar moved — your AI portfolio's defensibility stories (especially fine-tuning plays) need to be revisited at next board meetings.

If you genuinely cannot connect the story to the user's role, drop it. Better to have fewer high-signal stories than pad with weak relevance.

## Step 5: Format the brief

Default format (Markdown in chat):

```markdown
# News brief — [YYYY-MM-DD]

## [Category 1 — e.g., AI/ML]

**[Story title]** ([Source])
[One-line summary of what happened.]
*Why it matters:* [One sentence customized to user.]
[URL]

**[Story title 2]** ([Source])
...

## [Category 2 — e.g., Markets]

...
```

If the user's profile says "HTML file": use the same structure but write to `outputs/news-brief-{YYYY-MM-DD}.html` with simple styling. Present with a `computer://` link.

If "email-ready text": same structure but plain text, ready to paste into an email. No markdown headers — use line breaks and CAPS for category headers.

## Step 6: Deliver

Show the brief in chat (or link to the HTML / paste the email text per the user's preferred format).

After delivery, offer once:

> "Want me to log any stories that missed the mark, or sources/categories to adjust?"

## Step 7: Calibration loop

If the user flags issues — "you missed the BoC rate cut", "TechCrunch is too noisy, drop it", "the why-it-matters lines are too generic" — copy `calibration/_template.md`, fill in, save as `calibration/YYYY-MM-DD-short-slug.md`. Future runs apply the lessons.

For source/category adjustments, also update `references/profile.md` directly.

## Rules

- Every story must come from a search done in this conversation. Do not fabricate stories.
- Every URL must work. If WebFetch returns 404 or redirects suspiciously, drop the story or note "URL may have changed" with the search-result URL.
- Every "why it matters" must be specific to the user's role. Generic relevance is worse than no story.
- No em dashes in summaries or "why it matters" lines. Use commas, parentheses, or new sentences.
- Default to 24-hour lookback. Don't surface week-old news as "today's brief."
- Honor the user's per-category cap. Quality over volume.

## Troubleshooting

**Source returns no results for the date range.**
Cause: Slow news day for that source, or the search query is too narrow.
Solution: Broaden the search (drop category keyword, expand to 48 hours). If still nothing, note the source had nothing relevant today rather than including a stale story.

**A URL doesn't work after WebFetch.**
Cause: Paywall redirect, link rot, source restructured URL.
Solution: Try the search-result URL. If still broken, drop the story rather than ship a broken link.

**Two sources cover the same story differently.**
Cause: Conflicting reporting or different angles.
Solution: Surface both in the same bullet with a note: "FT and WSJ disagree on [point]; FT cites X, WSJ cites Y." Better to flag than pretend they agree.

**The "why it matters" line keeps being too generic.**
Cause: User's profile is too thin (e.g., role is just "investor" with no specifics).
Solution: After 2-3 generic briefs, ask the user for a sharper role description. Save to `references/profile.md`.

**User wants a specific story type filtered out (e.g., "no celebrity news").**
Cause: Filter is too broad.
Solution: Add to a `references/exclusions.md` file — keywords or topics to always drop.

## References

- **`references/profile.md`** — User's sources, categories, industry, role, and format preferences. Created during first-run setup.
- **`references/profile-template.md`** — Structure for `profile.md`.
- **`references/exclusions.md`** — Optional. Topics or keywords to always filter out.
- **`calibration/`** — Past misses and noise reports.
