# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-13 13:51:41 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **7 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **-3.5**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.20 | 0.65 |
| Civil Service and Agency Independence | 10 | 2.00 | 5.00 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.47 | 0.95 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Independent Agency Capture | civil_service_integrity | 3.00 (Orange) | ai | 1 | 2 |
| Inspector General Retaliation | civil_service_integrity | 1.65 (Watch) | ai | 0 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 0.95 (Watch) | keyword | 0 | 0 |
| Security Sector Loyalty Tests | security_sector_neutrality | 0.95 (Watch) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 0.60 (Green) | ai | 0 | 8 |

## Evidence Samples

### Independent Agency Capture
- Assessment: This item reports that Trump is 'still trying to fire' Federal Reserve Board member Lisa Cook 'despite Supreme Court order.' If accurate, this describes an explicit, ongoing attempt to remove an independent agency official in defiance of a Supreme Court directive—a clear and serious action that weakens legal safeguards for independent regulatory decision-making and constitutes an official action contra judicial authority.
- [Blavity News] Trump Still Trying To Fire Federal Reserve Board’s Lisa Cook Despite Supreme Court Order - Blavity News (2026-08-11) - https://news.google.com/rss/articles/CBMiqwFBVV95cUxPMkNZVnh3eHRIWTJmclJNaXMtWHBZV2czR09oLVFxeVlXdDdaSkZ4TXRZS2EyLUhiOEhaaG14YVY5Ti0zYzNWS3hPNzkzbV9jT2kzVUlmcHFYZG9PT1VPM3EzZzV4cmprNGxfS3Q4NllxTVdyaVJiaEFDUGg2LWZlUDdOTjYtZ2ZfbGE0WkdsMXdYZTM1U3VOYzE3SGNUcFo3S1RWRXdFWHpDc00?oc=5

### Inspector General Retaliation
- [courtlistener.com] **[official record]** McCann, Alisha v. United States (2026-08-11) - https://www.courtlistener.com/docket/74220062/1/mccann-alisha-v-united-states/
- [courtlistener.com] **[official record]** Rosenzweig v. Blanche (2026-08-07) - https://www.courtlistener.com/docket/73734036/1/rosenzweig-v-blanche/
- [courtlistener.com] **[official record]** Doe v. School Board of Duval County, Florida (2026-08-06) - https://www.courtlistener.com/docket/73732850/1/doe-v-school-board-of-duval-county-florida/

### Civil Service Purge / Schedule F
- No fresh evidence links in the current lookback window.
### Security Sector Loyalty Tests
- No fresh evidence links in the current lookback window.
### Legislative Bypass by Executive
- [constitutioncenter.org] Trump mail voting executive order on Supreme Court’s radar - constitutioncenter.org (2026-08-12) - https://news.google.com/rss/articles/CBMimAFBVV95cUxNZTJlM0RhYnhuM09zUjVFWGFYUUM5bUNfWHZNek5wcWphb1dGMVlXenMyVTVES0hOdUtXcWRWQnREWlVjUURMZ21VVFY5a195Y1NpUGRETXc2dTlJNjRESmJubENkS2l1RWo0QU5IaGRhdm01bm9tSWRzb1RCUU9MV1dUWUJvSXhJSjZKQUhBSE5KLVJSMVFwNNIBngFBVV95cUxNb25qdkt0bkU2ZlFaUXdIRUNqNXFXVk9GVWVsN1dfbHJUS3h3T2JNYkJZd0VsdGlQRzVlT21WY3VBZ0hnMFR0VUw0ZjFKZTlWLWxlRGktVklJNXJWUERBZHM2MjF1VWNyM1pYclVKeVpHN1NDcXFEQ19tOG5zV1A1azNhT1BOU1lnaWFSRlZjekE4WTZFNGE5dFR1eDVOUQ?oc=5
- [National Desk] Fact Check Team: Executive orders explained. How much power does a president really have? - National Desk (2026-08-13) - https://news.google.com/rss/articles/CBMihgJBVV95cUxPSTdpVVNpRDNXZXl0c0dib0lwakx4NHpJZUdvRnFQWGpSRVA1WTZLdmM4MTZfT3BtN1NGSjhUUFNjT21HLUhZOVhiam5iYlFRWWdvbGdaeHliUzB4UXpaek45WC1CS0h6SWlBWUxPNGdobkNZQ2R2MlBkVl83cnI5cEloRmc1RDFCWFhvNGlmNXlBWHo0UHRPNnVJYWdaRTMzek5VT1BCcmlCWVAyM0ZqaHl6S2ZlNFljdXptekRmSmFqVHp1dTFkNEhDak5RX1FvQUE1ZUQwVnJMeUVsNnVSN01SUWt4eWItS2pRY25KLV8zX2tIdGp4S1BMd29xaDVfMDhZX1Rn?oc=5
- [Center for American Progress] The Trump Administration Is Interfering in the 2026 Midterm Elections To Entrench the Imperial Presidency - Center for American Progress (2026-08-12) - https://news.google.com/rss/articles/CBMi4AFBVV95cUxNSDM1dkxielZMa3RLOXJ3R3VUeHJ3b1NLdkVHamU4TVJWR185YW9ZX1pKRks0U05jRlVjcFlhQWZOdkp6Vl8tZ2JlZnI3SGI5TlV0NFFEbU9MZGtvNmdBTmtGYjZPSU9jUzRaSmlKMjhSS2VIc0lYT2Njcl9Nd3ZSZzZWSXBFS0pGdXhQV2ZVNEJqZ0JPd2gtUXhudC1Ib2ladUxaaE53S3JydEQyMzhkSDhLTmg0dVZzOXY1MUI3bmladVlRZDhMTDhiMFE3dmxEUWdkRld1Y19KTTl2NlVGUg?oc=5

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 8 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
