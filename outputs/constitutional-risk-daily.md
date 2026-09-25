# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-25 12:41:11 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **17 / 100** (Elevated Strain)
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
| Opposition Rights and Political Pluralism | 14 | 0.65 | 2.27 |
| Executive Constraints and Emergency Powers | 13 | 1.10 | 3.57 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.65 | 1.62 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.82 | 1.65 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 5 |
| Statistical Agency Integrity | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 3 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 2 |
| Opposition Ballot Exclusion | opposition_pluralism | 1.65 (Watch) | ai | 0 | 12 |
| Legislative Oversight Obstruction | federalism_oversight | 1.65 (Watch) | keyword | 0 | 0 |
| Emergency Powers Expansion | executive_constraints | 1.30 (Watch) | ai | 0 | 2 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 1 |

## Evidence Samples

### Election Administration Capture
- Assessment: This item reports a real, verifiable action: a specific individual with a documented record of partisan voter-challenge activity has been hired into an election administration position (Georgia State Election Board). This is a concrete instance of partisan personnel placement in election administration, matching the signal of election administration moving toward partisan control. The placement is confirmed and has occurred, but it is a single personnel decision rather than a structural, systemic capture or an official policy dismantling neutral process. Severity 2 reflects that this is a real, credible stress signal (personnel capture) but not yet a high-severity structural breach.
- [Mother Jones] A MAGA activist flooded Georgia with voter challenges. Now he works for the State Election Board. - Mother Jones (2026-09-24) - https://news.google.com/rss/articles/CBMi6AFBVV95cUxPY3B6V1ZMWWpwWUZMNmo5NkN5bzZOQ3plRGE2d1lxcUNKbktiTGVmWDRjc3p0dkMzQkJMNmtFR3ZySGxBX3VodEZEanh5OEh1WVlXSjlLU2VzSUhKVGIxSU41VzFhZktyaDdXcjBWUmFZcDVUdXc3MlJtTWZmcWFMSUhtb0RPTWs5NTVyTm9UN1VZZDh1cF9US2RmMG1lbjk0WDRPaW43d2d6UVFobmRmaHVBNmxDcmFvUU5aTDYyaVpaOVloZHoxdDFhMlJKZVl6SDd1Q2N0SGtqRUM2Z0xjVzVBeFF5aF91?oc=5

### Statistical Agency Integrity
- Assessment: This is an official Federal Register notice confirming that the HUD has not made inflation adjustments to civil monetary penalties for 2026, as required by statute. This represents a departure from mandatory procedure, though the practical impact on BLS/BEA/Census integrity is unclear. The act itself (non-compliance with inflation adjustment requirement) has occurred, but severity is moderate because the connection to statistical agency integrity is indirect and the item does not demonstrate interference with core economic data production.
- [federalregister.gov] **[official record]** Civil Monetary Penalty Amounts for 2026 (2026-09-24) - https://www.federalregister.gov/documents/2026/09/24/2026-19600/civil-monetary-penalty-amounts-for-2026

### Legislative Bypass by Executive
- Assessment: The item reports that Trump executive orders have been issued expanding hunting and fishing across America. This represents executive action taken unilaterally rather than through legislation. However, expansion of hunting/fishing regulations, while a legitimate exercise of executive power in certain domains (e.g., public lands management under existing statutes), does not constitute a major governance bypass of legislative authority. The action appears to operate within delegated executive authority rather than circumventing statute. This is a contained application of existing executive power, not a structural constitutional violation. Severity is modest because the scope (hunting/fishing) is narrow and the underlying authority is typically delegated to the executive branch.
- [Buckeye Firearms Association] New Trump executive orders expand hunting, fishing across America - Buckeye Firearms Association (2026-09-25) - https://news.google.com/rss/articles/CBMinAFBVV95cUxPNlhGWFpuMDJNd0I5YkZES081cXVtVW15T3E2Ymxva2ZOOGdTQmhwXzlXT1ZEQWR6ZzA3THF4aXVRUlFoN2VkM0I2b3RlbjBzaGJQbXZaV0NEQW9Mc3BzaUJmQ0NKQ0s5cFUtdUoxNXdhZzVkTF9JNmNQdEF2Y0FSVXBIcTdrLTJ4NVlPME5KUi1CanNRVFBseTFQTFU?oc=5

### Opposition Ballot Exclusion
- [Al Jazeera] Arab parties denounce ban from Israel’s October election - Al Jazeera (2026-09-24) - https://news.google.com/rss/articles/CBMipgFBVV95cUxPdnVQQkNrZk1PUDlwOEZaWElnTVNHUUotMEZRelpQVjhOQ0tnakl1SnVnNzhrM0ktajdtQU51b19KdzN1Tl9LVGFzcUREUjN2VTJzbHFrY0pXbF9pMm1Uc2NZOF9iTVBJMTRQOTFVX0NaS2FwTVU0amJxUDJTWVhGOEtNODNLbmZJSVpEWlhXekJkeDZaaDVRd283aDNSdk4zZWJBbEpR0gGrAUFVX3lxTE5ad1p6czlmemFOLUtMT05XZnpvTldZN2JVam03N3R3Ynpxa1V4UExtNmlldktiUzZzQWVnUjcxLVlFcFdpTWVNWExaTlJIeDdKdndsczM4M1A2LVZYeVc5dW5yWXBSaVpBVnY0YmQtNVBVdXVRUy1jbEVvRldIY3FLbGp2N01HYTdGZGtCUzlDMkRDUVRpV1Ryem4wWERwUV9tUHlZRTBwWjctMA?oc=5
- [Good Authority] Russia’s 2026 Duma elections left voters few alternatives - Good Authority (2026-09-23) - https://news.google.com/rss/articles/CBMikgFBVV95cUxQM3I0cWZKYVZQRDEzYzE2MnlJUk5ONEVjVXVsYTJ4Sl9sdnNLSC1YdUJkMFlsSWh0ZmpELWtxM2ZLbnlJdWNQMDFRVmYtSkRCUWpKdmJIUE1xTk0taUxxNHBSZy1wWnpBekN2WVAtdlBYMkZETkJwZ0pqRFRwa3VyT2Npdk1oRmhPQ0NUREFuLUJiQQ?oc=5
- [The Jerusalem Post] Israel Central Elections Committee clears Otzma Yehudit for October vote - The Jerusalem Post (2026-09-24) - https://news.google.com/rss/articles/CBMiaEFVX3lxTFA2Q0c2VEZjTnR3V3FDdDBrak5CdTVOUFVhQmdOMkU4YURxSzBZMXBhSi1kV19DWEhUaFJyT3haUjltNW1ydTRRWkptemZLUFB0SmtreUM1TDFOZlphV2RDaTNSVXNsSHhD?oc=5

### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 17 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
