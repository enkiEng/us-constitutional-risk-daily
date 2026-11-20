# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-20 12:28:55 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **10 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **-1.8**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.30 | 7.15 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.32 | 1.03 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.75 | 1.88 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.30 (Yellow) | ai | 0 | 2 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.95 (Watch) | keyword | 0 | 0 |
| Public Funds for Political Promotion | civil_liberties_information | 0.95 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- [The Columbus Dispatch] Ohio bill would let lone Republican audit Amy Acton, Democrats - The Columbus Dispatch (2026-11-19) - https://news.google.com/rss/articles/CBMi3wFBVV95cUxObDBfN0JrSjdhUjAzSW9ETXc1MVo5T2dsVHFIUmE0MmhSRmp5dEp0VkpqR044VjAwMFZoR0s3YU1pQ2lzcEFKMTI0YVAxUEI1bUJoYzlJTkRRckJ1clVwUEptYUFBdnpkdjA5djFjTmVDVHhodVcwR19UdzdMQWpqT284aWhtR3c4Z01HZFl0OFFvTVM2d2E1QnZrWmZkcmFQb0NmdDlNSUR2N0RaWU90cjdocVhEVUhhbUJjdkxGYzM1Zzl1YUI5TTJ5eEZISUY2aHBIalRpVXNObGdXRFA4?oc=5
- [ABC News - Breaking News, Latest News and Videos] 'Going to be practical': Sen. Markwayne Mullin speaks out after being named Noem's replacement at DHS - ABC News - Breaking News, Latest News and Videos (2026-11-19) - https://news.google.com/rss/articles/CBMipgFBVV95cUxQRGFPSVpoVFZTUlFjaDZRakItV05kaVlGVlluM1pMRGRvTkpaS2RFNlY2ZElwbFFOUEwtQVhSTzVVZlRmSmVBb1JFZDBaaVRqR05kNnZydDNBcFVOak5ENzZvRmdaOFdLTk9sUk9Kc3hSdnB4a3VEcGl6NDJ0M2RNTG9mMjFSUkd0MlNUYnl2QTNjeDI3aWt1UHM3WVBXaGhTOVY0VXBR0gGrAUFVX3lxTE1JN1FWZ1RwMHQ4aEpyckdLR2RxTnhucVUwZ21uVWZscnBKU3MxZFBQX3RaTXlBZE45YnBXLUo0OW4tSWRWdDRRVnFtTHhxbVdzMTJuLTNYQXdQUlB2M0hobldMT05hN2xscnlXLXVjT2VaX2I5WXlzWWdiY0lWNHIzZ0dDMnBDTFN5bUx1bXpQRkduNzdjcF9nS2ZqbTZZMm5YQmRaOTlPVjdNYw?oc=5

### Press Restrictions or Retaliation
- [ipi.media] Azerbaijan: IPI demands release of jailed Abzas Media journalists and others held behind bars - ipi.media (2026-11-20) - https://news.google.com/rss/articles/CBMisAFBVV95cUxNajdxSmNsWENuSHRpR0JyWWM0Rll0QzZad0M2anB5SjZ3VlVXQXM1MGpxR0xFaVliZnFKNUZCb3R5Skc5LXVNM2lHYjFUSjA1aWtVQk1uaDJRZE81ZHpLZnBiTmZESzhDMUtEOE5LZkc2MXp2c25LcUszSUpFN2Nwem14U3RPT1VHYXZKbnBUTmJVZ1Z1VHk3UGRxdDlPQjBQd0YwZEJYMC1uQVVuUzNHMQ?oc=5

### Legislative Bypass by Executive
- No fresh evidence links in the current lookback window.
### Public Funds for Political Promotion
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 23
- Query feeds failed: 2
- Primary-source lookups: 22 signals, 7 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - election_certification_interference: courtlistener: HTTP Error 401: Unauthorized
  - election_delay_or_cancellation: courtlistener: HTTP Error 401: Unauthorized
  - alternate_elector_scheme: courtlistener: HTTP Error 401: Unauthorized
  - politicized_prosecution_opposition: courtlistener: HTTP Error 401: Unauthorized
  - opposition_ballot_exclusion: courtlistener: HTTP Error 401: Unauthorized
  - court_order_noncompliance: courtlistener: HTTP Error 401: Unauthorized
  - judicial_review_foreclosure: courtlistener: HTTP Error 401: Unauthorized
  - independent_agency_capture: courtlistener: HTTP Error 401: Unauthorized
  - inspector_general_retaliation: courtlistener: HTTP Error 401: Unauthorized
  - military_domestic_political_use: HTTP Error 429: Too Many Requests

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
