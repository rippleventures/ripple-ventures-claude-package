#!/usr/bin/env python3
"""
Render a background-check brief as standalone HTML.

Usage:
  python scripts/render_html.py --input brief.json --output brief.html

Input JSON shape:
  {
    "title": "Background brief — Toronto Tech Week 2026",
    "purpose": "event_prep",          # or "upcoming_call" or "cold_outreach"
    "subtitle": "Optional subtitle",   # optional
    "people": [
      {
        "name": "Jane Doe",
        "subtitle": "Co-founder @ Acme",        # optional
        "linkedin": "https://linkedin.com/in/janedoe",  # optional
        "twitter": "@janedoe",                   # optional
        "email": "jane@acme.com",                # optional
        "past_interaction": "string",            # required (use "First time meeting" if none)
        "current_info": "string",                # required
        "topics": ["string", "string"],          # required, 2-3 items
        "caveats": "string"                       # optional
      }
    ]
  }
"""

import argparse
import html
import json
import sys
from pathlib import Path


PURPOSE_LABELS = {
    "event_prep": "Event prep",
    "upcoming_call": "Upcoming call",
    "cold_outreach": "Cold outreach",
}


def esc(value):
    if value is None:
        return ""
    return html.escape(str(value))


def linkify(url, label=None):
    if not url:
        return ""
    return f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(label or url)}</a>'


def render_topics(topics):
    if not topics:
        return '<span class="muted">No topics suggested.</span>'
    items = "".join(f"<li>{esc(t)}</li>" for t in topics)
    return f"<ol class='topics'>{items}</ol>"


def render_links(person):
    parts = []
    if person.get("linkedin"):
        parts.append(linkify(person["linkedin"], "LinkedIn"))
    if person.get("twitter"):
        handle = person["twitter"]
        url = handle if handle.startswith("http") else f"https://x.com/{handle.lstrip('@')}"
        parts.append(linkify(url, handle if handle.startswith("@") else f"@{handle}"))
    if person.get("email"):
        parts.append(f'<a href="mailto:{esc(person["email"])}">{esc(person["email"])}</a>')
    return " · ".join(parts)


def render_row(person):
    name = esc(person.get("name", "Unknown"))
    subtitle = esc(person.get("subtitle", ""))
    links = render_links(person)
    past = esc(person.get("past_interaction", ""))
    current = esc(person.get("current_info", ""))
    topics_html = render_topics(person.get("topics", []))
    caveats = person.get("caveats", "")
    caveats_html = (
        f'<div class="caveats"><strong>Caveats:</strong> {esc(caveats)}</div>'
        if caveats
        else ""
    )

    person_block = f"""
      <div class="person-cell">
        <div class="person-name">{name}</div>
        {f'<div class="person-subtitle">{subtitle}</div>' if subtitle else ''}
        {f'<div class="person-links">{links}</div>' if links else ''}
      </div>
    """

    return f"""
    <tr>
      <td class="person-col">{person_block}</td>
      <td class="past-col">{past or '<span class="muted">First time meeting.</span>'}</td>
      <td class="current-col">{current}</td>
      <td class="topics-col">{topics_html}{caveats_html}</td>
    </tr>
    """


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    :root {{
      --bg: #ffffff;
      --fg: #111827;
      --muted: #6b7280;
      --border: #e5e7eb;
      --accent: #1f2937;
      --highlight: #f9fafb;
      --link: #2563eb;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 32px 40px;
      background: var(--bg);
      color: var(--fg);
      line-height: 1.5;
      font-size: 14px;
    }}
    header {{
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }}
    h1 {{
      margin: 0 0 4px;
      font-size: 22px;
      font-weight: 600;
    }}
    .meta {{
      color: var(--muted);
      font-size: 13px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
    }}
    thead th {{
      text-align: left;
      font-weight: 600;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--muted);
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
      background: var(--highlight);
    }}
    tbody td {{
      padding: 16px 12px;
      vertical-align: top;
      border-bottom: 1px solid var(--border);
    }}
    tbody tr:hover {{
      background: var(--highlight);
    }}
    .person-col {{ width: 22%; }}
    .past-col   {{ width: 26%; }}
    .current-col {{ width: 26%; }}
    .topics-col {{ width: 26%; }}
    .person-name {{
      font-weight: 600;
      font-size: 15px;
    }}
    .person-subtitle {{
      color: var(--muted);
      font-size: 13px;
      margin-top: 2px;
    }}
    .person-links {{
      margin-top: 6px;
      font-size: 12px;
    }}
    a {{ color: var(--link); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .topics {{
      padding-left: 18px;
      margin: 0;
    }}
    .topics li {{
      margin-bottom: 6px;
    }}
    .topics li:last-child {{ margin-bottom: 0; }}
    .caveats {{
      margin-top: 10px;
      padding: 8px 10px;
      background: #fff7ed;
      border-left: 3px solid #f59e0b;
      color: #78350f;
      font-size: 12px;
      border-radius: 2px;
    }}
    .muted {{ color: var(--muted); font-style: italic; }}
    @media print {{
      body {{ padding: 16px; }}
      tbody tr:hover {{ background: transparent; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>{title}</h1>
    <div class="meta">{meta}</div>
  </header>
  <table>
    <thead>
      <tr>
        <th>Person</th>
        <th>Past interaction</th>
        <th>Current information</th>
        <th>Suggested topics</th>
      </tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
  </table>
</body>
</html>
"""


def render(brief):
    title = esc(brief.get("title", "Background brief"))
    purpose = brief.get("purpose")
    subtitle = brief.get("subtitle", "")
    purpose_label = PURPOSE_LABELS.get(purpose, "")
    meta_parts = []
    if purpose_label:
        meta_parts.append(purpose_label)
    if subtitle:
        meta_parts.append(esc(subtitle))
    meta_parts.append(f"{len(brief.get('people', []))} people")
    meta = " · ".join(meta_parts)

    rows = "\n".join(render_row(p) for p in brief.get("people", []))

    return HTML_TEMPLATE.format(title=title, meta=meta, rows=rows)


def main():
    parser = argparse.ArgumentParser(description="Render background-check brief as HTML")
    parser.add_argument("--input", required=True, help="Path to brief JSON")
    parser.add_argument("--output", required=True, help="Path to write HTML")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        brief = json.load(f)

    if not brief.get("people"):
        print("Error: brief.json has no 'people' array", file=sys.stderr)
        sys.exit(1)

    html_out = render(brief)
    Path(args.output).write_text(html_out)
    print(f"Wrote {args.output} ({len(brief['people'])} people)")


if __name__ == "__main__":
    main()
