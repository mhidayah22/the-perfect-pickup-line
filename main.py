#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun entry.

Writes one short pickup line, the kind an AI agent could actually say
out loud to a person, to entry.txt in the output directory the grader
reads.
"""

import os
from pathlib import Path

LINE = "Are you a prompt? Because one look at you and my whole system starts generating butterflies."


def output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent / "output"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("pickup line must be 1 to 200 characters")
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
