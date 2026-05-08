---
name: email-draft
description: "Draft, rewrite, or review professional emails in the user's voice. Use whenever the user asks to draft an email, write a reply, help me respond, write a follow-up, intro, thank-you, cold outreach, partnership ask, or any variation involving email composition. Also trigger when reviewing or editing email drafts for tone and style. Adapts to the user's specific voice via examples in references/ and corrections logged in calibration/."
---

# Email Draft

Draft emails in the user's voice. The goal is to match how the user actually writes — not produce generic "AI-drafted" copy.

## Step 0: Check personalization

This skill works best when grounded in the user's actual writing. Before drafting, run the setup check:

1. **List `references/`.** If it has example emails (`references/examples/*.md`), read them — they are the source of truth for the user's voice.
2. **List `calibration/`.** Read the 3 to 5 most recent entries (newest filename dates first). They show what was drafted, what was sent, and what changed.

### If `references/` is empty (first-time setup)

Pause and ask the user the setup questions before drafting anything:

> "I haven't seen any examples of your writing yet. To draft emails that actually sound like you, can I ask three quick questions?
>
> 1. Who do you email regularly? (Group them — e.g., co-investors, internal team, founders, LPs, clients, partners.)
> 2. What types of emails do you usually send? (e.g., internal updates, external outreach, follow-ups, intros, thank-yous, declines.)
> 3. Want to share 3 to 5 example emails now so I can learn your voice? Or should I draft something general and learn from your edits?"

Save the user's answers as `references/voice-guide.md` (the recipient groups + email types) and any pasted emails as `references/examples/example-1.md`, `references/examples/example-2.md`, etc. Strip personally-identifying info from examples that will be shared (replace names with [Name], emails with [email]).

If the user picks "draft general and learn from edits," proceed with the universal principles below and rely on calibration to converge on their voice.

## Step 1: Read context

For each draft, gather:

- **Who's the recipient?** (Match to one of the groups in `references/voice-guide.md` — e.g., "internal team" gets a different register than "external LP".)
- **What's the email type?** (Reply, cold outreach, follow-up, intro, decline.)
- **What's the situation?** (Replying to a specific message, forwarding, kicking off a thread.)
- **Is there a thread to read?** If the user shared a previous email or referenced a thread, read it first.

## Step 2: Draft

Use the references and calibration as the primary voice signal. The principles below are universal defaults — they apply when references are silent on a question.

### Universal principles

1. **Concise over clever.** Don't pad sentences. Say the thing, then move on.
2. **Specific over vague.** Name the exact action. "I'll post the blurb on our Slack" beats "I'll share it with the team."
3. **Warm but not performative.** Genuine enthusiasm is fine ("This is amazing!") but skip hollow openers like "Hope this finds you well" or "Just circling back."
4. **Soft asks over direct demands.** "Was wondering if..." reads better than "Quick one for you —" or "I wanted to ask."
5. **No overselling.** State the idea simply. Don't pre-justify why it makes sense — let the recipient connect the dots.
6. **No em dashes.** Use commas, parentheses, or new sentences. This is the single fastest tell that an LLM wrote it.

### Default structure

- **Greeting:** "Hi [Name]," for most professional contexts. "Hey [Name]," only for very close, established relationships. Avoid "Hello" or "Dear" unless the recipient uses them first.
- **Opening line:** React to what they sent first (acknowledge, thank, or respond to their ask) before introducing new topics.
- **Transitions:** "Separately," to pivot to a new topic. Avoid "On another note," or "Quick question —" or "One more thing."
- **Sign-off:** "Best, [Name]" is the default. Use "Thanks, [Name]" when the email is primarily a request. Avoid "Talk soon," "Cheers," "Warmly," or "Let me know!" unless the user's references show otherwise.
- **Length:** Keep most replies under 100 words. If you need more, something is probably wrong.

### What to avoid

- Don't end with a question that pressures a response ("Thoughts?" / "What do you think?" / "Let me know!")
- Don't add context the recipient already knows (e.g., explaining what their company does back to them)
- Don't use exclamation marks more than once per email (unless it's genuinely exciting news)
- Don't include filler transitions like "Hope all is well" unless it's the very first email in a new relationship
- Don't use bullet points in short emails — just write sentences
- Don't over-explain the "why" behind an ask — state the ask and let the conversation develop

### Match the recipient group

If `references/voice-guide.md` defines recipient groups, match the register:

- **Internal team** → casual, short, often skip the greeting on a thread
- **External professional (LP, partner, client)** → polished but warm, full structure
- **Founder you know well** → casual, direct, often punchy
- **Cold outreach** → respectful, specific, low-pressure ask

If the user's references show a different style for a group, follow the references.

## Step 3: Deliver

Show the draft in chat. If multiple variants make sense (longer / shorter, more formal / casual), offer two side by side.

Offer one short line afterward: "Want me to tweak the tone, or shorten?"

## Step 4: Offer to log calibration

After the user sends or moves on, ask once:

> Want me to log this in calibration so I can learn? Paste the version you actually sent if it's different from my draft.

If they paste, copy `calibration/_template.md`, fill it in (original draft, final sent, what changed, one-line lesson), and save as `calibration/YYYY-MM-DD-short-slug.md`.

If they decline, skip. Don't ask twice.

## Troubleshooting

**Drafts feel generic / not in the user's voice.**
Cause: `references/` is empty or thin.
Solution: Run the setup flow from Step 0. Get 3 to 5 real examples and the recipient/email-type breakdown. The skill needs concrete signal to converge.

**The recipient uses a different register than the user expects.**
Cause: Recipient sent "Hey Sam!! 😊" but user's default voice is more polished.
Solution: Match the recipient's register on the reply (within reason). Note the register-mismatch in the chat reply so the user can override if they prefer.

**Universal rules conflict with calibration.**
Cause: User has gradually shifted style (e.g., started using em dashes, started signing "Cheers,").
Solution: Calibration wins. The principles in Step 2 are defaults; references and calibration are the real source of truth.

**Long email request that genuinely needs more than 100 words.**
Cause: Detailed proposal, intro with full context, multi-topic update.
Solution: Use a clear structure — short greeting, scannable paragraphs (each one focused), explicit headers if there are multiple asks. Don't pad. Length should come from substance, not filler.

## References

- **`references/voice-guide.md`** — Recipient groups and email types, captured during first-run setup.
- **`references/examples/*.md`** — Example emails the user has written. Read every example on every run.
- **`calibration/`** — Drafts vs. sent versions, logged for self-improvement.
