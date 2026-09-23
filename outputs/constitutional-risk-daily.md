# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-23 12:40:51 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **16 / 100** (Elevated Strain)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **+0.2**

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
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 6 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 3 |
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Statistical Agency Integrity | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: This item reports a real, verifiable action: a specific individual with a documented record of partisan voter-challenge activity has been hired into an election administration position (Georgia State Election Board). This is a concrete instance of partisan personnel placement in election administration, matching the signal of election administration moving toward partisan control. The placement is confirmed and has occurred, but it is a single personnel decision rather than a structural, systemic capture or an official policy dismantling neutral process. Severity 2 reflects that this is a real, credible stress signal (personnel capture) but not yet a high-severity structural breach.
- [Mother Jones] A MAGA activist flooded Georgia with voter challenges. Now he works for the State Election Board. - Mother Jones (2026-09-22) - https://news.google.com/rss/articles/CBMi6AFBVV95cUxPY3B6V1ZMWWpwWUZMNmo5NkN5bzZOQ3plRGE2d1lxcUNKbktiTGVmWDRjc3p0dkMzQkJMNmtFR3ZySGxBX3VodEZEanh5OEh1WVlXSjlLU2VzSUhKVGIxSU41VzFhZktyaDdXcjBWUmFZcDVUdXc3MlJtTWZmcWFMSUhtb0RPTWs5NTVyTm9UN1VZZDh1cF9US2RmMG1lbjk0WDRPaW43d2d6UVFobmRmaHVBNmxDcmFvUU5aTDYyaVpaOVloZHoxdDFhMlJKZVl6SDd1Q2N0SGtqRUM2Z0xjVzVBeFF5aF91?oc=5

### Press Restrictions or Retaliation
- Assessment: This is an official White House statement articulating the legal position that White House access is a privilege and not a right. As an official government statement, it reflects a position taken by the administration that can change the practical rights of press members seeking access. The statement itself constitutes state action communicating a legal stance that alters the ground rules for press access, even if no further enforcement mechanism is detailed in this item alone.
- [The White House (.gov)] White House Access Is a Privilege — Not a Right - The White House (.gov) (2026-09-21) - https://news.google.com/rss/articles/CBMilAFBVV95cUxOaGRBVWRLbk5HdHk2ZnB3bUVaZG40VzRZbGEzNDRQcGJucWtOZ1ljWW9RMm9uN0NQQTVLN1JHdTA2dnRucG9oYVhmN3ZoQmZ5X2FWdXZVbTlvMmozckNnS1A2Ujh1bkQ4NTE4ZzRoaVBCWS1DanUzRFhfRmM0bkJrMmxKbTMzbGdZX3VmZDFmcnJHNWJQ?oc=5

### Legislative Oversight Obstruction
- Assessment: A House vote to hold a witness in contempt for failure to comply with subpoenas represents a real exercise of legislative fact-finding authority and a response to obstruction of legislative oversight. This is a confirmed action (a House vote occurred) that demonstrates the legislature asserting its power to compel testimony and sanction non-compliance. However, severity is 2 rather than higher because: (1) this is a single enforcement action against one individual, not a systematic barrier to legislative oversight; (2) contempt votes are a normal, routine tool of legislative authority, not evidence of obstruction of that authority itself; (3) there is no indication here that the legislature's fact-finding power has been systematically impaired or that executive officials are defying legislative processes. The signal 'Legislative Oversight Obstruction' typically flags when oversight capacity itself is being blocked or removed. A contempt vote is the legislature exercising oversight, not being obstructed from it. This scores as a real but contained stress signal rather than evidence of systematic barriers to legislative accountability.
- [Legis1] House Votes to Hold Leon Black in Contempt Over Epstein Subpoenas - Legis1 (2026-09-22) - https://news.google.com/rss/articles/CBMifEFVX3lxTE95M2VhUng0Rjg2QXlDMkI0ZVVBRWozaW9xcm5lemJhRGpwazA3dzFIMmZxRHRVZTZMS2RiRHNvTWVSYjU1bkZPemY3TzF2RFMyY2Ywa0xJeGlEUmJYbk9DcndBUkxseTBVUUZHdkczLXB6MXQxNEJFXzdoRzc?oc=5

### Emergency Powers Expansion
- Assessment: This is an official record of continuation of a pre-existing national emergency declaration. The continuation itself is a routine renewal mechanism established under the National Emergencies Act (50 U.S.C. § 1601 et seq.), whereby the President may extend a declared emergency for successive one-year periods without new legislative authorization. While this document confirms the use of emergency authorities to maintain expanded executive powers outside ordinary legislative process—and therefore matches the signal—the action is procedurally lawful, statutorily authorized, and represents the normal operation of the emergency declaration system rather than an expansion or abuse of emergency powers. The severity is 2 (a real but contained and legally-authorized stress signal) because emergency declarations do represent a bypass of ordinary process, but this particular continuation is a standard recurring action, not a novel expansion or defiance of law.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Persons Who Commit, Threaten To Commit, or Support Terrorism (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-19053/continuation-of-the-national-emergency-with-respect-to-persons-who-commit-threaten-to-commit-or

### Statistical Agency Integrity
- Assessment: This is an OFFICIAL RECORD—a final rule issued by DOL that materially changes data availability protocols for confidential unemployment compensation information. The rule mandates disclosure of previously confidential UC data to Federal officials for oversight and audits. This is a real, accomplished action (a final rule) that alters the scope and handling of statistical/administrative data outside normal notice procedures, which constitutes a credible stress signal on statistical agency integrity. However, the framing as 'oversight and audits' by DOL's own OIG suggests internal administrative coordination rather than external political manipulation of methodology, definitions, or suppression. The action is real and confirmed, but contained in scope and justified as administrative oversight rather than politicized interference with the independence or objectivity of statistical production. Severity 2 reflects a confirmed, material change to data protocols that warrants monitoring, but without evidence of removal of statistical leadership, improper methodology changes, or withheld releases.
- [federalregister.gov] **[official record]** Federal-State Unemployment Compensation (UC) Program; Data Availability (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-18978/federal-state-unemployment-compensation-uc-program-data-availability

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 17 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
