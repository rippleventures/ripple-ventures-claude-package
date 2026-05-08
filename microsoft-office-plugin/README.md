# Microsoft Office Plugin

Foundation skills, slash commands, scripts, and examples for creating and auditing Microsoft Excel and PowerPoint files. Used by other plugins (especially `deals-plugin`) and reusable in any workflow that produces Office files.

## Install

```bash
# Via Cowork: Settings → Plugins → Install plugin → point at this folder
# Or zip and share:
cd microsoft-office-plugin && zip -r /tmp/microsoft-office.plugin . -x "*.DS_Store"
```

## Folder structure

```
microsoft-office-plugin/
├── .claude-plugin/plugin.json
├── README.md                       ← this file
├── skills/                         ← skills the plugin registers
│   ├── xlsx-author/
│   ├── pptx-author/
│   └── audit-xls/
├── commands/                       ← slash commands for explicit invocation
│   ├── audit.md                    /audit
│   ├── format-xls.md               /format-xls
│   ├── build-deck.md               /build-deck
│   └── check-deck.md               /check-deck
├── scripts/                        ← Python utilities the skills call
│   ├── validate_xls.py             Workbook QC checks
│   ├── extract_named_ranges.py     Pull named ranges → JSON
│   ├── check_deck.py               PowerPoint QC pass
│   ├── validate_color_coding.py    Verify blue/black/green standard
│   └── requirements.txt            openpyxl + python-pptx
└── examples/                       ← reference structures
    ├── example-three-statement-structure.md
    ├── example-pitch-deck-structure.md
    └── example-color-coding.md
```

## Skills

### `xlsx-author`

Creates Excel workbooks with proper structure, named ranges, and consistent formulas. Foundation for any other skill that produces an .xlsx file.

**Used by:** `model-builder`, `earnings-reviewer`, `valuation-reviewer`, `pitch-deck-creator`, `dcf-model`, `lbo-model`, `3-statement-model`, `comps-analysis`, `model-update`

### `pptx-author`

Creates PowerPoint files with slide layouts, charts bound to data, and consistent typography. Foundation for any other skill that produces a .pptx file.

**Used by:** `pitch-deck-creator`, `market-researcher`, `pitch-deck`, `deck-refresh`

### `audit-xls`

Excel formatting standards and QC checks (blue inputs / black formulas / green cross-sheet links / red external links, balance checks, no hardcodes in calc cells, no `#REF!` errors).

**Used by:** every modeling skill in `deals-plugin`. Always invoke after building or modifying a model.

## Slash commands

Quick explicit invocation when the user wants to skip the natural-language layer.

| Command | What it does |
|---|---|
| `/audit /path/to/model.xlsx` | Run the full audit-xls QC pass on a workbook |
| `/format-xls /path/to/model.xlsx` | Apply institutional color coding (blue/black/green) |
| `/build-deck /path/to/template.pptx /path/to/model.xlsx` | Populate a pitch deck template with data from a model |
| `/check-deck /path/to/deck.pptx` | QC a finished pitch deck (totals tie, footnotes, dates) |

Slash commands invoke the same underlying skills — they're shortcuts for explicit, deterministic invocation.

## Scripts

Standalone Python scripts the skills call for deterministic checks (faster and more reliable than language-based inspection).

### `scripts/validate_xls.py`

Audits a workbook against institutional formatting standards. Outputs JSON.

```bash
python scripts/validate_xls.py model.xlsx
python scripts/validate_xls.py model.xlsx --strict   # exit 1 on any failure
```

Checks: hardcodes in calc cells, reference errors (`#REF!`, `#DIV/0!`, `#NAME?`), external workbook links.

### `scripts/extract_named_ranges.py`

Pulls every named range from a workbook with sheet, range, and value. Used by `build-deck` to map PowerPoint placeholders to Excel data.

```bash
python scripts/extract_named_ranges.py model.xlsx
```

### `scripts/check_deck.py`

QC pass on a PowerPoint deck. Outputs JSON.

```bash
python scripts/check_deck.py deck.pptx
python scripts/check_deck.py deck.pptx --source-model model.xlsx   # also verify totals tie
```

Checks: leftover placeholders (`[TBD]`, `[PLACEHOLDER]`), page numbers present, currency consistency across slides, date consistency.

### `scripts/validate_color_coding.py`

Verifies every cell in a workbook has the right font color per the standard. Outputs JSON listing violations.

```bash
python scripts/validate_color_coding.py model.xlsx
```

### Dependencies

```bash
pip install -r scripts/requirements.txt
```

Installs `openpyxl` (Excel reading) and `python-pptx` (PowerPoint reading).

## Examples

Reference structures for building consistent Office files.

### `examples/example-three-statement-structure.md`

What a properly-formatted 3-statement model looks like — sheet structure, color coding, line item ordering, plug check, conventions for negatives and currency labeling.

### `examples/example-pitch-deck-structure.md`

Standard slide order for an IB pitch deck — cover, situation, snapshot, market overview, football field, comps, precedents, DCF, LBO, process. Footnote conventions, layout standards, common mistakes.

### `examples/example-color-coding.md`

The blue/black/green/red standard with examples of correct and incorrect cells. Used by `validate_color_coding.py` as the source of truth.

## Why this is a separate plugin

These three skills + tooling are pure foundations — they don't have domain logic of their own. Extracting them means:

1. **Reusable** — install once, use across any plugin that produces Office files
2. **Smaller plugin sizes** — `deals-plugin` doesn't need to bundle Office foundations
3. **Single source of truth** — update Office foundations in one place
4. **Single source of scripts** — Python utilities don't get duplicated across workflow plugins

## Dependency note

`deals-plugin` depends on this plugin. If you install `deals-plugin` without `microsoft-office-plugin`, the orchestration skills (`model-builder`, `pitch-deck-creator`, etc.) will fail when they try to invoke `xlsx-author`, `pptx-author`, or `audit-xls`.

Install both together. The two install processes are independent — Cowork doesn't auto-install dependencies.

## Calibration

Each skill has its own `calibration/` and `references/` folders. Calibration is empty by default — log entries when you find QC patterns the skill consistently misses or formatting conventions specific to your firm.

## Reference

Original source: Anthropic's [financial-services reference repo](https://github.com/anthropics/financial-services). The three foundation skills appear in multiple agent-plugins in the original (pitch-agent, model-builder, earnings-reviewer, etc.) — extracting them here removes the duplication. Slash commands, Python scripts, and examples are additions specific to this package.
