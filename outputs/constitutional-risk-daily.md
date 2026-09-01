# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-01 16:44:13 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **11 / 100** (Baseline Institutional Noise)
- Previous day delta: **+2.0**
- Delta vs 7-day average: **-4.9**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.32 | 1.11 |
| Executive Constraints and Emergency Powers | 13 | 1.33 | 4.33 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.12 | 2.81 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 3 |
| Political Speech Criminalization or Surveillance | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Independent Agency Capture | civil_service_integrity | 1.25 (Watch) | ai | 0 | 4 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.95 (Watch) | ai | 0 | 3 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: This item references Trump issuing a mail-ballot order and subsequent Supreme Court litigation. This indicates an executive order on voting administration (mail ballots) bypassing legislative process, with the order being challenged before the Supreme Court. This constitutes a plausible instance of major governance action shifted to unilateral executive authority regarding electoral administration. However, severity is capped at 2 because: (1) the item is from a secondary source summarizing the dispute rather than the order itself, (2) the outcome is still in litigation with no confirmation the action succeeded or persists, and (3) a single order challenged in court is a stressed signal but not yet a confirmed structural failure.
- [Legal Service India] Who Controls American Elections? Trump’s Mail-Ballot Order and Supreme Court Battle - Legal Service India (2026-09-01) - https://news.google.com/rss/articles/CBMiuwFBVV95cUxOTnpHVXFEc1UybGFBWmlueUFsZTlVMU9oeGlMR0dvQ1pCbndKNHN4d21iR1V0Wm9wUEpDZXFuWW9SZkszNFFIWUFUcE55ZmJ6VDl6c1VJWnZibjNWWUdlSGdpdkR6dlRJQ2EwZVFGelp2eXZPUVc3cm0xZlgySWlHNDJsZGxxd2FhNDYycmlLS3U4Mk0wQmpZZDhwekFUSkJQWGdxM0hFQWZONFNNOEVneFdSdjU3dUFLc184?oc=5

### Political Speech Criminalization or Surveillance
- Assessment: Unicorn Riot reports DHS deployed facial recognition software against individuals identified as 'Minnesota 15,' apparently protest participants or activists. This represents a verified use of surveillance technology by a federal agency against individuals apparently identified by their participation in lawful protest or political activity. The report title explicitly connects the surveillance tool to a specific group, suggesting targeting based on political association or dissent. This is a credible, real occurrence of surveillance expansion targeting political actors, though the scope appears limited to a specific incident rather than a systematic policy change. No indication that this was illegal or that DHS has been enjoined; the action has been taken and represents actual surveillance of dissidents.
- [Unicorn Riot] DHS Facial Recognition Software Used Against Minnesota 15 - Unicorn Riot (2026-09-01) - https://news.google.com/rss/articles/CBMikwFBVV95cUxNX3dmU0lMaDJNaUxyT3FyUmhjSWQzWVBNbFZLNDlXak1IZHREQno1QzZibDZoakhRUHg3TzNfaFJLTUgtNVNWOWVEMnFzRzZnZGRsSkpjd2E4S0h5ZVA3ZEVFM1RQUV9NTWkwTmxZQkdkXzZTUlFFblNlc25NTjFmNDZ0X2lpOHY3czdQeURPUUwyZWs?oc=5

### Emergency Powers Expansion
- Assessment: A presidential emergency declaration, published in the Federal Register, is a verifiable use of statutory emergency authority to invoke powers that bypass ordinary legislative process. The National Emergencies Act (50 U.S.C. § 1601 et seq.) permits the President to declare a national emergency and activate specified statutory powers without a new legislative act. This document itself constitutes the exercise of emergency authority. However, the severity is 2 rather than higher because: (1) emergency declaration authority is congressionally authorized and contemplated by law; (2) without the full text of the declaration and its specific invocations, the scope of actual powers being deployed cannot be verified; (3) this represents a legitimate if stress-laden tool rather than an unconstitutional usurpation. The mere invocation of emergency power for critical infrastructure (bulk-power system security) is a real constitutional stress signal—bypassing the ordinary appropriations and regulatory process—but not yet evidence of structural failure or clear defiance of law.
- [federalregister.gov] **[official record]** Declaring a National Emergency To Secure the United States Bulk-Power System (2026-08-31) - https://www.federalregister.gov/documents/2026/08/31/2026-17843/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system

### Civil Service Purge / Schedule F
- Assessment: This is an official Federal Register document confirming that OPM has issued a final rule titled 'Improving Performance, Accountability and Responsiveness in the Civil Service' (published February 6, 2026, effective March 9, 2026). The August 25, 2026 entry is a technical correction to that rule. The original February rule directly addresses civil service structure and performance accountability, consistent with Schedule F concerns about reclassification of career positions. As an issued final rule effective before this correction, it represents a material structural change to civil service rules. The correction itself confirms the underlying rule exists and operates. Severity is 2 (repeated/credible stress signal, real but contained action) rather than higher because the document excerpt does not detail the specific reclassification powers granted, only that such a rule has been issued and corrected. The fact that a major civil service reform rule exists and is being administratively refined constitutes verifiable evidence of civil service policy change, though the full scope of at-will reclassification authority is not detailed in this excerpt.
- [federalregister.gov] **[official record]** Improving Performance, Accountability and Responsiveness in the Civil Service, and Recruitment and Relocation Incentive Waivers; Correcting Amendments (2026-08-25) - https://www.federalregister.gov/documents/2026/08/25/2026-17334/improving-performance-accountability-and-responsiveness-in-the-civil-service-and-recruitment-and

### Independent Agency Capture
- [courtlistener.com] **[official record]** Dillinger's LLC, a Wyoming Limited Liability Company and Ryan Clement, an Individual v. CR-GTD, LLC, a Wyoming Limited Liability Company and EFTI, LLC, a Wyoming Limited Liability Company (2026-08-25) - https://www.courtlistener.com/opinion/10957585/dillingers-llc-a-wyoming-limited-liability-company-and-ryan-clement-an/
- [www.iconnectblog.com] The Unitary Executive Theory after Slaughter: A Comparative Hispanic Perspective - www.iconnectblog.com (2026-09-01) - https://news.google.com/rss/articles/CBMirgFBVV95cUxOd1RiVThoUVhsWXdDR1luSWZOWExYWENJYjdHWWR0THpDVEFKanFadFJoUEVmTXpJYmR1N2dyN1VwSEtEZFhWTno2OVMzVGdNaXBIOFdEZi1zeFdKZkN0YW9nMHZGVjFJMjNmZkk0Z3llNDRfWHpDckdtbXY1QW9BR1huUGZCU25HM2pheVU5NlpLanpnbEtTRzJTN1Z1UEhQM0lOdWdGMnRNSzJmUEE?oc=5
- [Liberal Currents] Guardrails for Democracy: How Congress Can Reinforce Privacy Rights and Independent Oversight - Liberal Currents (2026-08-31) - https://news.google.com/rss/articles/CBMiwwFBVV95cUxOX3BMQkZHczFDcVJUaFU5N0FNWExneXJKYXpJV3VsTkxuejlBczc4dnFKUWhMcGRYVS13eWJ1dldzUUVGQUhuMFZoZnF2cGM4Z0xnYzRGUm1vR2ZTQjlyeUpyQW9ObTRkbzdqRnpaY3RTemZvMjJLS0VROXdYdnZyZ0VVVzNuRlJGRDJmTHFyOHhlbFA5UV9Ca3hwd2MtTVN1WkhGYzVzUDA2MjQ1bUVHRVJxVE9KZGFoX1BPU2RHMFhXYjg?oc=5

## Data Quality

- Query feeds attempted: 23
- Query feeds successful: 23
- Query feeds failed: 0
- Primary-source lookups: 21 signals, 20 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
