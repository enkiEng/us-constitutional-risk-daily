# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-29 12:33:05 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **20 / 100** (Elevated Strain)
- Previous day delta: **-4.0**
- Delta vs 7-day average: **-2.0**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.30 | 7.15 |
| Judicial Independence and Rule of Law | 15 | 0.33 | 1.22 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.10 | 3.57 |
| Civil Service and Agency Independence | 10 | 0.24 | 0.59 |
| Civil Liberties and Information Environment | 10 | 1.33 | 3.33 |
| Security Sector Neutrality | 8 | 0.30 | 0.60 |
| Federalism and Legislative Oversight | 8 | 1.65 | 3.30 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Oversight Obstruction | federalism_oversight | 2.65 (Yellow) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 2.30 (Yellow) | ai | 1 | 6 |
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 4 | 6 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 2 | 4 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | ai | 0 | 2 |
| Court Order Noncompliance | judiciary_rule_of_law | 1.30 (Watch) | ai | 0 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 0.95 (Watch) | ai | 0 | 0 |
| Election Certification Interference | elections_transfer | 0.60 (Green) | ai | 0 | 2 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 0.60 (Green) | ai | 0 | 1 |

## Evidence Samples

### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-10-29) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Public Funds for Political Promotion
- Assessment: Court order blocking taxpayer-funded partisan ads represents confirmed judicial action against alleged misuse of public funds for campaign-style promotion. The judge's issuance of an injunction is itself an action that changes legal status—the administration can no longer air these ads without violating the order. This is a real, credible stress event. However, severity is 2 rather than 3 because this is a single blocked campaign caught and restrained by judicial review, not a structural breakdown or pattern of defiance.
- [Common Dreams] Siding With DNC a Week Before Midterms, Judge Blocks Trump's Taxpayer-Funded 'Propaganda Campaign' - Common Dreams (2026-10-28) - https://news.google.com/rss/articles/CBMidkFVX3lxTFBaRnJfaE0xNnU5LWdFZVpTSHJKNzhnTHNINmJPSUVfWmlUTHNOVTFhZDhlU01aR2V1QWhYTkZRR0FJSGE5RVpCd1ExNzJNQ1RnTUFMSTVsWXQyQWlhSk5LODQyaFhSUTk5cjZlc2xHYldZdlZIalE?oc=5
- [The Independent] Trump barred from airing White House ‘propaganda’ ads, judge rules - The Independent (2026-10-28) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxNOEJkdmhSQklvQUdNY2xhV2hXaFpiZjFRQjFyNERvWG5rM1ZOek9pVmQxeVlyNnc2NmZaZmhpOU1MVHFqVFo5eFVIZmtxRWloYWVWMF9zU2pqRkVKc3VIOTRwVkxCRUloVWNWMzk1bURqX0h1VHpqLWxuU0pBWTU1MGhyRjZYWm8zT0JXZV9xVWlsdmpLSHQ0ZzRaZURCT1VUVW00YjAxUmxId1c0WUJPZTJFLWxkbGNy?oc=5
- [AOL.co.uk] 'Conceded the merits': Judge issues injunction barring Trump admin from using taxpayer funds for 'partisan campaign' ads, finds DHS likely violated the law - AOL.co.uk (2026-10-28) - https://news.google.com/rss/articles/CBMijgFBVV95cUxPS1V2VVdYdGZtbWxodHk4RldORjlFdG11dlpqeVpsc1NWRnY4TGwzQ3pEaVF0MTFpSGFORFM3alJRQUt0aFpfSEhRN0NhTEFRV194Q01DS1NuSUpIcTZtdG94dkdXY1NTUUZxbVJHYTFuaWRfRXNtdmZ2M0lfX2syVFZLSkxjSXVnTzdHempR?oc=5

### Press Restrictions or Retaliation
- Assessment: This reports that 6 citizens have filed suit against Trump alleging a news-media ban imposed by the White House. The existence of a ban (whether or not ultimately upheld) represents documented state action raising costs/legal risk for press entities and creating barriers to independent reporting. The lawsuit confirms the ban exists and is being contested. This is a real but currently contested action, hence severity 2 rather than 3 or 4. The date (2026) is future-fictional but treated as the scenario's present.
- [Free Speech Center] 6 citizens sue Trump, saying news-media ban deprives them of news as audience stakeholders - Free Speech Center (2026-10-27) - https://news.google.com/rss/articles/CBMixgFBVV95cUxQM2RuZFcxLXhzMzZScGdfN2tjeldsQk1QaGpZUkg3eXNMYTZwN1lGdWVSdWJUY0xqUXNSSjFNZXU1Y09HX3ZJMkRtMEl2aXBDa0owU3FtVTdBeHU3ZmVlVGhDckpsN1Y2Q1RDVUk0R0w2bGw5NDYwLWFqLWhvNlZNWnhGaXJrQzhULThCd2dsWjhoS0RhWG1fbFRvMmpnVF9McDFhR3huV08zUXFoV01BRWJpNlI2Tm9FV2w1T3htcUwtSXdvZ0E?oc=5
- [Journalism Pakistan] US citizens seek broad injunction over White House press ban - Journalism Pakistan (2026-10-27) - https://news.google.com/rss/articles/CBMinAFBVV95cUxPVWc5YXJqY3RSQWF3RlJPXzJkSWV4VDhJcHBlTW1Hek1Sc1RBWW15U1NNQmROTVpTRlRsenIyYkZ4aVlJZFhOQlIyT1JJTDRvdkd4c3p6dnVYaE16VTZjQ2Vrckl2QUZ2elFfZ0lfZkI4T3VOVE4wakJCTU9xU1c2S2ZzMmgzZTQ5M0d3MHZKUlBfZi0xOHNLeDZKU0I?oc=5

### Emergency Powers Expansion
- Assessment: A Presidential Determination under Section 303 of the Defense Production Act of 1950 is a lawful exercise of delegated emergency authority that does invoke statutory emergency powers to direct economic activity. Section 303 authorizes the President to require priority allocation and controlled distribution of materials. This is a real occurrence of emergency-powers invocation, documented in the Federal Register. However, it represents authorized use of congressionally-delegated wartime/emergency authority rather than an unconstitutional bypass of the legislative process. The DPA itself is a statutory grant of emergency authority enacted by Congress, so its invocation is use of authority granted in advance, not a constitutional circumvention. Severity is 2 (a real but contained, legally-authorized action) rather than 3+, as this is neither an extralegal assertion of power nor a defiance of constitutional constraint.
- [federalregister.gov] **[official record]** Presidential Determination Pursuant to Section 303 of the Defense Production Act of 1950, as Amended, on Domestic Petroleum Production, Refining, and Logistics Capacity (2026-10-28) - https://www.federalregister.gov/documents/2026/10/28/2026-22052/presidential-determination-pursuant-to-section-303-of-the-defense-production-act-of-1950-as-amended

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 9 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **High**
- Fetch errors:
  - election_certification_interference: courtlistener: HTTP Error 401: Unauthorized
  - election_delay_or_cancellation: courtlistener: HTTP Error 401: Unauthorized
  - alternate_elector_scheme: courtlistener: HTTP Error 401: Unauthorized
  - politicized_prosecution_opposition: courtlistener: HTTP Error 401: Unauthorized
  - opposition_ballot_exclusion: courtlistener: The read operation timed out
  - court_order_noncompliance: courtlistener: The read operation timed out
  - judicial_review_foreclosure: courtlistener: HTTP Error 401: Unauthorized
  - independent_agency_capture: courtlistener: HTTP Error 401: Unauthorized
  - inspector_general_retaliation: courtlistener: HTTP Error 401: Unauthorized
  - military_domestic_political_use: courtlistener: HTTP Error 401: Unauthorized

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
