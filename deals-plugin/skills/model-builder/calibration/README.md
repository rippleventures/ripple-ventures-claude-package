# Calibration log

Each file captures an orchestration run where the skill missed something or chained the wrong sub-skills.

## How to use

When the user flags a miss, copy `_template.md`, fill in, save as `YYYY-MM-DD-short-slug.md`.

## What gets logged

- Sub-skill ordering mistakes (e.g., should have run audit-xls before sensitivities)
- Missing inputs the skill should have requested upfront
- Output format that diverged from the user's preference
- Sector / model / template patterns that recur
