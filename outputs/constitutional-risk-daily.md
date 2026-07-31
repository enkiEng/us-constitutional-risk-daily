# Constitutional Risk Dashboard (0-100)

- Generated: 2026-07-31 14:39:56 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **7 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-2.6**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.33 | 1.79 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 0.43 | 1.41 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 1 | 1 |
| Election Administration Capture | elections_transfer | 1.30 (Watch) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Opposition Ballot Exclusion
- Assessment: A Libertarian gubernatorial candidate was removed from the ballot in Iowa and is planning to appeal. This is a confirmed real occurrence of ballot exclusion of an opposition candidate. The fact that an appeal is being filed confirms the removal happened. However, without evidence of systematic, statewide, or coordinated removal of multiple opposition candidates, and given that legal challenge mechanisms appear available, this represents an isolated or contained action rather than structural failure. Severity 2: real but not yet confirmed as part of a systematic campaign.
- [Iowa Capital Dispatch] Iowa Libertarian gubernatorial candidate plans to file appeal in ballot removal case - Iowa Capital Dispatch (2026-07-29) - https://news.google.com/rss/articles/CBMixwFBVV95cUxPcmpTZGx4MkpaUW1Xb0FHX21iTS1rVk9PN1FDMlV5MzVNNlZOdmxKdGt5dFdwdnZfa195TzYyZERTdGRmaFgtdzIzUS1hT0NCZHdfTHlZSGNvR0tRTEFMWm5ielIwR1JNNjliSW5jZ2Y5WVdfZURCY1JBTkRoUjZzVHdMUEYzVnZpNF92Skk4aXhiNTFXTFRDcndlU2FfRUJ0UUZGSDdlMDUxc3QwUlNsQWI2akNGTGxyYmFHU3pEQXFRNFhHU2RF?oc=5

### Election Administration Capture
- No fresh evidence links in the current lookback window.
### Legislative Bypass by Executive
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 10 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
