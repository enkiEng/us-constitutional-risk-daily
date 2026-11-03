# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-03 12:27:54 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **18 / 100** (Elevated Strain)
- Previous day delta: **0.0**
- Delta vs 7-day average: **-1.0**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 0.32 | 1.11 |
| Executive Constraints and Emergency Powers | 13 | 1.10 | 3.57 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.30 | 3.25 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.45 | 0.90 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.30 (Yellow) | ai | 2 | 3 |
| Election Certification Interference | elections_transfer | 2.00 (Yellow) | ai | 1 | 3 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 2.00 (Yellow) | ai | 1 | 2 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 2 |
| Election Administration Capture | elections_transfer | 1.30 (Watch) | ai | 0 | 10 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | ai | 0 | 5 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.95 (Watch) | ai | 0 | 1 |
| Legislative Oversight Obstruction | federalism_oversight | 0.90 (Watch) | keyword | 0 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.25 (Green) | ai | 0 | 3 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: News report confirming that an administration aired TV advertisements promoting the officeholder using taxpayer funds. This constitutes spending of appropriated public money on communications that promote the officeholder rather than serve a public-information purpose, which directly matches the signal definition. The report itself treats this as a real occurrence (not hypothetical, opinion, or allegation), though the severity is moderate because this appears to be a discrete action that has been detected and is now subject to public scrutiny and potential legal challenge. No court order has been defied, no structural constitutional breakdown has occurred, but the alleged violation of the 1950s appropriations prohibition on 'publicity or propaganda purposes' is material.
- [ABC News - Breaking News, Latest News and Videos] Administration's pro-Trump TV ad is taxpayer-funded - ABC News - Breaking News, Latest News and Videos (2026-11-02) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxNNEc3UWRPWjdaWkt2Wk9vcklvTkd3LUU0eEFHNnBTNGE1M01jZ1ZsczFwN0o1VjVmMk9rU3kxOUx5M1N2V1MtLVRqNjFfUXJYV0FQeFJSV3pBSEJ1Y2NFV29FMzFGLUxmVGVRa2tVVnhwM3hRYVhzSnFRM2YzUklyR3BjQm4xOUltenU0V2lRSHB2SzJlVmpMLV9lMHdGT2dJU3FBZG5FVVnSAa4BQVVfeXFMT2lPdUJtQ0JKMEs1aVhMMUFfOXFWRmxwZlBsSk9LYjFHX3pMamdNOUV6c1BNZnQwdGtVUzRTMS1IVzJoWjl4c3Z1elZtdWotY2MwazN5UzhQNGk1TGtnSGJhMzI3WUNlY3BlemEzWGlNMkpGNnFjNXZiZU1vQVZ3SFRPYklhZjN1ek4wWUN3ZUt4YUxMcDJpTmhGMjhaVkg4Wm0tMm9CbERyWnVENjNB?oc=5
- [Knewz] 'Purely partisan': Federal judge orders Trump admin to pull three taxpayer-funded ads featuring the president - Knewz (2026-11-02) - https://news.google.com/rss/articles/CBMirAFBVV95cUxOdTAzMExyV184WDdCNVBCWlN5d2UzNnZwOUs4OGE0UDVYcnpVV0hCZGZkN0dJdnljV1diMzQ5X0ZSRmhOMXFZMDlWemlhOUV6ZHdzMWJrbGhJNmJhc3MwT2RrckxCX1lvQkxLUU9nMVlBUVBPcUhMNDVDTkY1ZlNFMkJjMUhpZmpLX3dRSTJJc3FmdGlIQjhDa3JHZXpxWjZhclgwNWlBSWUtZzVW?oc=5

### Election Certification Interference
- Assessment: This is a credible report that the Trump administration has requested a top court to set aside 20,000 California ballots. This represents a real attempt to interfere with election certification by seeking to override lawful ballot counts through judicial action. The action has verifiably occurred (a request has been filed), though the outcome remains uncertain. This constitutes a material stress signal: an official action to block or override lawful election results. Severity is 2 rather than 3 because it is a single legal filing rather than a pattern of confirmed successful defiance or a structural dismantling of certification authority. The source is a news outlet; ideally a court docket would confirm the filing.
- [The Korea Times] Trump admin asks top court to set aside 20,000 California ballots - The Korea Times (2026-11-03) - https://news.google.com/rss/articles/CBMirAFBVV95cUxOVm9sSW04eVBqYWQ1LVgxZmgwMHprNk9CUG9nR3NSQjN4RDdocndVTm1maV96Y3AyR1RyZlBoa0ZqeDNTckZ2TnRXd2VNMXdhWmF6WnctaWNnb1N6MFRCT2RBeEI3SkZkS0tCRTI1MGx4b2dzam9yOWFhbDY5cHB3YTVZQlFYMEZ2YmRJQ3NaLVNHc215ZV9lX21aSXZoc2F0NkR5WkRsNHFlQzJJ0gGyAUFVX3lxTFBGUnpoSnJHQVRXVUxXcVRkcVZ2WUpZZ2ZrQUxMYnBGdjVVMEpyNHZoNzZBTzcyczZ0VUpvX19yNkdybUREY0xqeW1HU2lJY0VFZzNrbTJ1RUtqYXJ0R3lWRjRSY1gtM0RsYVBPaEZxUmNBVzhRZ2tmWU5la2ppXzRiVmxMWG9tRzB5RjVCZ21jeTh5RDRLTnZpRFpfWFBoVk5wVEVkVnVMVjAzME5KRGJvX0E?oc=5

### Judicial Review Foreclosure
- Assessment: A federal court dismissed a lawsuit challenging Alaska Senate election certification on threshold grounds rather than addressing the merits of the constitutional claim. This is a concrete instance of judicial review foreclosure—a plaintiff seeking to test the legality of government action (election certification) was denied standing or had the case dismissed on justiciability grounds, leaving no forum to adjudicate the underlying constitutional question. This is a real occurrence, not a hypothetical or proposal. The severity is 2 rather than higher because this is a single instance of a threshold dismissal in one case, not a systematic campaign or structural breakdown. The court's act has already occurred (the dismissal issued), but it is limited in scope to one election challenge and does not yet indicate a pattern that would rise to severity 3.
- [CyberScoop] Federal court tosses Trump lawsuit challenging Alaska Senate certification - CyberScoop (2026-11-01) - https://news.google.com/rss/articles/CBMihAFBVV95cUxNR0YwRkpKTndxRzdoVl9hOV9vVHgxNkRWd3JONTgwU1hienJyTW1uY1V6NEVObktLZE8wQkZIVVNRaDdaMG04UUtPVXVheE00bjhLQzVNY0ZWWUhXRmhQeG0xRDF3akNuMjhncUdZSkNkUGpfY05zdjZkNktBNzI3RWNyc2U?oc=5

### Emergency Powers Expansion
- Assessment: A Presidential Determination under Section 303 of the Defense Production Act of 1950 is a lawful exercise of delegated emergency authority that does invoke statutory emergency powers to direct economic activity. Section 303 authorizes the President to require priority allocation and controlled distribution of materials. This is a real occurrence of emergency-powers invocation, documented in the Federal Register. However, it represents authorized use of congressionally-delegated wartime/emergency authority rather than an unconstitutional bypass of the legislative process. The DPA itself is a statutory grant of emergency authority enacted by Congress, so its invocation is use of authority granted in advance, not a constitutional circumvention. Severity is 2 (a real but contained, legally-authorized action) rather than 3+, as this is neither an extralegal assertion of power nor a defiance of constitutional constraint.
- [federalregister.gov] **[official record]** Presidential Determination Pursuant to Section 303 of the Defense Production Act of 1950, as Amended, on Domestic Petroleum Production, Refining, and Logistics Capacity (2026-10-28) - https://www.federalregister.gov/documents/2026/10/28/2026-22052/presidential-determination-pursuant-to-section-303-of-the-defense-production-act-of-1950-as-amended

### Election Administration Capture
- [California State Portal | CA.gov] Governor Newsom highlights California’s work to deliver a free and fair election tomorrow; defend democracy from ongoing and anticipated attacks - California State Portal | CA.gov (2026-11-02) - https://news.google.com/rss/articles/CBMiiAJBVV95cUxPRHhNWG5lMk9tWno2VHBOVV9MT1ZwV3gzQ0xiNVE4a1UwMVg1dUd1Y2w1OVBZNTc1b2d6bEhGQUdNM2JpVmlNY0JRNzhSUmRfU01mNThrVHhxQXI0STliYk1hNWVfYlJGcEpmZnVCbnhNYlB4QWh0TTRpTnlsOVRQa2tCNU5SWUh5RWJZd1lZdmpaenB6Uno2Y0tpVWwyWUhaVy01SEZyeFN3Njd6S1VQdkNoRnF6UW1uOUx3d3lYd0s0a0dHRFBDR1BIVTJucWlKamljZlE4TW1CdllRVzdSbjUtdkZtRFA4X0lDQ2V2Z0xiREtZN1U1Vm92dEh2YlhCdm1SVXVRQms?oc=5
- [Spotlight PA] What to know about DOJ election monitors in the 2026 midterms - Spotlight PA (2026-11-02) - https://news.google.com/rss/articles/CBMiwwFBVV95cUxQQkcyRXlUMWIyb2VQQUlJVm16VmFfMXE2cHB3b0hUdWFuRTVETFhNdFg4clhVWDUtTW8wMzk4bmxSVmVVN3EwZEpESC1ZdG5tLVJHSjVjUEZOei10TFNrTThVOUR3dnBuMDFBUHdaZ1lReXh3UjlwXzgwOTZudW1ueGdWM0wtcnRDXzFFWWp0bC05eVFZRGk5aEJfdGxzQW43QTFKcWF3WkRQRlBSNDY2N3VoVXJyc0h0UmQ0MG9JX0Jrams?oc=5
- [Tennessee Lookout] Tennessee Supreme Court paves way to cut Metro Council, give state control of airport authority - Tennessee Lookout (2026-11-02) - https://news.google.com/rss/articles/CBMi0AFBVV95cUxPdlBsOUsweUp4dzVwWVZ4Zl9jcmhleFVlNmoyQlNMN1lnM0JZVmZIbFllNVBNNTA4cEphNDZxWDlSUlBPaEpMWjRMcDQydHdFUlozbTlIYUNzQ2RheWRlNmZTZVhTUDRxSmVzVVdXOE9jeEQ3YlNMUnhmNUtGLWs1cGJvRkRrME5Qakh2SEo5WEZRUHVwM1NvWUpDQ0draEVZaVlWbTRFVlFDeUJlZ19Wc2pMMGVnMkV4cjBUSDZLZUVRNkEwcDdUYXlKLTBZTHpt?oc=5

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
