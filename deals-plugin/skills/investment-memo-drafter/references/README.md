# References

Two files drive this skill:

## `template.md` (created during first-run setup)

The user's preferred memo structure: section headers, recommended length per section, any firm-specific sections (e.g., "Sourcing Fit", "Co-investor Wishlist", "Pro-rata Plan").

If absent, the skill falls back to the generic VC seed/Series A template defined in `SKILL.md` Step 4.

## `sample-memos/*.md` (collected over time)

Example memos the user has written or approved. Each file is one memo, with a brief header noting:

- Stage (pre-seed / seed / Series A / etc.)
- Recommendation (Pass / Lean / Yes)
- Sector
- Anything notable about why this is a good example

Privacy note: strip identifying details before saving where possible — replace company name with `[Company]`, founder names with `[Founder]`, dollar amounts can stay since they convey memo style.

## How they're used

On every memo draft:

1. Read `template.md` to know the structure to follow
2. Read all `sample-memos/*.md` to absorb tone, depth, and the user's voice
3. Read recent calibration entries to apply evolving patterns

If both are empty, the skill runs the first-run setup flow described in `SKILL.md` Step 0.
