# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-23 12:30:13 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **10 / 100** (Baseline Institutional Noise)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **-1.4**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.65 | 1.62 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 2 | 4 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 1 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: The item reports a verifiable executive order requiring federal contractors to obtain White House approval before responding to Congressional requests. This is a real action that shifts a governance function (Congressional oversight/contractor communication) from statutory process to executive gatekeeping. However, severity is 2 rather than 3 because: (1) the scope is limited to federal contractors, not broad executive authority; (2) it represents executive overreach but does not constitute outright defiance of law or structural constitutional failure; (3) it is a single, contained action rather than part of a confirmed campaign to systematically dismantle checks and balances. The order is likely legally vulnerable but has been issued as binding executive direction, making it a real signal rather than a proposal.
- [NPR] Trump orders federal contractors to check with White House before responding to Congress - NPR (2026-11-21) - https://news.google.com/rss/articles/CBMieEFVX3lxTE5iVVMyejhOQXItTVVVdmVsQTR1SFBGeGVMWUI4enZsYkU1SW9DQ1hSbW1hNmo3SlFkdDBJSl82WEgxVlVGMGx0cUdETWJrcEJWamdUa3ZlbVZsWTUxUmN4REdKOHZrV3NfcmZMaFJneDJXdFFQOUNyYw?oc=5
- [Limapagi] Trump Restricts Congressional Access to Federal Contractors - Limapagi (2026-11-22) - https://news.google.com/rss/articles/CBMidkFVX3lxTE9BS1N4ajh2alhYNUk4WEV2eWtyZk9YRTU2WTJLV3h6OHVhbHhZdkpXTm5FZEZySkRzTGUteXVDM3hCeGtrS3lxV192WW9IOF9WZ3BMNVZtdnNVN3ExYlRZUGpXd09rQkFrc0NUWTVrVVhpVEN1Unc?oc=5

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-11-21) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Press Restrictions or Retaliation
- [The New Arab] Thousands protest closure of pro-opposition Turkish media outlets - The New Arab (2026-11-22) - https://news.google.com/rss/articles/CBMimwFBVV95cUxOWUVKbGFybmNsdnNBc3Z3VmkzNGVLd3NUaDFWTW5ramNlMVBoeFF5b0VqUXBsMmlZbGJTT2twUTJYSVlGLWo0MWRLck52MjcxaXlqU01LakJpR1R0MTNpWlVCbzBhMEdIVkNVMWZaOUhyWFduUnNuaV9Kbm0tMzlvb2lPVE9BQ1d3VEJJX0dTV3dGOUJOR0psRG5MTdIBmwFBVV95cUxOWUVKbGFybmNsdnNBc3Z3VmkzNGVLd3NUaDFWTW5ramNlMVBoeFF5b0VqUXBsMmlZbGJTT2twUTJYSVlGLWo0MWRLck52MjcxaXlqU01LakJpR1R0MTNpWlVCbzBhMEdIVkNVMWZaOUhyWFduUnNuaV9Kbm0tMzlvb2lPVE9BQ1d3VEJJX0dTV3dGOUJOR0psRG5MTQ?oc=5
- [The Business Standard] Thousands protest closure of critical media outlets in Turkey - The Business Standard (2026-11-23) - https://news.google.com/rss/articles/CBMipgFBVV95cUxNQzJZVVlvbWN5YWFnbXFtYzNnYVN3SUZzMU5tazhMM2hGb0plQzlrMUY2YnFKbjZWclZGY1BCS2hkX3hXclp5RENuQjlqSktJYXFaM29kZ1lhclJGT3NCakZ6azYyVVIwZUhIT0t3cXRkZ3dLc0otamlKVm1SRmhXTjhLbnVpQ193M3hFTHByNmJ2ZWNCYlJRYzVrSXJ5NFdaOTZLYWR3?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 7 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - election_certification_interference: courtlistener: HTTP Error 401: Unauthorized
  - election_delay_or_cancellation: courtlistener: HTTP Error 401: Unauthorized
  - alternate_elector_scheme: courtlistener: HTTP Error 401: Unauthorized
  - politicized_prosecution_opposition: courtlistener: HTTP Error 401: Unauthorized
  - opposition_ballot_exclusion: courtlistener: HTTP Error 401: Unauthorized
  - court_order_noncompliance: courtlistener: HTTP Error 401: Unauthorized
  - judicial_review_foreclosure: courtlistener: HTTP Error 401: Unauthorized
  - independent_agency_capture: courtlistener: HTTP Error 401: Unauthorized
  - inspector_general_retaliation: courtlistener: HTTP Error 401: Unauthorized
  - military_domestic_political_use: courtlistener: HTTP Error 401: Unauthorized

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
