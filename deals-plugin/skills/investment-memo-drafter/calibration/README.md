# Calibration log

Each file captures a draft → final memo comparison after IC. The skill reads recent entries on every run.

## How to use

After IC, when the user is finished editing the memo, copy `_template.md`, fill in, save as `YYYY-MM-DD-company-slug.md`.

Slug examples:

- `2026-05-08-acme-pre-seed`
- `2026-05-12-bravo-series-a`
- `2026-05-15-charlie-extension`

## What gets logged

- Recurring section reorderings
- Voice / depth patterns that diverge from the skill's draft
- Sources the skill consistently fails to consult
- Risk-framing patterns specific to the user's firm
- Recommendation framing (the user's threshold for Pass / Lean / Yes)

## Relationship to references/

`references/template.md` and `references/sample-memos/` are the static voice source.
`calibration/` captures evolving patterns from individual deals.

When a calibration entry reveals a permanent change in template (e.g., "always include a 'Why us' section"), update `references/template.md` directly.
