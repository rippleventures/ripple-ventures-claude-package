# Cross-border checklist (Canada / US)

When a deal spans Canadian and US parties — Canadian entity with US investors, or US entity with Canadian investors — these are the recurring traps.

## Securities law

### Canadian side

- **NI 45-106** governs prospectus exemptions in Canada.
- For accredited investors, the **accredited investor exemption** (s. 2.3) is the typical path.
- Required: investor reps confirming AI status, prescribed risk acknowledgement form for individual AIs in some provinces.
- Hold period: **4 months + 1 day** for resale, prescribed legend on the cert.
- Canadian companies are typically **private issuers** (s. 2.4) — verify the company qualifies and add the rep.

### US side

- **Regulation D Rule 506** is the typical path for private placements.
  - 506(b): no general solicitation, accredited and up to 35 non-accredited (with disclosure)
  - 506(c): general solicitation OK, all investors must be verified accredited
- Required: investor reps confirming accredited status, Form D filing within 15 days of first sale.
- "Bad actor" rep from issuer.

### Both at once

If the deal has both Canadian and US investors, the SPA needs **dual reps** — one section for NI 45-106 reps, one for Reg D reps. Don't conflate.

## Governing law and forum

- Default: governing law = entity's jurisdiction of incorporation.
  - Ontario corp → Ontario law, Toronto courts (or Toronto arbitration)
  - Delaware corp → Delaware law, Delaware Chancery
- **Don't apply Delaware law to a Canadian entity.** Canadian corporate law applies regardless; Delaware governing law just creates dispute uncertainty.
- Forum should match governing law.

## CCPC status (Canadian-Controlled Private Corporation)

CCPC status is hugely valuable for Canadian companies — it gates SR&ED tax credits and the $500K small business deduction.

CCPC requires:

- Canadian-controlled (Canadian residents control more than 50%)
- Private (not listed on a designated stock exchange)
- Not controlled, directly or indirectly in any manner whatever, by one or more non-residents or public corporations

**Things that blow up CCPC:**

- Non-resident shareholders gaining majority voting control (>50%)
- Non-resident-controlled investor board majority
- "Control in fact" provisions giving non-residents operational override (broad protective provisions on day-to-day matters)
- Stacked drag-alongs that effectively let non-residents dictate exit terms
- Convertible instruments that, if converted, would push non-resident ownership over 50% — even if not yet converted, CRA may deem control passed

**Safe patterns:**

- US investors taking minority equity stakes — fine
- Single board seat for a US investor on a 5-7 person board — fine
- Standard CVCA protective provisions (sale, dissolution, charter changes) at the class level — fine
- US-led seed/Series A where the lead takes one seat and Canadian founders/funds keep majority — fine

**Watch carefully:**

- Series B+ where US investors collectively hold >50% — may have already lost CCPC
- Operational vetoes on hiring, contracts, normal-course expenditures — could constitute control in fact
- "Affiliate" definitions that pull in US investor parents

## SR&ED and tax structuring

- SR&ED is paid as a refundable credit for CCPCs (cash, even with no taxable income).
- Non-CCPCs only get a non-refundable credit (against tax owing).
- For early-stage Canadian companies with no revenue, SR&ED cash is often material to runway. Losing CCPC status materially harms the company.

**Section 116** — non-resident vendors selling Canadian shares need a clearance certificate from CRA. Doesn't apply to founders in most early-stage scenarios but watch on secondaries with US sellers.

## Practical drafting

For Canadian entity + US investors:

- Governing law: Canadian (Ontario / BC / Alberta typically, depending on inc.)
- Securities reps: dual NI 45-106 + Reg D
- Hold period: 4 months + 1 day legend
- Board: structure to preserve Canadian-resident majority
- Protective provisions: class-level, fundamental matters only; avoid operational vetoes
- Dispute resolution: arbitration in Toronto / Vancouver, ICC or LCIA rules

For US entity + Canadian investors:

- Governing law: Delaware (or other US state)
- Securities reps: NI 45-106 reps still required for the Canadian investor's purchase, even though the entity is US
- Hold period: 4 months + 1 day legend on the cert (yes, even for shares of a Delaware corp held by a Canadian investor)
- No CCPC concerns (US entity, US tax)
- Form D filing on the US side

## Common mistakes

1. **Putting Delaware governing law on a Canadian entity term sheet** because the lead is from the US. Wrong.
2. **Skipping the Canadian hold period legend** on certificates issued to Canadian residents.
3. **Forgetting to add NI 45-106 reps** when the deal has any Canadian investors.
4. **Not flagging CCPC risk** when US investors take more than 30-40% — even if not yet majority, getting close should be a yellow flag for future rounds.
5. **Stacking drag-alongs that effectively give non-residents control in fact**.
