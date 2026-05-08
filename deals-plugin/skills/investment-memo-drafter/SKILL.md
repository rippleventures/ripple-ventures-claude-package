---
name: investment-memo-drafter
description: "Draft an investment memo for a venture deal under consideration. Use when the user is evaluating a startup investment and asks to 'draft an IC memo', 'write up the deal', 'put together a memo on [company]', 'draft an investment memo', 'memo this deal', 'IC writeup', 'deal memo', or shares a pitch deck and asks for a memo. Adapts to the user's preferred memo template via examples in references/. Pulls factual content from the deck, founder calls, and external research; flags gaps where the analyst needs to fill in."
---

# Investment Memo Drafter

Draft an investment memo for a venture deal. The output should follow the user's firm's template, ground every claim in source material (the deck, founder calls, public research), and explicitly flag gaps the analyst needs to fill in. Memos are first drafts for the analyst to refine, not final products.

## Step 0: Check personalization and calibration

Read these in order:

1. **`references/template.md`** — the user's preferred memo structure. Drives section ordering and length.
2. **`references/sample-memos/`** — past memos the user has written or approved. The voice / depth source.
3. **`calibration/`** entries newest first — past memos that missed something or got the framing wrong.

### If `references/template.md` is missing (first-time setup)

Pause and ask:

> "Memos work best when they match your firm's template. Two questions:
>
> 1. Do you have a memo template you'd like me to follow? Paste it (section headers, length per section, anything else) and I'll save it as `references/template.md`. Or skip and I'll use a generic VC memo structure as a starting point.
> 2. Want to share 1-2 example memos you've written or approved? Saves them to `references/sample-memos/` so I can match your voice and depth on future memos."

If the user provides a template, save it. If they skip, use the generic structure in Step 4. Either way, log the choice.

## Step 1: Gather source material

Ask the user what's available:

- **Pitch deck** (PDF, PPTX, or link) — the primary source
- **Founder call notes / transcripts** — secondary source (Granola, Fireflies, paste from their notes app)
- **Memo from sourcing notes** (any pre-existing structured info from the user's CRM)
- **Public research already done** (market size, comp companies, news)
- **Reference checks** (if they've happened — paste notes)

Read everything before drafting. Don't draft from memory or partial info.

If the only input is a deck, ask the user if there's been a founder call or any other context. Decks alone make weak memos.

## Step 2: Pull from external research where the deck is thin

For any claim in the deck the user wants substantiated, run web searches:

- **Market sizing** — verify TAM/SAM claims against industry reports
- **Comp companies** — find publicly-disclosed comps (revenue, valuation, raise history) via Crunchbase, news, public filings
- **Founder backgrounds** — verify LinkedIn, prior companies, prior exits
- **Customer logos** — verify customers actually exist (especially for early-stage decks)
- **Competitive landscape** — what's already been funded in the space

If you cannot verify a claim, do not include it as fact. Write "[CHECK: deck claims X — could not verify]" inline so the analyst knows to chase.

## Step 3: Draft the memo

Follow the structure in `references/template.md`. If no template exists, use this generic VC seed/Series A memo structure:

```
1. Executive Summary (3-5 sentences)
   - The ask, the company, the recommendation, the key risk
2. The Company
   - What they do (one paragraph, plain English)
   - Stage, traction, revenue (with source attribution)
3. The Round
   - Round size, lead, valuation, our proposed check
   - Use of funds, runway implied
4. Why Now
   - Market timing, technology timing, regulatory shifts
5. The Market
   - TAM, growth rate, segmentation
   - Adjacent markets and expansion vectors
6. The Product
   - What it does, how it differs from alternatives
   - Demo notes, technical advantages (if any)
7. The Team
   - Founders' backgrounds, why this team for this problem
   - Key hires, gaps, advisors
8. Traction
   - Customers, revenue, pipeline, growth rate
   - Retention / engagement signals
   - Anything verifiable (logos, ARR, NRR, NPS)
9. Competition
   - Direct competitors with funding/stage
   - Indirect / adjacent competitors
   - Why we think this team wins
10. Risks
    - Market risk, execution risk, founder risk, financial risk
    - Each with a 1-line mitigant or "we're betting on X"
11. Recommendation
    - Pass / Lean / Yes
    - If Yes: terms we'd want, any conditions
    - If Pass: why, and what would change our mind
```

Adapt section length to stage:

- **Pre-seed** — short on traction, long on team and market thesis
- **Seed** — balance team / market / early traction
- **Series A** — heavy on traction (revenue, retention, unit economics)
- **Series B+** — heavy on traction, GTM efficiency, financial discipline

## Step 4: Flag gaps explicitly

Every memo should end with a "Gaps" section listing things the analyst needs to chase:

```
## Gaps to chase before IC

- Confirm reported ARR with founder (deck says $1.2M, sourcing notes say $900K)
- Reference check on technical co-founder
- Verify LOI status with [customer name]
- Get unit economics breakdown (CAC, payback, gross margin)
```

Better to flag a gap than to invent a number.

## Step 5: Tone and format rules

- **Lead with the recommendation.** Executive summary first sentence: "Recommendation: [Pass / Lean / Yes]." Don't bury it.
- **Specific over vague.** Numbers, names, dates, sources. "ARR: $1.2M as of March 2026 per founder call" beats "strong revenue growth."
- **Source every factual claim.** "(per deck slide 8)", "(per founder call 2026-04-15)", "(per Crunchbase)". If the analyst reads the memo a month later, they should know where every number came from.
- **No em dashes.** Use commas, parentheses, or new sentences.
- **No filler.** No "in today's competitive landscape", no "we believe this represents an exciting opportunity."
- **Plain English.** Write like you're talking to a partner who hasn't seen the deck. Don't pretend you have certainty you don't.

## Step 6: Deliver

Save the memo as a markdown file in the outputs folder:

```
outputs/memo-{company-slug}-{YYYY-MM-DD}.md
```

Or if the user prefers it in chat for inline editing, present it directly in the chat with section headers.

After delivery, ask:

> "Want this in a Word doc or just stay in markdown? And want me to log this in calibration once you've finalized the version that goes to IC?"

## Step 7: Calibration

After the user finalizes the memo (post-IC), ask once:

> "Want me to log this — your final version vs. my draft, what changed, what I missed? It'll make future memos better."

If the user shares the final version, copy `calibration/_template.md`, fill in (deal context, draft summary, final summary, key changes, lesson), save as `calibration/YYYY-MM-DD-company-slug.md`.

## Rules

- Every factual claim must trace to a source (deck, call notes, web search). No invented numbers.
- Always include a "Gaps" section. Don't paper over missing info.
- Lead with the recommendation. Don't make the reader scroll.
- Match the section structure in `references/template.md` if it exists. Otherwise use the generic structure above.
- Adapt depth to stage. A pre-seed memo isn't a Series B memo.
- No em dashes. No filler.
- Memos are first drafts. Always treat as a starting point, not a final product.

## Troubleshooting

**Deck claims and call notes contradict each other.**
Cause: Founder updated numbers between deck and call, or one source is stale.
Solution: Surface both with attribution: "Deck slide 6 says ARR is $1.2M; founder call 2026-04-15 says $900K." Add to the Gaps section: "Confirm current ARR with founder."

**Public research can't verify a market-size claim.**
Cause: Niche market, no published data, or founder used a custom calculation.
Solution: Say so: "Market size: deck claims $50B TAM; could not find independent verification. [CHECK: ask founder for the calculation source.]" Don't restate the claim as fact.

**No `references/template.md` and the user wants a quick memo.**
Cause: First-time use, no template captured.
Solution: Use the generic structure in Step 4. After delivering, ask if they want to save the structure as their template (or modify and save the modified version).

**Memo is way too long.**
Cause: Padded sections to "look thorough."
Solution: Cut. A seed memo over 2,500 words is usually padded. Aim for 1,500-2,000 words for seed, 2,500-4,000 for Series A+.

**The user keeps editing the same patterns out of every memo.**
Cause: Skill is missing a recurring style preference.
Solution: Log to calibration. After 2-3 entries with the same pattern, update `references/template.md` to bake the pattern in.

## References

- **`references/template.md`** — User's preferred memo structure. Drives section ordering and length.
- **`references/sample-memos/`** — Example memos the user has written or approved. Voice / depth source.
- **`calibration/`** — Past misses logged for self-improvement.
