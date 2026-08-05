# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-05 14:37:10 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **12 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **+0.9**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.43 | 1.52 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 1.00 | 2.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Security Sector Loyalty Tests | security_sector_neutrality | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 1 | 0 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 4 |
| Opposition Ballot Exclusion | opposition_pluralism | 1.30 (Watch) | ai | 0 | 1 |

## Evidence Samples

### Civil Service Purge / Schedule F
- Assessment: OPM has issued a final rule modifying RIF regulations to prioritize performance over tenure and length of service. This is a real, published regulatory action that materially changes federal personnel protections by reducing seniority-based safeguards. While presented as merit-based efficiency, the shift from tenure-protective RIF procedures to performance-based retention creates a concrete mechanism for politicizing career civil service. This is a contained but credible stress signal—a structural change to established civil-service protections, not a mass purge event or emergency action.
- [federalregister.gov] **[official record]** Reduction in Force (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15665/reduction-in-force
- [federalregister.gov] **[official record]** Streamlining Probationary and Trial Period Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15654/streamlining-probationary-and-trial-period-appeals
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Security Sector Loyalty Tests
- Assessment: This is a final OPM regulation that removes the Merit Systems Protection Board (MSPB)—an independent adjudicative body—from appeals of suitability actions and consolidates that authority within OPM itself. Suitability determinations affect federal employment eligibility and can be used to screen personnel. Removing independent oversight of such determinations and concentrating appeals authority within the executive personnel office constitutes a material shift in internal review mechanisms that could enable partisan loyalty filters in federal personnel decisions. This is a confirmed structural change to a coercive-state institution's internal accountability, though it remains procedural rather than involving overt purges or open defiance of courts. Severity 2: real, confirmed, official action affecting institutional independence in personnel matters.
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Legislative Oversight Obstruction
- Assessment: An official motion to quash third-party subpoenas filed by the Executive Office of the President represents a verifiable action to obstruct legislative fact-finding. The filing of a motion to quash subpoenas is a concrete legal action aimed at preventing disclosure of information to Congress or its agents. This constitutes a real occurrence of obstruction of legislative oversight, though the motion itself is a procedural challenge rather than an outright defiance of a court order or systematic campaign. The severity is 2 (repeated or credible stress signal—a real but contained action) rather than 3, because this is a single motion through the normal judicial process, not an open defiance or structural campaign to prevent oversight.
- [courtlistener.com] **[official record]** IN RE SUBPOENAS ON BORIS EPSHTEYN (2026-07-02) - https://www.courtlistener.com/docket/73690657/2/in-re-subpoenas-on-boris-epshteyn/

### Election Administration Capture
- [pbs.org] Live Results: Kansas midterm primaries - pbs.org (2026-08-04) - https://news.google.com/rss/articles/CBMigAFBVV95cUxPVjY5ZXBYOGdvQ3NkLTVHUXFjdm5CbUprWTJwMHFtM3QwRGZ5ZXBsajhyM2t4VmhkeGlfYVZzQVVOTUcwTW5vWDRwNmtzZHc2ZUV1WWo2bUl3WmN5QnBDODlkbnVNRm5vcUpUSVExNFNGRld0a2pnYXV0Uk81NjF2RdIBhgFBVV95cUxNWjA2WHMwYnZreHZxZUVNQThGWEdSb3BnOEIxWXNuTV9qU0c4NW5pSE1TMGNTd3VOVmh3eVRqVjZva3Bxem83YWQ5c0JYS2MwQkhxbGl0dFBudlJ6dDFTX0IxdXB1bDdOZF8zSVA2REZjWDB4MERwX1p1WENXRnFUR0d4WWJVUQ?oc=5
- [AJC.com] Georgia State Election Board tests limits ahead of midterms - AJC.com (2026-08-03) - https://news.google.com/rss/articles/CBMingFBVV95cUxNa0pMUHB4Z1Z0SF82c0V0NDVuemRoUEM3ZVNKeWUxdXppTzV1U0pHWlNjN3R3T1BqNUdTTjB1akUzZnR2ajFIZDlOLWg3WGp1M3lTbm45N0cza0RVZlZSMzZIYWxkU2N2RUJwQWhsbnlxR0tkWjVBek9WOGtGanFCN3ZmRkptbEZXSi1uTDVvNDBwalBENzVqNGhzTTlxdw?oc=5
- [KCTV] ELECTION GUIDE: Here’s what you need to know for the August 4 primary in Missouri - KCTV (2026-08-04) - https://news.google.com/rss/articles/CBMioAFBVV95cUxOZzEyT1BrQ3ZmWG8xRmZGTkp2Z3NCUmxGbFQwYmt5dlUxVFZzbHNKX1dCUWctNXdRVV9nLVlSZ2pRUFRseXBCalFvV2FFcU1TMFZUa1IxbWpUb0x1bk04WUluQzZZNG16ZHZUY0xaeVJwanZsYjZYOFpmUlFUY2ZObFY5TE4xLUpFUFoxWGN2b1Izcjc5VXBwakdUVFFITENh?oc=5

### Opposition Ballot Exclusion
- [The New Indian Express] Congress holds Datia as BJP suffers by-poll setback in Madhya Pradesh - The New Indian Express (2026-08-03) - https://news.google.com/rss/articles/CBMi0gFBVV95cUxOYUVLa21UT2RQc1RqOHktaWlrT0k3ZDNwaWlHY0FIVGQtc21sUTBPVXNGTnUyRkpmVkpGSGc1WlpGY0dCOFZrQjdkdE16QWxqQnRIcVM5alJ3RUNEVkxZbDVGMC10RXlfZHE2SFlzUlUyVWw3RkREVzNPZXRKckl5eE5CeWNOWTRUa05wanVaWXVRNDNfTFlTN0lUd0NWVUV2WWpfRVZ2NVRJSmpxX083Y2NsYXdNS3BzTUdqbzRUNWp0azZ1NDJRVWZuLWN5UjF2d2fSAd8BQVVfeXFMT01PTEUzbWJXR25aOXAwY2w5eV9xcUFFa3BMMWI0YUtDbkFDaTB2YmRoSTdpZHF3LXRVbWxUMmYzMElicS1hT0N0LWdJemlsWkpLYmNpRWJWN240TkJRMlAyM00wTXlWWWJrMmNndHU0U184Mk9SQzctN1hOUFFyYWd2aUtxNnhiRW5yaFpWSldXX0Nnbmtyb0VrdVB1azZCWFgwMTdwSGJVN3cxdnR2UjdyMjRUOVplaXdQV0NVVEo1a19NRWtDMk40a2lScnc2WWR5MFNIT3BYRzduVWt4RQ?oc=5

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 17 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 5
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - election_certification_interference: courtlistener: The read operation timed out

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
