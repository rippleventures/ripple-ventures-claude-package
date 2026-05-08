---
description: QC a finished PowerPoint pitch deck — totals tie, footnotes present, dates consistent, no leftover placeholders. Use before sending a deck to a client or senior reviewer.
---

# /check-deck

QC pass on a finished pitch deck.

## What this command does

1. Locate the deck
2. Run a series of checks:
   - **Totals tie** — every number on a slide traces to the source workbook
   - **Footnotes** — every data slide has a "Source:" footnote
   - **Dates consistent** — all dates across slides reference the same as-of date
   - **Currency consistent** — all monetary values use the same currency unit
   - **Page numbers** — present on every content slide
   - **Placeholders** — no `[PLACEHOLDER]`, `[TBD]`, `[CHECK]`, or `XXX` text remaining
   - **Spelling** — flag obvious typos in company names, ticker symbols
3. Output a structured report with PASS/FAIL per check and slide numbers for failures

## Usage

```
/check-deck /path/to/deck.pptx [/path/to/source-model.xlsx]
```

If a source model is provided, the totals-tie check verifies against it.

## Rules

- Read-only. Never modify the deck. Surface findings; let the user fix.
- Cite specific slides for failures (e.g., "Slide 7: number $1.2B doesn't tie to workbook").
- Don't pretend a check passed if the script returned errors.

## Implementation

Invokes the `ib-check-deck` skill (in deals-plugin) plus `scripts/check_deck.py` for the deterministic checks.
