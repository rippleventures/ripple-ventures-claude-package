# Example: 3-statement model structure

A reference for what a properly-formatted 3-statement model looks like. The `xlsx-author` skill builds new models that match this layout.

## Sheet structure

```
Workbook/
├── Cover                    Title, authorship, model version, date
├── Assumptions              All blue inputs — driver assumptions, no formulas
├── Historicals              Reported financials (5+ years) — typed in blue
├── Income Statement         Calculated forward — black/green formulas only
├── Balance Sheet            Calculated forward — black/green formulas only
├── Cash Flow                Calculated forward — derived from IS + BS
├── Debt Schedule            Tranches, interest expense flowing back to IS
├── Working Capital          AR, inventory, AP — flowing to BS
├── Equity Schedule          Share count, dividends, buybacks
└── Sensitivities            Outputs only — no inputs here
```

## Color coding

Every cell follows the standard:

- **Blue** (#0070C0) — typed inputs on Assumptions and Historicals sheets
- **Black** (#000000) — formulas referencing only the same sheet
- **Green** (#00B050) — formulas linking to a different sheet (e.g., IS revenue line pulling from Assumptions)
- **Red** (#FF0000) — external workbook links (should never appear; flag and remove)

## Income Statement layout

Standard line items in this order:

1. Revenue (multiple lines if segmented)
2. Cost of revenue
3. **Gross profit** (calculated)
4. Operating expenses (R&D, S&M, G&A as separate lines)
5. **Operating income / EBIT** (calculated)
6. Interest expense (linked to Debt Schedule)
7. Other income / expense
8. **Pre-tax income** (calculated)
9. Tax expense (effective rate from Assumptions)
10. **Net income** (calculated)
11. Diluted EPS (linked to Equity Schedule for share count)

## Balance Sheet layout

Assets:
- Current assets (cash, AR, inventory, prepaid, other)
- PP&E
- Goodwill / intangibles
- Other long-term assets
- **Total assets** (sum)

Liabilities + Equity:
- Current liabilities (AP, accrued, current debt, other)
- Long-term debt (linked to Debt Schedule)
- Other LT liabilities
- Stockholders' equity (linked to Equity Schedule)
- **Total L+E** (sum)

**Plug check** — `Total assets - Total L+E` should equal zero, every period. Cell color: black, value should always be zero. If it's nonzero, the model is broken.

## Cash Flow Statement layout

- Net income (linked from IS)
- Depreciation, amortization (non-cash adjustments)
- Working capital changes (linked from WC schedule)
- Capex (linked from Assumptions)
- **Free cash flow** (calculated)
- Debt issuance / repayment (linked to Debt Schedule)
- Equity issuance / buybacks (linked to Equity Schedule)
- Dividends
- **Change in cash** (sum)
- Beginning cash + change = ending cash, must tie to BS

## Conventions

- Negative numbers in parens: `(1,234)` not `-1,234`
- Currency unit clearly labeled in cell A1 of each sheet (e.g., "$ in millions")
- Period columns: most recent left-most or right-most (pick one and be consistent)
- Footnotes for any non-obvious calculation (e.g., "FX as of [date]")

## Common mistakes

- Mixing inputs and formulas on the same sheet (always separate)
- Hardcoding numbers in the IS (use Assumptions sheet)
- Skipping the plug check (run audit-xls to catch)
- Inconsistent date formatting across periods
- Missing parens on negative numbers
