#!/usr/bin/env python3
"""Write one sentence pitching the worst, most useless app idea imaginable.

Deterministic: every run writes byte-identical entry.txt.
Python 3 standard library only, no network access.
"""

import os

PITCH = (
    "KettleWatch is a ten-dollar-a-month app that hires a certified "
    "kettle-watching professional to watch your kettle boil over "
    "livestream and text you the exact second it clicks off, a job "
    "your own ears already do for free."
)

MAX_CHARS = 240
TERMINATORS = ".!?"


def validate(text: str) -> None:
    """Enforce the entry rules; raise ValueError on any violation."""
    if not text:
        raise ValueError("pitch must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"pitch is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    marks = sum(1 for ch in text if ch in TERMINATORS)
    if marks != 1:
        raise ValueError(
            f"pitch must contain exactly one sentence-terminating mark, found {marks}"
        )
    if not text.endswith(tuple(TERMINATORS)):
        raise ValueError("pitch must end with its single sentence-terminating mark")


def main() -> None:
    validate(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = PITCH.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes, {len(PITCH)} characters to {path}")


if __name__ == "__main__":
    main()
