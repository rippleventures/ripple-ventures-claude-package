# Example: Excel color coding standard

The institutional standard for color-coding Excel models. `audit-xls` and `validate_color_coding.py` enforce these conventions.

## The four colors

| Color | Hex | What it means |
|---|---|---|
| **Blue** | `#0070C0` | Typed input — a number or text the user typed in |
| **Black** | `#000000` | Formula referencing only cells on the same sheet |
| **Green** | `#00B050` | Formula linking to a different sheet in the same workbook |
| **Red** | `#FF0000` | Formula linking to an external workbook (should be removed) |

## Why color matters

When someone else picks up your model, color coding tells them at a glance:

- "Where can I change assumptions?" → blue cells
- "What's calculated from those assumptions?" → black/green cells
- "Is anything pulling from another file (fragile)?" → red cells

Without this convention, finding the inputs in a 50-tab model is a treasure hunt.

## Examples

### Assumptions sheet

```
Assumptions!C5    Revenue growth Year 1     5%       BLUE   (typed)
Assumptions!C6    Revenue growth Year 2     6%       BLUE   (typed)
Assumptions!C7    Revenue growth Year 3     =AVERAGE(C5:C6)  BLACK  (same-sheet formula)
```

### Income Statement sheet

```
IS!D5    Revenue Year 1         =Historicals!D10*(1+Assumptions!C5)   GREEN  (cross-sheet)
IS!D6    Revenue Year 2         =D5*(1+Assumptions!C6)                 GREEN  (cross-sheet to Assumptions)
IS!D8    Gross profit           =D5-D7                                  BLACK  (same-sheet)
```

### Bad: hardcode in a calculation cell

```
IS!D5    Revenue Year 1         =100*(1+Assumptions!C5)    ❌
```

The `100` should live on Assumptions or Historicals, not embedded in the IS formula. `audit-xls` flags this as "hardcode in calc cell."

### Bad: external link

```
IS!D5    Revenue Year 1         ='[OldModel.xlsx]Sheet1'!A5    ❌
```

External links break when the model is shared. `validate_color_coding.py` flags this RED and the user needs to either:
- Replace the value with a typed input (blue)
- Replace with a formula referencing data inside the current workbook

## How to apply

In Excel: select cells → Home → Font color → choose from the standard palette.

Or use `/format-xls` to apply automatically. The skill walks every cell, infers the type, and sets the color.

## Cells that should be empty (no color)

Empty cells need no color. Don't apply blue to a cell with no typed input — it implies "this is an input, fill it in" which is a different convention (intentional blanks).

For optional inputs the user can fill: leave empty, but add a comment indicating "[optional]".

## Header / label cells

Bold black labels (column headers, row labels) are not part of the standard. They use whatever font color the firm's template specifies. The four colors above only apply to **value cells**.
