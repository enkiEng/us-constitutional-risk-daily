# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-10 16:30:19 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-4.9**
- Data status: **No successful feed pulls. Treat today's numeric score as unavailable/provisional.**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.23 | 1.24 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.22 | 3.95 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.82 | 1.65 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | keyword | 0 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 1.65 (Watch) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 0.90 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Emergency Powers Expansion
- Assessment: A presidential continuation of a national emergency declaration is a real, documented action that invokes emergency authorities to maintain powers that bypass ordinary legislative process. This is an official Federal Register record of an executive action. However, this represents a routine renewal of a long-standing emergency declaration (post-9/11 terrorist emergency), not a novel expansion or structural breach. The National Emergencies Act (50 U.S.C. § 1601 et seq.) permits such continuations and requires congressional notification. While emergency powers do bypass ordinary process, this is within the statutory framework and constitutes a contained, recurring action rather than a new seizure of authority or defiance of legislative/judicial check. Severity is 2: a credible, real stress signal (emergency authority maintained) that is repetitive and authorized by statute, but not a serious novel violation or structural failure.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Certain Terrorist Attacks (2026-09-10) - https://www.federalregister.gov/documents/2026/09/10/2026-18589/continuation-of-the-national-emergency-with-respect-to-certain-terrorist-attacks

### Civil Service Purge / Schedule F
- Assessment: An official final rule by the MSPB, effective upon publication in the Federal Register, eliminates a longstanding procedural safeguard (the Douglas factors test) that previously constrained agency penalty selection in misconduct cases. This change immediately alters the legal landscape: agencies can now dismiss employees for misconduct without MSPB review of penalty proportionality under the prior multi-factor framework. The removal of this safeguard is itself an accomplished action, not a proposal. However, the severity is limited to 2 because the action is narrow in scope (affects one adjudicatory procedure), targeted at a specific category of decisions, and does not yet constitute a wholesale structural failure or a purge in progress. No mass dismissals have occurred under this rule; the change creates a new permissive legal condition for politicized removals but does not demonstrate that such a campaign has been launched.
- [federalregister.gov] **[official record]** Determining the Appropriate Penalty for Federal Employees Charged With Misconduct (2026-09-03) - https://www.federalregister.gov/documents/2026/09/03/2026-18061/determining-the-appropriate-penalty-for-federal-employees-charged-with-misconduct

### Legislative Bypass by Executive
- No fresh evidence links in the current lookback window.
### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 0
- Query feeds failed: 24
- Primary-source lookups: 22 signals, 12 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Low**
- Fetch errors:
  - election_certification_interference: HTTP Error 503: Service Unavailable
  - election_administration_capture: HTTP Error 503: Service Unavailable
  - election_delay_or_cancellation: HTTP Error 503: Service Unavailable
  - alternate_elector_scheme: HTTP Error 503: Service Unavailable
  - politicized_prosecution_opposition: HTTP Error 503: Service Unavailable
  - opposition_ballot_exclusion: HTTP Error 503: Service Unavailable
  - retaliation_architecture: HTTP Error 503: Service Unavailable
  - judge_intimidation_campaign: HTTP Error 503: Service Unavailable
  - court_order_noncompliance: HTTP Error 503: Service Unavailable
  - jurisdiction_stripping_targeted: HTTP Error 503: Service Unavailable

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
