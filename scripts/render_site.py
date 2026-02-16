#!/usr/bin/env python3
"""
Render a public static HTML dashboard from latest score artifacts.
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
        default=Path("data/constitutional_risk_history.csv"),
        help="Path to score history CSV.",
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
    return f"hsl({hue:.1f} 82% 38%)"


def signal_row(result: dict[str, Any]) -> str:
    name = html.escape(str(result.get("name", "")))
    domain_id = html.escape(str(result.get("domain_id", "")))
    severity = result.get("severity", 0)
    severity_label = html.escape(str(result.get("severity_label", "")))
    hits = result.get("hits", 0)
    publishers = result.get("unique_publishers", 0)
    return (
        "<tr>"
        f"<td>{name}</td>"
        f"<td>{domain_id}</td>"
        f"<td>{severity:.2f} ({severity_label})</td>"
        f"<td>{hits}</td>"
        f"<td>{publishers}</td>"
        "</tr>"
    )


def domain_row(row: dict[str, Any]) -> str:
    name = html.escape(str(row.get("name", "")))
    weight = row.get("weight", 0)
    avg = row.get("avg_severity", 0.0)
    points = row.get("points", 0.0)
    return (
        "<tr>"
        f"<td>{name}</td>"
        f"<td>{weight}</td>"
        f"<td>{avg:.2f}</td>"
        f"<td>{points:.2f}</td>"
        "</tr>"
    )


def evidence_blocks(top_signals: list[dict[str, Any]]) -> str:
    blocks: list[str] = []
    for signal in top_signals[:3]:
        evidence = signal.get("evidence", [])
        signal_name = html.escape(str(signal.get("name", "")))
        blocks.append(f"<section class=\"panel\"><h3>{signal_name}</h3>")
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
                f"<a href=\"{link}\" target=\"_blank\" rel=\"noopener noreferrer\">{title}</a>"
                f" <span class=\"meta\">{publisher} | {published_text}</span>"
                "</li>"
            )
        blocks.append("</ul></section>")
    return "\n".join(blocks)


def render_html(summary: dict[str, Any], history_rows: list[dict[str, str]]) -> str:
    score = int(summary.get("score", 0))
    score_css_color = score_color(score)
    band = summary.get("band", {})
    band_label = html.escape(str(band.get("label", "")))
    band_desc = html.escape(str(band.get("description", "")))
    generated_at = html.escape(str(summary.get("generated_at", "")))
    data_available = bool(summary.get("data_available", False))

    domain_breakdown = list(summary.get("domain_breakdown", []))
    domain_breakdown.sort(key=lambda row: float(row.get("points", 0.0)), reverse=True)
    top_signals = list(summary.get("top_signals", []))

    history_rows = sorted(history_rows, key=lambda row: row.get("date", ""))
    last_30 = history_rows[-30:]
    chart_labels = [row.get("date", "") for row in last_30]
    chart_values: list[float] = []
    for row in last_30:
        try:
            chart_values.append(float(row.get("score", "0")))
        except ValueError:
            chart_values.append(0.0)

    status_class = "status-ok" if data_available else "status-warning"
    status_text = (
        "Live data pulled today."
        if data_available
        else "No successful feed pulls today. Score is provisional."
    )

    signal_rows_html = "\n".join(signal_row(item) for item in top_signals[:12])
    if not signal_rows_html:
        signal_rows_html = (
            "<tr><td colspan=\"5\">No active signals above 0 severity in this run.</td></tr>"
        )
    domain_rows_html = "\n".join(domain_row(item) for item in domain_breakdown)
    evidence_html = evidence_blocks(top_signals)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>US Constitutional Risk Daily</title>
  <style>
    :root {{
      --bg: #f5f7fb;
      --ink: #152238;
      --muted: #57657a;
      --panel: #ffffff;
      --line: #dbe3ee;
      --accent: #0b5ed7;
      --accent-soft: #e8f0ff;
      --warn: #b54708;
      --ok: #027a48;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Source Sans 3", "Segoe UI", Tahoma, sans-serif;
      background: radial-gradient(circle at top right, #ebf2ff, var(--bg) 45%);
      color: var(--ink);
      line-height: 1.5;
    }}
    main {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 28px 16px 48px;
    }}
    h1, h2, h3 {{
      font-family: "Merriweather", Georgia, serif;
      margin: 0 0 10px;
    }}
    .headline {{
      display: grid;
      gap: 12px;
      margin-bottom: 18px;
    }}
    .score-row {{
      display: flex;
      align-items: baseline;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .score {{
      font-size: clamp(2rem, 4vw, 3rem);
      font-weight: 800;
      color: {score_css_color};
      text-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);
    }}
    .score-scale-note {{
      color: var(--muted);
      font-size: 0.95rem;
      font-weight: 600;
    }}
    .risk-context {{
      color: var(--muted);
      font-size: 0.95rem;
      max-width: 900px;
    }}
    .band {{
      background: var(--accent-soft);
      color: var(--accent);
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 0.95rem;
      font-weight: 700;
    }}
    .status {{
      padding: 8px 10px;
      border-radius: 8px;
      font-weight: 600;
      margin-top: 4px;
    }}
    .status-ok {{
      background: #ecfdf3;
      color: var(--ok);
      border: 1px solid #c8ecd8;
    }}
    .status-warning {{
      background: #fff6eb;
      color: var(--warn);
      border: 1px solid #f7dfbd;
    }}
    .grid {{
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 14px;
      margin: 16px 0;
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 14px;
      box-shadow: 0 2px 6px rgba(14, 31, 53, 0.04);
    }}
    .metrics {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
    }}
    .metric {{
      background: #f8fbff;
      border: 1px solid #e1eaf7;
      border-radius: 10px;
      padding: 10px;
    }}
    .metric .k {{
      color: var(--muted);
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .metric .v {{
      font-size: 1.25rem;
      font-weight: 700;
      margin-top: 2px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
    }}
    th, td {{
      border-bottom: 1px solid var(--line);
      text-align: left;
      padding: 8px 6px;
      vertical-align: top;
    }}
    th {{
      color: var(--muted);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    ul {{
      margin: 0;
      padding-left: 20px;
    }}
    li {{
      margin: 8px 0;
    }}
    a {{
      color: var(--accent);
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    .meta {{
      color: var(--muted);
      font-size: 0.85rem;
    }}
    .note {{
      color: var(--muted);
      font-size: 0.92rem;
    }}
    footer {{
      margin-top: 20px;
      font-size: 0.9rem;
      color: var(--muted);
    }}
    canvas {{
      width: 100%;
      height: 280px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
    }}
    @media (max-width: 840px) {{
      .grid {{ grid-template-columns: 1fr; }}
      .metrics {{ grid-template-columns: 1fr 1fr; }}
    }}
    @media (max-width: 520px) {{
      .metrics {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <main>
    <section class="headline">
      <h1>US Constitutional Risk Daily</h1>
      <div class="score-row">
        <div class="score">{score} / 100</div>
        <div class="band">{band_label}</div>
      </div>
      <div class="score-scale-note">Scale: 0 = no constitutional risk, 100 = constitution destroyed.</div>
      <div class="risk-context">
        This score estimates current constitutional-order stress from observable events across elections, courts, executive power, and opposition rights.
        A score of 0 means no credible current events indicating breakdown risk beyond normal political noise, while 100 means effective constitutional failure where lawful transfer of power and checks-and-balances no longer function.
      </div>
      <div>{band_desc}</div>
      <div class="status {status_class}">{status_text}</div>
      <div class="note">Updated: {generated_at}</div>
    </section>

    <section class="grid">
      <div class="panel">
        <h2>30-Day Trend</h2>
        <canvas id="scoreChart" width="700" height="280"></canvas>
      </div>
      <div class="panel">
        <h2>Quick Metrics</h2>
        <div class="metrics">
          <div class="metric"><div class="k">Previous Day Delta</div><div class="v">{fmt_number(summary.get("delta_previous_day"))}</div></div>
          <div class="metric"><div class="k">Delta vs 7-Day Avg</div><div class="v">{fmt_number(summary.get("delta_vs_7d"))}</div></div>
          <div class="metric"><div class="k">Feed Pull Success</div><div class="v">{summary.get("successful_queries", 0)} / {summary.get("attempted_queries", 0)}</div></div>
          <div class="metric"><div class="k">Confidence</div><div class="v">{html.escape(str(summary.get("confidence", "n/a")))}</div></div>
        </div>
      </div>
    </section>

    <section class="panel">
      <h2>Domain Breakdown</h2>
      <table>
        <thead>
          <tr>
            <th>Domain</th>
            <th>Weight</th>
            <th>Avg Severity (0-4)</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {domain_rows_html}
        </tbody>
      </table>
    </section>

    <section class="panel">
      <h2>Highest-Risk Signals Today</h2>
      <table>
        <thead>
          <tr>
            <th>Signal</th>
            <th>Domain</th>
            <th>Severity</th>
            <th>Hits</th>
            <th>Unique Publishers</th>
          </tr>
        </thead>
        <tbody>
          {signal_rows_html}
        </tbody>
      </table>
    </section>

    {evidence_html}

    <footer>
      <p>Method: score is a weighted 0-100 indicator from domain-level constitutional stress signals. This is an early-warning tool, not legal proof.</p>
      <p>Use high-severity changes only after validating with primary legal records, court orders, and official filings.</p>
      <p>Raw artifacts: <a href="./data/latest_dashboard.json">latest_dashboard.json</a> | <a href="./data/constitutional_risk_history.csv">constitutional_risk_history.csv</a></p>
    </footer>
  </main>

  <script>
    const labels = {json.dumps(chart_labels)};
    const values = {json.dumps(chart_values)};
    const canvas = document.getElementById("scoreChart");
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;
    const pad = {{ l: 44, r: 18, t: 16, b: 34 }};
    const x0 = pad.l;
    const y0 = h - pad.b;
    const x1 = w - pad.r;
    const y1 = pad.t;
    const chartW = x1 - x0;
    const chartH = y0 - y1;

    function yFor(v) {{
      return y0 - (Math.max(0, Math.min(100, v)) / 100) * chartH;
    }}
    function xFor(i) {{
      if (values.length <= 1) return x0;
      return x0 + (i / (values.length - 1)) * chartW;
    }}

    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, w, h);
    ctx.strokeStyle = "#dbe3ee";
    ctx.lineWidth = 1;

    [0, 20, 40, 60, 80, 100].forEach((tick) => {{
      const y = yFor(tick);
      ctx.beginPath();
      ctx.moveTo(x0, y);
      ctx.lineTo(x1, y);
      ctx.stroke();
      ctx.fillStyle = "#57657a";
      ctx.font = "12px sans-serif";
      ctx.fillText(String(tick), 8, y + 4);
    }});

    ctx.strokeStyle = "#0b5ed7";
    ctx.lineWidth = 2;
    ctx.beginPath();
    values.forEach((v, i) => {{
      const x = xFor(i);
      const y = yFor(v);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }});
    ctx.stroke();

    ctx.fillStyle = "#0b5ed7";
    values.forEach((v, i) => {{
      const x = xFor(i);
      const y = yFor(v);
      ctx.beginPath();
      ctx.arc(x, y, 3, 0, Math.PI * 2);
      ctx.fill();
    }});

    ctx.fillStyle = "#57657a";
    ctx.font = "12px sans-serif";
    if (labels.length > 0) {{
      ctx.fillText(labels[0], x0, h - 10);
      const rightText = labels[labels.length - 1];
      const textW = ctx.measureText(rightText).width;
      ctx.fillText(rightText, x1 - textW, h - 10);
    }}
  </script>
</body>
</html>
"""


def main() -> int:
    args = parse_args()
    summary = read_json(args.summary_json)
    history_rows = read_history(args.history)

    output_html = render_html(summary, history_rows)
    args.output_html.parent.mkdir(parents=True, exist_ok=True)
    args.output_html.write_text(output_html, encoding="utf-8")

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    args.output_history.parent.mkdir(parents=True, exist_ok=True)
    if args.history.exists():
        args.output_history.write_text(args.history.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"Rendered {args.output_html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
