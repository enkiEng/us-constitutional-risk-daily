# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-24 12:30:29 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **8 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-2.6**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.43 | 1.08 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | keyword | 0 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: The item describes a presidential order directing federal contractors to notify the White House before providing information to Congress. This represents a shift of information-control authority from normal legislative channels to unilateral executive gatekeeping, which constitutes a real governance action that bypasses normal statutory procedures for congressional oversight and access to information from federal contractors. However, without access to the full text of the order or confirmation of its legal status and actual implementation, and given that this appears to be framed as 'law commentary' rather than an official record, the severity is assessed as 2—a credible but contained stress signal representing a real action that materially alters executive-legislative balance, rather than a 3 or 4 which would require documented defiance of statute or structural constitutional breakdown. The action is not hypothetical or proposed; it is described as an order that has been issued.
- [Law Commentary] Trump Orders Federal Contractors to Notify White House Before Giving Congress Information - Law Commentary (2026-11-23) - https://news.google.com/rss/articles/CBMioAFBVV95cUxNUXZzWUJuQ1B5aWJWS2lNV1JXRFVudWV5TGgxd0ExUmRPRF8xeXo2UkhrQ0Z4R0dVV1VWMDd2eHNtYnZfYUNMVGxsd2szeHVzWVU5MXMzbUhKZ01ZaTEtVUFkcDcyQmxzcTMwSU9TQ3FIeFkxWkxRbXhsd2Z1YTZ3OTRjd2VGYW1LNXNqbW9HVGFxN0U3NWQ5aHJ3YnUyM1pf?oc=5

### Election Administration Capture
- No fresh evidence links in the current lookback window.
### Press Restrictions or Retaliation
- [The New Arab] Thousands protest closure of pro-opposition Turkish media outlets - The New Arab (2026-11-22) - https://news.google.com/rss/articles/CBMimwFBVV95cUxOWUVKbGFybmNsdnNBc3Z3VmkzNGVLd3NUaDFWTW5ramNlMVBoeFF5b0VqUXBsMmlZbGJTT2twUTJYSVlGLWo0MWRLck52MjcxaXlqU01LakJpR1R0MTNpWlVCbzBhMEdIVkNVMWZaOUhyWFduUnNuaV9Kbm0tMzlvb2lPVE9BQ1d3VEJJX0dTV3dGOUJOR0psRG5MTdIBmwFBVV95cUxOWUVKbGFybmNsdnNBc3Z3VmkzNGVLd3NUaDFWTW5ramNlMVBoeFF5b0VqUXBsMmlZbGJTT2twUTJYSVlGLWo0MWRLck52MjcxaXlqU01LakJpR1R0MTNpWlVCbzBhMEdIVkNVMWZaOUhyWFduUnNuaV9Kbm0tMzlvb2lPVE9BQ1d3VEJJX0dTV3dGOUJOR0psRG5MTQ?oc=5
- [The Business Standard] Thousands protest closure of critical media outlets in Turkey - The Business Standard (2026-11-23) - https://news.google.com/rss/articles/CBMipgFBVV95cUxNQzJZVVlvbWN5YWFnbXFtYzNnYVN3SUZzMU5tazhMM2hGb0plQzlrMUY2YnFKbjZWclZGY1BCS2hkX3hXclp5RENuQjlqSktJYXFaM29kZ1lhclJGT3NCakZ6azYyVVIwZUhIT0t3cXRkZ3dLc0otamlKVm1SRmhXTjhLbnVpQ193M3hFTHByNmJ2ZWNCYlJRYzVrSXJ5NFdaOTZLYWR3?oc=5

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
  - alternate_elector_scheme: HTTP Error 429: Too Many Requests
  - alternate_elector_scheme: courtlistener: HTTP Error 401: Unauthorized
  - politicized_prosecution_opposition: courtlistener: HTTP Error 401: Unauthorized
  - opposition_ballot_exclusion: courtlistener: HTTP Error 401: Unauthorized
  - court_order_noncompliance: courtlistener: HTTP Error 401: Unauthorized
  - jurisdiction_stripping_targeted: HTTP Error 429: Too Many Requests
  - judicial_review_foreclosure: courtlistener: HTTP Error 401: Unauthorized
  - independent_agency_capture: courtlistener: HTTP Error 401: Unauthorized

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
