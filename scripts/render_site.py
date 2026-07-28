#!/usr/bin/env python3
"""
Render a public static HTML dashboard from latest score artifacts.

v2 page: a legible gauge + band ladder ("what would move this to the next
band"), a per-domain heat strip so a reader sees *where* stress is
concentrated, signal chips carrying the AI/keyword source, the confirmed-event
count, a day-over-day trend arrow and the model's one-line rationale, a
trip-wire banner for confirmed catastrophic events, a longer trend chart, and
accessibility fixes (severity is never encoded by colour alone). The
methodology docs are linked from the page.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render static Constitutional Risk site.")
    parser.add_argument(
        "--summary-json",
        type=Path,
        default=Path("data/latest_dashboard.json"),
        help="Path to latest summary JSON from update_constitutional_risk.py",
    )
    parser.add_argument(
        "--history",
        type=Path,
        default=Path("data/constitutional_risk_history_v2.csv"),
        help="Path to score history CSV (v2 series).",
    )
    parser.add_argument(
        "--signal-history",
        type=Path,
        default=Path("data/constitutional_signal_scores.csv"),
        help="Path to per-signal history CSV (used for day-over-day trend arrows).",
    )
    parser.add_argument(
        "--output-html",
        type=Path,
        default=Path("site/index.html"),
        help="Path to rendered output HTML.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("site/data/latest_dashboard.json"),
        help="Path to copied summary JSON for public consumption.",
    )
    parser.add_argument(
        "--output-history",
        type=Path,
        default=Path("site/data/constitutional_risk_history.csv"),
        help="Path to copied history CSV for public consumption.",
    )
    return parser.parse_args()


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_history(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def fmt_number(value: Any, digits: int = 1) -> str:
    if value is None:
        return "n/a"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return "n/a"
    if number > 0:
        return f"+{number:.{digits}f}"
    return f"{number:.{digits}f}"


def score_color(score: int) -> str:
    clamped = max(0, min(100, int(score)))
    # 0 -> green (120), 50 -> yellow (60), 100 -> red (0)
    hue = 120 - (clamped * 1.2)
    return f"hsl({hue:.1f} 82% 34%)"


# --- severity (0-4) -> colour + label, never colour alone -------------------

_SEV_STOPS = [
    (0.75, "Green", "#e8f5ec", "#0b5f2e", "#8fce9f"),
    (1.75, "Watch", "#eef4ff", "#1a4b8f", "#a9c4ef"),
    (2.75, "Yellow", "#fff6e5", "#8a5a00", "#f0cf88"),
    (3.5, "Orange", "#fde9df", "#a2400f", "#f0b190"),
    (99, "Red", "#fbe0e0", "#8f1414", "#e79a9a"),
]


def severity_style(value: float) -> tuple[str, str, str, str]:
    """Return (label, background, ink, border) for a 0-4 severity."""
    for threshold, label, bg, ink, border in _SEV_STOPS:
        if value < threshold:
            return label, bg, ink, border
    return _SEV_STOPS[-1][1:]


def prev_severity_map(signal_rows: list[dict[str, str]], current_date: str) -> dict[str, float]:
    """Severity per signal on the most recent date strictly before ``current_date``."""
    dates = sorted({row.get("date", "") for row in signal_rows if row.get("date")})
    prior = [d for d in dates if d < current_date]
    if not prior:
        return {}
    target = prior[-1]
    out: dict[str, float] = {}
    for row in signal_rows:
        if row.get("date") != target:
            continue
        try:
            out[row.get("signal_id", "")] = float(row.get("final_score", "0"))
        except (TypeError, ValueError):
            continue
    return out


def trend_arrow(current: float, previous: float | None) -> tuple[str, str]:
    """Return (glyph, aria-label) for a day-over-day severity change."""
    if previous is None:
        return "•", "no prior reading"
    delta = current - previous
    if delta >= 0.5:
        return "▲", "rising"
    if delta <= -0.5:
        return "▼", "easing"
    return "▬", "steady"


def band_ladder_html(bands: list[dict[str, Any]], score: int) -> str:
    rows: list[str] = []
    current_idx = 0
    for idx, band in enumerate(bands):
        if int(band["min"]) <= score <= int(band["max"]):
            current_idx = idx
    for idx, band in enumerate(bands):
        lo, hi = int(band["min"]), int(band["max"])
        label = html.escape(str(band["label"]))
        is_current = idx == current_idx
        hue = 120 - (((lo + hi) / 2) * 1.2)
        marker = "◀ current" if is_current else ""
        cls = "rung rung-current" if is_current else "rung"
        rows.append(
            f'<div class="{cls}" aria-current="{"true" if is_current else "false"}">'
            f'<span class="rung-swatch" style="background:hsl({hue:.0f} 70% 45%)" aria-hidden="true"></span>'
            f'<span class="rung-range">{lo}–{hi}</span>'
            f'<span class="rung-label">{label}</span>'
            f'<span class="rung-marker">{marker}</span>'
            "</div>"
        )
    return "\n".join(rows)


def next_band_note(bands: list[dict[str, Any]], score: int) -> str:
    for band in sorted(bands, key=lambda b: int(b["min"])):
        if int(band["min"]) > score:
            need = int(band["min"]) - score
            return (
                f"<strong>+{need} point{'s' if need != 1 else ''}</strong> would move the index into "
                f"<em>{html.escape(str(band['label']))}</em>."
            )
    return "The index is already in the highest band."


def heat_strip_html(domain_breakdown: list[dict[str, Any]]) -> str:
    cells: list[str] = []
    for row in sorted(domain_breakdown, key=lambda r: float(r.get("points", 0.0)), reverse=True):
        name = html.escape(str(row.get("name", "")))
        sev = float(row.get("avg_severity", 0.0))
        weight = row.get("weight", 0)
        points = float(row.get("points", 0.0))
        label, bg, ink, border = severity_style(sev)
        pct = max(4, min(100, (sev / 4.0) * 100))
        cells.append(
            f'<div class="heat-cell" style="border-color:{border}">'
            f'<div class="heat-top"><span class="heat-name">{name}</span>'
            f'<span class="heat-badge" style="background:{bg};color:{ink}">{label} {sev:.1f}</span></div>'
            f'<div class="heat-bar" role="img" aria-label="{name}: severity {sev:.1f} of 4 ({label})">'
            f'<span class="heat-fill" style="width:{pct:.0f}%;background:{ink}"></span></div>'
            f'<div class="heat-meta">weight {weight} · {points:.1f} pts</div>'
            "</div>"
        )
    return "\n".join(cells)


def signal_row(result: dict[str, Any], prev: dict[str, float]) -> str:
    name = html.escape(str(result.get("name", "")))
    domain_id = html.escape(str(result.get("domain_id", "")))
    severity = float(result.get("severity", 0))
    sev_label, bg, ink, border = severity_style(severity)
    mode = str(result.get("evidence_mode", "keyword"))
    mode_label = {
        "ai": "AI-confirmed",
        "keyword": "keyword",
        "override": "human-verified",
    }.get(mode, mode)
    confirmed = result.get("confirmed_hits", 0)
    rationale = str(result.get("rationale") or result.get("override_note") or "")
    prev_sev = prev.get(str(result.get("id", "")))
    glyph, arrow_label = trend_arrow(severity, prev_sev)
    primary = str(result.get("primary_source_url") or "")
    primary_html = (
        f' <a class="primary-src" href="{html.escape(primary)}" target="_blank" '
        f'rel="noopener noreferrer">primary source</a>'
        if primary
        else ""
    )
    rationale_html = (
        f'<div class="sig-rationale">{html.escape(rationale)}{primary_html}</div>' if rationale else ""
    )
    return (
        "<tr>"
        f'<td><span class="sig-name">{name}</span>'
        f'<span class="sig-domain">{domain_id}</span>{rationale_html}</td>'
        f'<td><span class="sev-chip" style="background:{bg};color:{ink};border-color:{border}">'
        f'{severity:.1f} {sev_label}</span></td>'
        f'<td class="trend" title="{arrow_label}" aria-label="{arrow_label}">{glyph}</td>'
        f'<td><span class="src-tag src-{mode}">{mode_label}</span></td>'
        f'<td class="num">{confirmed}</td>'
        "</tr>"
    )


def evidence_blocks(top_signals: list[dict[str, Any]]) -> str:
    blocks: list[str] = []
    for signal in top_signals[:4]:
        evidence = signal.get("evidence", [])
        signal_name = html.escape(str(signal.get("name", "")))
        blocks.append(f'<section class="panel"><h3>{signal_name}</h3>')
        rationale = str(signal.get("rationale") or "")
        if rationale:
            blocks.append(f'<p class="note">{html.escape(rationale)}</p>')
        if not evidence:
            blocks.append("<p>No evidence links in current lookback window.</p></section>")
            continue
        blocks.append("<ul>")
        for item in evidence[:5]:
            publisher = html.escape(str(item.get("publisher") or "unknown"))
            title = html.escape(str(item.get("title") or "(untitled)"))
            link = html.escape(str(item.get("link") or ""))
            published = item.get("published")
            if published:
                try:
                    published = dt.datetime.fromisoformat(str(published).replace("Z", "+00:00"))
                    published_text = published.strftime("%Y-%m-%d")
                except ValueError:
                    published_text = "unknown date"
            else:
                published_text = "unknown date"
            blocks.append(
                "<li>"
                f'<a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a>'
                f' <span class="meta">{publisher} | {published_text}</span>'
                "</li>"
            )
        blocks.append("</ul></section>")
    return "\n".join(blocks)


def trip_wire_html(trip_wires: list[dict[str, Any]]) -> str:
    if not trip_wires:
        return ""
    items = "".join(
        f"<li><strong>{html.escape(str(tw.get('label', '')))}</strong> "
        f"(severity {float(tw.get('severity', 0)):.1f}) — floors the index to at least "
        f"{int(tw.get('floor_score', 0))}</li>"
        for tw in trip_wires
    )
    return (
        '<section class="tripwire" role="alert">'
        "<h2>⚠ Active trip-wires</h2>"
        "<p>A confirmed catastrophic event has floored the index above the weighted total:</p>"
        f"<ul>{items}</ul></section>"
    )


def render_html(
    summary: dict[str, Any],
    history_rows: list[dict[str, str]],
    signal_rows: list[dict[str, str]],
) -> str:
    score = int(summary.get("score", 0))
    score_css_color = score_color(score)
    band = summary.get("band", {})
    band_label = html.escape(str(band.get("label", "")))
    band_desc = html.escape(str(band.get("description", "")))
    generated_at = html.escape(str(summary.get("generated_at", "")))
    data_available = bool(summary.get("data_available", False))
    methodology_version = summary.get("methodology_version", 2)
    extraction_mode = str(summary.get("extraction_mode", "keyword"))
    trip_wires = list(summary.get("trip_wires_fired", []))
    bands = list(summary.get("_bands", [])) or _DEFAULT_BANDS

    domain_breakdown = list(summary.get("domain_breakdown", []))
    top_signals = list(summary.get("top_signals", []))
    generated_date = generated_at[:10] if len(generated_at) >= 10 else ""
    prev = prev_severity_map(signal_rows, generated_date)

    history_rows = sorted(history_rows, key=lambda row: row.get("date", ""))
    last = history_rows[-60:]
    chart_labels = [row.get("date", "") for row in last]
    chart_values: list[float] = []
    for row in last:
        try:
            chart_values.append(float(row.get("score", "0")))
        except ValueError:
            chart_values.append(0.0)

    status_class = "status-ok" if data_available else "status-warning"
    status_text = (
        "Live data pulled today."
        if data_available
        else "No successful feed pulls today. Score is provisional (persistence + last state)."
    )
    extraction_label = (
        "AI event extraction" if extraction_mode == "ai" else "keyword volume (AI extraction unavailable)"
    )

    active_signals = [s for s in top_signals if float(s.get("severity", 0)) > 0]
    signal_rows_html = "\n".join(signal_row(item, prev) for item in active_signals[:14])
    if not signal_rows_html:
        signal_rows_html = '<tr><td colspan="5">No active signals above 0 severity in this run.</td></tr>'
    heat_html = heat_strip_html(domain_breakdown)
    evidence_html = evidence_blocks(top_signals)
    ladder_html = band_ladder_html(bands, score)
    next_note = next_band_note(bands, score)
    tripwire_banner = trip_wire_html(trip_wires)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>US Constitutional Risk Daily</title>
  <link rel="icon" type="image/svg+xml" href="./assets/favicon/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="./assets/favicon/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="./assets/favicon/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="./assets/favicon/apple-touch-icon.png">
  <link rel="shortcut icon" href="./assets/favicon/favicon.ico">
  <style>
    :root {{
      --bg: #f5f7fb; --ink: #152238; --muted: #57657a; --panel: #ffffff;
      --line: #dbe3ee; --accent: #0b5ed7; --accent-soft: #e8f0ff;
      --warn: #b54708; --ok: #027a48;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0; font-family: "Source Sans 3", "Segoe UI", Tahoma, sans-serif;
      background: radial-gradient(circle at top right, #ebf2ff, var(--bg) 45%);
      color: var(--ink); line-height: 1.5;
    }}
    main {{ max-width: 1080px; margin: 0 auto; padding: 28px 16px 48px; }}
    h1, h2, h3 {{ font-family: "Merriweather", Georgia, serif; margin: 0 0 10px; }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .headline {{ display: grid; gap: 10px; margin-bottom: 18px; }}
    .score-row {{ display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; }}
    .score {{ font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: {score_css_color}; }}
    .badges {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .band {{ background: var(--accent-soft); color: var(--accent); padding: 4px 10px;
      border-radius: 999px; font-size: 0.95rem; font-weight: 700; }}
    .tag {{ background: #eef2f7; color: var(--muted); padding: 3px 9px; border-radius: 999px;
      font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.03em; }}
    .tag-ai {{ background: #ecfdf3; color: var(--ok); }}
    .score-scale-note {{ color: var(--muted); font-size: 0.95rem; font-weight: 600; }}
    .risk-context {{ color: var(--muted); font-size: 0.95rem; max-width: 900px; }}
    .status {{ padding: 8px 10px; border-radius: 8px; font-weight: 600; margin-top: 4px; }}
    .status-ok {{ background: #ecfdf3; color: var(--ok); border: 1px solid #c8ecd8; }}
    .status-warning {{ background: #fff6eb; color: var(--warn); border: 1px solid #f7dfbd; }}
    .tripwire {{ background: #fbe9e6; border: 1px solid #f0b6ab; border-left: 5px solid #b42318;
      border-radius: 10px; padding: 12px 16px; margin: 14px 0; }}
    .tripwire h2 {{ color: #912018; margin-bottom: 6px; }}
    .grid {{ display: grid; grid-template-columns: 1.25fr 1fr; gap: 14px; margin: 16px 0; }}
    .panel {{ background: var(--panel); border: 1px solid var(--line); border-radius: 12px;
      padding: 14px; box-shadow: 0 2px 6px rgba(14, 31, 53, 0.04); }}
    .ladder {{ display: grid; gap: 3px; }}
    .rung {{ display: grid; grid-template-columns: 14px 54px 1fr auto; align-items: center; gap: 8px;
      padding: 3px 6px; border-radius: 6px; font-size: 0.9rem; color: var(--muted); }}
    .rung-current {{ background: var(--accent-soft); color: var(--ink); font-weight: 700; }}
    .rung-swatch {{ width: 14px; height: 14px; border-radius: 3px; }}
    .rung-range {{ font-variant-numeric: tabular-nums; }}
    .rung-marker {{ color: var(--accent); font-weight: 700; font-size: 0.82rem; }}
    .next-note {{ margin-top: 10px; padding-top: 10px; border-top: 1px dashed var(--line);
      font-size: 0.92rem; color: var(--muted); }}
    .heat {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }}
    .heat-cell {{ border: 1px solid var(--line); border-left-width: 4px; border-radius: 8px; padding: 8px 10px; }}
    .heat-top {{ display: flex; justify-content: space-between; align-items: center; gap: 6px; }}
    .heat-name {{ font-weight: 600; font-size: 0.9rem; }}
    .heat-badge {{ font-size: 0.75rem; font-weight: 700; padding: 1px 7px; border-radius: 999px; white-space: nowrap; }}
    .heat-bar {{ height: 6px; background: #eef1f5; border-radius: 999px; margin: 6px 0 4px; overflow: hidden; }}
    .heat-fill {{ display: block; height: 100%; border-radius: 999px; }}
    .heat-meta {{ color: var(--muted); font-size: 0.78rem; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.95rem; }}
    th, td {{ border-bottom: 1px solid var(--line); text-align: left; padding: 8px 6px; vertical-align: top; }}
    th {{ color: var(--muted); font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.04em; }}
    td.num, th.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
    .sig-name {{ font-weight: 600; display: block; }}
    .sig-domain {{ color: var(--muted); font-size: 0.8rem; }}
    .sig-rationale {{ color: var(--muted); font-size: 0.85rem; margin-top: 3px; }}
    .primary-src {{ font-weight: 600; }}
    .sev-chip {{ display: inline-block; padding: 2px 9px; border-radius: 999px; border: 1px solid;
      font-size: 0.82rem; font-weight: 700; white-space: nowrap; }}
    .trend {{ font-size: 1.05rem; text-align: center; }}
    .src-tag {{ font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 999px;
      background: #eef2f7; color: var(--muted); white-space: nowrap; }}
    .src-ai {{ background: #ecfdf3; color: var(--ok); }}
    .src-override {{ background: #eef2ff; color: var(--accent); }}
    .metrics {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }}
    .metric {{ background: #f8fbff; border: 1px solid #e1eaf7; border-radius: 10px; padding: 10px; }}
    .metric .k {{ color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.04em; }}
    .metric .v {{ font-size: 1.25rem; font-weight: 700; margin-top: 2px; }}
    ul {{ margin: 0; padding-left: 20px; }}
    li {{ margin: 8px 0; }}
    .meta {{ color: var(--muted); font-size: 0.85rem; }}
    .note {{ color: var(--muted); font-size: 0.92rem; }}
    .legend {{ display: flex; flex-wrap: wrap; gap: 10px; font-size: 0.82rem; color: var(--muted); margin-top: 8px; }}
    .legend span {{ display: inline-flex; align-items: center; gap: 5px; }}
    .legend i {{ width: 12px; height: 12px; border-radius: 3px; display: inline-block; }}
    footer {{ margin-top: 20px; font-size: 0.9rem; color: var(--muted); }}
    canvas {{ width: 100%; height: 260px; border: 1px solid var(--line); border-radius: 8px; background: #fff; }}
    @media (max-width: 840px) {{ .grid {{ grid-template-columns: 1fr; }} .heat {{ grid-template-columns: 1fr; }} }}
    @media (max-width: 520px) {{ .metrics {{ grid-template-columns: 1fr 1fr; }} }}
  </style>
</head>
<body>
  <main>
    <section class="headline">
      <h1>US Constitutional Risk Daily</h1>
      <div class="score-row">
        <div class="score">{score} / 100</div>
        <div class="badges">
          <span class="band">{band_label}</span>
          <span class="tag {"tag-ai" if extraction_mode == "ai" else ""}">Methodology v{methodology_version} · {extraction_label}</span>
        </div>
      </div>
      <div class="score-scale-note">Scale: 0 = no constitutional risk, 100 = constitution destroyed. Ideally this stays near 0.</div>
      <div class="risk-context">
        This score estimates current constitutional-order stress from observable events across elections, courts,
        executive power, and opposition rights. A single confirmed catastrophic event (a defied court order, a
        cancelled election) trips a floor that raises the whole index regardless of the weighted total.
      </div>
      <div>{band_desc}</div>
      <div class="status {status_class}">{status_text}</div>
      <div class="note">Updated: {generated_at}</div>
    </section>

    {tripwire_banner}

    <section class="grid">
      <div class="panel">
        <h2>Where the score sits</h2>
        <div class="ladder">
          {ladder_html}
        </div>
        <div class="next-note">{next_note}</div>
      </div>
      <div class="panel">
        <h2>Quick metrics</h2>
        <div class="metrics">
          <div class="metric"><div class="k">Previous Day Delta</div><div class="v">{fmt_number(summary.get("delta_previous_day"))}</div></div>
          <div class="metric"><div class="k">Delta vs 7-Day Avg</div><div class="v">{fmt_number(summary.get("delta_vs_7d"))}</div></div>
          <div class="metric"><div class="k">Feed Pull Success</div><div class="v">{summary.get("successful_queries", 0)} / {summary.get("attempted_queries", 0)}</div></div>
          <div class="metric"><div class="k">Confidence</div><div class="v">{html.escape(str(summary.get("confidence", "n/a")))}</div></div>
        </div>
      </div>
    </section>

    <section class="panel">
      <h2>Domain stress</h2>
      <p class="note">Severity is shown by both a labelled badge and a bar, so the reading does not depend on colour.</p>
      <div class="heat">
        {heat_html}
      </div>
    </section>

    <section class="panel">
      <h2>60-day trend</h2>
      <canvas id="scoreChart" width="700" height="260" role="img" aria-label="Line chart of the 0-100 constitutional risk score over the last 60 days"></canvas>
    </section>

    <section class="panel">
      <h2>Highest-risk signals today</h2>
      <table>
        <thead>
          <tr><th>Signal</th><th>Severity</th><th>Trend</th><th>Source</th><th class="num">Confirmed</th></tr>
        </thead>
        <tbody>
          {signal_rows_html}
        </tbody>
      </table>
      <div class="legend">
        <span><i style="background:#0b5f2e"></i>Green</span>
        <span><i style="background:#1a4b8f"></i>Watch</span>
        <span><i style="background:#8a5a00"></i>Yellow</span>
        <span><i style="background:#a2400f"></i>Orange</span>
        <span><i style="background:#8f1414"></i>Red</span>
        <span>▲ rising · ▬ steady · ▼ easing</span>
      </div>
    </section>

    {evidence_html}

    <footer>
      <p><strong>Method:</strong> a weighted 0-100 early-warning indicator. Per-domain severity uses
      <code>max(mean, max&minus;1)</code> so one confirmed red signal is not averaged away; trip-wires floor the
      index for confirmed catastrophic events. When available, an AI extraction layer confirms whether each event
      actually occurred (vs hypothetical, denied, historical, or foreign) before it is scored.</p>
      <p>How this score works &amp; its limits:
      <a href="https://github.com/enkieng/us-constitutional-risk-daily/blob/main/docs/constitutional-risk-deep-dive.md" target="_blank" rel="noopener noreferrer">methodology deep-dive</a>
      · <a href="https://github.com/enkieng/us-constitutional-risk-daily/blob/main/docs/constitutional-risk-improvement-proposal.md" target="_blank" rel="noopener noreferrer">v2 rationale</a>.
      This is an early-warning tool, not legal proof; confirm high-severity changes with primary legal records.</p>
      <p>Raw artifacts: <a href="./data/latest_dashboard.json">latest_dashboard.json</a> | <a href="./data/constitutional_risk_history.csv">constitutional_risk_history.csv</a> (v2 series)</p>
      <p>More analysis: <a href="https://progressive-mandate.org" target="_blank" rel="noopener noreferrer">Progressive Mandate</a></p>
    </footer>
  </main>

  <script>
    const labels = {json.dumps(chart_labels)};
    const values = {json.dumps(chart_values)};
    const canvas = document.getElementById("scoreChart");
    const ctx = canvas.getContext("2d");
    const w = canvas.width, h = canvas.height;
    const pad = {{ l: 44, r: 18, t: 16, b: 34 }};
    const x0 = pad.l, y0 = h - pad.b, x1 = w - pad.r, y1 = pad.t;
    const chartW = x1 - x0, chartH = y0 - y1;
    function yFor(v) {{ return y0 - (Math.max(0, Math.min(100, v)) / 100) * chartH; }}
    function xFor(i) {{ return values.length <= 1 ? x0 : x0 + (i / (values.length - 1)) * chartW; }}
    ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, w, h);
    ctx.strokeStyle = "#dbe3ee"; ctx.lineWidth = 1;
    [0, 20, 40, 60, 80, 100].forEach((tick) => {{
      const y = yFor(tick);
      ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
      ctx.fillStyle = "#57657a"; ctx.font = "12px sans-serif"; ctx.fillText(String(tick), 8, y + 4);
    }});
    ctx.strokeStyle = "#0b5ed7"; ctx.lineWidth = 2; ctx.beginPath();
    values.forEach((v, i) => {{ const x = xFor(i), y = yFor(v); i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y); }});
    ctx.stroke();
    ctx.fillStyle = "#0b5ed7";
    values.forEach((v, i) => {{ ctx.beginPath(); ctx.arc(xFor(i), yFor(v), 2.5, 0, Math.PI * 2); ctx.fill(); }});
    ctx.fillStyle = "#57657a"; ctx.font = "12px sans-serif";
    if (labels.length > 0) {{
      ctx.fillText(labels[0], x0, h - 10);
      const rightText = labels[labels.length - 1];
      ctx.fillText(rightText, x1 - ctx.measureText(rightText).width, h - 10);
    }}
  </script>
</body>
</html>
"""


_DEFAULT_BANDS = [
    {"min": 0, "max": 14, "label": "Baseline Institutional Noise"},
    {"min": 15, "max": 29, "label": "Elevated Strain"},
    {"min": 30, "max": 44, "label": "Serious Constitutional Stress"},
    {"min": 45, "max": 59, "label": "Crisis Trajectory"},
    {"min": 60, "max": 74, "label": "Acute Constitutional Crisis"},
    {"min": 75, "max": 89, "label": "Near-Failure"},
    {"min": 90, "max": 100, "label": "Constitutional Failure / Overturn"},
]


def main() -> int:
    args = parse_args()
    summary = read_json(args.summary_json)
    history_rows = read_history(args.history)
    signal_rows = read_history(args.signal_history)

    # Load the full band ladder from config if available for the ladder widget.
    config_path = Path("config/constitutional_risk_config.json")
    if config_path.exists():
        try:
            summary["_bands"] = read_json(config_path).get("risk_bands", _DEFAULT_BANDS)
        except (OSError, json.JSONDecodeError):
            summary["_bands"] = _DEFAULT_BANDS

    output_html = render_html(summary, history_rows, signal_rows)
    args.output_html.parent.mkdir(parents=True, exist_ok=True)
    args.output_html.write_text(output_html, encoding="utf-8")

    summary.pop("_bands", None)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    args.output_history.parent.mkdir(parents=True, exist_ok=True)
    if args.history.exists():
        args.output_history.write_text(args.history.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"Rendered {args.output_html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
