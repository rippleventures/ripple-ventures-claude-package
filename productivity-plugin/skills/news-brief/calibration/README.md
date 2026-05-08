# Calibration log

Each file captures a brief that missed important stories, included noise, or had weak "why it matters" lines.

## How to use

When the user flags issues with a brief, copy `_template.md`, fill in, save as `YYYY-MM-DD-short-slug.md`.

Slug examples:

- `2026-05-08-missed-boc-rate-cut`
- `2026-05-12-techcrunch-noise`
- `2026-05-15-generic-why-matters`

## What gets logged

- Stories the skill should have caught (suggests a missing source or weak filtering)
- Sources that consistently produce noise (suggests dropping or narrowing the source's category)
- "Why it matters" lines that miss — patterns over time
- Format/length adjustments the user makes consistently

## Relationship to references/

`references/profile.md` is the user's static configuration (sources, categories, role).
`calibration/` is the log of corrections that gets applied on each run.

When a calibration entry suggests a permanent change (e.g., always drop TechCrunch), update `references/profile.md` directly so the change is durable.
