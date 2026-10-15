# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-15 12:42:10 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **6 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **-3.1**

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
| Civil Service and Agency Independence | 10 | 0.24 | 0.59 |
| Civil Liberties and Information Environment | 10 | 2.00 | 5.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 3.00 (Orange) | ai | 5 | 6 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 3 |
| Independent Agency Capture | civil_service_integrity | 0.95 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.60 (Green) | ai | 0 | 4 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: Report indicates government spent $10 million on pro-Trump ads after president indicated a super PAC would fund them instead. This describes actual expenditure of appropriated public funds on partisan political advertising promoting an officeholder, which directly violates the 1950s-era appropriations bar on publicity or propaganda purposes. The fact that a super PAC was supposed to fund it but government funds were used instead, after a presidential statement, indicates knowing misuse of public money for campaign-style promotion. This is a confirmed high-severity action meeting the signal definition.
- [Oregon Public Broadcasting - OPB] Government spent $10 million on pro-Trump ads after president said super PAC would fund - Oregon Public Broadcasting - OPB (2026-10-13) - https://news.google.com/rss/articles/CBMioAFBVV95cUxQc0ttNUdGUTNncV9rNTkyZzhkbmY2ZTZUWTRhU0IyOWE2cDNmQThxZTloRzdkVkY2Tm9WZ0E1UGx0ZUNFV2xEa2wxYmY0RHRLMDZVcjluUDJfbVYxeUVNaDJ6R0xGcmQ4NXBTb0dXaWJrZUJrMzNCNUZmMXQ0VjJaSmpVNE9hS1RvOG1QS2dCOWROSUhGWXJ0eGl1WEFfRkdB?oc=5
- [Ars Technica] Trump commercial railing against his enemies kept airing after court blocked it - Ars Technica (2026-10-13) - https://news.google.com/rss/articles/CBMivwFBVV95cUxOQXZNNkN6dGw5bmpGY1Z5LTRXYVJSN1Jkci1YN0NlVXE2ZnhlS2RqN3VLNXFfM3J2bzg1ZUhsV2tlMzNuYWg2elhfUzdObG43NzZEa0kwMU1Fc01lSFplNF9YaWZYWWxVbjJzRFRXN19BRld1SGhnUUViNWpIUy0yMEZlOE83SW5OZklMeVpsbk42b2FHeWRfbzc2Tzg4V2t4OFlOaFJCeEgtWE1KMlphNjA1WXNOX3NmQ3BqSC1sOA?oc=5
- [- SoMD Chronicle] ‘Egregious and utterly illegal.’ Maryland lawmakers blast Trump’s taxpayer-funded TV ads - - - SoMD Chronicle (2026-10-14) - https://news.google.com/rss/articles/CBMipgFBVV95cUxQdGgwcUFFa0J0eXVGcHBLLTNuX1R5cGpPVkJUSnpnT0VJYjgwNkl5ZUthTExiRHBQWndwSkh3c2VVMkJjNlB0UmIxLVpOYlpxSG1ZQmhYWGQwV1lKWXRqTzdRZVRoWXp2UldyLVdLZ0FYZHVHWk1jUkVpLW5xZHhoNEkxSFBvdlVrOU9lcGZrSngtLUZNNkl2LVBfVXp0THBYc2NERzln?oc=5

### Press Restrictions or Retaliation
- [The Express Tribune] Judge extends White House access for CNN, MS NOW, Politico amid legal fight - The Express Tribune (2026-10-14) - https://news.google.com/rss/articles/CBMirwFBVV95cUxONE50OUF0LU1waHVUMHJhOW5PTk1URUxhOGtxSkFWRUF1V2lZN2hCNE8zbzJYVWR5Z0JFZGlyVUUtNS0wdVFpZjJpckhtalVrWHlVQ3pOM2NzQmVOaHctYnRIb0l6QzJULTBsV0hMS3Z6MTFCUVVMSmVCYjJYdmFJN3RFaFpQem9JbHlibnh4WnRraEZaV1YySFAtQ0VKbjJGV0pBUWk1M3RHcXdHVnp30gG3AUFVX3lxTE1UZjhoU0QxcWJYX0duakxlV2lES21rdVRSVGs3UGxQNWNkaDhMbHVXMVpUTTRvMWtjenBOVjJIaDRBT3N3bUhjV1p1MG15LXBoYXlmcTBIQ0hmREtvZENGdXJiRzk5dWpXR19YcXZhUFVTM01DSmRHc2tJNjEwX1N4NHZkRV9Nckk1SUY2cEhZRk9vX3BCel9KUGJwTjVtcmlQVVRrM2s0UUdQcm03VlNtV19MSi1aZw?oc=5
- [https://dailyasianage.com/] Democrats Slam White House for Showing Hostility to Journalists - https://dailyasianage.com/ (2026-10-14) - https://news.google.com/rss/articles/CBMiowFBVV95cUxNU1lhUmVoaURNYnlyNEhjdHJBejVkQXUyQTFCSTV6YjB3d1ZMM01oZm5tM0NCZ0hpUFhnZFhqalNBUDFZY3hIYXJkdGZwQ2g5UFhmMWN0TXNlRmlEX2o5c2V6UjJUQ0U0N3NvMW5iSkpidmJsalhyUVBtZmduQ3FZOHFqUWdxbVNiUml0U1JaQUFSSFlnNEdhNUc2WGtWMk9tMU9V?oc=5
- [MyJoyOnline] Judge extends White House access for CNN, MS NOW, Politico amid legal fight - MyJoyOnline (2026-10-14) - https://news.google.com/rss/articles/CBMipAFBVV95cUxNMTZpRzdFT2lMQTdtMEIwcmpLRjZ6eE5VSWIwak9VUkdFQWFkeGdENEdMUmg3RXBGOXU2UzFuLUZzUVFRd2FPMEdsS2RZQjNldUQxOXJmZVh2V1RnUjZodzVUR0diMUpBejZjOHQzd1YwRTZTdWhGamtWdUkwNTZqTnhhWEZIMngxakFybjBHdHhpaEQzRUM5dGVfODhoaXcwcHpxdg?oc=5

### Independent Agency Capture
- [ИФЗ РАН] Why The White House Battle Over Federal Reserve Governor Lis - ИФЗ РАН (2026-10-14) - https://news.google.com/rss/articles/CBMilwFBVV95cUxNbExfdnkxMV9OaE4yQXNZeGZYNS1vbTFBWVluT2hBdjFQNjhPZGh6UTM1SnJmNXE0RXFqU0RmTXRHYkFnSFVwanY2eEJXRnJ4bVRzSUE4NW0xeGtIVkluYVhRTm8wQlU5eW9iMnZfb21vNjVqa2dYeGxpbUZFeDNLdU9lOUZSejlacEp6RDRqTHdxN3ZxSkxr?oc=5

### Legislative Bypass by Executive
- [Protect Democracy] Frequently asked questions about the 2026 midterm elections - Protect Democracy (2026-10-15) - https://news.google.com/rss/articles/CBMimgFBVV95cUxNaGc2YzZlb2ZjZmFHdmFUZ2o2eGtYX0phYl9lWUcxaHVFV2N2NlIzbjFsejdlMUJLdnZoclpkakw0d2U1VjlTODBETDVXNW9iWmZGMU93R2lRRy1iYW50eXZmQnduUmhlZWRZbWlPNlRkQ1IzTmdTTjM2T21kTnhZdHlhYlVROEFVY1NGN3ZDRVZGVENsTTVzYk9n?oc=5
- [Election Law Blog] Watch Archived Video of Safeguarding Democracy Project Webinar: "What Can Go Wrong (and What Can Go Right) with November's Midterm Elections?" - Election Law Blog (2026-10-13) - https://news.google.com/rss/articles/CBMi_gFBVV95cUxNZ2pXa0dOU1N2TFItS3RKOFdqNC12UUJBU2p4ZUtKTWlVeHJGQzVLU0xxMVkwM1RwSjAxLTFqWGFHNnRsZU43X2I0MDlXZ21XMGM3TmxSU1NvVGpWWGpRQ0dINF9rUEtKblRkakxUS0dLaV81cXh2YjFiTTZDV0xSMDNNZGtuSEh3QTl3TTZzRlBlekRDVUtZUEprSFJNZUZHenFVdU5ic21oTTlaMVJ3RUk5WlgtbXdhSUNMMkFrM0JUdFNBc1BUQmxHdThSRG5TR0llWFpCUmZ4TmlQNGNpc2t4SzB3WkUzLTFjenlvVHpmdm5JbzVBbkFTVFM1QQ?oc=5
- [Reuters] Nine ways the Trump administration could interfere with the midterms - Reuters (2026-10-14) - https://news.google.com/rss/articles/CBMijAFBVV95cUxOdTJERWh3UV90cVhMS01kYVY1TzFKSGFndGROSDlWNnpLaWhhUXp6VkJSQ3VwZHJWb1NyeEpVX2dJYzBIaXFtb0dmc19KM1cyemlRVzA4NWxGeHRLRHRTZDdPMVdmRExwMmtvc0tqcjRnRzAzLTlBVURZV2J4VnJxbTJnX3dEdTFad2RvZA?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 10 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
