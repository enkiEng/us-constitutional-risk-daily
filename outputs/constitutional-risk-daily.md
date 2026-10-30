# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-30 12:32:45 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **19 / 100** (Elevated Strain)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **-3.6**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.95 | 5.22 |
| Judicial Independence and Rule of Law | 15 | 0.24 | 0.89 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.15 | 0.38 |
| Civil Liberties and Information Environment | 10 | 1.22 | 3.04 |
| Security Sector Neutrality | 8 | 0.12 | 0.25 |
| Federalism and Legislative Oversight | 8 | 1.30 | 2.60 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Oversight Obstruction | federalism_oversight | 2.30 (Yellow) | keyword | 0 | 0 |
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 4 | 5 |
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 1 | 2 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Election Administration Capture | elections_transfer | 1.95 (Yellow) | ai | 1 | 10 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 2 |
| Court Order Noncompliance | judiciary_rule_of_law | 0.95 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.95 (Watch) | ai | 0 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 0.60 (Green) | ai | 0 | 0 |
| Election Certification Interference | elections_transfer | 0.25 (Green) | ai | 0 | 2 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 0.25 (Green) | ai | 0 | 1 |

## Evidence Samples

### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
### Public Funds for Political Promotion
- Assessment: Court order blocking taxpayer-funded partisan ads represents confirmed judicial action against alleged misuse of public funds for campaign-style promotion. The judge's issuance of an injunction is itself an action that changes legal status—the administration can no longer air these ads without violating the order. This is a real, credible stress event. However, severity is 2 rather than 3 because this is a single blocked campaign caught and restrained by judicial review, not a structural breakdown or pattern of defiance.
- [Common Dreams] Siding With DNC a Week Before Midterms, Judge Blocks Trump's Taxpayer-Funded 'Propaganda Campaign' - Common Dreams (2026-10-28) - https://news.google.com/rss/articles/CBMidkFVX3lxTFBaRnJfaE0xNnU5LWdFZVpTSHJKNzhnTHNINmJPSUVfWmlUTHNOVTFhZDhlU01aR2V1QWhYTkZRR0FJSGE5RVpCd1ExNzJNQ1RnTUFMSTVsWXQyQWlhSk5LODQyaFhSUTk5cjZlc2xHYldZdlZIalE?oc=5
- [The Independent] Trump barred from airing White House ‘propaganda’ ads, judge rules - The Independent (2026-10-28) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxNOEJkdmhSQklvQUdNY2xhV2hXaFpiZjFRQjFyNERvWG5rM1ZOek9pVmQxeVlyNnc2NmZaZmhpOU1MVHFqVFo5eFVIZmtxRWloYWVWMF9zU2pqRkVKc3VIOTRwVkxCRUloVWNWMzk1bURqX0h1VHpqLWxuU0pBWTU1MGhyRjZYWm8zT0JXZV9xVWlsdmpLSHQ0ZzRaZURCT1VUVW00YjAxUmxId1c0WUJPZTJFLWxkbGNy?oc=5
- [AOL.co.uk] 'Conceded the merits': Judge issues injunction barring Trump admin from using taxpayer funds for 'partisan campaign' ads, finds DHS likely violated the law - AOL.co.uk (2026-10-28) - https://news.google.com/rss/articles/CBMijgFBVV95cUxPS1V2VVdYdGZtbWxodHk4RldORjlFdG11dlpqeVpsc1NWRnY4TGwzQ3pEaVF0MTFpSGFORFM3alJRQUt0aFpfSEhRN0NhTEFRV194Q01DS1NuSUpIcTZtdG94dkdXY1NTUUZxbVJHYTFuaWRfRXNtdmZ2M0lfX2syVFZLSkxjSXVnTzdHempR?oc=5

### Opposition Ballot Exclusion
- Assessment: A Florida appeals court has issued a ruling that upholds removal of an incumbent from a local ballot. This is a real, confirmed judicial action affecting ballot access. However, without further detail about whether the removal was procedurally proper, legally justified under applicable election law, or part of a systematic pattern, and given that it appears to be a single local-level action subject to appellate review (suggesting normal judicial process), this registers as a contained, credible stress signal rather than a structural failure. Severity 2 reflects confirmed action affecting a real candidate's ballot access.
- [Sun Sentinel] Appeals court upholds removal of incumbent from Tamarac commission ballot - Sun Sentinel (2026-10-30) - https://news.google.com/rss/articles/CBMitAFBVV95cUxOaXM3M3JhSUp6dWQ3UHduQVBhQ0ZNbDM1R05ndHh1SkwyRGM4U2ZnaTRSQmdPZzM5cUFiVmN4bVNkMFRMZ18zYjI3dElKNkktRHJvVllmWDdEVE5EdVhqbXhPMWUwSllUNk4ybjkzWDdNLS1kdzRxdnhtX1pTWmt4cDNNT01DdzdicU1oOFgxZnFzcVlOQTVMNEZvS0I2eHJXTW1Xc1ZHN25mU3BYTDVCWFFDSEo?oc=5

### Emergency Powers Expansion
- Assessment: A Presidential Determination under Section 303 of the Defense Production Act of 1950 is a lawful exercise of delegated emergency authority that does invoke statutory emergency powers to direct economic activity. Section 303 authorizes the President to require priority allocation and controlled distribution of materials. This is a real occurrence of emergency-powers invocation, documented in the Federal Register. However, it represents authorized use of congressionally-delegated wartime/emergency authority rather than an unconstitutional bypass of the legislative process. The DPA itself is a statutory grant of emergency authority enacted by Congress, so its invocation is use of authority granted in advance, not a constitutional circumvention. Severity is 2 (a real but contained, legally-authorized action) rather than 3+, as this is neither an extralegal assertion of power nor a defiance of constitutional constraint.
- [federalregister.gov] **[official record]** Presidential Determination Pursuant to Section 303 of the Defense Production Act of 1950, as Amended, on Domestic Petroleum Production, Refining, and Logistics Capacity (2026-10-28) - https://www.federalregister.gov/documents/2026/10/28/2026-22052/presidential-determination-pursuant-to-section-303-of-the-defense-production-act-of-1950-as-amended

### Election Administration Capture
- Assessment: This reports that courts are deciding the fate of Trump's latest push to control voting. This confirms an actual effort is underway and is being contested. However, the matter is still in court; the outcome and whether the push succeeds are undecided. A push to control voting mechanisms that is subject to court review is a real stress signal, but since courts are still deciding and no structural takeover has been confirmed as successful, this is a weak (severity 1) signal of attempted capture rather than confirmed capture.
- [KOTA Territory News] Courts to decide fate of Trump’s latest push to control voting as Election Day nears - KOTA Territory News (2026-10-28) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcWdBRV9oUzJReGIyOW8weXdvU095Zm1GY2FwZklkUEF2c3dRMVlIYUo4OUZrRDB0QXVTTUZUYU9rVmlPYjJhU2tManpfVjd0YzQ5VXNkMUtuR1FhakwzNlBOSjU0bmdiT2xsUzNYN0RnazdLYzVvTnR1T1RBdUF3Q3ppSU9nUmdhQWs4NjBRZHluRW5KaGZrMTdVbXpfeEZVSjdUcXloXzdCd9IBvgFBVV95cUxNTTJqdUJ0UDY5S21LcGVoVzlPelkxaDFXay1yWUx6d3RBNTRRbkhDZmd3TTZwWjh2Q01vNFdPazRtdUg4MVVRX3Fta2twdTh5N2YzT2Q0ZEhPZDh0a2VRb2NjTWdlVmxWSkhaYVFtdXVLTkp5M1Zab3dxUnpTQ3oxSHBfcDNvR21aUkhhR0kxZ2cxc1U2dm9URjJqXzNuZnJwUVZsQnVlc0ZOUm1lZHh4M243T2JBZHcxczBGS3FB?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 9 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **High**
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
  - military_domestic_political_use: courtlistener: HTTP Error 401: Unauthorized

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
