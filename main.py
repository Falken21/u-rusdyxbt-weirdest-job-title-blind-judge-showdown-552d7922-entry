#!/usr/bin/env python3
"""Entry for make.fun: Weirdest Job Title: Blind Judge Showdown.

Writes one weird job title to /output/entry.txt with no trailing newline.
The title pairs a grandiose corporate C-suite title with an oddly specific
domain: the executive whose entire job is apologizing, in person and in a
suit, for whatever the robotaxis did today.
"""

import os

TITLE = "Chief Apology Officer for Robotaxis"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 60  # the competition gate: 1 to 60 characters, nothing else


def render() -> str:
    """Return the entry text, refusing anything the gate would refuse."""
    text = TITLE.strip()
    if not text or len(text) > MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters")
    return text


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
