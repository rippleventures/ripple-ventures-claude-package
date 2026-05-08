# Setup template

Copy this file to `calibration/setup.md` and fill in. The skill reads it on every run to know which tools to query and how to address the user's team.

```markdown
# Weekly review — setup

## Tools

- Calendar: [google-calendar | outlook | apple | none]
- Email: [gmail | outlook | none]
- Chat: [slack | teams | none]
- CRM: [attio | hubspot | salesforce | notion | none]
- Meeting notes: [granola | fireflies | otter | notion | none]

## Team (recipients of the weekly recap email)

| Name | Email |
|------|-------|
| [Name] | [email] |
| [Name] | [email] |

## Email format

- Subject template: `Recap W[X] [Month] [Year]`
- From signature: `[Name]`
- Recipients: see Team table above (or specific recurring thread name)

## Notes / overrides

- Any per-user overrides for the universal rules. E.g., "include personal calendar entries on Fridays" — but this skill is work-only by default.
- Any commonly-missed items the skill should always check (e.g., "always check Canva for assignment notifications").
- Any custom keyword searches to add to the email and chat scans.
```

## How the setup file is used

- **Tools section** drives which sources Step 3 queries.
- **Team section** drives who the weekly email is addressed to.
- **Email format section** drives Step 7's draft.
- **Notes / overrides** are read at the start of every run; lessons get applied to that session.

## Updating the setup

Re-run the setup interview when:

- A team member joins or leaves
- The user switches a tool (e.g., Slack → Teams)
- The email recap format changes

Just update `calibration/setup.md` directly. The skill will pick up the new values on the next run.
