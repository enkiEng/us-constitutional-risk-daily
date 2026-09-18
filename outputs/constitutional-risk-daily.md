# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-18 16:31:34 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **14 / 100** (Baseline Institutional Noise)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **-0.2**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.24 | 1.31 |
| Judicial Independence and Rule of Law | 15 | 0.24 | 0.89 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 2.00 | 4.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Oversight Obstruction | federalism_oversight | 3.00 (Orange) | ai | 1 | 12 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Statistical Agency Integrity | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Election Administration Capture | elections_transfer | 0.95 (Watch) | ai | 0 | 1 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 0.95 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.25 (Green) | ai | 0 | 2 |

## Evidence Samples

### Legislative Oversight Obstruction
- Assessment: DOJ assertion that a House-issued subpoena no longer obligates testimony constitutes a direct obstruction of legislative fact-finding. The DOJ has taken an affirmative position that removes the binding effect of a lawful legislative subpoena without a court order or statutory authority. This is a confirmed high-severity action blocking executive accountability to Congress in an ongoing investigation. The systematic claim (that the subpoena 'no longer obligates') represents an official position that strips the House Oversight Committee of its core fact-finding power in this matter.
- [ABC News - Breaking News, Latest News and Videos] DOJ says House Oversight's subpoena 'no longer obligates' Bondi testimony in Epstein matter - ABC News - Breaking News, Latest News and Videos (2026-09-16) - https://news.google.com/rss/articles/CBMirwFBVV95cUxORTJiZlVKWkpFTkRRTnUtaVl2MkptSGRSZ1ROV1pyV3dLNFdyRGV6RDRybUJXMzgySjJkYUhsbGdHNGw1Mmw4VExNY1JaMENkSWtFeE5qM3pOUk9seW42eHhCYTQ0ZUcxLTM5TXdTQVdwOHVsVlFmUUpTQ0J0TGEwYVFLaHN5d3pHTGlVaTBhc1BHdFZvdzN5MzVrenZ3VldUcnhmSXZKRTlDWEUtQ1Q00gG0AUFVX3lxTE5ad3ZZQm5USXplejJSZkdVTnNHcUJ2U3ZLTlhnUTR1RTU5WVFjYVRoM181UW9sV1RJdnMtUWNiVXJ6WjQ2T3dyZ1FmaWxmWnh6cHdMTmFSaWgtZzVjNHlhN05BR09IX2p0Mk9FTEVVYU5yTFVkbFdNU3hpanhGaFpXU2ZZeEdKRzZscGRVVnJ5SlM4UHF5c0lBQ2FkN1pvdkd0UjBIN3JkN0ZIUjdNeDN1bVE0Yg?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-09-17) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Emergency Powers Expansion
- Assessment: This is an official record of continuation of a pre-existing national emergency declaration. The continuation itself is a routine renewal mechanism established under the National Emergencies Act (50 U.S.C. § 1601 et seq.), whereby the President may extend a declared emergency for successive one-year periods without new legislative authorization. While this document confirms the use of emergency authorities to maintain expanded executive powers outside ordinary legislative process—and therefore matches the signal—the action is procedurally lawful, statutorily authorized, and represents the normal operation of the emergency declaration system rather than an expansion or abuse of emergency powers. The severity is 2 (a real but contained and legally-authorized stress signal) because emergency declarations do represent a bypass of ordinary process, but this particular continuation is a standard recurring action, not a novel expansion or defiance of law.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Persons Who Commit, Threaten To Commit, or Support Terrorism (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-19053/continuation-of-the-national-emergency-with-respect-to-persons-who-commit-threaten-to-commit-or

### Statistical Agency Integrity
- Assessment: This is an OFFICIAL RECORD—a final rule issued by DOL that materially changes data availability protocols for confidential unemployment compensation information. The rule mandates disclosure of previously confidential UC data to Federal officials for oversight and audits. This is a real, accomplished action (a final rule) that alters the scope and handling of statistical/administrative data outside normal notice procedures, which constitutes a credible stress signal on statistical agency integrity. However, the framing as 'oversight and audits' by DOL's own OIG suggests internal administrative coordination rather than external political manipulation of methodology, definitions, or suppression. The action is real and confirmed, but contained in scope and justified as administrative oversight rather than politicized interference with the independence or objectivity of statistical production. Severity 2 reflects a confirmed, material change to data protocols that warrants monitoring, but without evidence of removal of statistical leadership, improper methodology changes, or withheld releases.
- [federalregister.gov] **[official record]** Federal-State Unemployment Compensation (UC) Program; Data Availability (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-18978/federal-state-unemployment-compensation-uc-program-data-availability

### Election Administration Capture
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-09-17) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 18 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
