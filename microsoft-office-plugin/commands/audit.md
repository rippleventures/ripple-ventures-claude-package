---
description: Run the audit-xls workflow against an Excel workbook. Checks formatting standards (color coding, no hardcodes in calc cells), balance equations, and reference integrity. Use when the user types /audit and wants a quick QC pass on a model.
---

# /audit

Run the audit-xls workflow against the workbook the user shared (or the most recent one in the conversation).

## What this command does

1. Locate the workbook (path argument, or most recent xlsx in conversation)
2. Run `scripts/validate_xls.py` against it
3. Surface a structured report:
   - Formatting check (blue inputs / black formulas / green cross-sheet links)
   - Hardcode check (no typed numbers in calculation cells)
   - Balance check (assets = liabilities + equity, every period)
   - Reference integrity (`#REF!`, `#DIV/0!`, `#NAME?` errors)
   - Circular references (intentional only, must be flagged)

## Usage

```
/audit /path/to/model.xlsx
```

If no path provided, look for the most recent xlsx in the conversation.

## Output

A markdown report with PASS/FAIL for each check and specific cell references for failures.

If anything fails: stop, surface the failure, do not auto-fix. The user reviews and decides.

## Rules

- Read-only. Never modify the workbook directly. Surface findings; let the user fix.
- Cite specific cells (e.g., `Assumptions!C12` has hardcode in a formula).
- Don't pretend a check passed if the script returned errors.

## Implementation

This command invokes the `audit-xls` skill via its standard workflow. The slash command is just a shortcut for explicit invocation.
