---
description: Apply standard Excel formatting (blue inputs / black formulas / green links) to a workbook. Use when the user shares an unformatted model and wants to bring it up to institutional formatting standards before review.
---

# /format-xls

Apply institutional-quality formatting standards to an Excel workbook.

## What this command does

1. Locate the workbook
2. Walk every cell in calculation sheets:
   - Cells containing only a typed number (no formula) → color **blue** (#0070C0)
   - Cells containing a formula referencing only the same sheet → color **black** (#000000)
   - Cells containing a formula referencing another sheet → color **green** (#00B050)
   - Cells linking to an external workbook → color **red** (#FF0000) and flag for review
3. Apply standard fonts (Calibri 11) to data cells, Calibri 11 bold to headers
4. Number format: comma separator with negatives in parens for currency, % with 1 decimal for percentages
5. Standardize column widths (8.43 default, headers fit-to-content)
6. Save the formatted version with `_formatted` suffix

## Usage

```
/format-xls /path/to/model.xlsx
```

## Rules

- Don't overwrite the original workbook. Save as a new file.
- Don't change any cell values or formulas — only formatting.
- If a cell already has the correct color, leave it alone.
- Surface a summary at the end: how many cells changed, any anomalies (e.g., external links found).

## Implementation

Invokes the `xlsx-author` skill's formatting workflow plus `scripts/validate_color_coding.py` for the color check.
