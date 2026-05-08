# Task buckets

The weekly review groups all non-calendar work items into one of these 6 buckets. Don't invent new buckets — if something doesn't fit, expand the closest bucket's definition.

## Fixed order

1. **LP**
2. **Portfolio Support**
3. **Deals/Investments**
4. **Fund Operations**
5. **Events**
6. **Fund Software**

The HTML and email both render in this order. Sections with zero items still show the header with "(0) — nothing this week" so the structure is predictable.

## Bucket definitions

### LP

- LP outreach, follow-ups, intros
- LPAC deck work
- Fundraising strategy and materials
- AGM speaker prep, AGM materials, AGM logistics that are LP-facing
- Specific LP relationship work (named LPs, family offices, fund-of-funds)

### Portfolio Support

- Founder requests, intros, hiring help
- Portfolio company updates that need a reply
- Reporting deck updates and follow-ups for portfolio companies
- Quarterly update collection from portfolio CEOs
- Board meeting prep for portfolio companies

### Deals/Investments

- New deal diligence and memos
- Pass communications
- Deal sourcing, intros, qualifying
- Data room reviews
- Term sheet / SAFE / SPV work

### Fund Operations

- Onboarding documentation for new hires
- Internal hiring and team coordination
- Expenses, reimbursements, payments (e.g., travel)
- Fund admin, legal, compliance
- CRM/notes ops, internal tooling cleanup
- Anything internal coordinators (Ops, EAs, fund admins) are coordinating with the user

### Events

- AGM logistics (venue, swag, name tags, photographer)
- City-specific event planning
- Industry summit attendance
- Conference scouting and event scouting

### Fund Software

- Internal AI agent infrastructure
- Skill builds, MCP integrations, deployments
- Workshop content (LP workshops, internal team training)
- Internal portals (LP portal, NAV tracking, news agent, recruiting agent)
- AI tool testing
- Client AI setups (when the fund builds AI for portfolio or LPs)

## Conflict resolution

When a task could fit two buckets, prefer the bucket that matches the **primary stakeholder**:

- **LP-facing workshop deck** → LP (because it's for an LP), NOT Fund Software
- **Internal slide prep for a meeting** → Fund Software (because it's the technical content), UNLESS the meeting itself is the user's deliverable, in which case it's the bucket of the meeting (LP, Portfolio Support, etc.)
- **Portfolio reporting collection from CEOs** → Portfolio Support (the work is supporting portfolio cos), NOT Fund Operations
- **Travel booking for an event** → Events (it's tied to an event), NOT Fund Operations
- **Hiring for a portfolio company** → Portfolio Support, NOT Fund Operations
- **Hiring for the fund itself** → Fund Operations

## Within-bucket sort

Within each bucket, sort by urgency:

1. Items with explicit deadlines or someone-waiting first
2. Then everything else

If urgency is tied, alphabetize by topic.

## Customizing for a different fund / org

The 6 buckets above match a venture fund's workflow. For a different org type:

- **Operating company exec**: replace LP/Portfolio Support/Deals with team-management / customer / sales / product equivalents
- **Solo consultant**: replace with client-facing / business-development / ops / personal-dev

Update this reference file with new bucket names and definitions. The SKILL.md doesn't hardcode the bucket names — it pulls from this file.
