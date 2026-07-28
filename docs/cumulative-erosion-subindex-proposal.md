# Proposal: Cumulative Erosion Sub-Index (CEI)

Status: **draft for review** — follow-through on §1.4 ("decay treats permanent
damage as fading news") and §1.5 ("it measures flow, not stock") of
`constitutional-risk-improvement-proposal.md`, which v2 did not implement.

## The gap this fills

The v2 daily score is an **acute-event tripwire**: confirmed events in a 2-day
window, decaying at 0.35/day. That is the right design for early warning, but
it is structurally blind to the thing most observers actually worry about:

1. **No accumulation.** Fifty severity-2 norm-eroding actions spread over a
   year each fade within a week. The stock of damage never appears anywhere.
2. **Lawful consolidation is invisible.** A court ruling or statute that
   *removes a check* is a lawful-process outcome and scores ~0. The acute index
   cannot distinguish "the checks are holding" from "the checks are being
   dismantled through legal channels" — it only fires when someone finally
   defies a ruling or cancels an election, i.e. after the guardrails are gone.

The CEI is a second published number measuring the **stock of eroded checks**,
displayed alongside the acute score. The two answer different questions:

| | Acute index (existing) | CEI (proposed) |
|---|---|---|
| Question | "Is a constitutional breach happening *right now*?" | "How much of the constitutional immune system has been *durably removed*?" |
| Time profile | Spikes and decays in days | Ratchets up; declines only on verified repair |
| Moves on | Confirmed events | Structural conditions + sustained event pressure |
| Analogy | Seismograph | Sea level |

## Design: two components

### Component 1 — Structural Condition Ledger (primary, human-vetted)

A curated ledger of named, durable conditions that remove or weaken a check.
Each entry is a *state*, not an event: it stays on the books until verifiably
reversed. This is what captures lawful consolidation — rulings, statutes,
executive actions, and entrenched practices.

New file `data/erosion_ledger.json`, one entry per condition:

```json
{
  "id": "example_for_cause_removal_narrowed",
  "domain_id": "civil_service_integrity",
  "title": "For-cause removal protection narrowed for independent agencies",
  "class": "ruling",              // statute | ruling | executive_action | practice
  "magnitude": 3,                  // 1-4, how much of the check is gone (rubric below)
  "status": "active",              // active | partially_reversed | reversed
  "established": "YYYY-MM-DD",
  "reversed": null,
  "evidence": ["<primary source URL>", "<secondary URL>"],
  "note": "audit trail: why this magnitude, what would reverse it"
}
```

**Magnitude rubric (1–4):**

- **1** — a norm or informal practice abandoned; check still legally intact
- **2** — a check weakened for a targeted scope (one agency, one class of case)
- **3** — a check broadly weakened or made discretionary (survives only if the
  executive chooses restraint)
- **4** — a check effectively eliminated (no remaining institutional remedy
  short of constitutional amendment or court-composition change)

**Status transitions:** `partially_reversed` halves the magnitude;
`reversed` zeroes it but keeps the entry for the historical record. Reversal
requires the same evidence bar as establishment (primary source: ruling text,
statute, executed order).

**Who writes it:** the daily AI pass *proposes*, a human *disposes*. After the
normal daily run, one additional model call reviews the day's confirmed
events plus the current ledger and emits proposals (new entry / magnitude
change / reversal) to `data/erosion_ledger_proposals.json`. Nothing enters the
published number until manually merged into the ledger — same philosophy as
v2's "aggregation stays pure Python": the published score must be reproducible
and human-vetted. This is one low-volume call/day, so it can afford a stronger
model than the classifier (e.g. `claude-sonnet-5`) via a new `ai.ledger_model`
config key.

**Scoring:** per domain, active magnitudes sum with saturation so stacked
conditions in one domain approach but never exceed the 0–4 scale:

```
domain_erosion = 4 * (1 - exp(-Σ magnitude_i / 4))
ledger_score   = Σ_domains  weight_d * domain_erosion_d / 4      # 0-100
```

Saturation keeps one captured domain from dominating: three magnitude-3
conditions in one domain read as "this check is mostly gone" (~3.6), not 9.

### Component 2 — Event-Pressure EWMA (automatic, backfillable)

Captures the "fifty severity-2 events over a year" pattern the ledger's
discrete entries may miss. An exponentially weighted moving average of each
signal's daily `final_score` with a **180-day half-life** (config-tunable):

```
pressure_signal(t) = λ * pressure_signal(t-1) + (1-λ) * final_score(t)
λ = 0.5^(1/180)                                    # per day
pressure_score = same domain aggregation + weights as ledger_score   # 0-100
```

Fully computable today from `data/constitutional_signal_scores.csv` (per-signal
daily history since 2026-02-16) — a backfill script seeds it in one pass, the
daily run then updates it incrementally. No new data collection, no human
curation.

### Combination

```
CEI = min(100, ledger_score + 0.35 * pressure_score)
```

The ledger is the primary instrument (structural, vetted); pressure is a
bounded supplement so sustained sub-structural churn registers without
double-counting events that later graduate into ledger entries. Both
components published separately in `latest_dashboard.json` so the page can
show the split.

**Bands** (parallel to the acute bands, different labels — this is a stock):

| CEI | Label |
|---|---|
| 0–14 | Checks intact |
| 15–29 | Noticeable erosion |
| 30–49 | Substantial erosion |
| 50–69 | Severe erosion |
| 70–100 | Consolidation — checks largely dismantled |

### Interaction with the acute index

**None, in v1.** The CEI never trips acute trip-wires and the acute score
never feeds the ledger automatically. They share domain weights and the
signal/domain taxonomy, nothing else. (A future version could let high CEI
lower the evidence bar for acute severity — a system with fewer checks
escalates faster — but keeping them decoupled makes both auditable.)

## Illustrative worked example

*Numbers below are placeholders to show the arithmetic — actual entries get
established during the seeding review, with evidence.*

| Ledger entry (hypothetical) | Domain (weight) | Mag |
|---|---|---|
| For-cause removal narrowed | civil_service_integrity (10) | 3 |
| Civil-service reclassification in effect | civil_service_integrity (10) | 3 |
| Emergency powers used for routine domestic policy | executive_constraints (13) | 2 |
| IG independence weakened | civil_service_integrity (10) | 2 |

civil_service erosion: `4·(1−e^−(3+3+2)/4) = 3.46` → `10 · 3.46/4 = 8.7 pts`
executive_constraints: `4·(1−e^−0.5) = 1.57` → `13 · 1.57/4 = 5.1 pts`
ledger_score ≈ **13.8**; with pressure ≈ 20 → `13.8 + 0.35·20` → **CEI ≈ 21
("Noticeable erosion")** — while the acute index sits at 10. That divergence
*is the product*: quiet day, eroding foundations.

## Rollout plan

1. **Backfill pressure component** — `scripts/backfill_erosion_pressure.py`
   over the existing per-signal CSV; add EWMA update to the daily run.
   Publish CEI (pressure-only, ledger empty) as *provisional*.
2. **Seeding review** — one-time session: model surveys the period since
   project start (and notable pre-history) and drafts candidate ledger
   entries with evidence; human reviews each, sets magnitudes, merges.
   CEI leaves provisional status when the ledger is seeded.
3. **Daily proposals** — add the ledger-review call to `run_daily.py`;
   surface pending proposals count on the page so review debt is visible.
4. **Page** — second dial next to the acute score, CEI history sparkline,
   expandable ledger table (title, domain, magnitude, established, evidence
   links). The ledger table doubles as the public audit trail.
5. **Calibration** — sanity-check annually against V-Dem / Bright Line Watch
   direction-of-travel; they measure adjacent constructs and won't match
   numerically, but the *sign* of year-over-year change should agree.

## Open questions

- Half-life for pressure (180d proposed): long enough to accumulate, short
  enough that a genuinely calm year reads as recovery?
- Should `practice`-class entries (abandoned norms, mag 1) require a
  sustained-pattern test (e.g. 3+ distinct confirmed events) before entry,
  to keep the ledger from collecting one-offs?
- Pressure coefficient (0.35): calibrate after backfill so that the observed
  2026 event history contributes a defensible share of the total.
- New CSV `data/cumulative_erosion_history.csv` for the CEI time series
  (date, ledger_score, pressure_score, cei) — start at step 1.
