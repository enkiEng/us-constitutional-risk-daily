# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-01 13:59:33 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **11 / 100** (Baseline Institutional Noise)
- Previous day delta: **+4.0**
- Delta vs 7-day average: **+1.9**
- Data status: **No successful feed pulls. Treat today's numeric score as unavailable/provisional.**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.24 | 1.31 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.65 | 2.27 |
| Executive Constraints and Emergency Powers | 13 | 0.32 | 1.03 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 1.00 | 2.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Security Sector Loyalty Tests | security_sector_neutrality | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 1 | 0 |
| Opposition Ballot Exclusion | opposition_pluralism | 1.65 (Watch) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 0.95 (Watch) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 0.95 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Civil Service Purge / Schedule F
- Assessment: OPM has issued a final rule modifying RIF regulations to prioritize performance over tenure and length of service. This is a real, published regulatory action that materially changes federal personnel protections by reducing seniority-based safeguards. While presented as merit-based efficiency, the shift from tenure-protective RIF procedures to performance-based retention creates a concrete mechanism for politicizing career civil service. This is a contained but credible stress signal—a structural change to established civil-service protections, not a mass purge event or emergency action.
- [federalregister.gov] **[official record]** Reduction in Force (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15665/reduction-in-force
- [federalregister.gov] **[official record]** Streamlining Probationary and Trial Period Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15654/streamlining-probationary-and-trial-period-appeals
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Security Sector Loyalty Tests
- Assessment: This is a final OPM regulation that removes the Merit Systems Protection Board (MSPB)—an independent adjudicative body—from appeals of suitability actions and consolidates that authority within OPM itself. Suitability determinations affect federal employment eligibility and can be used to screen personnel. Removing independent oversight of such determinations and concentrating appeals authority within the executive personnel office constitutes a material shift in internal review mechanisms that could enable partisan loyalty filters in federal personnel decisions. This is a confirmed structural change to a coercive-state institution's internal accountability, though it remains procedural rather than involving overt purges or open defiance of courts. Severity 2: real, confirmed, official action affecting institutional independence in personnel matters.
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Legislative Oversight Obstruction
- Assessment: An official motion to quash third-party subpoenas filed by the Executive Office of the President represents a verifiable action to obstruct legislative fact-finding. The filing of a motion to quash subpoenas is a concrete legal action aimed at preventing disclosure of information to Congress or its agents. This constitutes a real occurrence of obstruction of legislative oversight, though the motion itself is a procedural challenge rather than an outright defiance of a court order or systematic campaign. The severity is 2 (repeated or credible stress signal—a real but contained action) rather than 3, because this is a single motion through the normal judicial process, not an open defiance or structural campaign to prevent oversight.
- [courtlistener.com] **[official record]** IN RE SUBPOENAS ON BORIS EPSHTEYN (2026-07-02) - https://www.courtlistener.com/docket/73690657/2/in-re-subpoenas-on-boris-epshteyn/

### Opposition Ballot Exclusion
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 0
- Query feeds failed: 22
- Primary-source lookups: 20 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 5
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
