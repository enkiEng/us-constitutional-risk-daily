# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-21 12:38:30 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **16 / 100** (Elevated Strain)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **+0.6**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.97 | 1.95 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 2 | 3 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 2 | 2 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Statistical Agency Integrity | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 1.95 (Yellow) | keyword | 0 | 0 |

## Evidence Samples

### Press Restrictions or Retaliation
- Assessment: Multiple credible U.S. news organizations (MS NOW, CNN, Politico) report denial of White House press access following a Trump ban. This is a repeated, confirmed action by a state actor that raises costs/access for independent reporting. However, severity remains 2 rather than 3 because this appears to be localized access denial rather than a structural campaign with legal jeopardy or defiance of court orders. The action is real and material but contained to credential/venue restrictions.
- [PBS] MS NOW, CNN and Politico say their journalists were denied access to White House after Trump ban - PBS (2026-09-19) - https://news.google.com/rss/articles/CBMizgFBVV95cUxOWE9LdFRLOVA4aWFzVXdJSnNUUGJUb0xWLVJvZnFlVk9JS0NRcU1EQ2Z3ZHV6MDBZQS16eUNrSFAyWGtKQzdDdE1tMXFIZE05MVRpaXd2Sk5SczJNX2pYMk9KTlNoaVFlMk9HQlloLTdST3RfNVcwVW9jVGRmTllTZWFYZzV1d3Y1N1EySTVMNlNSWUJnM1lnTnJ4MUhqMHg1YkVFRGVlUmtDM3kyRFo3c09Ud1JNRlRkNVBSWDRaN0QzRC1xN285Nkl4dkZvd9IB0wFBVV95cUxQYkZuNWJWN2oxbmplczdoMERUbVNxTEVVRG9Wak16SUtTd2VOUG9ydjFGSnRURF9ORDNhTXZjSjhhVWlJZ3lqa0hfc1psWHFMZW9WTnRsV3ZMSVdLTFpCWUR6b1RsZGxERkN2MWhwNXRaVlctZmhiYnlpMlA4bGxkR1NIXzFmVWIteGRhU0tEcVhDMDl4U0tlQmw3c1dTeV81dldTZE1QRG45QlVJVnlhWnBPSE5OOWNheVdGU25GNEFvMkR0NUt0SnVMeTFKRkZZcUo4?oc=5
- [streamlinefeed.co.ke] Journalists detained and deported in US immigration crackdown, investigation finds - streamlinefeed.co.ke (2026-09-21) - https://news.google.com/rss/articles/CBMitgFBVV95cUxPR1NvZWExbjhRbWJzRmNOWVpMRlVNRlZyZ2FnVFFRajg3MFBwdUJ0ZGJ1TmlYQkd3ZllBdzZTR1hmX3VQVmlSRjJhOTNGMkZSYlNHeVY0bjRCX1YwTXZJR19Bc1d3aDcyM3dxVmFvNlpyTGI5bHI4bTREM2thNlpxOUREOG5BT0RXYjBoTXNZVzF0WjlxbkNKc0NfQXkybDNaZHVjTXF5Sjl1LS01QzlBUDJDd0NJUQ?oc=5

### Election Administration Capture
- Assessment: This item reports a real, verifiable action: a specific individual with a documented record of partisan voter-challenge activity has been hired into an election administration position (Georgia State Election Board). This is a concrete instance of partisan personnel placement in election administration, matching the signal of election administration moving toward partisan control. The placement is confirmed and has occurred, but it is a single personnel decision rather than a structural, systemic capture or an official policy dismantling neutral process. Severity 2 reflects that this is a real, credible stress signal (personnel capture) but not yet a high-severity structural breach.
- [Mother Jones] A MAGA activist flooded Georgia with voter challenges. Now he works for the State Election Board. - Mother Jones (2026-09-21) - https://news.google.com/rss/articles/CBMi6AFBVV95cUxPY3B6V1ZMWWpwWUZMNmo5NkN5bzZOQ3plRGE2d1lxcUNKbktiTGVmWDRjc3p0dkMzQkJMNmtFR3ZySGxBX3VodEZEanh5OEh1WVlXSjlLU2VzSUhKVGIxSU41VzFhZktyaDdXcjBWUmFZcDVUdXc3MlJtTWZmcWFMSUhtb0RPTWs5NTVyTm9UN1VZZDh1cF9US2RmMG1lbjk0WDRPaW43d2d6UVFobmRmaHVBNmxDcmFvUU5aTDYyaVpaOVloZHoxdDFhMlJKZVl6SDd1Q2N0SGtqRUM2Z0xjVzVBeFF5aF91?oc=5
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-09-20) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Emergency Powers Expansion
- Assessment: This is an official record of continuation of a pre-existing national emergency declaration. The continuation itself is a routine renewal mechanism established under the National Emergencies Act (50 U.S.C. § 1601 et seq.), whereby the President may extend a declared emergency for successive one-year periods without new legislative authorization. While this document confirms the use of emergency authorities to maintain expanded executive powers outside ordinary legislative process—and therefore matches the signal—the action is procedurally lawful, statutorily authorized, and represents the normal operation of the emergency declaration system rather than an expansion or abuse of emergency powers. The severity is 2 (a real but contained and legally-authorized stress signal) because emergency declarations do represent a bypass of ordinary process, but this particular continuation is a standard recurring action, not a novel expansion or defiance of law.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Persons Who Commit, Threaten To Commit, or Support Terrorism (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-19053/continuation-of-the-national-emergency-with-respect-to-persons-who-commit-threaten-to-commit-or

### Statistical Agency Integrity
- Assessment: This is an OFFICIAL RECORD—a final rule issued by DOL that materially changes data availability protocols for confidential unemployment compensation information. The rule mandates disclosure of previously confidential UC data to Federal officials for oversight and audits. This is a real, accomplished action (a final rule) that alters the scope and handling of statistical/administrative data outside normal notice procedures, which constitutes a credible stress signal on statistical agency integrity. However, the framing as 'oversight and audits' by DOL's own OIG suggests internal administrative coordination rather than external political manipulation of methodology, definitions, or suppression. The action is real and confirmed, but contained in scope and justified as administrative oversight rather than politicized interference with the independence or objectivity of statistical production. Severity 2 reflects a confirmed, material change to data protocols that warrants monitoring, but without evidence of removal of statistical leadership, improper methodology changes, or withheld releases.
- [federalregister.gov] **[official record]** Federal-State Unemployment Compensation (UC) Program; Data Availability (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-18978/federal-state-unemployment-compensation-uc-program-data-availability

### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 17 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
