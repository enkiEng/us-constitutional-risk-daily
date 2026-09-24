# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-24 12:41:35 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **18 / 100** (Elevated Strain)
- Previous day delta: **+2.0**
- Delta vs 7-day average: **+1.5**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.82 | 2.06 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 1 | 12 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 4 |
| Statistical Agency Integrity | civil_service_integrity | 2.00 (Yellow) | ai | 2 | 1 |
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 1.65 (Watch) | ai | 0 | 2 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Opposition Ballot Exclusion
- Assessment: Item reports the ANC challenging the IEC's exclusion of 181 candidates from its list in South African elections, now being taken to South Africa's Constitutional Court. While this involves ballot exclusion, the IEC and Constitutional Court referenced are South African institutions, not U.S. institutions. The event is in South Africa, not the United States.
- [news24.com] ANC takes IEC list battle for 181 excluded candidates to ConCourt - news24.com (2026-09-23) - https://news.google.com/rss/articles/CBMisAFBVV95cUxOXzhFZG82WWRDaEJJWWRxNTlnMXZDTWFwYjZrWWlXOVdaMEczd2VpZW5Td1BIMmxWOXR5TWJ6TkZieWhCS1BzbkZCWU1yaG0wczB5ZlQyTHVoQ2NlRE9oTGFkbk9fVGR5aTYzLTNXcWZQYWpGSnRyOTh1bUZWalVtMmZqTDVGaTlZOXZVOXVKb09fMkh2QzJtQkozN2lSU0c3ZnpGbWNQdnl4MTZDOVpKVQ?oc=5

### Election Administration Capture
- Assessment: This item reports a real, verifiable action: a specific individual with a documented record of partisan voter-challenge activity has been hired into an election administration position (Georgia State Election Board). This is a concrete instance of partisan personnel placement in election administration, matching the signal of election administration moving toward partisan control. The placement is confirmed and has occurred, but it is a single personnel decision rather than a structural, systemic capture or an official policy dismantling neutral process. Severity 2 reflects that this is a real, credible stress signal (personnel capture) but not yet a high-severity structural breach.
- [Mother Jones] A MAGA activist flooded Georgia with voter challenges. Now he works for the State Election Board. - Mother Jones (2026-09-23) - https://news.google.com/rss/articles/CBMi6AFBVV95cUxPY3B6V1ZMWWpwWUZMNmo5NkN5bzZOQ3plRGE2d1lxcUNKbktiTGVmWDRjc3p0dkMzQkJMNmtFR3ZySGxBX3VodEZEanh5OEh1WVlXSjlLU2VzSUhKVGIxSU41VzFhZktyaDdXcjBWUmFZcDVUdXc3MlJtTWZmcWFMSUhtb0RPTWs5NTVyTm9UN1VZZDh1cF9US2RmMG1lbjk0WDRPaW43d2d6UVFobmRmaHVBNmxDcmFvUU5aTDYyaVpaOVloZHoxdDFhMlJKZVl6SDd1Q2N0SGtqRUM2Z0xjVzVBeFF5aF91?oc=5

### Statistical Agency Integrity
- Assessment: This is an official Federal Register notice confirming that the HUD has not made inflation adjustments to civil monetary penalties for 2026, as required by statute. This represents a departure from mandatory procedure, though the practical impact on BLS/BEA/Census integrity is unclear. The act itself (non-compliance with inflation adjustment requirement) has occurred, but severity is moderate because the connection to statistical agency integrity is indirect and the item does not demonstrate interference with core economic data production.
- [federalregister.gov] **[official record]** Civil Monetary Penalty Amounts for 2026 (2026-09-24) - https://www.federalregister.gov/documents/2026/09/24/2026-19600/civil-monetary-penalty-amounts-for-2026
- [WPSU] Warren demands Trump officials explain removing a ban on interference in census data - WPSU (2026-09-24) - https://news.google.com/rss/articles/CBMiugFBVV95cUxOUGFJaGdCdDQ3NGFqTWprYk04aVhTdXJGZXhUMVZ1Tm5yQWtWUkloQzJFNjhnR0lBd3pNQ1BiVTF0OERvOGpudHMzWEFpU3k0MS1UbWFtTGpCeWdFQWFUX1l3VldaajJJVHFsdnF4OHduRHZQN1BGODBiang3Z0pNZjJLa3g4ZmhWcDdUYTRuY0hLT05yeTlUNVRTa2RCLVZTVjNfR1h5MFVGZkJmNUhTNS0yejBSbi1YcWc?oc=5

### Legislative Oversight Obstruction
- Assessment: A House vote to hold a witness in contempt for failure to comply with subpoenas represents a real exercise of legislative fact-finding authority and a response to obstruction of legislative oversight. This is a confirmed action (a House vote occurred) that demonstrates the legislature asserting its power to compel testimony and sanction non-compliance. However, severity is 2 rather than higher because: (1) this is a single enforcement action against one individual, not a systematic barrier to legislative oversight; (2) contempt votes are a normal, routine tool of legislative authority, not evidence of obstruction of that authority itself; (3) there is no indication here that the legislature's fact-finding power has been systematically impaired or that executive officials are defying legislative processes. The signal 'Legislative Oversight Obstruction' typically flags when oversight capacity itself is being blocked or removed. A contempt vote is the legislature exercising oversight, not being obstructed from it. This scores as a real but contained stress signal rather than evidence of systematic barriers to legislative accountability.
- [Legis1] House Votes to Hold Leon Black in Contempt Over Epstein Subpoenas - Legis1 (2026-09-22) - https://news.google.com/rss/articles/CBMifEFVX3lxTE95M2VhUng0Rjg2QXlDMkI0ZVVBRWozaW9xcm5lemJhRGpwazA3dzFIMmZxRHRVZTZMS2RiRHNvTWVSYjU1bkZPemY3TzF2RFMyY2Ywa0xJeGlEUmJYbk9DcndBUkxseTBVUUZHdkczLXB6MXQxNEJFXzdoRzc?oc=5

### Emergency Powers Expansion
- [Augusta Free Press] John Whitehead | When everything becomes a national security threat - Augusta Free Press (2026-09-23) - https://news.google.com/rss/articles/CBMiogFBVV95cUxQeC1aVGdSdklWcGV1S0paaHZpTV9aV19lQVJCLWxQeEdydGJLQnVRUkVZV3l6NS14emFQLXBUMFB2X190YWE4U1lydlU3c01SeHhIMjkwX0g5cnA0ZVlMQmNnUkdqVmdQVlg2UDM4ZEIwZnFiRzhBeXB1bEd2dW4wT05KZ2xodTl5VGJuVnVYU256eUlPQ3RGejZYUFQ5SGxFcmc?oc=5
- [thenewamerican.com] When Everything Becomes a National Security Threat - thenewamerican.com (2026-09-23) - https://news.google.com/rss/articles/CBMijwFBVV95cUxOV1BxUlZZenBqLWZkZnZTSDYtOHVCOHhZY2NhQThjeFpqX0lVbkQtaDFDd05uOUN1VDI0TWp2dHlyU3FDOGR0eGVUQW4tZlZjN1FHd0h1T1lEQkhnVDdyYVZ5SlJOWW81enhLUFcwNDVaeUVVczNsanRrR1FRZnk4OXVWWnNLUTBkUkVtTlhkbw?oc=5

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 16 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
