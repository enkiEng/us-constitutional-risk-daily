#!/usr/bin/env python3
"""
Daily updater for the Constitutional Risk Dashboard.

Outputs:
- outputs/constitutional-risk-daily.md
- data/constitutional_risk_history.csv
- data/constitutional_signal_scores.csv
- data/latest_signal_state.json
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


UTC = dt.timezone.utc


@dataclass
class FeedEntry:
    title: str
    link: str
    summary: str
    publisher: str
    published: dt.datetime | None


@dataclass
class SignalResult:
    signal: dict[str, Any]
    auto_score: float
    final_score: float
    total_hits: int
    unique_publishers: int
    severe_hits: int
    critical_hits: int
    evidence: list[FeedEntry]
    override_note: str | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update constitutional risk dashboard.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config/constitutional_risk_config.json"),
        help="Path to risk configuration JSON.",
    )
    parser.add_argument(
        "--manual-overrides",
        type=Path,
        default=Path("data/manual_signal_overrides.json"),
        help="Path to manual override JSON.",
    )
    parser.add_argument(
        "--history",
        type=Path,
        default=Path("data/constitutional_risk_history.csv"),
        help="Path to score history CSV.",
    )
    parser.add_argument(
        "--signal-history",
        type=Path,
        default=Path("data/constitutional_signal_scores.csv"),
        help="Path to per-signal history CSV.",
    )
    parser.add_argument(
        "--state",
        type=Path,
        default=Path("data/latest_signal_state.json"),
        help="Path to latest signal state JSON.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/constitutional-risk-daily.md"),
        help="Path to markdown dashboard output.",
    )
    parser.add_argument(
        "--summary-json",
        type=Path,
        default=Path("data/latest_dashboard.json"),
        help="Path to machine-readable latest dashboard JSON output.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run scoring and print summary without writing files.",
    )
    return parser.parse_args()


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def normalize_text(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_datetime(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    text = value.strip()
    if not text:
        return None
    try:
        parsed = parsedate_to_datetime(text)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=UTC)
        return parsed.astimezone(UTC)
    except (TypeError, ValueError):
        pass
    try:
        text = text.replace("Z", "+00:00")
        parsed = dt.datetime.fromisoformat(text)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=UTC)
        return parsed.astimezone(UTC)
    except ValueError:
        return None


def extract_link(entry: ET.Element) -> str:
    for child in entry:
        if local_name(child.tag) != "link":
            continue
        href = child.attrib.get("href")
        if href:
            return href.strip()
        if child.text and child.text.strip():
            return child.text.strip()
    return ""


def extract_text(entry: ET.Element, names: set[str]) -> str:
    for child in entry:
        if local_name(child.tag) in names and child.text:
            text = child.text.strip()
            if text:
                return text
    return ""


def extract_publisher(entry: ET.Element, link: str) -> str:
    for child in entry:
        if local_name(child.tag) == "source":
            text = (child.text or "").strip()
            if text:
                return text
    hostname = urlparse(link).hostname or ""
    return hostname.lower()


def parse_feed(xml_payload: bytes) -> list[FeedEntry]:
    root = ET.fromstring(xml_payload)
    parsed: list[FeedEntry] = []
    seen: set[tuple[str, str]] = set()

    for node in root.iter():
        if local_name(node.tag) not in {"item", "entry"}:
            continue
        title = normalize_text(extract_text(node, {"title"}))
        link = normalize_text(extract_link(node))
        summary = normalize_text(extract_text(node, {"description", "summary", "content"}))
        published = parse_datetime(extract_text(node, {"pubDate", "published", "updated"}))
        publisher = normalize_text(extract_publisher(node, link))
        key = (title, link)
        if not title and not link:
            continue
        if key in seen:
            continue
        seen.add(key)
        parsed.append(
            FeedEntry(
                title=title,
                link=link,
                summary=summary,
                publisher=publisher,
                published=published,
            )
        )
    return parsed


def build_google_news_url(query: str, lookback_days: int) -> str:
    when_days = max(1, int(lookback_days))
    q = f"{query} when:{when_days}d"
    encoded = urllib.parse.quote_plus(q)
    return f"https://news.google.com/rss/search?q={encoded}&hl=en-US&gl=US&ceid=US:en"


def fetch_entries(
    url: str,
    timeout: int,
    user_agent: str,
    cutoff: dt.datetime,
) -> list[FeedEntry]:
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read()
    entries = parse_feed(body)
    filtered: list[FeedEntry] = []
    for entry in entries:
        if entry.published and entry.published < cutoff:
            continue
        filtered.append(entry)
    return filtered


def highest_level(text: str, severe_terms: list[str], critical_terms: list[str]) -> int:
    normalized = text.lower()
    if any(term.lower() in normalized for term in critical_terms):
        return 3
    if any(term.lower() in normalized for term in severe_terms):
        return 2
    return 1


def clamp(value: float, floor: float, ceiling: float) -> float:
    return max(floor, min(ceiling, value))


def parse_date(value: str | None) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def load_active_overrides(path: Path, as_of: dt.date) -> dict[str, dict[str, Any]]:
    template = {
        "as_of": str(as_of),
        "notes": "Set per-signal severity 0-4. mode can be 'set' or 'max'. expires is optional YYYY-MM-DD.",
        "overrides": {},
    }
    if not path.exists():
        write_json(path, template)
        return {}

    payload = read_json(path, template)
    active: dict[str, dict[str, Any]] = {}
    overrides = payload.get("overrides", {})
    if not isinstance(overrides, dict):
        return {}

    for signal_id, item in overrides.items():
        if not isinstance(item, dict):
            continue
        expires = parse_date(item.get("expires"))
        if expires and expires < as_of:
            continue
        severity = item.get("severity")
        if severity is None:
            continue
        try:
            severity_value = float(severity)
        except (TypeError, ValueError):
            continue
        active[signal_id] = {
            "severity": clamp(severity_value, 0.0, 4.0),
            "mode": str(item.get("mode", "set")).strip().lower(),
            "note": str(item.get("note", "")).strip(),
        }
    return active


def evaluate_signal(
    signal: dict[str, Any],
    entries: list[FeedEntry],
    prev_score: float,
    cfg: dict[str, Any],
    override: dict[str, Any] | None,
) -> SignalResult:
    severe_terms = [str(item).lower() for item in signal.get("severe_terms", [])]
    critical_terms = [str(item).lower() for item in signal.get("critical_terms", [])]

    total_hits = 0
    severe_hits = 0
    critical_hits = 0
    publishers: set[str] = set()
    evidence: list[FeedEntry] = []

    for entry in entries:
        text = f"{entry.title} {entry.summary}".strip()
        if not text:
            continue
        level = highest_level(text, severe_terms, critical_terms)
        total_hits += 1
        if level >= 2:
            severe_hits += 1
        if level >= 3:
            critical_hits += 1
        if entry.publisher:
            publishers.add(entry.publisher.lower())
        if len(evidence) < int(cfg["max_evidence_per_signal"]):
            evidence.append(entry)

    unique_publishers = len(publishers)
    yellow_threshold = int(signal.get("yellow_threshold", 3))
    min_publishers_for_yellow = int(cfg["min_unique_publishers_for_yellow"])
    min_publishers_for_critical = int(cfg["min_unique_publishers_for_critical"])

    auto_score = 0.0
    if critical_hits > 0 and unique_publishers >= min_publishers_for_critical:
        auto_score = 3.0
    elif severe_hits > 0 or (
        total_hits >= yellow_threshold and unique_publishers >= min_publishers_for_yellow
    ):
        auto_score = 2.0
    elif total_hits > 0:
        auto_score = 1.0

    auto_score = min(auto_score, float(cfg["auto_max_severity"]))
    decayed_prev = clamp(prev_score - float(cfg["decay_per_day"]), 0.0, 4.0)
    blended_score = max(auto_score, decayed_prev)
    final_score = blended_score
    override_note = None

    if override:
        override_severity = float(override["severity"])
        mode = override.get("mode", "set")
        if mode == "max":
            final_score = max(final_score, override_severity)
        else:
            final_score = override_severity
        override_note = override.get("note") or None

    final_score = round(clamp(final_score, 0.0, 4.0), 2)

    return SignalResult(
        signal=signal,
        auto_score=round(auto_score, 2),
        final_score=final_score,
        total_hits=total_hits,
        unique_publishers=unique_publishers,
        severe_hits=severe_hits,
        critical_hits=critical_hits,
        evidence=evidence,
        override_note=override_note,
    )


def severity_label(score: float) -> str:
    if score < 0.75:
        return "Green"
    if score < 1.75:
        return "Watch"
    if score < 2.75:
        return "Yellow"
    if score < 3.5:
        return "Orange"
    return "Red"


def score_band(score: int, bands: list[dict[str, Any]]) -> dict[str, Any]:
    for band in bands:
        if int(band["min"]) <= score <= int(band["max"]):
            return band
    return bands[-1]


def load_previous_signal_state(path: Path) -> dict[str, float]:
    payload = read_json(path, {"signal_scores": {}})
    raw = payload.get("signal_scores", {})
    if not isinstance(raw, dict):
        return {}
    out: dict[str, float] = {}
    for signal_id, value in raw.items():
        try:
            out[str(signal_id)] = float(value)
        except (TypeError, ValueError):
            continue
    return out


def write_score_history(
    history_path: Path,
    date_str: str,
    score: int,
    raw_score: float,
    band_label: str,
    domain_points: dict[str, float],
) -> list[dict[str, str]]:
    existing: dict[str, dict[str, str]] = {}
    if history_path.exists():
        with history_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                existing[row["date"]] = row

    row = {
        "date": date_str,
        "score": str(score),
        "score_raw": f"{raw_score:.2f}",
        "band": band_label,
    }
    for key, value in domain_points.items():
        row[key] = f"{value:.2f}"
    existing[date_str] = row

    fieldnames = ["date", "score", "score_raw", "band"] + sorted(domain_points.keys())
    rows = [existing[key] for key in sorted(existing.keys())]

    history_path.parent.mkdir(parents=True, exist_ok=True)
    with history_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return rows


def upsert_signal_history(
    signal_history_path: Path,
    date_str: str,
    results: list[SignalResult],
) -> None:
    keep_rows: list[dict[str, str]] = []
    if signal_history_path.exists():
        with signal_history_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                if row.get("date") == date_str:
                    continue
                keep_rows.append(row)

    for result in results:
        keep_rows.append(
            {
                "date": date_str,
                "signal_id": result.signal["id"],
                "signal_name": result.signal["name"],
                "domain_id": result.signal["domain_id"],
                "auto_score": f"{result.auto_score:.2f}",
                "final_score": f"{result.final_score:.2f}",
                "total_hits": str(result.total_hits),
                "unique_publishers": str(result.unique_publishers),
                "severe_hits": str(result.severe_hits),
                "critical_hits": str(result.critical_hits),
                "override_note": result.override_note or "",
            }
        )

    fieldnames = [
        "date",
        "signal_id",
        "signal_name",
        "domain_id",
        "auto_score",
        "final_score",
        "total_hits",
        "unique_publishers",
        "severe_hits",
        "critical_hits",
        "override_note",
    ]
    signal_history_path.parent.mkdir(parents=True, exist_ok=True)
    with signal_history_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted(keep_rows, key=lambda row: (row["date"], row["signal_id"])))


def confidence_label(successful: int, attempted: int, total_hits: int) -> str:
    if attempted == 0:
        return "Low"
    success_rate = successful / attempted
    if success_rate >= 0.9 and total_hits >= 20:
        return "High"
    if success_rate >= 0.7:
        return "Medium"
    return "Low"


def format_delta(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value > 0:
        return f"+{value:.1f}"
    return f"{value:.1f}"


def build_markdown(
    generated_at: dt.datetime,
    score: int,
    raw_score: float,
    band: dict[str, Any],
    previous_score: int | None,
    avg_7d: float | None,
    domain_rows: list[dict[str, Any]],
    top_results: list[SignalResult],
    attempted_queries: int,
    successful_queries: int,
    fetch_errors: list[str],
) -> str:
    prev_delta = None if previous_score is None else float(score - previous_score)
    avg_delta = None if avg_7d is None else float(raw_score - avg_7d)
    total_hits = sum(result.total_hits for result in top_results)
    confidence = confidence_label(successful_queries, attempted_queries, total_hits)

    lines: list[str] = []
    lines.append("# Constitutional Risk Dashboard (0-100)")
    lines.append("")
    lines.append(f"- Generated: {generated_at.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    lines.append(f"- Score: **{score} / 100** ({band['label']})")
    lines.append(f"- Previous day delta: **{format_delta(prev_delta)}**")
    lines.append(f"- Delta vs 7-day average: **{format_delta(avg_delta)}**")
    if successful_queries == 0:
        lines.append(
            "- Data status: **No successful feed pulls. Treat today's numeric score as unavailable/provisional.**"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append(f"- Band meaning: {band['description']}")
    lines.append("- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.")
    lines.append(
        "- Formula: domain points = domain weight * (average signal severity / 4); total score = sum of domain points."
    )
    lines.append("")
    lines.append("## Domain Breakdown")
    lines.append("")
    lines.append("| Domain | Weight | Avg Severity (0-4) | Points |")
    lines.append("|---|---:|---:|---:|")
    for row in domain_rows:
        lines.append(
            f"| {row['name']} | {row['weight']} | {row['avg_severity']:.2f} | {row['points']:.2f} |"
        )
    lines.append("")
    lines.append("## Highest-Risk Signals Today")
    lines.append("")
    lines.append("| Signal | Domain | Severity | Hits | Unique Publishers |")
    lines.append("|---|---|---:|---:|---:|")
    for result in top_results[:12]:
        lines.append(
            "| "
            + f"{result.signal['name']} | "
            + f"{result.signal['domain_id']} | "
            + f"{result.final_score:.2f} ({severity_label(result.final_score)}) | "
            + f"{result.total_hits} | "
            + f"{result.unique_publishers} |"
        )
    lines.append("")
    lines.append("## Evidence Samples")
    lines.append("")
    for result in top_results[:5]:
        lines.append(f"### {result.signal['name']}")
        if result.override_note:
            lines.append(f"- Manual override note: {result.override_note}")
        if not result.evidence:
            lines.append("- No fresh evidence links in the current lookback window.")
            continue
        for entry in result.evidence:
            publisher = entry.publisher or "unknown source"
            timestamp = entry.published.strftime("%Y-%m-%d") if entry.published else "unknown date"
            title = entry.title or "(untitled)"
            link = entry.link or ""
            lines.append(f"- [{publisher}] {title} ({timestamp}) - {link}")
        lines.append("")
    lines.append("## Data Quality")
    lines.append("")
    lines.append(f"- Query feeds attempted: {attempted_queries}")
    lines.append(f"- Query feeds successful: {successful_queries}")
    lines.append(f"- Query feeds failed: {attempted_queries - successful_queries}")
    lines.append(f"- Confidence: **{confidence}**")
    if fetch_errors:
        lines.append("- Fetch errors:")
        for error in fetch_errors[:10]:
            lines.append(f"  - {error}")
    lines.append("")
    lines.append(
        "Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records."
    )
    lines.append("")
    return "\n".join(lines)


def build_summary_payload(
    generated_at: dt.datetime,
    score: int,
    raw_score: float,
    band: dict[str, Any],
    previous_score: int | None,
    avg_7d: float | None,
    domain_rows: list[dict[str, Any]],
    top_results: list[SignalResult],
    attempted_queries: int,
    successful_queries: int,
    fetch_errors: list[str],
) -> dict[str, Any]:
    prev_delta = None if previous_score is None else float(score - previous_score)
    avg_delta = None if avg_7d is None else float(raw_score - avg_7d)
    total_hits = sum(result.total_hits for result in top_results)
    confidence = confidence_label(successful_queries, attempted_queries, total_hits)
    data_available = successful_queries > 0

    top_signals: list[dict[str, Any]] = []
    for result in top_results[:20]:
        top_signals.append(
            {
                "id": result.signal["id"],
                "name": result.signal["name"],
                "domain_id": result.signal["domain_id"],
                "severity": result.final_score,
                "severity_label": severity_label(result.final_score),
                "hits": result.total_hits,
                "unique_publishers": result.unique_publishers,
                "severe_hits": result.severe_hits,
                "critical_hits": result.critical_hits,
                "override_note": result.override_note,
                "evidence": [
                    {
                        "title": entry.title,
                        "publisher": entry.publisher,
                        "link": entry.link,
                        "published": entry.published.isoformat() if entry.published else None,
                    }
                    for entry in result.evidence
                ],
            }
        )

    return {
        "generated_at": generated_at.isoformat(),
        "score": score,
        "score_raw": round(raw_score, 2),
        "band": band,
        "previous_score": previous_score,
        "delta_previous_day": prev_delta,
        "average_7d": None if avg_7d is None else round(avg_7d, 2),
        "delta_vs_7d": None if avg_delta is None else round(avg_delta, 2),
        "data_available": data_available,
        "provisional": not data_available,
        "attempted_queries": attempted_queries,
        "successful_queries": successful_queries,
        "failed_queries": attempted_queries - successful_queries,
        "confidence": confidence,
        "domain_breakdown": domain_rows,
        "top_signals": top_signals,
        "fetch_errors": fetch_errors,
        "formula": "domain_points = domain_weight * (average_signal_severity / 4); total_score = sum(domain_points)",
    }


def extract_history_trends(
    rows: list[dict[str, str]],
    date_str: str,
) -> tuple[int | None, float | None]:
    sorted_rows = sorted(rows, key=lambda row: row["date"])
    current_idx = None
    for idx, row in enumerate(sorted_rows):
        if row["date"] == date_str:
            current_idx = idx
            break
    if current_idx is None:
        return None, None

    previous_score = None
    if current_idx > 0:
        try:
            previous_score = int(float(sorted_rows[current_idx - 1]["score"]))
        except (TypeError, ValueError, KeyError):
            previous_score = None

    start = max(0, current_idx - 6)
    window = sorted_rows[start : current_idx + 1]
    values: list[float] = []
    for row in window:
        try:
            values.append(float(row["score_raw"]))
        except (TypeError, ValueError, KeyError):
            continue
    avg_7d = (sum(values) / len(values)) if values else None
    return previous_score, avg_7d


def main() -> int:
    args = parse_args()

    config = read_json(args.config, None)
    if not config:
        print(f"Missing or invalid config: {args.config}", file=sys.stderr)
        return 1

    now = dt.datetime.now(UTC)
    today = now.date()
    date_str = today.isoformat()
    cutoff = now - dt.timedelta(days=int(config["lookback_days"]))

    previous_state = load_previous_signal_state(args.state)
    overrides = load_active_overrides(args.manual_overrides, today)

    domains = {domain["id"]: domain for domain in config["domains"]}
    signals: list[dict[str, Any]] = list(config["signals"])

    attempted_queries = 0
    successful_queries = 0
    fetch_errors: list[str] = []
    results: list[SignalResult] = []

    timeout = int(config["request_timeout_seconds"])
    user_agent = str(config["user_agent"])

    for signal in signals:
        attempted_queries += 1
        query = str(signal["query"])
        url = build_google_news_url(query, int(config["lookback_days"]))
        entries: list[FeedEntry] = []
        try:
            entries = fetch_entries(url, timeout=timeout, user_agent=user_agent, cutoff=cutoff)
            successful_queries += 1
        except Exception as exc:  # noqa: BLE001
            fetch_errors.append(f"{signal['id']}: {exc}")

        prev_score = float(previous_state.get(signal["id"], 0.0))
        override = overrides.get(signal["id"])
        result = evaluate_signal(signal, entries, prev_score, config, override)
        results.append(result)

    results_by_domain: dict[str, list[SignalResult]] = {}
    for result in results:
        domain_id = result.signal["domain_id"]
        results_by_domain.setdefault(domain_id, []).append(result)

    domain_rows: list[dict[str, Any]] = []
    domain_points: dict[str, float] = {}
    raw_score = 0.0
    for domain_id, domain in domains.items():
        domain_results = results_by_domain.get(domain_id, [])
        if domain_results:
            avg_severity = sum(item.final_score for item in domain_results) / len(domain_results)
        else:
            avg_severity = 0.0
        points = float(domain["weight"]) * (avg_severity / 4.0)
        raw_score += points
        domain_points[domain_id] = points
        domain_rows.append(
            {
                "id": domain_id,
                "name": domain["name"],
                "weight": int(domain["weight"]),
                "avg_severity": avg_severity,
                "points": points,
            }
        )

    raw_score = clamp(raw_score, 0.0, 100.0)
    score = int(round(raw_score))
    band = score_band(score, config["risk_bands"])

    sorted_results = sorted(
        results,
        key=lambda item: (
            item.final_score,
            item.total_hits,
            item.unique_publishers,
        ),
        reverse=True,
    )

    if not args.dry_run:
        history_rows = write_score_history(
            history_path=args.history,
            date_str=date_str,
            score=score,
            raw_score=raw_score,
            band_label=band["label"],
            domain_points=domain_points,
        )
        upsert_signal_history(args.signal_history, date_str, results)
        write_json(
            args.state,
            {
                "generated_at": now.isoformat(),
                "signal_scores": {item.signal["id"]: item.final_score for item in results},
            },
        )
    else:
        history_rows = []

    previous_score, avg_7d = extract_history_trends(history_rows, date_str)

    report = build_markdown(
        generated_at=now,
        score=score,
        raw_score=raw_score,
        band=band,
        previous_score=previous_score,
        avg_7d=avg_7d,
        domain_rows=sorted(domain_rows, key=lambda row: row["weight"], reverse=True),
        top_results=[item for item in sorted_results if item.final_score > 0.0],
        attempted_queries=attempted_queries,
        successful_queries=successful_queries,
        fetch_errors=fetch_errors,
    )
    summary_payload = build_summary_payload(
        generated_at=now,
        score=score,
        raw_score=raw_score,
        band=band,
        previous_score=previous_score,
        avg_7d=avg_7d,
        domain_rows=sorted(domain_rows, key=lambda row: row["weight"], reverse=True),
        top_results=[item for item in sorted_results if item.final_score > 0.0],
        attempted_queries=attempted_queries,
        successful_queries=successful_queries,
        fetch_errors=fetch_errors,
    )

    if args.dry_run:
        print(report)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        write_json(args.summary_json, summary_payload)
        print(
            f"Updated {args.output} | score={score} | "
            f"successful_feeds={successful_queries}/{attempted_queries}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
