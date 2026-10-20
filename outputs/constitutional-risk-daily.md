# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-20 12:42:16 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **14 / 100** (Baseline Institutional Noise)
- Previous day delta: **+7.0**
- Delta vs 7-day average: **+5.1**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.08 | 2.71 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 4 |
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 2 | 2 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | keyword | 0 | 0 |
| Public Funds for Political Promotion | civil_liberties_information | 1.60 (Watch) | ai | 0 | 3 |

## Evidence Samples

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-10-19) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Opposition Ballot Exclusion
- Assessment: A sitting U.S. mayor was removed from a reelection ballot. This is a real ballot-exclusion event in a U.S. jurisdiction. However, severity is 2 rather than higher because the exclusion appears to be grounded in a specific, facially neutral compliance issue (cashier's checks regulation) rather than systematic political targeting. No evidence presented of a pattern or defiance of legal process. The action occurred through apparent application of existing rules, not through extrajudicial or unconstitutional removal mechanisms. This is a contained, credible stress signal but not a structural constitutional failure.
- [Caribbean National Weekly] North Miami Mayor Alix Desulme disqualified from reelection bid over cashier’s checks - Caribbean National Weekly (2026-10-20) - https://news.google.com/rss/articles/CBMiygFBVV95cUxNYlBRalpTU0pMQ0JnV0pEeFJJNVNXbzJOZzJGQWVIeFlhQUZfWFhtT3VxSzhuMlNSSnZCTHYxX2tRMzl0djFSNlo3U2ZQQlV1ZVFEci1fOEowYUhKb3g3dkF3ZmNpWXlGdzBLQTNJQkRsR0s4UHBDSjE4bDZhRkplVnVlcXY0bVBnbkJZcEJKck92c1Bra2ZraWZkc2VDbk1ZTE9xbWhzNkhMVjlrY0RDeXBzM0dJc0NadHJ4S2xzOTI3LTkzdHlxTTNn?oc=5
- [Miami Herald] As early voting begins, North Miami mayor is disqualified from ballot. Here’s why - Miami Herald (2026-10-19) - https://news.google.com/rss/articles/CBMimAFBVV95cUxNNVZnSDZoMEpjenU1aWNwQ3pDaHZBcE4yVF9XQ2l3SzZwS2ZxRjRmQ1VNdEgtU29GbzRETml3TVZWSWlZRUhRMHNfaHg5bElSWHFsT05veXFfdFdSMXhUbzVVQ1dPYTRqS29rQ1JEby15eGFoYjNyMldST0hJWHFVLTNFZjQtQl9QUi1MUmRpZlZQeFZBV1lhQtIBmAFBVV95cUxOQ2FTam5BRFhoUzROOU9yWkZmbmdfSzNmenB0NUY3aVJPSGdCa2dnbnVUUTNHWXgyNlUwbEFucUpiYkU3Q3NDLUZaSlI3NHRIRHU0XzZSU1ZTT2JLSmdFajlhazZTNmk2NXdkRDdHaVN4Q1Mtc2lDSGtHbk5VX3QwUXlldDdEUjd6RHNxVXBYbDRiWGFybkx3Rg?oc=5

### Civil Service Purge / Schedule F
- Assessment: Final rule issued by OPM expanding the scope and legitimate uses of administrative leave, including explicitly for 'workforce realignment initiatives.' This is an accomplished regulatory action (not a proposal) that creates new legal authority for executive discretion in removing or repositioning civil servants. Administrative leave can facilitate workforce removal without competitive process protections. Severity 2 because this is a real, confirmed action that materially expands tools available for politicized personnel actions, but it is a procedural/regulatory change rather than a demonstrated mass removal or targeted purge yet executed.
- [federalregister.gov] **[official record]** Administrative Leave for Workforce Realignment and Other Purposes (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21320/administrative-leave-for-workforce-realignment-and-other-purposes
- [federalregister.gov] **[official record]** Elimination of Time-in-Grade (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21319/elimination-of-time-in-grade
- [federalregister.gov] **[official record]** Managing Senior Professional Performance (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21316/managing-senior-professional-performance

### Press Restrictions or Retaliation
- No fresh evidence links in the current lookback window.
### Public Funds for Political Promotion
- [notus.org] DNC Asks Judge to Stop New MAGA Inc. Midterm Ad From Airing - notus.org (2026-10-19) - https://news.google.com/rss/articles/CBMiY0FVX3lxTE40MU9lMm9RNjZwdFh3RnJLSlUzX1hhVVl3VnozbDVYNGtFTklTeXZiUERNcHVST2VUQ0p3WDM3M0Rqd1VtWUxZZm42blFZMzczdnBqenNRRTNzTjhpMUdkYzRmVQ?oc=5
- [Zeteo | Substack] Why Is Israel Running TV Ads in Iowa Ahead of the Midterms? - Zeteo | Substack (2026-10-20) - https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5NVnJ6ajViU2h6UjNUTHZxcG9JTEs4cFpSM2pCVXJWWUZGd3RnWWxwQzd4N1FrVkMyZjdXRW1ockd4ZzdWeTJYd0FTdDY3SlRBd2taTTBFMzBEOTBOcmV3aFB5aGZHY1E?oc=5
- [The Washington Stand] Socialist Mexico Contributes to Castroist Propaganda for Children - The Washington Stand (2026-10-19) - https://news.google.com/rss/articles/CBMiowFBVV95cUxQRk9aVEo1VVhBdkF6QnVhcUF3TGVYY3pWWnB1Qjh3akNEM0lkUTh4SmtwVFBuenRPM3ZEN2RQYVB2M1c4VHZwc1Z6VlA4UGJ3RVR5bXM2c1pSbE1UWi14WnhNc2J0M2VMM1RGRkhYWlR0UGZGS2syTjBDdVk2QWVFMll2b1d3S19HSTUtQmNNcUIzNi1TMHZERFg3NTZsU0ZGTUV3?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 17 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
