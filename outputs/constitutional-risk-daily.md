# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-05 12:46:30 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **12 / 100** (Baseline Institutional Noise)
- Previous day delta: **+2.0**
- Delta vs 7-day average: **+3.1**

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
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.50 | 1.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 4 | 8 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 2 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 2 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 1.00 (Watch) | ai | 1 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.95 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: This report indicates that an ad aired during a major sports broadcast (FOX NFL Sunday) that is characterized as Trump propaganda and allegedly funded by taxpayers. The specificity (13 ads, $20M campaign, taxpayer-funding, named individual Natalie Harp at center) across multiple corroborating sources (items 4, 6) suggests a real campaign occurred rather than a hypothetical or rumor. However, the sources are press coverage rather than official agency records documenting the appropriation and authorization. The evidence is credible but not yet at the documentary level that would warrant severity 3+.
- [AOL.com] NFL fans furious as Trump 'propaganda' ad funded by taxpayers airs during FOX NFL Sunday - AOL.com (2026-10-04) - https://news.google.com/rss/articles/CBMigwFBVV95cUxQbDA4QjNWZ3NObjRSaWpwSGM0MlI0eUROLTFEdGwzNnpxcGpVZDBYZ0NWWDBTaUdtTXhibXFaWlQ1U0paUk1oWVNuNHZwdThBZUVOdzU3MFVtWUgxMkgxWEdsdmxVRTMxVDJpOUUxaFJ4aWpQRHNTbjhHaGNva1p2LTk0cw?oc=5
- [The Economic Times] “God Made Trump, the Country He Loves”: 13 taxpayer-funded ads and $20 million campaign revealed as Trump’ - The Economic Times (2026-10-03) - https://news.google.com/rss/articles/CBMiyAJBVV95cUxQODJRdnNEUDM5aWZiM1JLYzBpUElnUk9DUXA2NUFtdUNtNkNpQk1LSExjRXZDc3FCWnMwU3JlUGlibGNiRFRUVHVlOWJGQ0dBeVZuRjRmQVQxLXhXZEx0a1FFNUwtTTlPQTM2NU9uOVNQN3hxRmlCSE04YThvM0RyS1pOa3E5US00SERjMWZZLXpWSWxhU3NnVG14WTZ1YnNoZk41VWZsSFlvdjVLWWNRaXlRc3JwRDJYLTFoRktuZ2FZYkg5c0U1Zk45Sl9UbzlaN0ZYQU1iOEVMODN3RVU4c1gzaXBBSkkxTTFZSm5fMVNDTDdWLXJ5SUVTRWVtZk95bVFwSWtfUzZlRVlEWFBVRVAxRzc3MnVXSVJqQW1tWmFWNEN1bTk1Q0UtbGVkWUJ2U0FLcjkwYmZ5TElBUnNnNXJLdFB4eVB00gHIAkFVX3lxTFA4MlF2c0RQMzlpZmIzUktjMGlQSWdST0NRcDY1QW11Q202Q2lCTUtITGNFdkNzcUJaczBTcmVQaWJsY2JEVFRUdWU5YkZDR0F5Vm5GNGZBVDEteFdkTHRrUUU1TC1NOU9BMzY1T245U1A3eHFGaUJITThhOG8zRHJLWk5rcTlRLTRIRGMxZlktelZJbGFTc2dUbXhZNnVic2hmTjVVZmxIWW92NUtZY1FpeVFzcnBEMlgtMWhGS25nYVliSDlzRTVmTjlKX1RvOVo3RlhBTWI4RUw4M3dFVThzWDNpcEFKSTFNMVlKbl8xU0NMN1YtcnlJRVNFZW1mT3ltUXBJa19TNmVFWURYUFVFUDFHNzcydVdJUmpBbW1aYVY0Q3VtOTVDRS1sZWRZQnZTQUtyOTBiZnlMSUFSc2c1ckt0UHh5UHQ?oc=5
- [news.meaww.com] Natalie Harp at the center of Trump’s $20M ad controversy: What we now know - news.meaww.com (2026-10-03) - https://news.google.com/rss/articles/CBMinAFBVV95cUxNZ0Z5QXFPSExrX2tqNUU5eUlUOGF4dzZqVzlZclp5aXhNeU9yU0lsV1Rqcm9jTG53UU56NXd3UWx5a3JrX2NYSUU5UGxzVWIzSWthR01wMTNIa2kwRXB5VzFWNWpFcW84d3RzZVJXWU5QSUxqZVMxWUNLLXpBTGNqcWxUanNWUk9SM19Md2YtdjdzMXpKektsTElJV1A?oc=5

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [abcnews.com] Trump director of election security sparked Georgia office raid, affidavit says - abcnews.com (2026-10-03) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [abcnews.com] Supreme Court allows Trump to implement parts of his mail-in voting executive order - abcnews.com (2026-10-03) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5

### Domestic Military Use in Political Conflict
- Assessment: A civil complaint has been filed in federal court (D. Minnesota) naming multiple current and former federal officials. The complaint itself is an official record indicating that plaintiffs have asserted claims regarding potentially unlawful conduct by these defendants. However, without access to the complaint's substantive allegations, the severity cannot be determined beyond acknowledging that a legal action has been initiated. The filing is a real procedural event, but severity is limited to 1 because a complaint represents an allegation, not a proven occurrence, and the specific nature of the alleged conduct cannot be assessed from the docket summary alone.
- [courtlistener.com] **[official record]** Ganger v. Ross (2026-10-01) - https://www.courtlistener.com/docket/74901903/1/ganger-v-ross/

### Press Restrictions or Retaliation
- [Journalism Pakistan] Arrests and censorship tighten grip on global press - Journalism Pakistan (2026-10-04) - https://news.google.com/rss/articles/CBMijwFBVV95cUxNaVVISjFFTnN0Y2xkWWFtTExaU1dEOFJPc2o2QTlSQmlCYkpfYWtsa1lTUnMtMm5mbWR4RnVVZEZBZXgwZnBzdWlCakNlSmdkT2hhdTJmMlZLNmNvN21hb3pxRk85Z0dpSk1xOW5RNi11UW9DTFJvZVY2NlJGbDBiVTNMQmtaekctVVNrdVQxMA?oc=5
- [Journalism Pakistan] JP Global Media Review | September 2026: Bans, arrests and AI - Journalism Pakistan (2026-10-03) - https://news.google.com/rss/articles/CBMilwFBVV95cUxQWk94Qm9kZUxKSU8ta3gzbk5fU0ZXQU5QN3BjU1p3WVZzaHo3NGUyWTg0dlNuWTZhandmNThpQ1VRbmtxSTRDZlBxRUZMSjV2U01FblJpTi1Ea19aSnQxQVdGVmdLYkluVHpRWXJHV1FJcHN6YVVnd21PWXhIOVhiNTg2eDJrRDROV25fSmtaQVNJYkZlMXQ0?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 14 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - independent_agency_capture: courtlistener: The read operation timed out

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
