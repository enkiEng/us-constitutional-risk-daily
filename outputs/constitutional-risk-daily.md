# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-20 12:36:20 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **17 / 100** (Elevated Strain)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **+1.6**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.06 | 0.23 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 1.30 | 2.60 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Oversight Obstruction | federalism_oversight | 2.30 (Yellow) | keyword | 0 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 2 | 3 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 2 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Statistical Agency Integrity | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
### Press Restrictions or Retaliation
- Assessment: Multiple credible news organizations (MSNBC, CNN, Politico) report that their journalists were denied White House access following an executive action or directive. This constitutes a real, verifiable state action raising costs and legal/practical barriers to independent reporting by restricting press access to official spaces. The action is confirmed and contemporaneous rather than hypothetical. Severity is 2 (repeated, credible stress signal, real but contained action) rather than 3 because this is denial of access/credential rather than a broader campaign of legal jeopardy, prosecution, or systematic removal of press freedoms, and appears focused on specific outlets rather than a structural dismantling of press independence.
- [spectrumlocalnews.com] MS NOW, CNN and Politico say their jour­nalists were denied access to White House after Trump ban - spectrumlocalnews.com (2026-09-19) - https://news.google.com/rss/articles/CBMi7wFBVV95cUxNUl9CYlE3ZmlsUFVrdTc0TFRnYzVlXzVmZlJuZzB1UXZ6Z3RHX3FnazNhZmJERnBBVHVQYlpwbzNQbkxFOTloQy1YRmFLOEhvRURBVTFkazFPV0xQcE9vRVpUdzBsMnFSOFYweGx1TElCdy1TcU56bk5Xc0pQWFhCRWRrc0diQlFTYzFCRnV6ejhiNW9NNFJJNWZLNTFhTk5rbzJ1clRkdm1kU2hRckh6R0hNNjBodldHNzN1ZjZXMFRmMEtJSERNSWdWQ25UaDRYOTRxMm0zelhyamMyREJQZU12OThucVM1UXprY0gwcw?oc=5
- [PBS] WATCH: Trump says he is banning CNN, MSNOW and Politico from the White House - PBS (2026-09-18) - https://news.google.com/rss/articles/CBMisgFBVV95cUxOYVVTNmxRQjNWTEw5ZGh0NzVyOTZaR1gxaGZULUpJcXZkRUZaMng1aE1kTEdjWVAtNkRoalZzZ3ZkbGRid0VqdUlPX1JYenFNdWlrRkVJaHh0Wng2R01VOHFtN0o0S3VmNTlNYnBIM2tubGFaUFBPdGYtTW83QlJja2VaeGNkaWRHZnNFTnpZMVE0RVo2VGhSbkpXeFlQU0s0cUxqVlQ1RXJyZW1ENjdLMEZR0gG3AUFVX3lxTE1UMVpULTRGUVZrbjBuX0lWSVg1VTFFSmNrNVdHOUFtVTVXUDQtZXhxdjlrRUpCZWhucFFDT3lWOFFpcXVlYUMyb1JwcHJ2RzlTTldUaGxOZThUQUo0Q01DQ2U4SUpxM0xRZkV1TEhLN2dxQmVYUkhWSDJZNGFBUDN5ZEN0UUZ1MHllT3RRcThjaGt4QzFyQld1VGxla20wMzVXMHk0ZjZWQjhPWDlRT2NNN3pTVENUQQ?oc=5

### Election Administration Capture
- Assessment: This item reports a real, verifiable action: a specific individual with a documented record of partisan voter-challenge activity has been hired into an election administration position (Georgia State Election Board). This is a concrete instance of partisan personnel placement in election administration, matching the signal of election administration moving toward partisan control. The placement is confirmed and has occurred, but it is a single personnel decision rather than a structural, systemic capture or an official policy dismantling neutral process. Severity 2 reflects that this is a real, credible stress signal (personnel capture) but not yet a high-severity structural breach.
- [Mother Jones] A MAGA activist flooded Georgia with voter challenges. Now he works for the State Election Board. - Mother Jones (2026-09-20) - https://news.google.com/rss/articles/CBMi6AFBVV95cUxPY3B6V1ZMWWpwWUZMNmo5NkN5bzZOQ3plRGE2d1lxcUNKbktiTGVmWDRjc3p0dkMzQkJMNmtFR3ZySGxBX3VodEZEanh5OEh1WVlXSjlLU2VzSUhKVGIxSU41VzFhZktyaDdXcjBWUmFZcDVUdXc3MlJtTWZmcWFMSUhtb0RPTWs5NTVyTm9UN1VZZDh1cF9US2RmMG1lbjk0WDRPaW43d2d6UVFobmRmaHVBNmxDcmFvUU5aTDYyaVpaOVloZHoxdDFhMlJKZVl6SDd1Q2N0SGtqRUM2Z0xjVzVBeFF5aF91?oc=5

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
- Primary-source lookups: 22 signals, 16 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
