# References

The skill reads files in this folder on every run to ground drafts in the user's actual voice.

## What goes here

Two kinds of files:

### `voice-guide.md` (created during first-run setup)

Describes:

- **Recipient groups** — who the user emails regularly, grouped by relationship type (e.g., co-investors, internal team, founders, LPs, clients, partners)
- **Email types** — the kinds of emails the user sends (e.g., internal updates, external outreach, follow-ups, intros, thank-yous, declines)
- **Voice notes** — anything specific to the user's style (greeting preferences, sign-offs, signature phrases)

### `examples/*.md` (collected over time)

Example emails the user has written and flagged as canonical. Each file is one email, with a short header noting:

- Recipient group
- Email type
- Anything notable about why this is a good example

Example filename: `examples/founder-followup-good.md`

## Privacy

Examples may contain personal info (real names, emails, deal terms). Strip identifying details before saving where possible — replace with `[Name]`, `[email]`, `[company]`. The skill cares about the writing patterns, not the specifics.

## How they're used

On every run, the skill:

1. Reads `voice-guide.md` to know recipient groups and email types
2. Reads all `examples/*.md` to absorb tone, length, and structure
3. Reads recent calibration entries to pick up evolving patterns

If both are empty, the skill runs the first-run setup flow described in `SKILL.md` Step 0.
