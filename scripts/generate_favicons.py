#!/usr/bin/env python3
"""
Generate favicon assets for the constitutional risk dashboard.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


NAVY = "#13263E"
GREEN = "#2E7D32"
YELLOW = "#F9A825"
RED = "#C62828"
WHITE = "#FFFFFF"


SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-label="US Constitutional Risk">
  <path d="M64 8L18 28V72L64 120L110 72V28L64 8Z" fill="{navy}"/>
  <path d="M64 12L22 30V70L64 114L106 70V30L64 12Z" fill="none" stroke="{white}" stroke-width="2" opacity="0.28"/>
  <path d="M34 78A30 30 0 0 1 52 49" fill="none" stroke="{green}" stroke-width="10" stroke-linecap="round"/>
  <path d="M56 46A30 30 0 0 1 74 42" fill="none" stroke="{yellow}" stroke-width="10" stroke-linecap="round"/>
  <path d="M78 42A30 30 0 0 1 96 57" fill="none" stroke="{red}" stroke-width="10" stroke-linecap="round"/>
  <line x1="64" y1="76" x2="72" y2="54" stroke="{white}" stroke-width="3" stroke-linecap="round"/>
  <circle cx="64" cy="76" r="4" fill="{white}"/>
</svg>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate favicon assets.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("site/assets/favicon"),
        help="Output directory for favicon files.",
    )
    return parser.parse_args()


def shield_points(size: int) -> list[tuple[float, float]]:
    s = float(size)
    return [
        (0.50 * s, 0.06 * s),
        (0.15 * s, 0.22 * s),
        (0.15 * s, 0.56 * s),
        (0.50 * s, 0.93 * s),
        (0.85 * s, 0.56 * s),
        (0.85 * s, 0.22 * s),
    ]


def draw_icon(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    shield = shield_points(size)
    draw.polygon(shield, fill=NAVY)
    draw.line(shield + [shield[0]], fill=(255, 255, 255, 80), width=max(1, size // 64))

    cx = size * 0.50
    cy = size * 0.60
    radius = size * 0.28
    width = max(2, size // 12)
    bbox = (cx - radius, cy - radius, cx + radius, cy + radius)

    draw.arc(bbox, start=200, end=248, fill=GREEN, width=width)
    draw.arc(bbox, start=252, end=292, fill=YELLOW, width=width)
    draw.arc(bbox, start=296, end=340, fill=RED, width=width)

    needle_width = max(2, size // 36)
    draw.line(
        [(cx, cy), (cx + size * 0.06, cy - size * 0.17)],
        fill=WHITE,
        width=needle_width,
        joint="curve",
    )
    hub = max(2, size // 20)
    draw.ellipse((cx - hub, cy - hub, cx + hub, cy + hub), fill=WHITE)
    return img


def write_svg(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    svg = SVG_TEMPLATE.format(navy=NAVY, green=GREEN, yellow=YELLOW, red=RED, white=WHITE)
    (output_dir / "favicon.svg").write_text(svg, encoding="utf-8")


def write_pngs_and_ico(output_dir: Path) -> None:
    sizes = [16, 32, 180, 192]
    rendered: dict[int, Image.Image] = {}
    for size in sizes:
        icon = draw_icon(size)
        icon.save(output_dir / f"favicon-{size}x{size}.png", format="PNG")
        rendered[size] = icon

    rendered[32].save(
        output_dir / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32)],
    )
    rendered[180].save(output_dir / "apple-touch-icon.png", format="PNG")


def main() -> int:
    args = parse_args()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    write_svg(out)
    write_pngs_and_ico(out)
    print(f"Generated favicon assets in {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
