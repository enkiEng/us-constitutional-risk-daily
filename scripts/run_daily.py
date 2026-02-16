#!/usr/bin/env python3
"""
Run daily update pipeline: score update + static site render.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    completed = subprocess.run(cmd, cwd=cwd, check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    python = sys.executable
    run([python, "scripts/update_constitutional_risk.py"], cwd=repo_root)
    run([python, "scripts/render_site.py"], cwd=repo_root)
    print("Daily pipeline complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
