# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-09 12:28:50 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **15 / 100** (Elevated Strain)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **+1.9**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.65 | 9.07 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.22 | 3.04 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.65 (Yellow) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 4 |
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 2 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 1 |
| Emergency Powers Expansion | executive_constraints | 1.00 (Watch) | ai | 3 | 0 |
| Election Certification Interference | elections_transfer | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- No fresh evidence links in the current lookback window.
### Legislative Bypass by Executive
- Assessment: This item reports that Trump ordered the DOJ to conduct a probe of Democratic politicians. If accurate, an order to the Executive Branch to investigate political opponents represents a unilateral executive action (directing an agency without new statute) that could bypass or preempt legislative oversight. However, the severity is limited to 2 because: (1) the report is from secondary news coverage, not an official DOJ announcement or executive order text; (2) directing investigation of political figures, while constitutionally concerning, is not yet confirmation of a completed structural bypass of legislative authority, merely an exercise of prosecutorial discretion under existing Executive power; (3) Rep. Balint's statement confirms congressional awareness and pushback, suggesting oversight mechanisms are still engaged. This merits a credible stress signal but does not rise to severity 3 (serious, confirmed high-severity action such as open defiance of a court order or removal campaign) without further evidence of systematic dismantling of legislative authority.
- [NewsBreak: Local News & Alerts] Rep. Becca Balint Defends Congress’s Oversight Powers After Trump Orders DOJ Probe of Democrats — “We Will Not Be Deterred” - NewsBreak: Local News & Alerts (2026-11-08) - https://news.google.com/rss/articles/CBMijgJBVV95cUxNTDVOZldhOW9NSFlKOGVFTDloUDZZcWxEOFh1LTlJaDNoME14RWFtLTRZWXhPMzU3bTk4ZGJsdHcwSXI3RHFlNFdrN0Rtc3ZzLXhFdk9BWk1yTEVUeEU5bFBHVVp4ak5Vdl96VVdWVnJXU3RQYmFQTnpvdHdkRWMtaDJwTllPQ252WDFQeFp1dGdycVplb3VrY3V3Vm9rUDF6Vno2NEd6NV9XRld2eExiOWV3TDQ1cmNwZm9pRVlFc0ppYmM2alFlVDRPMWZnWkd2U0JHOEVyTGgzUWpvd19IZ2k2VkFVSnBrVXdjX1lEQkc1Q3FhWmtPd0RVUnZHYV95NDdfTWhoUEJwSEQwdUE?oc=5

### Public Funds for Political Promotion
- Assessment: The item reports that a federal judge has issued an order directing the Trump administration to pull three taxpayer-funded advertisements featuring the president, characterizing them as 'purely partisan.' This represents a real, confirmed instance of public funds being spent on communications that promote the officeholder in a partisan manner—the core of this signal. The judge's order indicates that the ads violated the statutory bar on using appropriated funds for 'publicity or propaganda purposes' as interpreted by GAO. This is a contained, specific action with judicial confirmation rather than a structural constitutional failure or systematic pattern. Severity 2 reflects that this is a credible, confirmed stress signal of real but bounded significance—a judge had to intervene to stop the conduct, which demonstrates both that the violation occurred and that existing legal checks functioned to address it.
- [Wonderwall] ‘Purely partisan’: Federal judge orders Trump admin to pull three taxpayer-funded ads featuring the president - Wonderwall (2026-11-08) - https://news.google.com/rss/articles/CBMi0gFBVV95cUxPb21LbVZkbUhpdjBpV2xNUVFZRmZ3ZUhnTVkxcEJ1SFBZS1dCem1iUU94U0tHQzNQZl8tdVRMU3hIdjFQWXhoZUtxWmpnSEJULThzSUE0MGhqODNCN1pSYUVPaVVKZ3g4RE01LWVYbUk5cklFTVdobko1M1U5X0VZekxmOXpiY2RUVGVwNGxIck9vU3FKSWhJdUNCc0NtcmVVaGlHaXJIVE9uYmpPTW1UdGtVc1B3WTNVUUJjLWFsd3ctVHpKUUd1S1l6ZU9qWjBPdFE?oc=5

### Press Restrictions or Retaliation
- [MyJoyOnline] Media owners must invest in training, safety and fair remuneration – Kwakye Ofosu - MyJoyOnline (2026-11-09) - https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbXNDcng1Z1ZhZ1dwZjREUFY1WXlLbTN0Zm96Y2pQX2lXaUZUVEFUZER1TFpodUo2T1hkcjh0UmpudFVMdFdQal9WQktDZzQtM0tqRERGRlJldVdmVldMQWkxa3lXcE1Pb2RfX2JlTUtxME96bU1sYVdCOHB0VmtBaTNQWWh5QlNkZzhUUWp6d0VKbzRwc2RicE81MkwzZ0lObTlmSmIzMEdFdFk?oc=5

### Emergency Powers Expansion
- Assessment: This is a continuation of an existing declared national emergency under the National Emergencies Act (NEA). Continuation of a previously declared emergency is a routine executive action that renews authorities already granted by Congress through the NEA framework. While the NEA does permit emergency powers to bypass ordinary rulemaking, continuation documents are ministerial renewals of standing authorizations, not new expansions. The underlying emergency was declared in an earlier year; this 2026 continuation represents ongoing use of existing delegated authority rather than a novel expansion. Severity is low because continuation is the ordinary operation of a congressionally-authorized framework, not a structural bypass of legislative process.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to the Threat From Securities Investments That Finance Certain Companies of the People's Republic of China (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22688/continuation-of-the-national-emergency-with-respect-to-the-threat-from-securities-investments-that
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to the Proliferation of Weapons of Mass Destruction (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22686/continuation-of-the-national-emergency-with-respect-to-the-proliferation-of-weapons-of-mass
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Iran (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22685/continuation-of-the-national-emergency-with-respect-to-iran

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 10 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**
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
