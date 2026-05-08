# Example: IB pitch deck structure

Standard slide order for an investment banking pitch deck. The `pitch-deck` skill (in deals-plugin) populates templates that match this structure.

## Slide order

1. **Cover** — target name, situation, date, firm logo
2. **Situation overview** — one-paragraph narrative; "what's changed and why now"
3. **Company snapshot** — business description, segments, geography, key metrics
4. **Industry / market overview** — TAM, growth, structure, where this name plays
5. **Valuation summary (football field)** — min/median/max from each methodology, current price marker
6. **Trading comps detail** — table of public peers with multiples
7. **Precedent transactions detail** — historical M&A in the sector
8. **DCF summary** — projection summary, WACC build, sensitivity grid (WACC × terminal growth)
9. **LBO summary** — sponsor case, returns waterfall, sensitivity grid (entry × exit multiple)
10. **Illustrative process** — timeline, next steps

## Football field slide (the centerpiece)

Horizontal bar chart with one bar per methodology:

- Trading comps (multiple range × current revenue/EBITDA)
- Precedent transactions (multiple range × current revenue/EBITDA)
- DCF (low/base/high cases)
- LBO (entry price implied by target IRR)

Plus:
- Vertical line at current share price
- Each bar labeled with the dollar range
- Footnote: source for each methodology, as-of date

Every number on this slide must trace to a named range in the source workbook.

## Footnotes

Every data-heavy slide has a footnote in 8pt at the bottom:

```
Source: [data source], as of [date]. Note: [any methodology assumptions].
```

Examples:
- "Source: CapIQ as of [Date]. Comps median excludes outliers."
- "Source: Company filings, broker estimates. DCF assumes [WACC]% WACC, [g]% terminal growth."

## Layout conventions

- **Title bar** — top of every slide, target name + slide topic
- **Page numbers** — bottom right, every slide except cover
- **Source footnote** — bottom left, every data slide
- **Brand colors** — apply firm's standard palette
- **Font** — Calibri or firm's standard (consistent across all slides)
- **Number formatting** — comma separators, parens for negatives, consistent currency unit

## Charts

Every chart is bound to a named range in the source workbook. When the model updates, the chart updates automatically. Never paste static images of charts.

For bar charts: legend on the right, horizontal axis labeled with units.
For line charts: legend on the bottom, axis labels include units, gridlines subtle (light gray).

## Common mistakes (caught by the check-deck QC pass)

- `[TBD]` or `[PLACEHOLDER]` text remaining
- Numbers on slides that don't tie to the workbook
- Inconsistent dates (one slide says Q4 2025, another says Q1 2026)
- Mixed currencies (USD on one slide, EUR on another, no conversion footnote)
- Missing page numbers
- Footnotes missing on data slides
- Spelling errors in company / ticker names

## Customization

Different firms have different templates and conventions. Save your firm's:

- Standard slide order in `deals-plugin/skills/pitch-deck-creator/references/`
- Brand colors and fonts in `microsoft-office-plugin/skills/pptx-author/references/brand-standards.md`
- Footnote conventions in `microsoft-office-plugin/skills/pptx-author/references/footnote-format.md`

The skills will read these on every run.
