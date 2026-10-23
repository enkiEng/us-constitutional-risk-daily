# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-23 12:40:50 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **+2.0**
- Delta vs 7-day average: **+1.9**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.65 | 2.27 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.98 | 2.46 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 3 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Public Funds for Political Promotion | civil_liberties_information | 1.65 (Watch) | ai | 0 | 2 |
| Opposition Ballot Exclusion | opposition_pluralism | 1.65 (Watch) | ai | 0 | 1 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 4 |
| Inspector General Retaliation | civil_service_integrity | 1.30 (Watch) | ai | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-10-21) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Civil Service Purge / Schedule F
- Assessment: Final rule issued by OPM expanding the scope and legitimate uses of administrative leave, including explicitly for 'workforce realignment initiatives.' This is an accomplished regulatory action (not a proposal) that creates new legal authority for executive discretion in removing or repositioning civil servants. Administrative leave can facilitate workforce removal without competitive process protections. Severity 2 because this is a real, confirmed action that materially expands tools available for politicized personnel actions, but it is a procedural/regulatory change rather than a demonstrated mass removal or targeted purge yet executed.
- [federalregister.gov] **[official record]** Administrative Leave for Workforce Realignment and Other Purposes (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21320/administrative-leave-for-workforce-realignment-and-other-purposes
- [federalregister.gov] **[official record]** Elimination of Time-in-Grade (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21319/elimination-of-time-in-grade
- [federalregister.gov] **[official record]** Managing Senior Professional Performance (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21316/managing-senior-professional-performance

### Public Funds for Political Promotion
- [notus.org] The DNC Says MAGA Inc. Is Airing Another Ad Created With Taxpayer Dollars - notus.org (2026-10-21) - https://news.google.com/rss/articles/CBMiY0FVX3lxTE5wU0E1dUptcnJTT0RYejdSSDlSMThWVzRMWF9TTXo1X05wVWtDQk10ZEVGRGl5QS1FU21wMTlDM3FrQlBGRDIwYVNXQ09zMlRnYVhNWnpnRmMxQ0RiSjJPU1lxSQ?oc=5
- [International Trade Union Confederation] Corporate Underminers of Democracy 2026 - International Trade Union Confederation (2026-10-21) - https://news.google.com/rss/articles/CBMic0FVX3lxTE14ZU9NbThDQ2p3Q3hMVnpfQ08tRGw0Ykg3OE5laGNyVHo1Z2NzSmFqam93VlgwcXp3N2NVYnRTNHE2NVBYc09RelB0TTBZMG5QU0FiX2tSbG5xd0MwTzkyQmhfMV81TEpoekFFbTJQcWNZQmc?oc=5

### Opposition Ballot Exclusion
- [IOL] Court rules Mbalula unlawfully removed Lungisa from ANC election list - IOL (2026-10-23) - https://news.google.com/rss/articles/CBMivgFBVV95cUxPSm1WM1JYdWlUYWRzRklDbnByYi0tZmlBSmFsN2tHaWRWVDViN3hnVmpJRS1zVEstUy1POC1sRzBlZV9wU0ZzX1o2RlBXOEJSUll5cDZwV0xDRzVIaVVrN2M0MFJkVXBkajZTQjU1YW1aS3plakl0dG5aWjBpVHRUbG5FSDdONlg0LVpJWVdJZXBWSlFnU3k0RmZKRnl4cGZ1Zkk2LXZpQ0VZYkpzV0lGeUtlWU1YUHgxeVRTdmJB?oc=5

### Press Restrictions or Retaliation
- [Freedom House] Sudan: Freedom on the Net 2026 Country Report - Freedom House (2026-10-22) - https://news.google.com/rss/articles/CBMiZkFVX3lxTFBBeGJkaEhuSFlQVmNhZ2tDUFZBQXo4VjZ1SmRINHVDTkZDdHlYVVluazZIbl96Mk1pT1luaE8zRGZpd3prdUtETDNpLWRQLUk2N2l0RU9uZTVDV0dpTklCQ1F4ODVGdw?oc=5
- [Tech Policy Press] Age Checks, AI Regulation and Censorship Put Internet Freedom Under Pressure - Tech Policy Press (2026-10-22) - https://news.google.com/rss/articles/CBMiogFBVV95cUxNM0wtcGQyY0dvY3pBMmRSNEd2ZXNpcmx5T2tRcGJDaEN4WUt6amxvTHg1ZFJtSXpNeUpILVJCNlRtVkY2RkN6aS1hYXdGQ3E4RWxRdWFudm90U3Q2REloU1pZbHlTaVV3VlFOcXVFR01mbFFicldTc2poTExxV2RtQUYtajk2em4zZGMwdnBscWxET2VuZnVJNnUwSzItU3FrZ0E?oc=5
- [Journalism Pakistan] Could the White House press pool model work in Pakistan? - Journalism Pakistan (2026-10-23) - https://news.google.com/rss/articles/CBMilAFBVV95cUxONUhFRUJ5alBQUGZhaTR3cU92ZXR3RnZveEU3U3hDdjlEeG1pZ2F4RWlpV1NmYXZTS3Fkb3ZwZ0tZanVEN1U1VVZFUXlMaVRxaGdlZ1RQZW02aXFfMDkyQ3NOYjRocC05MzNodHgyUnFzQnBjeGhuOU1LMzRfVXdiYWI0TmlXR2dQZUJIUk44dHpOSDN2?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 26 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
