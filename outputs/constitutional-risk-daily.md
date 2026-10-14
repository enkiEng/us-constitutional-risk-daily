# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-14 12:40:59 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **7 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-3.7**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 0.06 | 0.23 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.32 | 1.03 |
| Civil Service and Agency Independence | 10 | 0.33 | 0.81 |
| Civil Liberties and Information Environment | 10 | 2.00 | 5.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 3.00 (Orange) | ai | 11 | 12 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 4 |
| Independent Agency Capture | civil_service_integrity | 1.30 (Watch) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 0.95 (Watch) | ai | 0 | 2 |
| Court Order Noncompliance | judiciary_rule_of_law | 0.25 (Green) | ai | 0 | 0 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: LEADERSHIP Newspapers reports a US judge's order to halt taxpayer-funded ads promoting Trump. Another corroborating account of the judicial intervention against the unlawful government spending. The order itself is the serious action; severity 3 reflects confirmed court response to the breach.
- [LEADERSHIP Newspapers] US Judge Orders Trump To Halt Taxpayer-Funded TV Ads - LEADERSHIP Newspapers (2026-10-12) - https://news.google.com/rss/articles/CBMigAFBVV95cUxNX1NWcmIxbi0tSnJLc0JmSTdEdHFBeUcxVy1vM21NS3RpN0xXb3VFSHNKM2lJcXc3UGhJeHRBN29TSWxZcXJZVEc3WENfMUhGU0NlQ254b0s0dXVFMFk5aDBrUWlxNE93YmN2WUhDQ08xaTVmSjhlNHlZWFQ3MF9vMg?oc=5
- [Blueprint Newspapers] Trump ordered to halt taxpayer-funded ads promoting himself - Blueprint Newspapers (2026-10-12) - https://news.google.com/rss/articles/CBMiiAFBVV95cUxQRTQyZDRYWHlZSjZzZ1p4Um4tMlUtSlVrRHJQZkZoeU5YSk5Jd3F4NkFOWW5YMEF3NExHbmZxYnNNMW5Ca0tXV2syMXE0ZkFDcXZVc3NZT1FEb0E1aUZ2UHA4a1VNYmFYRjJIYVhKS25hNUtCRmxEelVydjQtQXNJd2xUM09xbG1u?oc=5
- [Campaign Legal Center] Campaign Legal Center Action and Partners Successfully Halt President Trump’s Illegal Taxpayer-Funded Ads Scheme - Campaign Legal Center (2026-10-13) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxNZHMzN002ZGhPbE53bUEtclpRaXRERjR6M2RWV3NvNmxxcXQyRW1mMFloclZaRHlQb1BneXdvZ0xRblZvSU5PdWRnQkI2ekVhbldlaHZFcmhjY1BjU1ZMWi1IWjROYXN0LS16dVN2enk0alJuclZEN1lTRkNpakNFRWpINjFyUVJ6NkhoMEtSYXJkSGp0Sl85X18yUFRjOGdPandMd24zUVpfZEhRemZ3MmhCWHMzUlBB?oc=5

### Press Restrictions or Retaliation
- [조선일보] Russian FSB Detains Japanese Journalist Over Espionage - 조선일보 (2026-10-14) - https://news.google.com/rss/articles/CBMihAFBVV95cUxNbHZjRDViQ0tPNXNJWHN5SWpUbTNzM2d3VmtIVmtDbjBNdHJhcjNORmNpcmhiYTYzdTJ1aTJvakJLbF9WN3FrSUZsT0VqYVhiYnM0Tk8xMXVVY2hxNEIxM1Z1T2gya2FTeVNUUFBlZTRpejJKelIzQjhyS0hGRW5nSlNKQzY?oc=5
- [The Express Tribune] Judge extends White House access for CNN, MS NOW, Politico amid legal fight - The Express Tribune (2026-10-14) - https://news.google.com/rss/articles/CBMirwFBVV95cUxONE50OUF0LU1waHVUMHJhOW5PTk1URUxhOGtxSkFWRUF1V2lZN2hCNE8zbzJYVWR5Z0JFZGlyVUUtNS0wdVFpZjJpckhtalVrWHlVQ3pOM2NzQmVOaHctYnRIb0l6QzJULTBsV0hMS3Z6MTFCUVVMSmVCYjJYdmFJN3RFaFpQem9JbHlibnh4WnRraEZaV1YySFAtQ0VKbjJGV0pBUWk1M3RHcXdHVnp30gG3AUFVX3lxTE1UZjhoU0QxcWJYX0duakxlV2lES21rdVRSVGs3UGxQNWNkaDhMbHVXMVpUTTRvMWtjenBOVjJIaDRBT3N3bUhjV1p1MG15LXBoYXlmcTBIQ0hmREtvZENGdXJiRzk5dWpXR19YcXZhUFVTM01DSmRHc2tJNjEwX1N4NHZkRV9Nckk1SUY2cEhZRk9vX3BCel9KUGJwTjVtcmlQVVRrM2s0UUdQcm03VlNtV19MSi1aZw?oc=5
- [https://dailyasianage.com/] Democrats Slam White House for Showing Hostility to Journalists - https://dailyasianage.com/ (2026-10-14) - https://news.google.com/rss/articles/CBMiowFBVV95cUxNU1lhUmVoaURNYnlyNEhjdHJBejVkQXUyQTFCSTV6YjB3d1ZMM01oZm5tM0NCZ0hpUFhnZFhqalNBUDFZY3hIYXJkdGZwQ2g5UFhmMWN0TXNlRmlEX2o5c2V6UjJUQ0U0N3NvMW5iSkpidmJsalhyUVBtZmduQ3FZOHFqUWdxbVNiUml0U1JaQUFSSFlnNEdhNUc2WGtWMk9tMU9V?oc=5

### Independent Agency Capture
- No fresh evidence links in the current lookback window.
### Legislative Bypass by Executive
- [electionlawblog.org] Watch Archived Video of Safeguarding Democracy Project Webinar: "What Can Go Wrong (and What Can Go Right) with November's Midterm Elections?" - electionlawblog.org (2026-10-13) - https://news.google.com/rss/articles/CBMi_gFBVV95cUxNZ2pXa0dOU1N2TFItS3RKOFdqNC12UUJBU2p4ZUtKTWlVeHJGQzVLU0xxMVkwM1RwSjAxLTFqWGFHNnRsZU43X2I0MDlXZ21XMGM3TmxSU1NvVGpWWGpRQ0dINF9rUEtKblRkakxUS0dLaV81cXh2YjFiTTZDV0xSMDNNZGtuSEh3QTl3TTZzRlBlekRDVUtZUEprSFJNZUZHenFVdU5ic21oTTlaMVJ3RUk5WlgtbXdhSUNMMkFrM0JUdFNBc1BUQmxHdThSRG5TR0llWFpCUmZ4TmlQNGNpc2t4SzB3WkUzLTFjenlvVHpmdm5JbzVBbkFTVFM1QQ?oc=5
- [Liberal Currents] Checks and Balances Will Not Save Us - Liberal Currents (2026-10-14) - https://news.google.com/rss/articles/CBMieEFVX3lxTE9Lbm9nZEVlYXBzQllzTkVIZ2Rzb3FoNDh4cjVlV3Y1XzhYQ3pOLVJpQ21BcEJuSGdVZXZMME1NNG1aNHpCNzUwdUtxX3BiSmxsTC14eVZ6cFlKWC1pYVZiRjNjT3RYSjZiSkNPR2VaazlrWHhneWhxOA?oc=5

### Court Order Noncompliance
- [courtlistener.com] **[official record]** Allina Health System v. Minnesota Department of Human Services Commissioner John Connolly (2026-10-11) - https://www.courtlistener.com/docket/74943556/9/allina-health-system-v-minnesota-department-of-human-services-commissioner/

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
