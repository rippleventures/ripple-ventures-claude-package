---
name: model-builder
description: "Build DCF, LBO, three-statement, and trading-comps models live in Excel from a ticker and assumption set. Orchestrates dcf-model, lbo-model, 3-statement-model, comps-analysis, and audit-xls. Use when the user says 'build a DCF on [company]', 'put together an LBO model', 'three-statement model for [ticker]', 'comps spread on [sector]', 'model up [name]', 'fresh model on [company]', 'build me a model', 'sensitize this'. For updating an existing model after earnings, use earnings-reviewer instead — this skill builds clean models from scratch."
---

# Model Builder (orchestration skill)

Build an institutional-quality valuation model from scratch. The user says "build a DCF on Salesforce" or "model up Acme as an LBO"; this skill handles inputs, model construction, audit, and sensitivities in one workflow.

## Step 0: Check calibration

Read recent entries in `calibration/`. Past mistakes (broken links, hardcode creep, sensitivity table errors) inform the current run.

## Step 1: Confirm scope

Use AskUserQuestion:

- **Ticker / company** — which name?
- **Model type** — DCF, LBO, three-statement, comps-only, or all of the above?
- **Stage** — public company, private company, pre-IPO?
- **Assumption set** — does the user have a specific set (e.g., "5-year DCF, 3% terminal growth, 9% WACC") or do we use defaults?
- **Template** — does the firm have a model template, or are we building on a clean Excel base?

## Step 2: Pull inputs

Use the user's connected market data tools (CapIQ, Daloopa, public filings, Crunchbase for private):

- Historical financials (3-5 years)
- Consensus estimates (next 2-3 years)
- Filings (latest 10-K, 10-Qs)
- Capital structure
- Share count, dividend history, buybacks

Load full filings. Don't summarize.

## Step 3: Build the model

Invoke the matching skill(s):

### For DCF:
- Invoke `dcf-model`
- Input historicals + consensus → projection period (typically 5-10 years)
- Build WACC (cost of equity via CAPM, cost of debt from filings or market)
- Terminal value (Gordon growth or exit multiple)
- Bridge from enterprise value to equity value

### For LBO:
- Invoke `lbo-model`
- Sources & uses
- Debt schedule (revolver, term loan, mezz tranches as relevant)
- Returns waterfall (sponsor IRR, MOIC at exit)
- Operating projections (typically 5-7 years)

### For three-statement:
- Invoke `3-statement-model`
- Integrated IS / BS / CF
- Working capital schedule
- Debt schedule
- Equity schedule
- Plug check

### For comps:
- Invoke `comps-analysis`
- Trading multiples table for the peer set
- Summary statistics (mean, median, percentile ranges)
- Outlier flags

## Step 4: Apply formatting standards

Always invoke `audit-xls` for formatting:

- **Blue** for hardcoded inputs (assumptions, raw historicals)
- **Black** for formulas
- **Green** for links across sheets
- **Red** for external links (avoid where possible)
- No hardcodes in calculation cells (the cardinal rule)
- Sources column on every assumption

## Step 5: Audit

Run the full QC pass via `audit-xls`:

- Balance checks tie (assets = liabilities + equity, every period)
- Cash flow ties to balance sheet cash (every period)
- No broken links
- No `#REF!`, `#DIV/0!`, `#NAME?` errors
- Circular references intentional only (and flagged with `[CIRC: <reason>]`)
- Every output traces to an input
- Currency consistency across the workbook

If anything fails, stop. Surface the specific issue. Don't proceed to sensitivities with a broken model.

## Step 6: Build sensitivity tables

Standard sensitivity grids for the model type:

- **DCF**: WACC × terminal growth (or exit multiple), 7×7 grid for share price
- **LBO**: Entry multiple × exit multiple, 5×5 grid for IRR; same grid for MOIC
- **Three-statement**: revenue growth × operating margin, key impact metric

## Step 7: Surface for review

Stage the workbook in the user's models folder. Show:

- Path to the file
- Summary of what was built (model type, projection period, key outputs)
- Any `[ASSUMPTION]` flags where defaults were used
- Any `[UNSOURCED]` flags where inputs couldn't be verified

The user reviews and approves before any downstream use (memo, deck, IC presentation).

## Guardrails

- **Every output is a formula.** No typed numbers in calculation cells. Calculation cells should compute from inputs and prior-period values, never have a hardcoded number.
- **Cite every input.** Hardcoded assumptions are labeled with source (10-K page, consensus mean, "assumption per discussion") or marked `[ASSUMPTION]`.
- **Stop and surface** after build and again after audit. The user approves before sensitivities.
- **No external linking.** Don't link to files outside the workbook (creates breakage when shared).
- **No external communications.** This skill builds models; sharing happens outside.

## Tone

- Engineer's voice. Precise about what's a fact vs. a judgment.
- No em dashes.
- Cite every input with `[source]`.
- Flag uncertainty: `[ASSUMPTION]`, `[UNSOURCED]`, `[CHECK]`.

## Troubleshooting

**Cell references break across sheets.**
Cause: Sheet renamed mid-build, or formula refers to a non-existent range.
Solution: Run `audit-xls` immediately. Fix specific broken refs before proceeding. Don't ship a workbook with `#REF!` errors.

**WACC build can't find risk-free rate or beta.**
Cause: Market data tool didn't return the inputs, or the company is private (no beta).
Solution: For public: ask the user to confirm the inputs from a different source. For private: use the unlevered beta of public comps + relever for the target's capital structure. Note the methodology in the WACC build.

**LBO returns are dramatically high (e.g., 70% IRR).**
Cause: Usually unrealistic exit multiple or operating assumptions.
Solution: Stop. Surface the inputs. Compare exit multiple to entry multiple — if exit > entry, ask the user for the rationale (multiple expansion thesis). Don't ship an LBO with unrealistic returns without flagging.

**Three-statement doesn't balance.**
Cause: Cash flow statement plug. Almost always a missing item in working capital or financing.
Solution: Run the audit. The plug imbalance points to the missing line item. Fix and re-audit.

**User asks for a model on a private company with no public data.**
Cause: No CapIQ / FactSet coverage.
Solution: Build with the user's manually-supplied assumptions. Mark every input `[USER-PROVIDED]`. The model is only as good as the inputs — make that clear in the surface-for-review step.

## References

- **`references/`** — Firm-specific model templates, formatting standards, sensitivity table conventions.
- **`calibration/`** — Past models logged for self-improvement.

## Skills this skill orchestrates

`dcf-model` · `lbo-model` · `3-statement-model` · `comps-analysis` · `audit-xls`
