# News brief profile

Copy this to `profile.md` and fill in. The skill reads it on every run.

```markdown
# News brief profile

## Sources

List publications to pull from, one per line. Format: `[name]: [domain]`

Examples:
- Financial Times: ft.com
- Bloomberg: bloomberg.com
- The Information: theinformation.com
- Stratechery: stratechery.com
- Axios: axios.com
- Globe and Mail: theglobeandmail.com

## Categories

Topic buckets to organize stories into. Order = display order in the brief.

Examples:
- AI/ML
- Tech & Markets
- Global Politics
- Domestic Politics (Canada)
- Climate
- Crypto

## Industry

[One sentence — what sector or industry you're in.]

## Role

[Two or three sentences — your specific role, what you work on day-to-day, what your fund/company/team focuses on. The more specific, the sharper the "why it matters" lines will be.]

## Format preferences

- **Output format:** markdown in chat | HTML file | email-ready text
- **Stories per category cap:** [number, default 5]
- **Default lookback:** [hours, default 24]
- **Default time of day to run:** [optional — e.g., 6am ET — used by the schedule skill if the user automates this]

## Notes / overrides

[Anything else — e.g., "always include any story about Anthropic", "prioritize Canada angle on global stories", "drop TechCrunch on Fridays"]
```

## How the file is used

- **Sources** drives which `site:` searches the skill runs.
- **Categories** drives the brief's structure.
- **Industry + Role** drives the "why it matters for you" line.
- **Format preferences** drives the output format.
- **Notes / overrides** are read every run; lessons get applied.

## Updating

You can edit this file directly, or tell the skill in chat ("add Stratechery, drop TechCrunch") and it will update the file for you.
