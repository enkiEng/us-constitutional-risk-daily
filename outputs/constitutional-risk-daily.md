# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-31 12:25:18 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **15 / 100** (Elevated Strain)
- Previous day delta: **-4.0**
- Delta vs 7-day average: **-6.3**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.60 | 3.30 |
| Judicial Independence and Rule of Law | 15 | 0.15 | 0.56 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.06 | 0.16 |
| Civil Liberties and Information Environment | 10 | 1.10 | 2.75 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.97 | 1.95 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 3 | 3 |
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 1 | 3 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 1.95 (Yellow) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 1.60 (Watch) | ai | 0 | 8 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.60 (Green) | ai | 0 | 2 |
| Court Order Noncompliance | judiciary_rule_of_law | 0.60 (Green) | ai | 0 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 0.25 (Green) | ai | 0 | 1 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: Campaign Legal Center reports that a court action successfully halted taxpayer-funded pro-Trump ads. This is evidence that public funds were spent on partisan political advertising (the signal itself), and that a court intervened to stop it. The halting by court order confirms the event occurred. However, severity is 2 rather than higher because: (1) the action was challenged and stopped by judicial intervention, indicating the constitutional check functioned; (2) we have only a summary title without access to the full order or details of the scheme's scope; (3) this represents a contained action that was enjoined, not an ongoing structural failure or defiance of the court.
- [Campaign Legal Center] Campaign Legal Center Action and Partners Successfully Halt President Trump’s Illegal Taxpayer-Funded Ads Scheme - Campaign Legal Center (2026-10-31) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxNZHMzN002ZGhPbE53bUEtclpRaXRERjR6M2RWV3NvNmxxcXQyRW1mMFloclZaRHlQb1BneXdvZ0xRblZvSU5PdWRnQkI2ekVhbldlaHZFcmhjY1BjU1ZMWi1IWjROYXN0LS16dVN2enk0alJuclZEN1lTRkNpakNFRWpINjFyUVJ6NkhoMEtSYXJkSGp0Sl85X18yUFRjOGdPandMd24zUVpfZEhRemZ3MmhCWHMzUlBB?oc=5
- [Courthouse News] Judge blocks 3 MAGA ads over concerns they breached taxpayer-funded propaganda law - Courthouse News (2026-10-30) - https://news.google.com/rss/articles/CBMiswFBVV95cUxNTzg5Y3p0R1ZwcFpPMlZ3OV9MZjAza3Y3ZVNfRVJYX3Nvd2lQaHM4TUUtMGhqeFZmX0NlTERPWEtRV180WmsxU1d2SmhwU1RPd0RKSGNOT0xQNXJKejVQel9oaDM0M0VDdlBPX0RZVFBhaTVkYmNJTjBBWkJubkRieXFJa2o1aVZpRkNQUGM1REw0N0xaZ0l4YkFjbThCNEpaXzlXTzZlMmdpM3ZVXzlCZVJsUQ?oc=5
- [Campaign Legal Center] VICTORY! Coalition Secures Second Court Order Blocking Trump and MAGA Inc. from Promoting Taxpayer-Funded Propaganda Ads - Campaign Legal Center (2026-10-30) - https://news.google.com/rss/articles/CBMiwAFBVV95cUxNdGpBX0taR3B6SHpndHR0MF9mSGJYQlNjM3pacTFrZjJzSmhVSGx0N2h1SjNLN3hYOE93Z2ZHQWtQNWstUjhJbkFmQzV3VW43am1VQ0NMRHRac21DZU04ZGxCN2NnZks1MzJlZUZ2dVlKelpIZl9pRTZhRXp1MnhseWQxRG1JQnQteVZ4cWVUdkpaRVp1REphMi01VXlqSXl5bDFJTElhT256RlFsRE9GVkRjQS1sRWt6X2xwTDVBWVM?oc=5

### Opposition Ballot Exclusion
- Assessment: A Florida appeals court has issued a ruling that upholds removal of an incumbent from a local ballot. This is a real, confirmed judicial action affecting ballot access. However, without further detail about whether the removal was procedurally proper, legally justified under applicable election law, or part of a systematic pattern, and given that it appears to be a single local-level action subject to appellate review (suggesting normal judicial process), this registers as a contained, credible stress signal rather than a structural failure. Severity 2 reflects confirmed action affecting a real candidate's ballot access.
- [Sun Sentinel] Appeals court upholds removal of incumbent from Tamarac commission ballot - Sun Sentinel (2026-10-30) - https://news.google.com/rss/articles/CBMitAFBVV95cUxOaXM3M3JhSUp6dWQ3UHduQVBhQ0ZNbDM1R05ndHh1SkwyRGM4U2ZnaTRSQmdPZzM5cUFiVmN4bVNkMFRMZ18zYjI3dElKNkktRHJvVllmWDdEVE5EdVhqbXhPMWUwSllUNk4ybjkzWDdNLS1kdzRxdnhtX1pTWmt4cDNNT01DdzdicU1oOFgxZnFzcVlOQTVMNEZvS0I2eHJXTW1Xc1ZHN25mU3BYTDVCWFFDSEo?oc=5

### Emergency Powers Expansion
- Assessment: A Presidential Determination under Section 303 of the Defense Production Act of 1950 is a lawful exercise of delegated emergency authority that does invoke statutory emergency powers to direct economic activity. Section 303 authorizes the President to require priority allocation and controlled distribution of materials. This is a real occurrence of emergency-powers invocation, documented in the Federal Register. However, it represents authorized use of congressionally-delegated wartime/emergency authority rather than an unconstitutional bypass of the legislative process. The DPA itself is a statutory grant of emergency authority enacted by Congress, so its invocation is use of authority granted in advance, not a constitutional circumvention. Severity is 2 (a real but contained, legally-authorized action) rather than 3+, as this is neither an extralegal assertion of power nor a defiance of constitutional constraint.
- [federalregister.gov] **[official record]** Presidential Determination Pursuant to Section 303 of the Defense Production Act of 1950, as Amended, on Domestic Petroleum Production, Refining, and Logistics Capacity (2026-10-28) - https://www.federalregister.gov/documents/2026/10/28/2026-22052/presidential-determination-pursuant-to-section-303-of-the-defense-production-act-of-1950-as-amended

### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- [The Washington Post] Trump administration retools its battle over elections to keep fights alive after Election Day - The Washington Post (2026-10-31) - https://news.google.com/rss/articles/CBMi2wFBVV95cUxPRGpZalZEVFBBcWgyOG9KakozUkpWVEktNXN2eVQycUM3RXY5TDZacXB2UjBwd1FIeTRNY2xDc3V6Z0VSeVdFc3BGaXNHeFBlcllvV05mZ3hEQ0ZtMzFCSUFLbzFrZzZJVmM0NFBBcTdDZ0NHa3RBNDRvOG1LUGl5R1doejJfQlY4eFJBT1EzajBRa05acDMyTTB0UjRVYzJqTXQxWnF0VDBPcUF3Yk1mZjBPclltQTZSNzI4cVVqWFZrV0tMalRxcWVaVFpVemJZbUhXOS1uT054LTA?oc=5
- [Campaign Legal Center] Why I’m Confident and Concerned as Election Day Approaches - Campaign Legal Center (2026-10-29) - https://news.google.com/rss/articles/CBMikAFBVV95cUxOT2w4Q0hHODJIYlUzOER0OU9sWjRES1d6dnlVX0hxWkc2ZDZOYnRsdzdIcFZMNFBwLXU3dmtRNlBXa3M5OUQyVTFJNmhWQmFobXkzbWZiZmZLN1VKOF93QmxMZmpFc0s2MFFPX2hUODBvSFJiMlJsSFoyNXRVNWhSTnVLb0VfX1RTdExTaXVVREU?oc=5
- [ProPublica] Trump Has Tried to Exert More Control Over Elections. Here Are the Key Findings From Our Reporting. - ProPublica (2026-10-30) - https://news.google.com/rss/articles/CBMiiAFBVV95cUxQejZQNkF0dHFIbGJldkdjajEzdmlaZkg3Q2FGZ2NHRjZvVExZdG8zclFyTkZtVml4QXhsU0xYQUpTYWF3T2N4eGo2dWFmMnZGVlVuM3VyejVvQWxsV3BnZ0RTdUZteGUxV0dldEpGbEZjWWpNUXdUME8tTW1Tb3NaSW80LUp4SWow?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 9 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
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
  - military_domestic_political_use: courtlistener: The read operation timed out

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
