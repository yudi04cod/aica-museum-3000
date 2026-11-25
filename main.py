#!/usr/bin/env python3
"""Museum of the Year 3000 — a single museum label, written by a curator
from the year 3000, placed beside an ordinary object from today."""

import os

# The label: a group chat, misread by the year 3000 as a physical place
# where humans gathered nightly. Deadpan, one line, no explanation.
LABEL = (
    "Group Chat, c. 2024. Each night, humans gathered here to share "
    "pictures of food and argue, in writing, about where to eat. "
    "They never decided."
)


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= 200, f"label is {len(text)} chars"
    assert "\n" not in text, "label must be a single line"
    text.encode("utf-8")  # must be valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    # Read back what we wrote: the artifact on disk must be exactly the
    # label, one line, no trailing newline, valid UTF-8.
    with open("/output/entry.txt", "r", encoding="utf-8") as fh:
        written = fh.read()
    assert written == text, "entry.txt on disk differs from the label"


if __name__ == "__main__":
    main()
