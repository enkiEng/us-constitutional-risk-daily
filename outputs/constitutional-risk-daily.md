# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-16 17:06:31 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **14 / 100** (Baseline Institutional Noise)
- Previous day delta: **0.0**
- Delta vs 7-day average: **+0.0**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.65 | 2.44 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 9 | 10 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 2 | 0 |
| Statistical Agency Integrity | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 2 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 1.65 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.95 (Watch) | ai | 0 | 3 |

## Evidence Samples

### Legislative Oversight Obstruction
- Assessment: Survivors reporting on Black's contempt conviction for refusing to comply with a House Oversight subpoena in the Epstein probe. This is a real occurrence of executive/private defiance of legislative fact-finding authority, but it is isolated to a single individual resisting a single subpoena, not systematic obstruction of legislative oversight itself. Severity 2: a confirmed, credible stress signal (real but contained action by one actor).
- [newsnationnow.com] Epstein survivors push prosecution of Leon Black after contempt conviction - newsnationnow.com (2026-09-16) - https://news.google.com/rss/articles/CBMilgFBVV95cUxQa3FkSEowUGFjRUJtYmw5N05wT0lRemFoLV9GMGRCM0NsZ0hfdnB6aVRNdWdqQ0FNTHloN2hpMWZId0JVQ1NFWVZmUlg1aFlCazk5Q2NJWGFuSnZrSUREZWRKZXhkeUV5MHNTNHhoRUNGS0ZyT1JqSVNleG13ZTdIX1hJdzdRd3FJZ0lvNVNYNVRaZlBCcXfSAZsBQVVfeXFMTVhXWjdQYU8tMnZKVDlDcGlfZFo3OVdkVnhJZkRVam5kT0MxRUc1Q3BGTEczOU5KSHFOa0VEOThWeFNjYkJLTUlRR2VkUld5a0trQy1LZXFHZnBJT0lha0tZUnUzckZ3bG5MMk1aVmg4UUU3akdpTmRSQWV2LXY1STBUS1JqLUgyNjlvbE5RQjNCU2lmR2lJa09UcWc?oc=5
- [CNBC] House Oversight recommends holding Leon Black in contempt over Epstein subpoena standoff - CNBC (2026-09-15) - https://news.google.com/rss/articles/CBMinwFBVV95cUxNbHBFcE14eGdKMjVoTXlkX2lpTlp2Q0xCdTVLZEM1Z012S1F5dld0a3ZDYXcyWDZ3QldEY1FSRV8tUHpFeGVlRkxoOTdGNGh5M3FNVEgySTZkd2d4YXZHM29YZ3JIa0FfX3FYYmxBU3Mtb3dCdWFxTVlraTVmaUh1ckZFTUlqeVRjZzBMUVpXTTNUYWJBNUZ2SzMyaV8yX2_SAaQBQVVfeXFMTXA2SHNwZjA0WGF4NlB3M2VOay1xWUpCX2NreDg3a3lGbnNITXJIenpQd0VsN0dTcWhTZWMxTnZid2lGRmZLTnFHeUdoa294Sngyb0tjanNaVjhRYktnTHFvTkV2dHNpejk2bGNMVXdoTWVTSk1MVHVJYWhMVGtGRkdlWUo1N0pFTnB1R1c1M054NVZmVzM2SmNlTGRrdzNoQW9Ldlk?oc=5
- [newser.com] House Panel Recommends Contempt Charge for Leon Black - newser.com (2026-09-16) - https://news.google.com/rss/articles/CBMimgFBVV95cUxNWGg2SDM3bWdwMGt3TjlqZ3RfSmpwQ21tczBfSHdYNHFmeTktY3RUOWFXRUhobEJXeUFicG55cGFiQWJxbE5tS01BZ0xUNnNlSGN4Z1lqSWhKLU5xdWlYcW5EX2tZOW5QQzYxUWF2bWpIa3pyc1BmWldObGJSWTBYTFpZcFBKUUhJR295cXZYaHpWc1NwZjI4TmZ3?oc=5

### Emergency Powers Expansion
- Assessment: This is an official record of continuation of a pre-existing national emergency declaration. The continuation itself is a routine renewal mechanism established under the National Emergencies Act (50 U.S.C. § 1601 et seq.), whereby the President may extend a declared emergency for successive one-year periods without new legislative authorization. While this document confirms the use of emergency authorities to maintain expanded executive powers outside ordinary legislative process—and therefore matches the signal—the action is procedurally lawful, statutorily authorized, and represents the normal operation of the emergency declaration system rather than an expansion or abuse of emergency powers. The severity is 2 (a real but contained and legally-authorized stress signal) because emergency declarations do represent a bypass of ordinary process, but this particular continuation is a standard recurring action, not a novel expansion or defiance of law.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Persons Who Commit, Threaten To Commit, or Support Terrorism (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-19053/continuation-of-the-national-emergency-with-respect-to-persons-who-commit-threaten-to-commit-or
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Certain Terrorist Attacks (2026-09-10) - https://www.federalregister.gov/documents/2026/09/10/2026-18589/continuation-of-the-national-emergency-with-respect-to-certain-terrorist-attacks

### Statistical Agency Integrity
- Assessment: This is an OFFICIAL RECORD—a final rule issued by DOL that materially changes data availability protocols for confidential unemployment compensation information. The rule mandates disclosure of previously confidential UC data to Federal officials for oversight and audits. This is a real, accomplished action (a final rule) that alters the scope and handling of statistical/administrative data outside normal notice procedures, which constitutes a credible stress signal on statistical agency integrity. However, the framing as 'oversight and audits' by DOL's own OIG suggests internal administrative coordination rather than external political manipulation of methodology, definitions, or suppression. The action is real and confirmed, but contained in scope and justified as administrative oversight rather than politicized interference with the independence or objectivity of statistical production. Severity 2 reflects a confirmed, material change to data protocols that warrants monitoring, but without evidence of removal of statistical leadership, improper methodology changes, or withheld releases.
- [federalregister.gov] **[official record]** Federal-State Unemployment Compensation (UC) Program; Data Availability (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-18978/federal-state-unemployment-compensation-uc-program-data-availability

### Election Administration Capture
- [The New Republic] “Investigating What?”: Todd Blanche Brushes Off Trump Jr.’s Wedding - The New Republic (2026-09-15) - https://news.google.com/rss/articles/CBMikwFBVV95cUxPSEhiSnVmN1Joci0xaWdzOXl0NExSZUgtSzdTbDhjdW1nbjE4RDQyVEROZVpsaWFCNVNnaURlMU9wZC1sV3RIc3BnZ1FDY3Y4eWN1NHhBZnZ1akNPR0xwQkowUVF0UDdrYzVBajllZ0h5bHppOWNyTWpQanpfbEVKOFdudXJNWDRab1FXdlJqRnVqT3c?oc=5
- [easternherald.com] Supreme Court Deals Trump Major Blow on Mail Ballots, But His Election Takeover Continues - easternherald.com (2026-09-15) - https://news.google.com/rss/articles/CBMikAFBVV95cUxPSTZDRzZ3V3V1djVGeHVjSXV0NVhPaVFtV21lbm53bTFadGhSbjAxVUlRV2RzMktEbUlheU1oX3htbjNxcUFzS0k0RUpEVGRGTjZPS2s5ZDRhaHJDTzFuODRMVUlMTUgycDNhN2JRdnloVFZoS1RVZVFlZnFJX2R5UUNaX3hMUTA0QnltVTkwSVk?oc=5

### Judicial Review Foreclosure
- [courtlistener.com] **[official record]** Holem v. U.S. Department of Veterans Affairs (2026-09-10) - https://www.courtlistener.com/docket/74774751/1/holem-v-us-department-of-veterans-affairs/
- [tampafp.com] Shut Out By The State? Parents Take Washington Shelter Laws To The Supreme Court - tampafp.com (2026-09-16) - https://news.google.com/rss/articles/CBMipwFBVV95cUxPQ29JV29Ia3ZWZUNVODV2Tzc4TUN6cC0wOHpXMEc5ak5oWDVzSF9VUzBvS00ySnBEdEhSV3JCWDlNNkszVUdFekhEVmxNS2FDUkYydEpjQnVOejFhdmJfVmEwQjA3MFhqM0J3clRWbzhLNWRmTUhRQTV0RHg3TDBWT0RuZU9kYVVwYlBVRnZrdnoxTEs1S3loR0xVVGhXWmJfcERudFFhMA?oc=5

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 23 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - independent_agency_capture: courtlistener: The read operation timed out

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
