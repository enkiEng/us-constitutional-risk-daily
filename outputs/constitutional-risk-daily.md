# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-29 16:46:38 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **15 / 100** (Elevated Strain)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **+1.6**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.24 | 1.31 |
| Judicial Independence and Rule of Law | 15 | 0.32 | 1.19 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 1.32 | 4.28 |
| Civil Service and Agency Independence | 10 | 1.30 | 3.25 |
| Civil Liberties and Information Environment | 10 | 0.65 | 1.62 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Independent Agency Capture | civil_service_integrity | 2.30 (Yellow) | ai | 0 | 1 |
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 1 | 2 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.95 (Yellow) | ai | 0 | 2 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 3 |
| Election Administration Capture | elections_transfer | 0.95 (Watch) | ai | 0 | 2 |
| Politicized Prosecution of Opposition | opposition_pluralism | 0.95 (Watch) | ai | 0 | 1 |
| Targeted Jurisdiction Stripping | judiciary_rule_of_law | 0.95 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Independent Agency Capture
- [courtlistener.com] **[official record]** Dillinger's LLC, a Wyoming Limited Liability Company and Ryan Clement, an Individual v. CR-GTD, LLC, a Wyoming Limited Liability Company and EFTI, LLC, a Wyoming Limited Liability Company (2026-08-25) - https://www.courtlistener.com/opinion/10957585/dillingers-llc-a-wyoming-limited-liability-company-and-ryan-clement-an/
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-08-29) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Opposition Ballot Exclusion
- Assessment: A court ruling preventing the Iowa Libertarian Party from replacing candidates on the ballot for governor and Congress nominees is a real, judicially-ordered exclusion of opposition candidates from the ballot. This represents a credible, confirmed action (a court order) that removes opposition candidates from meaningful ballot participation. The action is narrow in scope (one party, one state, specific offices) and is subject to appeal, limiting severity to 2 rather than 3+. However, it is verifiable evidence that systematic removal has occurred through judicial order.
- [The Des Moines Register] Judge says Iowa Libertarians can't replace governor, Congress nominees - The Des Moines Register (2026-08-27) - https://news.google.com/rss/articles/CBMi7AFBVV95cUxPNTd6T0NGWjh6TVNJNUlLaGJoeTJTN0VFWjFneDdPV0RSaUkzMTFVOUpTd0xidmx5ZHVQRFhkemN3RUZla2lfbk5DaHVEbDB0N3lUMGRBNVZJeUxJak95cmQ1US1OeDI3b0Rfd09vUTVJdGJvQndLdWxwY1BMOXZzdWZhZ0hla1R2UWxaa051OFNMUE1nMW1talhKdTl4UC1DYWw1WGZ5b0VLRE5DdmJzekg1NjgzZmZoWDliaTJCWUYxbldJd1doOS1vS3JzclR6ekN3alZZSldCaDl0T2k4Y3BKaUQ3YXRycGpRYw?oc=5

### Emergency Powers Expansion
- Assessment: A presidential emergency declaration, published in the Federal Register, is a verifiable use of statutory emergency authority to invoke powers that bypass ordinary legislative process. The National Emergencies Act (50 U.S.C. § 1601 et seq.) permits the President to declare a national emergency and activate specified statutory powers without a new legislative act. This document itself constitutes the exercise of emergency authority. However, the severity is 2 rather than higher because: (1) emergency declaration authority is congressionally authorized and contemplated by law; (2) without the full text of the declaration and its specific invocations, the scope of actual powers being deployed cannot be verified; (3) this represents a legitimate if stress-laden tool rather than an unconstitutional usurpation. The mere invocation of emergency power for critical infrastructure (bulk-power system security) is a real constitutional stress signal—bypassing the ordinary appropriations and regulatory process—but not yet evidence of structural failure or clear defiance of law.
- [federalregister.gov] **[official record]** Declaring a National Emergency To Secure the United States Bulk-Power System (2026-08-31) - https://www.federalregister.gov/documents/2026/08/31/2026-17843/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system

### Civil Service Purge / Schedule F
- Assessment: This is an official Federal Register document confirming that OPM has issued a final rule titled 'Improving Performance, Accountability and Responsiveness in the Civil Service' (published February 6, 2026, effective March 9, 2026). The August 25, 2026 entry is a technical correction to that rule. The original February rule directly addresses civil service structure and performance accountability, consistent with Schedule F concerns about reclassification of career positions. As an issued final rule effective before this correction, it represents a material structural change to civil service rules. The correction itself confirms the underlying rule exists and operates. Severity is 2 (repeated/credible stress signal, real but contained action) rather than higher because the document excerpt does not detail the specific reclassification powers granted, only that such a rule has been issued and corrected. The fact that a major civil service reform rule exists and is being administratively refined constitutes verifiable evidence of civil service policy change, though the full scope of at-will reclassification authority is not detailed in this excerpt.
- [federalregister.gov] **[official record]** Improving Performance, Accountability and Responsiveness in the Civil Service, and Recruitment and Relocation Incentive Waivers; Correcting Amendments (2026-08-25) - https://www.federalregister.gov/documents/2026/08/25/2026-17334/improving-performance-accountability-and-responsiveness-in-the-civil-service-and-recruitment-and

### Legislative Bypass by Executive
- [ColombiaOne.com] How Far Can De la Espriella Really Go in Dismantling Total Peace and the FARC Peace Accord? - ColombiaOne.com (2026-08-27) - https://news.google.com/rss/articles/CBMieEFVX3lxTE5TdnZHQ0NZUENnbG1FM2dWcnlxM3d2Z0theElBYmRlQ29taU15cEJUak11eFRuSnhhMGNHLUxHbV95WDJSZzhqak1TRi10TW94eHNTeUQyNG1remRNTmpYMFMxV1RUc1NaMGJyOGJ6Q0JjcFZvWnIycw?oc=5
- [Newsmax] Trump Appeals New Court Block on Mail Voting Order as Midterms Near - Newsmax (2026-08-28) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxNeHlQNEI4eGpqcGVZODFDV2ozNnI3ekEyOHFOYjczd1FLYUF2U1FqbF9HUjROY0c4T3RKRzdkQ0kwY2JRaVpsRU85S1JGalpXMlZUd2t0SkZ6eFkwZkJ0LWVFTTdHWUFLbGZDYWp0Wm5COTZHeHRNMEVfN0FaUlBfSjh6b2lsMWE1MEVld0NmUk9zMHhma0tSV2lvSjhsb0c5SG1fdTFXc3hsTVdQWDV3S01YQllMWDdS?oc=5

## Data Quality

- Query feeds attempted: 23
- Query feeds successful: 23
- Query feeds failed: 0
- Primary-source lookups: 21 signals, 20 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
