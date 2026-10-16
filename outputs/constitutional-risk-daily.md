# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-16 12:41:40 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **11 / 100** (Baseline Institutional Noise)
- Previous day delta: **+5.0**
- Delta vs 7-day average: **+2.0**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.08 | 0.27 |
| Civil Service and Agency Independence | 10 | 0.15 | 0.38 |
| Civil Liberties and Information Environment | 10 | 2.00 | 5.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 3.00 (Orange) | ai | 6 | 7 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 7 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.95 (Watch) | ai | 0 | 1 |
| Independent Agency Capture | civil_service_integrity | 0.60 (Green) | ai | 0 | 2 |
| Legislative Bypass by Executive | executive_constraints | 0.25 (Green) | ai | 0 | 1 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: Report quotes Maryland lawmakers characterizing Trump's taxpayer-funded TV ads as 'egregious and utterly illegal.' This corroborates that government funds are actually being spent on pro-Trump advertising. The lawmakers' statements reflect a real event (ad spending using taxpayer money) rather than a hypothetical. The characterization as illegal and egregious by state officials, combined with corroboration from other items, confirms use of public funds for partisan promotion in violation of appropriations law.
- [- SoMD Chronicle] ‘Egregious and utterly illegal.’ Maryland lawmakers blast Trump’s taxpayer-funded TV ads - - - SoMD Chronicle (2026-10-14) - https://news.google.com/rss/articles/CBMipgFBVV95cUxQdGgwcUFFa0J0eXVGcHBLLTNuX1R5cGpPVkJUSnpnT0VJYjgwNkl5ZUthTExiRHBQWndwSkh3c2VVMkJjNlB0UmIxLVpOYlpxSG1ZQmhYWGQwV1lKWXRqTzdRZVRoWXp2UldyLVdLZ0FYZHVHWk1jUkVpLW5xZHhoNEkxSFBvdlVrOU9lcGZrSngtLUZNNkl2LVBfVXp0THBYc2NERzln?oc=5
- [The Hill] Judge extends block on taxpayer-funded Trump ads until after midterms - The Hill (2026-10-15) - https://news.google.com/rss/articles/CBMiowFBVV95cUxPd0U3ZUs1WWF4d3NJZTdPWkdtbUhYRVhQa0JRRHZjM2FtQjZ2SnJmXzNnODgtNV9fNnRYVHRUV1MtYzJ5dE40YW5iRmNNQk1HMUJ3SW92YWV0d01vLUNTSG53Z3RablJoa1kzSzlKQkN2YnZWb25ldktyTk95ZTN0dGx4Sk5MQUhnUjY4aVAxaTdZa2d5NFNBZ1pXQzhEUFoxWG9F0gGoAUFVX3lxTE0xX3E4RzgyOEc0dUxHcmVDN0J3UEFoSXFuQ1gza3hIYjRVbGs3RWd2OVV4ZElTV0E0UXV6SHdfRm5aTGpCZTZWeDNNMExlUDFFY3VNQUtFaUdZMDFUYXNHdkYyQk5qOVdfMmJiQzVrQnhtb2NZYmdoT0tscHlyNjNodjJRQi1nSVlFWjh6TDdvM2hvb3lLMllDM2xYczV0WmIxU1VKcWxScA?oc=5
- [Yahoo] Judge extends pause on taxpayer-funded Trump ads - Yahoo (2026-10-14) - https://news.google.com/rss/articles/CBMimwFBVV95cUxPY0QwVlBTWmtkQXNQdzZ5OUp3UGxJN0lmOGgwZ3lvMkg3S0xxWk14aVg5ZjJITnYzOThHbHdOTVlqdF9pWUgxcDFjdmxlX2ttQUR2blF3OEV4bTFQUmhEOVVGaXB0UzBXOFc3QnNHUlNrRDlPNWhocklFRFdESHU0alh2ZWRVR2RHdFlkdG9sNHIyeHRtVGdEdkQ4NA?oc=5

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-10-14) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Press Restrictions or Retaliation
- [The Guardsman Online] ‘Student Journalists Can Make Powerful Change’: Reporters and Lawyers on the Fight for Press Freedom - The Guardsman Online (2026-10-15) - https://news.google.com/rss/articles/CBMixgFBVV95cUxOWDRyUzFCVmF4TFV6V3M4bWJXeko4clpBd2t1RkRuV2RwSURNS0NySHA1Y2pNRWU3LXZnTDQwY3daZEpLZW9pZVZtbXFmdEI1dUthcDhmdDdXMVhORjBPUnRUdk9KSlRaT0RPUGlpWHQxdmUxb2JYdzdxaFg5R1lUUTY0ZDNFUHA0Mk9JdGVkcmNoTURvQUh1d2dVc0lubW9xOF9tSDdaUHZoN2o2SnZGcW5WSlRIZ1AwN3VuN0p5Q1hlcm96c3c?oc=5

### Independent Agency Capture
- [Consumer Finance Monitor] Podcast Release: The Supreme Court Opinions in Trump v. Slaughter and Trump v. Cook: What Do They Mean for the Future of the Administrative State? - Consumer Finance Monitor (2026-10-15) - https://news.google.com/rss/articles/CBMinAJBVV95cUxNLUJxT01sUmRISUl2NEttTDlZalhSbXFOa0RueENrTmh3NFlHeXlzMy1ZOWt1U01MMm8tQ28yazY0UVotRmhVQk5pYW9vTzRVT05HaFRubFUyREpRYnl0VzJPU2xfeUE5R09PaUxKNW5kSU8yZFltNXdwS2hJa3RZQldtUW1VYnJaNXh0bHRyUU8wRks4Vml2ZE1qd0lvVXY3QU5JamFtUHBWMHNNYTgxUU80VGttYTdNLVNqdXRXbEJmRTk2YS02amY3T29CT09VUEM1YldoWk9oSnl5WUVfZzlvamJmMDdyYzZjUmh3MTVyUjNsbDRJUDZnNHhoWnpCLVNwUXZMOGh3SVRFQThGQ1VNTmtJTnRiREcwXw?oc=5
- [The Daily Economy] Cook Case Tests the Limits of Fed Independence - The Daily Economy (2026-10-16) - https://news.google.com/rss/articles/CBMiiwFBVV95cUxPSDNkQXYtVktHT2IwVkpGQXBwbHJzdVNmOEcxN3VpVTcyYm1ydlRZQjNiTmM4Q19jMl9aYTVPS0dYOXU2MTF1M2ZMdXRDQ0w0OFFrbW5MNnFyejJkS3pfMHNtcjNQZEVOVmI4bmJZWDFvMjY0UWlPZzJiQWtqcW1oX1NOS0RnbHBuOG1z?oc=5

### Legislative Bypass by Executive
- [Firstpost] Can Donald Trump cancel the November 3 US midterm elections? - Firstpost (2026-10-16) - https://news.google.com/rss/articles/CBMirwFBVV95cUxOUU9RcnNRZFNteEc3QV95Ums0WV9IeE90UFAxUmpwX3VxeXRWLVFxVGtJemZiVGJUUGVPeTd6MlRwSEYzUnFDeUQwS0RaMklUMGtKVWRlVU0tVE04RzJ1MW5XRnBCUVpoNlBZcmFrQmJBeUxGdU5pQU1sNjhWaG92N0xZemlURnBRQVd3cVF2X1JWQnRFZ3pVVUNKaDJ3Q2FOcy16aWFfR280Z1lmLWY00gG0AUFVX3lxTE5JaWwwTmZnbWxTU1JBT2g1bmxPdi1peU1FWEgzRjdSNFAzTW93ck5BRFA3UjBZb3p0UzBUYXJQbzJxREpPQld4SWhRLVNoMXFLWGVIM1o4Ti15ejBlU0s0eU5jVmhmVFVxelZYaEJzWUpneVM4NW5qNUtJNTZvcVNmZHdIQzNUYkxWXzZOVS05Rlc2SzNvaWIxMlNFaXhYNHVLb2FTQmNObWdBVTQtalFFeDlFMg?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 10 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
