# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-14 18:05:47 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **15 / 100** (Elevated Strain)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **+2.4**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.22 | 3.95 |
| Civil Service and Agency Independence | 10 | 0.15 | 0.38 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.82 | 1.65 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 4 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 2.00 (Yellow) | ai | 1 | 0 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 1.65 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | keyword | 0 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 0.60 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: This item reports a real, verifiable action: a specific individual with a documented record of partisan voter-challenge activity has been hired into an election administration position (Georgia State Election Board). This is a concrete instance of partisan personnel placement in election administration, matching the signal of election administration moving toward partisan control. The placement is confirmed and has occurred, but it is a single personnel decision rather than a structural, systemic capture or an official policy dismantling neutral process. Severity 2 reflects that this is a real, credible stress signal (personnel capture) but not yet a high-severity structural breach.
- [Mother Jones] A MAGA activist flooded Georgia with voter challenges. Now he works for the State Election Board. - Mother Jones (2026-09-14) - https://news.google.com/rss/articles/CBMi6AFBVV95cUxPY3B6V1ZMWWpwWUZMNmo5NkN5bzZOQ3plRGE2d1lxcUNKbktiTGVmWDRjc3p0dkMzQkJMNmtFR3ZySGxBX3VodEZEanh5OEh1WVlXSjlLU2VzSUhKVGIxSU41VzFhZktyaDdXcjBWUmFZcDVUdXc3MlJtTWZmcWFMSUhtb0RPTWs5NTVyTm9UN1VZZDh1cF9US2RmMG1lbjk0WDRPaW43d2d6UVFobmRmaHVBNmxDcmFvUU5aTDYyaVpaOVloZHoxdDFhMlJKZVl6SDd1Q2N0SGtqRUM2Z0xjVzVBeFF5aF91?oc=5

### Judicial Review Foreclosure
- Assessment: An emergency motion to stay an injunction pending appeal is a threshold procedural action that, if granted, would foreclose judicial review of the underlying merits by suspending the injunction without addressing legality. The filing of such a motion by government defendants (LaRose and Norman) and its docketing by the court represents a real procedural event seeking to remove active judicial oversight of government action. This is credible evidence of judicial-review foreclosure via emergency-docket mechanism—a contained stress signal of moderate severity. However, the record shows only that the motion was filed and entered, not whether it was granted; a granted stay would elevate severity. As filed, this constitutes a confirmed action that manifests the signal's mechanism (threshold grounds used to bypass merits review), though the outcome remains pending.
- [courtlistener.com] **[official record]** Red Wine & Blue v. Frank LaRose (2026-09-09) - https://www.courtlistener.com/docket/74762684/5/red-wine-blue-v-frank-larose/

### Emergency Powers Expansion
- Assessment: A presidential continuation of a national emergency declaration is a real, documented action that invokes emergency authorities to maintain powers that bypass ordinary legislative process. This is an official Federal Register record of an executive action. However, this represents a routine renewal of a long-standing emergency declaration (post-9/11 terrorist emergency), not a novel expansion or structural breach. The National Emergencies Act (50 U.S.C. § 1601 et seq.) permits such continuations and requires congressional notification. While emergency powers do bypass ordinary process, this is within the statutory framework and constitutes a contained, recurring action rather than a new seizure of authority or defiance of legislative/judicial check. Severity is 2: a credible, real stress signal (emergency authority maintained) that is repetitive and authorized by statute, but not a serious novel violation or structural failure.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Certain Terrorist Attacks (2026-09-10) - https://www.federalregister.gov/documents/2026/09/10/2026-18589/continuation-of-the-national-emergency-with-respect-to-certain-terrorist-attacks

### Legislative Oversight Obstruction
- [Legis1] House Panel Moves Toward Contempt Vote on Leon Black Over Epstein Ties - Legis1 (2026-09-14) - https://news.google.com/rss/articles/CBMieEFVX3lxTE1hVWM1dWUzamJ0c3BKODRvbERrWmQyRjVaZWg1Wk1wVkdpbW9jUHUzbUgxSlFIYmZqVy1QRHJQQjZENjdGSElJR29YWFNjWDRZcGg2dmlGMUtYcVhkX2ZvQjNWUk5RSjYyYmVIeG5qeWlLb01uaml6OQ?oc=5

### Legislative Bypass by Executive
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 17 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
