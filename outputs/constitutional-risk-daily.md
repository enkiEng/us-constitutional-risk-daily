# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-02 12:27:57 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **18 / 100** (Elevated Strain)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **-2.4**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 0.43 | 1.52 |
| Executive Constraints and Emergency Powers | 13 | 1.22 | 3.95 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.65 | 4.12 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.62 | 1.25 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.65 (Yellow) | ai | 0 | 3 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 2 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 2.00 (Yellow) | ai | 1 | 1 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 10 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 6 |
| Opposition Ballot Exclusion | opposition_pluralism | 1.30 (Watch) | ai | 0 | 1 |
| Legislative Oversight Obstruction | federalism_oversight | 1.25 (Watch) | keyword | 0 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.60 (Green) | ai | 0 | 1 |

## Evidence Samples

### Public Funds for Political Promotion
- [Time Magazine] Top Trump Officials Are Hitting the Campaign Trail Ahead of the Midterms. Are They Allowed To? - Time Magazine (2026-11-01) - https://news.google.com/rss/articles/CBMimwFBVV95cUxQQ1F2b3Q5bTd4cENyVG40UmhmLUdjc01NX19vaDZ3WDZFVC1YZTRZdzJxUWxxaXE3T1laYW9oazlMdHNLNUxuaUdkcTBrSnFCOEIwc3RNTnRyOEdqZzJmX0gxSDB3Yk90djNsS0RINFc3ZDlPd0NCZEdId3RXQ2w3cU9VdkJYZUNMaWEzYkJNbFpmb2w5ek5RNm5WMA?oc=5
- [Newsweek] Biden-appointed judge blocks Trump ads days before midterms - Newsweek (2026-10-31) - https://news.google.com/rss/articles/CBMihwFBVV95cUxNTnpOelJyekJob1ZpUHI3QkxYVXZiU1NCeEwxbjZWN3RQTk9oMnJKQ1RUaHdLcVlBMWNENmhIQjFPQnlxSlRMOUtWNjBhaE1VeG1wT1FienQ2REh3Q2xsMnF4TDJxZHM4SEd5TzhTcmw2RGRsNDllY1J3eGNoSkZrV1ptZzZlUG8?oc=5
- [Istituto Impariamo] Taxpayer-Funded TV Ad Sparks Fierce Ethics Clash Across Live News: What the $14,000 ‘Public Service’ Spot Actually Shows and the Hatch Act Fight Behind It - Istituto Impariamo (2026-11-01) - https://news.google.com/rss/articles/CBMikAJBVV95cUxOT2lRb05TSVczYlJ0b25LVkxjRnMtVkd6X3BoWHMtYW1Fa09vbWpXWGFFMW5MdmpYLWNwWTI0Ylc1em1Hb205NFZXbnNORmdJcUtuemIzNnd2YnRjYlh4Y2l2bUJQRTUxdXoxWng4UjZHcHFDaEhDcURJd1lXc0NWdVhWM282bnBKYVUxaG9DZEhLU01yMDc1Mzh6TmFKRGNoQnJEZFJacTg1MThmRG1fUTQxdUhYQkYtSmptbUN3UjB0SHRLdjBBZHhWdEFPWHE4RjZBUGQzOHpxakpxTnE0SXdDV2NaNE5hWHoxaXJiREg2MzdINFUwUVY1RmRDRVB3YTFDbFhHOGE0aEZsTzFVNg?oc=5

### Emergency Powers Expansion
- Assessment: A Presidential Determination under Section 303 of the Defense Production Act of 1950 is a lawful exercise of delegated emergency authority that does invoke statutory emergency powers to direct economic activity. Section 303 authorizes the President to require priority allocation and controlled distribution of materials. This is a real occurrence of emergency-powers invocation, documented in the Federal Register. However, it represents authorized use of congressionally-delegated wartime/emergency authority rather than an unconstitutional bypass of the legislative process. The DPA itself is a statutory grant of emergency authority enacted by Congress, so its invocation is use of authority granted in advance, not a constitutional circumvention. Severity is 2 (a real but contained, legally-authorized action) rather than 3+, as this is neither an extralegal assertion of power nor a defiance of constitutional constraint.
- [federalregister.gov] **[official record]** Presidential Determination Pursuant to Section 303 of the Defense Production Act of 1950, as Amended, on Domestic Petroleum Production, Refining, and Logistics Capacity (2026-10-28) - https://www.federalregister.gov/documents/2026/10/28/2026-22052/presidential-determination-pursuant-to-section-303-of-the-defense-production-act-of-1950-as-amended

### Judicial Review Foreclosure
- Assessment: A federal court dismissed a lawsuit challenging Alaska Senate election certification on threshold grounds rather than addressing the merits of the constitutional claim. This is a concrete instance of judicial review foreclosure—a plaintiff seeking to test the legality of government action (election certification) was denied standing or had the case dismissed on justiciability grounds, leaving no forum to adjudicate the underlying constitutional question. This is a real occurrence, not a hypothetical or proposal. The severity is 2 rather than higher because this is a single instance of a threshold dismissal in one case, not a systematic campaign or structural breakdown. The court's act has already occurred (the dismissal issued), but it is limited in scope to one election challenge and does not yet indicate a pattern that would rise to severity 3.
- [CyberScoop] Federal court tosses Trump lawsuit challenging Alaska Senate certification - CyberScoop (2026-11-01) - https://news.google.com/rss/articles/CBMihAFBVV95cUxNR0YwRkpKTndxRzdoVl9hOV9vVHgxNkRWd3JONTgwU1hienJyTW1uY1V6NEVObktLZE8wQkZIVVNRaDdaMG04UUtPVXVheE00bjhLQzVNY0ZWWUhXRmhQeG0xRDF3akNuMjhncUdZSkNkUGpfY05zdjZkNktBNzI3RWNyc2U?oc=5

### Election Administration Capture
- [The Boston Globe] ‘We would be so cooked.’ Federalism prevented Trump’s election takeover. - The Boston Globe (2026-11-02) - https://news.google.com/rss/articles/CBMijwFBVV95cUxPVE1TczJsdkUtSGZYRHVqU1ctVGp6bk12a3RpMS1obDY4bi1zaGlJUk5SNFhQN0djeldqWkNPaUttbEgyTE8tRjNMb1lGVmtwYksxWXJyeFVFNVNHT0hhWHlsQUxyRUdlSDQxVl9OSlgzNllrSDNtbGhWVUgtRi1ENEVNeTNKZWphcGJFbGoxWQ?oc=5
- [The Washington Post] Trump administration retools its battle over elections to keep fights alive after Election Day - The Washington Post (2026-10-31) - https://news.google.com/rss/articles/CBMi2wFBVV95cUxPRGpZalZEVFBBcWgyOG9KakozUkpWVEktNXN2eVQycUM3RXY5TDZacXB2UjBwd1FIeTRNY2xDc3V6Z0VSeVdFc3BGaXNHeFBlcllvV05mZ3hEQ0ZtMzFCSUFLbzFrZzZJVmM0NFBBcTdDZ0NHa3RBNDRvOG1LUGl5R1doejJfQlY4eFJBT1EzajBRa05acDMyTTB0UjRVYzJqTXQxWnF0VDBPcUF3Yk1mZjBPclltQTZSNzI4cVVqWFZrV0tMalRxcWVaVFpVemJZbUhXOS1uT054LTA?oc=5
- [Bucks County Beacon] Everything You Need to Know About Trump’s Department of Justice Election Monitors - Bucks County Beacon (2026-11-01) - https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMTZDNlZ1d25VeUdmVmc0Y0EtWnFtclplNnpGSE02SDNZN2VSaktNcnUwOHBkakFFVkdOYmQ4SmtHOXctUzdPZjIxQldmckh1RVlUTUFuX29aN0h6WGUxT2wtbU9mTkdzMXBzcGpreWUzd1hBN0dqWExfdWVJQ2NQRnF5Mm9PNXBuYl9vVWZyVE1oOFNCcXJLM0tLTk9MMF9DZU45OUtLT3RzSzhMTnZFbjBXSDM1bnJneXNZ?oc=5

### Legislative Bypass by Executive
- [Reuters] Trump White House maps path to govern without Congress if Democrats win - Reuters (2026-11-01) - https://news.google.com/rss/articles/CBMivgFBVV95cUxOOXdkX2hvMlBTTmRRRGlTbndZSTFnWnZyYkJ5STRjNFBOUkdwQ3VDUjRuTUQySzhQMkp2UXh0MW5VS3E4WHVXeEhQQ2JnRnUxV0pIVTM3T1J6Y0o3Y1JWamZ4YXMwNEtjazNiU3pERzRaWC1XNXZBZk56UU1KSUFNMWtZS0hrUjNUSW5ILW9kdWVQa3BqYkNPSl9tQk90SEtWcDdXRjZXdkdUT1IzS2ViaTgwTmE5MnlCclh1T0pB?oc=5
- [EU Today] Is Donald Trump Preparing to Rule Without Congress – and Could America Be Heading Towards Another Constitutional Crisis? - EU Today (2026-11-01) - https://news.google.com/rss/articles/CBMie0FVX3lxTE1JRVhvM0pKNElHMWF5aWQ2TjZpdVA5U2NDXzVtX29PbWtIeXdUMHcxTjJTVVRTSzM5TUhPaHVBYTdFeGI2NWM4MTlrSk5aTXVZdGJMWkRhRzk4ajZuNGVLQnlLTDU5M28xTWFvZk5UWUExdEtSZGR3V1ExQQ?oc=5
- [Banglanews24] US midterms: Can the election weaken Trump's grip on power? - Banglanews24 (2026-11-02) - https://news.google.com/rss/articles/CBMickFVX3lxTE5Jck5hUUNvQUJTd2VaWXBBNEp5ZlpOUER0bjZYX25xZ0phdFZPQnljYzRwb2hKNzZaT2JDR0wxZURpSGRsNS1ncHh1aUlNajQ0OXFpQ3YzZ1hBekFoUlZhcy1yY2M2SWFSYmI4VzIwRjNEQQ?oc=5

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
