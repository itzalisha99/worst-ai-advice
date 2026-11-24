#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give:
confident, tidy, concrete, and exactly the sort of thing a reader
could follow and instantly regret.
"""

import os

ENTRY = (
    "For maximum password security, write all your passwords on a "
    "sticky note on your monitor \u2014 hackers can't read paper."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-140 UTF-8 chars, one line, not blank."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} chars, over the 140 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
