#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing that happened today.

Writes the entry line to /output/entry.txt. Deterministic, no network,
no randomness: the same line every run.
"""

import os

ENTRY = (
    "My six-year-old niece called today to say she'd saved me the last "
    "strawberry, then ate it 'to check it was safe' and promised to save "
    "me the next one."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
