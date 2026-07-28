# Proposal: Making the Constitutional Risk Daily More Accurate and Effective

Status: **Draft for review** · Scope: methodology, scoring engine, and public page
(`site/index.html`). This document proposes changes; nothing here is wired in yet.

The current system is a solid skeleton: a transparent, weighted, domain-based model
with a daily automated pull, decay, manual overrides, history, and a clean static
page. The problems below are not about the *structure* — they are about whether the
number the page shows actually tracks constitutional risk. Today, largely, it does not.

---

## Part 1 — Why today's number under-signals (accuracy problems)

### 1.1 The score is structurally incapable of showing a crisis
This is the most important finding. Two config choices combine to cap the automated
score far below the bands it advertises:

- Domain score = `weight * (average signal severity / 4)` — an **average** across all
  signals in the domain.
- `auto_max_severity = 3`, so the automated pipeline can never emit a `4` (Red). Only
  a manual override can.

Consequence: imagine three genuine, confirmed constitutional-crisis events at once —
an election-certification refusal, open defiance of a court order, and a martial-law
deployment against protesters (three signals at Red/4, everything else green). Run
through the current math that totals **14.8 / 100** — still "Baseline Institutional
Noise." The automated engine, in normal operation, essentially cannot leave the bottom
two bands no matter what happens in the country. A 0–100 gauge whose realistic ceiling
is ~25 is miscalibrated, and it fails at exactly the tail events it exists to catch.

**Fix direction:** replace within-domain averaging with a **max / top-k / soft-max**
aggregation so one Red signal moves its domain hard; add **trip-wire floors** (a
confirmed defied court order alone should floor the whole index into "Crisis
Trajectory"); and let the automated engine reach Red when evidence is primary-source
confirmed. Then either recalibrate the bands or keep 0–100 but make realistic crises
land where the labels say they should.

### 1.2 It counts media volume, not constitutional events
The engine scores keyword hits in Google News RSS titles/summaries. That measures **how
much the press is talking**, not **what actually happened**. Specific failure modes,
all of which currently push the score the *wrong* way:

- **Negation / denial:** "Governor says he will *not* cancel the election" hits the
  `cancel election` severe term and raises risk.
- **Hypotheticals & opinion:** "What if the president defied a court order?" — an op-ed
  scores like the event itself.
- **Historical / retrospective:** anniversary coverage of 2020 fake-elector cases hits
  `fake elector certificates` today.
- **Foreign leakage:** coverage of another country's canceled election passes a query
  even with "United States" in the string.
- **Salience ≠ severity:** a slow news day understates real stress; a media pile-on
  overstates it. The number tracks the news cycle, not the guardrails.

### 1.3 "Confirmation" bar is too weak, and source quality is ignored
`min_unique_publishers_for_critical = 2` means **two outlets** re-running the same wire
story counts as "critical." Google News often surfaces syndicated duplicates, so this
is frequently a single story. A personal blog and Reuters count equally toward "unique
publishers." There is no notion of **primary sources** (court dockets, the Federal
Register, DOJ/agency releases, the Congressional Record) — which is exactly what a
constitutional-risk index should be anchored to.

### 1.4 Decay treats permanent damage as fading news
`decay_per_day = 0.35` linearly fades a signal when coverage drops off. But a defied
court order that still stands, or an implemented Schedule F, is a **permanent state
change**, not a news story that cools off. The model conflates "the press moved on"
with "the risk resolved."

### 1.5 It measures flow, not stock
The index only reacts to *new events* in a 2-day lookback. It has no **standing
baseline** for the current structural state of the guardrails. Constitutional risk is
as much about the accumulated condition of institutions as about today's headline.

---

## Part 2 — Using AI to fix the accuracy layer (you said AI is OK)

The brittleness in Part 1 lives almost entirely in one place: turning raw articles into
a severity number by string-matching. That is precisely what a language model does well.
Keep the deterministic, auditable aggregation; swap the extraction layer for AI.

**Proposed AI extraction step (per candidate article):**
An LLM reads the headline + summary (or fetched article text) and returns a structured,
schema-validated judgment:

```json
{
  "is_us_domestic": true,
  "event_actually_occurred": true,      // vs hypothetical / denied / historical / opinion
  "signal_id": "court_order_noncompliance",
  "severity": 3,                         // against a written rubric, 0-4
  "actor": "Executive branch / DOJ",
  "primary_source_url": "https://...court order/filing if present",
  "one_line_rationale": "DOJ filed notice refusing to comply with the injunction in X v. Y",
  "confidence": 0.82
}
```

This single change removes the negation, hypothetical, historical, foreign-leakage, and
opinion false positives in one pass, and yields a **human-readable rationale per signal**
that can be shown on the page. Design notes:

- **Determinism & auditability:** AI runs only at extraction; scoring/aggregation stays
  pure Python so every published number is reproducible from the stored judgments.
- **Cost control:** cheap-model triage first, stronger model only on candidates that
  pass; cache by article URL; cap articles/signal. The daily run is small.
- **Fallback:** if the API is unavailable, fall back to today's keyword scorer and mark
  the day's confidence "Low / keyword-only" rather than failing.
- **Secrets/CI:** needs an API key in GitHub Actions secrets; document it alongside the
  existing `GITLAB_TRIGGER_TOKEN`.
- A second, optional LLM pass can write the **daily narrative summary** ("what changed
  and why") from the structured judgments — explanation, never the score itself.

---

## Part 3 — Aggregation & calibration redesign

1. **Within-domain aggregation:** move from mean to `max` or a top-2 soft-max, so a
   single Red isn't diluted by quiet sibling signals.
2. **Trip-wires:** a small set of signals (defied court order, election
   cancellation/override, martial law against political opposition, refusal to leave
   office) set a **floor band** regardless of the arithmetic total.
3. **Structural baseline (stock) + acute (flow):** maintain a slow-moving standing score
   for guardrails already damaged, and add today's acute events on top.
4. **Persistence instead of blind decay:** confirmed structural changes persist until an
   explicit resolution event; only unconfirmed/low-confidence spikes decay.
5. **Recalibrate the scale honestly.** Either remap bands to the realistic distribution
   or fix the math so crises reach the crisis bands — and **version the methodology**
   (e.g. `methodology_version: 2`) so the historical CSV isn't silently redefined. Keep
   the old series labeled v1.

---

## Part 4 — Page improvements (what the reader actually sees)

The page is clean but presents a single compressed number with little context. More
*indicative* presentation:

1. **Gauge + band ladder** showing the seven bands and a marker, plus an explicit
   "**what would move this to the next band**" line — makes the score legible.
2. **Per-domain heat strip + sparklines** (8 domains, colored severity, 30-day mini
   trends) instead of only one aggregate line — shows *where* stress is concentrated.
3. **Signal chips with trend arrows** (▲ new today / ▬ persisting / ▼ easing) and the
   AI one-line rationale on hover/expand — turns opaque rows into a readable situation.
4. **Structural vs Acute split** so a reader sees standing damage separately from
   today's flashpoints.
5. **Confidence & source tier, shown visually:** a confidence band on the trend line and
   badges distinguishing primary-source-confirmed from single-outlet-provisional signals.
6. **Provenance for overrides:** show "human-verified — <note>" where a manual override
   drives a score, so the reader knows what is machine-inferred vs. confirmed.
7. **Accessibility:** today severity is encoded by hue alone (`score_color`), which fails
   for color-blind readers and screen readers. Add text labels/patterns and ARIA, and
   check contrast on the colored score.
8. **Link the methodology.** The deep-dive and this proposal aren't linked from the page.
   Add a "How this score works / limitations" link so the prominent "subjective,
   experimental" framing is one click away.

---

## Part 5 — Suggested phased rollout

- **Phase 1 (no new infra):** fix aggregation (max/top-k), add trip-wire floors,
  recalibrate + version bands, and ship the page upgrades (gauge, heat strip, signal
  chips, accessibility, methodology link). Pure Python + template; immediately makes the
  number more indicative.
- **Phase 2 (AI extraction):** add the LLM classifier with caching + keyword fallback;
  surface rationale and source-tier badges on the page.
- **Phase 3 (structure):** structural-baseline model, confidence intervals, and a
  monthly false-positive review loop feeding query/rubric tuning.

Each phase is independently shippable and independently valuable.

---

## Appendix — Concrete evidence for §1.1

Using the current config and `domain_points = weight * (avg_severity / 4)`:

| Scenario | Signals at Red (4) | Total score | Band shown |
|---|---|---:|---|
| Three simultaneous confirmed crisis events | certification refusal + court defiance + martial-law deployment | **14.8** | Baseline / low Elevated |
| Every one of 22 signals at Red | all | 100 | Failure |

The gap between those two rows is the calibration problem: nothing short of near-total,
simultaneous, every-domain failure produces a number that looks alarming.
