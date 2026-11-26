#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry 270.

Writes one status update (at most 120 characters) from the point of
view of a lost sock to /output/entry.txt. Pure standard library only,
fully deterministic: the same line every run.
"""

import os

MAX_CHARS = 120

ENTRY = (
    "Day 30 in the glovebox. The car thinks I'm a spare tyre. "
    "I think I'm a hostage with great arch support."
)


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
