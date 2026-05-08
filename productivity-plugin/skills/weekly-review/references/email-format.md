# Email format — weekly team recap

The weekly review draft email follows this format exactly. Recipients and signature are pulled from `calibration/setup.md`.

## Subject

```
Recap W[X] [Month] [Year]
```

Example: `Recap W19 May 2026`

(Use the user's preferred subject template if `calibration/setup.md` overrides this.)

## Body structure

```
**[Topic Name]:** [Optional Links]
- What you did (past tense, concise)
- Another bullet if needed
- *Next Step*: What's coming next (only if there is a clear next step)

**[Topic Name 2]:**
- Bullet
- *Next Step*: ...

Best,
[Name]
```

## Section ordering

Mirror the task buckets in `task-buckets.md`. Use only sections that have content this week.

1. LP
2. Deals/Investments
3. Portfolio Support
4. Fund Software
5. Fund Operations
6. Events
7. Housekeeping (always last — purchases, expenses, equipment)

(Order matches the buckets but Deals comes before Portfolio Support in the email — front-load investment activity. Housekeeping is its own bucket only in the email, not the HTML.)

## Classification at email-draft time

Items go into one of three buckets:

### Bucket A — Core Work (main body)

- The user personally did the work (not forwarding someone else's)
- Substantive enough for a bullet point
- Directly advances core priorities

### Bucket B — Review Items (present to user for approval)

- Work someone else did that the user was tangentially involved in
- Minor portfolio support tasks
- Speculative or early-stage ideas shared but not acted on
- Things the user coordinated but didn't execute themselves

Present Bucket B as a numbered list before finalizing. The user picks which to include.

### Bucket C — Housekeeping

- Purchases, expenses, equipment orders
- Admin tasks
- Always include who approved the expense if discussed in chat

## Formatting rules

- **Bold** topic names, not numbered.
- Bullets under each topic (not numbered).
- Include source links where available.
- ***Next Step*** in bold italic only when there's a concrete next action. Skip it if the topic is just a "did this" report.
- End with `Best,\n[Name]`.
- No em dashes. Use commas, parentheses, or separate sentences.
- No tree/code-block formatting. Plain bullets only — this is an email, not a doc.
- Keep concise. Each bullet 1-2 sentences max.

## What NOT to include

- Casual chat banter, memes, or reactions
- One-word replies
- Tasks someone else did (even if user was CC'd)
- Internal debugging details (mention the outcome, not the process)
- Personal items of any kind

## Presenting the draft

After drafting, present Bucket B items for review:

> "Here are items I'm not sure about including:
>
> 1. [Item] — reason it's in review
> 2. [Item] — reason
>
> Reply with numbers to include, or 'none' to skip all."

Then present the final draft in chat. Wait for approval before any email tool action.

## Customizing for a different role

The default sections (LP, Deals, Portfolio Support, Fund Software, Fund Ops, Events, Housekeeping) match a venture fund. For a different role, edit the section list in this file and the buckets in `task-buckets.md` — keep them in sync. The SKILL.md reads from these references, so changing them propagates everywhere.
