# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-30 12:48:01 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **8 / 100** (Baseline Institutional Noise)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **-3.3**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.25 | 1.38 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.06 | 0.16 |
| Civil Liberties and Information Environment | 10 | 1.33 | 3.33 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 18 | 35 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 6 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 2 | 3 |
| Election Administration Capture | elections_transfer | 1.00 (Watch) | ai | 1 | 4 |
| Martial Law or Military Governance Language | executive_constraints | 0.60 (Green) | keyword | 0 | 0 |
| Statistical Agency Integrity | civil_service_integrity | 0.25 (Green) | ai | 0 | 0 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: News report from NBC citing an official statement that pro-Trump TV ads were paid for with CBP money. This is a credible report of an actual spending action (not a proposal or hypothetical). The ads are election-adjacent ('pro-Trump') and funded by an appropriated agency account, matching the signal definition. However, without access to the full text of the ads or a government audit confirming prohibited partisan/campaign content (versus borderline public-information framing), severity is held at 2—a repeated, credible stress signal of a real but as-yet-unconfirmed violation.
- [NBC News] Pro-Trump TV ads paid for with Customs and Border Protection money, official says - NBC News (2026-09-30) - https://news.google.com/rss/articles/CBMirgFBVV95cUxPLUdXSVlRTkJ5U2IwRUhEakgwTi13NWsyUFJOcExGVF9aMFZfXzdKVUNIZEI4NlZ3WjhaNzNoVExTVTdkQ3N4bWdqRTR3c1pmTXdBaTZqeXY5c2U4LUdqNzdGX3JtMDhqbllKMFdCSFQ1ZlVTLUJrVmIzMkEwLUI3X1FfcVEwRGgwd0VkU1RUSlhpeExpSk54SjhwLUJVOVlhY0R3UUJ6ZE84ME8wLVE?oc=5
- [PBS] Homeland Security spending $20M in taxpayer funds for pro-Trump ads - PBS (2026-09-29) - https://news.google.com/rss/articles/CBMipwFBVV95cUxNZDlpTmFNd1IwREdDeVNFcnVFSThEZ2xOazdOakxwdUVqczByekptNFFmeDRCelhmejhDRnF3TGZ5c3ZqWDNkSDA2TUZIZmsxUkJZTEY2OTV4Ukd5ZHVpMkNRVHY5aWhVcm13WkJZanFXZTg0cFEzZGp1V2M1SHdmbmhfZmJVUUVPdEgzUUdleVdJcFhTb0h0SkZRQ2NrREY1bXBFdGJNRdIBrAFBVV95cUxOU2hjZ3JITUlGaDB4TXZLSUVWNnp4TWdmdHp1emdFcC1YRTA1dGdxR2NCNHJKQlYyZ0RjZ1BrNWFjWFJrM1FSUGdrQmsyc3RsVUhNemI0OTZVeUIyd0s3dXFkQWIyRHRxUFpwWk9MTURrTExkN0kzNU04SFV4UUs3cGdJVFZSSGZlN0VNVDFwYUhvS0xOZUZQSF8zNTMza3VHcFdvTUZUWHdxZTR2?oc=5
- [cbsnews.com] Can the government use taxpayer money for political commercials? New pro-Trump TV ads raise questions - cbsnews.com (2026-09-30) - https://news.google.com/rss/articles/CBMiiAFBVV95cUxOcVoyaTFseWtaZDhHOF9rbEh0UUhhRkE4LU5MeDN4Vkh6cjh6R1h0V01XaUQ2YzVoak1DOUFXVXFjUlR3MjBOR0pOQzZOZWx0Y0k5b2dhZGtXSzNNQzFnWVpsS3J4ZzBnSFA2QzlVek1jVzJmeTJ0UUpLV2xsZ2VDb2dUeC1mQzRE?oc=5

### Legislative Bypass by Executive
- Assessment: Trump is seeking to cancel $810M in congressionally approved domestic programs. This represents an attempt to bypass legislative appropriations through executive action. However, a 'seek' or proposal to cancel is not yet an accomplished action that shifts governance from statute to unilateral executive action—it requires either successful execution or an official directive that removes the funds without further congressional action. The framing as a seek/proposal places this at the boundary between proposal and action. Without confirmation of actual execution or an official impoundment/rescission order, this is a credible but not yet fully materialized stress signal. Scored conservatively as severity 2 (repeated or credible stress signal of a real but contained action) rather than 3, pending evidence of actual implementation.
- [The Well News] Trump Seeks to Cancel $810M Congress Approved for Domestic Programs - The Well News (2026-09-28) - https://news.google.com/rss/articles/CBMirwFBVV95cUxON0JQSmZZaGJrWmlEaGdENUhhRnJoSEVSVDJBSTVRMHR5ZTZGa3otVXk0NXJhZlFlTmg4ZjdXUTNRWjdJQVRXOU52dXMxMkNRN3ZJeUdldWZleG5YVFhQcU5aS0dpdW9QN2p1S2YwaU5EbmdBaGFYWDFKM2U3S3BGd29hQXl4dmlQV2ZaUFZyclM0cE5DQWVFYUw5dkxXemJINnl4TUZ0YXNQdzZrMERB?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-09-30) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5
- [Outlook India] Why Trump’s White House Media Ban Has Become A First Amendment Fight - Outlook India (2026-09-29) - https://news.google.com/rss/articles/CBMirwFBVV95cUxOeUZYRFA1aUJGZnNiSDZMbkZ3WWNtOHlVaG5EVnQ5LVZFVnFRd2JtY3d3UlVFV1AwZFNtbFVvN2k2eU9MYUJzZVRlVXBiSzVZbTlhUHBJcWpoSnozNWN2b2dGSHFGRjgxRlFGV0oyTnBGcmFpMXFTbzNiN1IzSTdLcV9mdl85ZE0xdnJMb0ViRDhDeUY2c251Z1ZUbTIwMjhGVnZ2aUlsUzlpUnJGLUxF0gG8AUFVX3lxTE5GVjlZemhRbWhmUi1DMnloUnhtQnljSHJZYUdkb3JFYlFYM1p6QXNXY3l1MVlVcFJxVXBsWWxrV2lQZ1NDMTVuMGdUTHM1YkJNbW5GWDJSMWlzN3VwdnRlUFpwTDZrZExCaVhuUjJsX2xIZW41U2RzRzNnMC1DY3ROTUREdUthRGJ6ZXg5VW9VYjFrMHE4d2F4bXlnek93OHBfU1UzaF80Y3puVEtCWEpKTXpndTRQQnFENUxh?oc=5

### Election Administration Capture
- Assessment: The item reports that some North Carolina county election officials promoted conspiracy theories about the 2020 election outcome and January 6. This is a real occurrence—officials in administrative positions making partisan statements and promoting false narratives about elections. However, this is isolated conduct by unnamed officials at the county level and does not demonstrate systematic partisan capture of election administration authority or removal of neutral process safeguards. The severity is 1 (isolated or weak signal) rather than higher because: (1) it describes individual speech/promotion of conspiracy theories rather than structural changes to election administration authority; (2) it is geographically limited (some NC counties); (3) there is no indication these officials used their positions to alter election procedures or outcomes; (4) it does not show they have captured the administration in a way that prevents neutral process from functioning.
- [The Asheville Citizen Times] Some NC county election officials promoted conspiracies about 2020 outcome, Jan. 6 - The Asheville Citizen Times (2026-09-30) - https://news.google.com/rss/articles/CBMi3gFBVV95cUxOR3V1XzVWLWtERDNOMlRjTm5NR0UtbHl1d1BPeF92Mnl5TDRydzh5LTVBYVlnUUt3S1NyYXFKZWRNYXdNTDVIMkZQWkFJQzgyaHRUbU93clAtTldBQzlzS3lQeGpDaUN5NjVLbHI0ZjRDekxreW9rallTNm9HY3pSRXdJSlZvUUUyZEQxOXZZVGhzeVlCOWJ6ajZiS2FXRWY4VUN2THhPa1hkLTQtSWw1amZjZ2dQQTJzdDJOaFVoQXhjazY5MkVXemVEeW5tdWFDM0lFV0ZjanVyRFRBbVE?oc=5

### Martial Law or Military Governance Language
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 13 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
