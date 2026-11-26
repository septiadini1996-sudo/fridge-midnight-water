#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line to /output/entry.txt, as the competition
contract requires. The line is a dry status note from the fridge
itself, calling out its owner on the third midnight snack run.
"""

import os

LINE = "2:14 AM. Third midnight snack run. I have stopped pretending you came for water."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the scorer's gate before writing: the entry must be
    # UTF-8 text of 1 to 160 characters, not only white space.
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise ValueError(f"LINE fails the 1-160 character gate: {len(LINE)} chars")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    if written != LINE:
        raise ValueError("written entry.txt does not match LINE")
    print(LINE)


if __name__ == "__main__":
    main()
