# HTML design system

The weekly review HTML is a single self-contained file. No external CSS, no JS frameworks, no CDN dependencies. Inline everything.

## Palette (warm, terminal-inspired)

```css
:root {
  --bg:         #F4F3EE;   /* cream */
  --text:       #1A1915;   /* near black */
  --accent:     #C15F3C;   /* rust orange */
  --dim:        #5A4A3A;   /* dark warm brown */
  --surface:    #E8E5DA;   /* light warm gray */
  --border:     #C15F3C;   /* rust orange borders */
  --badge-task: #B8860B;   /* warm gold */
  --badge-call: #7A8C6A;   /* sage green */
  --badge-event:#A0785A;   /* warm brown */
  --badge-deadline: #C15F3C; /* rust orange */
}
```

## Rules

- Only warm colors. No cyan, teal, neon, cool gray. Browns, oranges, creams only.
- Every piece of text must be instantly readable on its background.
- Borders: rust/orange, never light gray.
- Font: `system-ui` or a clean sans-serif. No decorative fonts.
- Responsive: works on laptop screens. Mobile not required.

## Layout

### Section 1: Calendar week grid

A table with:

- **Header row**: Mon {date}, Tue {date}, Wed {date}, Thu {date}, Fri {date}, Sat {date}, Sun {date} (default Mon-Sun, or whatever 7-day window the user requested).
- Highlight today's column header in rust.
- Hatch (diagonal stripes) any day already in the past as of today.
- **Row 1 header**: "In-Person Meetings"
- **Row 2 header**: "Virtual Meetings"

The grid only shows meetings with other people. Self-created time-blocks are dropped — the actionable work they represent already lives in the Tasks section.

Each cell contains item cards with ONLY:

- Item name (bold, single line, truncate if long)
- Time (e.g., "2:30pm")
- Source badge (Cal)

Do NOT include attendee names, locations, conference URLs, or type badges. The row label already conveys whether the meeting is in-person or virtual. Card body is intentionally minimal.

If a cell has multiple items, stack vertically with a small gap.

There is NO Personal row.

### Section 2: Tasks (grouped, not a backlog)

Below the grid, render task groups as discrete sub-sections in the order defined in `task-buckets.md`. Each sub-section is a header with the count (e.g., "LP (4)") and a list underneath.

Each task item shows:

- Title (bold)
- Context (1-2 sentences: who, what, situation)
- Next step (concrete next action, prefixed with an arrow)
- Source link (chat permalink, email URL, meeting-notes ID)
- Source badge

Within each group, sort by urgency (deadlines/someone-waiting first, then everything else).

If a group has zero items, show the header with "(0) — nothing this week" rather than hiding the section.

There is NO Portfolio Signals section. Portfolio company mentions stay in source data and may inform the Portfolio Support bucket, but they aren't rendered as a separate section.

## Interactivity

Vanilla JavaScript only. No frameworks, no CDN dependencies.

- Each item has a checkbox. Semantics: **checked = done**, unchecked = still open.
- All checkboxes default to UNCHECKED (no items pre-checked, including grid items).
- Visual: unchecked items render at full opacity (active). Checked items render faded (done). Standard todo-list mental model.
- Floating "Summary" panel at the bottom shows the count of OPEN items (unchecked).
- "Copy Summary" button copies a text list of all UNCHECKED items, grouped by section.
- Clicking anywhere outside the checkbox toggles expand/collapse of full context.

The email draft step uses unchecked (open) items as the source. Checked items are treated as done and excluded.

## Accessibility

- Color contrast must pass WCAG AA against the cream background.
- All interactive elements (checkboxes, expand toggles) must be keyboard-reachable.
- Source links should have descriptive labels, not "click here."

## File output

```bash
open outputs/weekly-review-{YYYY-MM-DD}.html
```

The file is fully self-contained — should work even if the user's network is offline.
