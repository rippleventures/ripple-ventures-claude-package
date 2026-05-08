# Calibration log

Each file captures a draft → sent comparison. The skill reads the most recent 3-5 entries on every run.

## How to use

After the user sends (or moves on), copy `_template.md`, fill in, save as `YYYY-MM-DD-short-slug.md`.

Slug examples:

- `2026-05-08-acme-followup`
- `2026-05-12-cold-outreach-jane`
- `2026-05-15-decline-deal-bravo`

## What gets logged

- Recurring word swaps (e.g., user always replaces "circulate" with "post")
- Greeting / sign-off preferences for specific recipient groups
- Length patterns (user always cuts to under 80 words for internal email, etc.)
- Tone shifts the skill needs to learn for specific contact types

## Relationship to references/

`calibration/` is for ongoing learning from edits.
`references/examples/` is for ground-truth examples the user has flagged as canonical.

Both feed the skill's voice signal. References are read fully; calibration's most recent entries are read for pattern updates.
