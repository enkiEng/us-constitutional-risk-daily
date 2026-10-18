# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-18 12:36:49 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **8 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-1.0**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.33 | 1.79 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.32 | 3.29 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.30 (Yellow) | ai | 1 | 3 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 1 |
| Election Administration Capture | elections_transfer | 1.30 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: Trump lost a lawsuit over partisan ads paid for with public funds. This is direct evidence that public funds were allocated or spent on partisan advertising—the core signal—and that a court reviewed and rejected the administration's legal position. The loss confirms that a real attempt to fund campaign-style ads with taxpayer money occurred and was judicially invalidated.
- [Baptist News Global] Trump loses lawsuit over partisan ads paid for with public funds - Baptist News Global (2026-10-16) - https://news.google.com/rss/articles/CBMingFBVV95cUxQRlp0cGdBRS1uZE8yZklOdGlQQ0tZdk5RdFVaVG1DQTJCdXJRMHhZaFMwb0hGaGwwQVVpNVdoS1JmYXJpQVlmbEFLU0oybV9BR3pvTlgwT1hMOWp5ZHJjRmg4dm54ck5hcEZ5N0lZcTU0Vm1DX0FBRnQ5NVBIS3dFa2U4cWlLS1EwMFJucmFTUmdhWjlNLVRrQ2NoR0VNdw?oc=5

### Civil Service Purge / Schedule F
- Assessment: Final rule issued by OPM expanding the scope and legitimate uses of administrative leave, including explicitly for 'workforce realignment initiatives.' This is an accomplished regulatory action (not a proposal) that creates new legal authority for executive discretion in removing or repositioning civil servants. Administrative leave can facilitate workforce removal without competitive process protections. Severity 2 because this is a real, confirmed action that materially expands tools available for politicized personnel actions, but it is a procedural/regulatory change rather than a demonstrated mass removal or targeted purge yet executed.
- [federalregister.gov] **[official record]** Administrative Leave for Workforce Realignment and Other Purposes (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21320/administrative-leave-for-workforce-realignment-and-other-purposes
- [federalregister.gov] **[official record]** Elimination of Time-in-Grade (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21319/elimination-of-time-in-grade
- [federalregister.gov] **[official record]** Managing Senior Professional Performance (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21316/managing-senior-professional-performance

### Press Restrictions or Retaliation
- [The Statesman] Pakistan tightens grip on TV news, bars live terror attack coverage; press watchdog warns of censorship - The Statesman (2026-10-17) - https://news.google.com/rss/articles/CBMi7AFBVV95cUxPS00zV1FVR01ZM0dXOFF6MGl5R0todnAxVDAzWC1wdF8xZnVBQk9ESXRHbGM2RXRvc05XWUpzcjJVQk50Yy14cl91ZUNoMUJqNHlBQXFFV1FwTi1FN1l0R19iVDItQjU2UTFQQjBFb2pybVpvMEFPcFMxUVNjTnZxRVBmaVNBd3FSbDI3TEdWdlhCVVNOdjBFVVBkX2VXN2VHNGNXdE1CeENOM1p6NUxnVTBEdVZNSzc4UjlZdGo5blJVTE1aN3dSVy1jQ3ZBam5kV0pJNEVpZU4wenVfM0tFa0hqbmdDTWk4OU1aUtIB7AFBVV95cUxPS00zV1FVR01ZM0dXOFF6MGl5R0todnAxVDAzWC1wdF8xZnVBQk9ESXRHbGM2RXRvc05XWUpzcjJVQk50Yy14cl91ZUNoMUJqNHlBQXFFV1FwTi1FN1l0R19iVDItQjU2UTFQQjBFb2pybVpvMEFPcFMxUVNjTnZxRVBmaVNBd3FSbDI3TEdWdlhCVVNOdjBFVVBkX2VXN2VHNGNXdE1CeENOM1p6NUxnVTBEdVZNSzc4UjlZdGo5blJVTE1aN3dSVy1jQ3ZBam5kV0pJNEVpZU4wenVfM0tFa0hqbmdDTWk4OU1aUg?oc=5

### Election Administration Capture
- [Brennan Center for Justice] The Arkansas Election Interference Law Handbook - Brennan Center for Justice (2026-10-16) - https://news.google.com/rss/articles/CBMioAFBVV95cUxQMVJGelh2bkdpVEpIdzRtQW9lNm8tbUd4WGlKSGFPZzVRN2hOSHNieXB5MElLTHUxb1d1dVBOeXMtZHFsYWFBam5CWWdTRlFxZFNrSHlMZzN3T3MyWGRZcWdzeTdvWDFuR0Y2d3lKTlI2S2lRZ05wR2hCcWR0R1NwZVJ0eWxVOTF6aE9uc09qN1JWSEVQaERCMnZsMWZSRlJl?oc=5
- [GNN | Latest News] Will November stop Trump’s agenda? - GNN | Latest News (2026-10-17) - https://news.google.com/rss/articles/CBMibkFVX3lxTE5JbzJmN0JvXzRISkJZcHZGclZrdDRScEJINWVTcWlHMENRVkdRS0Z6akZLZ0tEc0kzTXJUZTNDODE0RDRPWk9ibzFyRXp1YnVSSEMzbVVpMHEwN2NKcW1PSG9aOUtVSVpPYTNzUEZR?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
