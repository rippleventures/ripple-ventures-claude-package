# Calibration log

Two kinds of files live here:

1. **`setup.md`** — the user's per-run setup (tools, team, email format). Created once during first-run setup. Updated whenever tools or team change.
2. **`YYYY-MM-DD-*.md`** — weekly miss logs.

## setup.md

Read on every run. Drives which tools the skill queries and who gets the recap email. Template structure is in `references/setup-template.md`.

## Weekly miss logs

After a weekly review, if the user flags items the skill missed or mis-classified, copy `_template.md`, fill in, save as `YYYY-MM-DD-short-slug.md`.

Slug examples:

- `2026-05-08-missed-canva-tasks`
- `2026-05-12-mis-bucketed-portfolio-update`
- `2026-05-15-over-included-completed`

## What gets logged

- Sources that should have been searched but weren't
- Bucket-classification mistakes
- Completion signals the skill missed
- Patterns where Bucket A vs Bucket B vs Bucket C judgement is consistently off

Don't log:

- One-off small misses with no pattern
- Stylistic preferences for the HTML or email format (those go in `references/`)
