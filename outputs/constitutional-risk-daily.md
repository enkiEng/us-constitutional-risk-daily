# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-04 14:16:30 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **10 / 100** (Baseline Institutional Noise)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **+1.6**

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
| Executive Constraints and Emergency Powers | 13 | 0.20 | 0.65 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.10 | 2.75 |
| Security Sector Neutrality | 8 | 0.50 | 1.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 6 | 8 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 4 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 2 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 1.00 (Watch) | ai | 1 | 0 |
| Legislative Bypass by Executive | executive_constraints | 0.60 (Green) | ai | 0 | 1 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: News report confirming that an administration aired TV advertisements promoting the officeholder using taxpayer funds. This constitutes spending of appropriated public money on communications that promote the officeholder rather than serve a public-information purpose, which directly matches the signal definition. The report itself treats this as a real occurrence (not hypothetical, opinion, or allegation), though the severity is moderate because this appears to be a discrete action that has been detected and is now subject to public scrutiny and potential legal challenge. No court order has been defied, no structural constitutional breakdown has occurred, but the alleged violation of the 1950s appropriations prohibition on 'publicity or propaganda purposes' is material.
- [abcnews.com] Administration's pro-Trump TV ad is taxpayer-funded - abcnews.com (2026-10-03) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxNNEc3UWRPWjdaWkt2Wk9vcklvTkd3LUU0eEFHNnBTNGE1M01jZ1ZsczFwN0o1VjVmMk9rU3kxOUx5M1N2V1MtLVRqNjFfUXJYV0FQeFJSV3pBSEJ1Y2NFV29FMzFGLUxmVGVRa2tVVnhwM3hRYVhzSnFRM2YzUklyR3BjQm4xOUltenU0V2lRSHB2SzJlVmpMLV9lMHdGT2dJU3FBZG5FVVnSAa4BQVVfeXFMT2lPdUJtQ0JKMEs1aVhMMUFfOXFWRmxwZlBsSk9LYjFHX3pMamdNOUV6c1BNZnQwdGtVUzRTMS1IVzJoWjl4c3Z1elZtdWotY2MwazN5UzhQNGk1TGtnSGJhMzI3WUNlY3BlemEzWGlNMkpGNnFjNXZiZU1vQVZ3SFRPYklhZjN1ek4wWUN3ZUt4YUxMcDJpTmhGMjhaVkg4Wm0tMm9CbERyWnVENjNB?oc=5
- [The New York Times] Trump Directed Use of Taxpayer Money for Ads Praising His Presidency - The New York Times (2026-10-02) - https://news.google.com/rss/articles/CBMibkFVX3lxTFBiejVxNFZGSTRKNlpwaTFSOUppTm9SOWJXVHJXblVVbkNTTklEQkZxLVQ0YlRDQUVHMWdsNkduUlcxWGpycmg3SFJLWDZQWDY2RDlld1AzN0NrOEVvVDNNOGxURFAzSFVTMFRCU1pR?oc=5
- [ABC7 Los Angeles] Trump defends spending millions on taxpayer-funded promotional ads: 'For the country' - ABC7 Los Angeles (2026-10-02) - https://news.google.com/rss/articles/CBMipwFBVV95cUxOU0hTaEotZmlGT1puOW84dk1rZnhlQng4R1ViYXBlXzZLUVQwM2Jyckt0bWIzQTV4cWV3Si1HZGlsYUtNVEl1R0Q3MWNWYTB2RTN3U3pxYjJ5dVlOOGV5UTMwaE9JTVN5bDRReVozUGdFTWpidUppSjlnUm5kUmIzTnNLS0M2YjA0ZHNPdDlIQ1FLWEhpa3NOR2FrWHFuUTUySnNTSlB3NA?oc=5

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-10-04) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Press Restrictions or Retaliation
- [Journalism Pakistan] Arrests and censorship tighten grip on global press - Journalism Pakistan (2026-10-04) - https://news.google.com/rss/articles/CBMijwFBVV95cUxNaVVISjFFTnN0Y2xkWWFtTExaU1dEOFJPc2o2QTlSQmlCYkpfYWtsa1lTUnMtMm5mbWR4RnVVZEZBZXgwZnBzdWlCakNlSmdkT2hhdTJmMlZLNmNvN21hb3pxRk85Z0dpSk1xOW5RNi11UW9DTFJvZVY2NlJGbDBiVTNMQmtaekctVVNrdVQxMA?oc=5
- [Journalism Pakistan] JP Global Media Review | September 2026: Bans, arrests and AI - Journalism Pakistan (2026-10-03) - https://news.google.com/rss/articles/CBMilwFBVV95cUxQWk94Qm9kZUxKSU8ta3gzbk5fU0ZXQU5QN3BjU1p3WVZzaHo3NGUyWTg0dlNuWTZhandmNThpQ1VRbmtxSTRDZlBxRUZMSjV2U01FblJpTi1Ea19aSnQxQVdGVmdLYkluVHpRWXJHV1FJcHN6YVVnd21PWXhIOVhiNTg2eDJrRDROV25fSmtaQVNJYkZlMXQ0?oc=5

### Domestic Military Use in Political Conflict
- Assessment: A civil complaint has been filed in federal court (D. Minnesota) naming multiple current and former federal officials. The complaint itself is an official record indicating that plaintiffs have asserted claims regarding potentially unlawful conduct by these defendants. However, without access to the complaint's substantive allegations, the severity cannot be determined beyond acknowledging that a legal action has been initiated. The filing is a real procedural event, but severity is limited to 1 because a complaint represents an allegation, not a proven occurrence, and the specific nature of the alleged conduct cannot be assessed from the docket summary alone.
- [courtlistener.com] **[official record]** Ganger v. Ross (2026-10-01) - https://www.courtlistener.com/docket/74901903/1/ganger-v-ross/

### Legislative Bypass by Executive
- [federalregister.gov] **[official record]** Rescissions Proposals Pursuant to the Congressional Budget and Impoundment Control Act of 1974 (2026-09-30) - https://www.federalregister.gov/documents/2026/09/30/2026-19965/rescissions-proposals-pursuant-to-the-congressional-budget-and-impoundment-control-act-of-1974
- [National Affairs] The Unfinished Work of Federal Permitting Reform - National Affairs (2026-10-04) - https://news.google.com/rss/articles/CBMimAFBVV95cUxOa0o4OXVkQkxHdXJ6VkxqLUNNTVhfQ0JFT3lYSDFLc2YycTlRUFV3VWp3TFhMMTgwSGZQaTdlU2RMNFBVZlV2Q05odjlFN3QwU0ZHVFh5QXE0OEJKRWh0dnR4ZGxFVk5KblVTWXI2UzJrRWlSeF9DWXAxX3lRNDRPMVBHdVlsdVZuemZZSjcyWGF0dUV1YnB3Xw?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 14 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
