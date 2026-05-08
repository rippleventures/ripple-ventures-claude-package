---
description: Populate a PowerPoint pitch deck template using data from an Excel workbook. Charts are bound to named ranges so the deck stays in sync with the model. Use when the user has a model + template and wants the deck filled in.
---

# /build-deck

Populate a PowerPoint deck template using data from an Excel workbook.

## What this command does

1. Locate the deck template (path argument)
2. Locate the source workbook (path argument)
3. Walk each slide in the template, look for placeholders (`[METRIC_NAME]`, `[CHART:NAMED_RANGE]`, etc.)
4. For each placeholder:
   - Text placeholder → look up the value in the workbook and insert
   - Chart placeholder → create a chart bound to the named range (so it updates when the model changes)
5. Save the populated deck with timestamp in the filename

## Usage

```
/build-deck /path/to/template.pptx /path/to/model.xlsx
```

## Output

Path to the generated deck. Summary of:

- Placeholders filled (count and a sample list)
- Placeholders with no matching workbook data (flagged for the user to fill manually or check the template)
- Charts created and the ranges they bind to

## Rules

- Every number on a slide must trace to a named range in the workbook. If a number can't be sourced, mark `[CHECK]` in the slide rather than typing it.
- Don't modify the source workbook.
- Don't auto-add slides — only fill what's in the template.

## Implementation

Invokes `pptx-author` for the populate workflow plus `scripts/extract_named_ranges.py` to map placeholders to data.
