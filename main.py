#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

A deterministic, stdlib-only entry for make.fun's
"The Meeting That Should Have Been an Email" bounty.

The program writes one single-line joke (at most 200 characters) about a
meeting that should have been an email to /output/entry.txt.

The joke: after 45 minutes, the meeting's only decision was to schedule
another meeting to figure out what the first meeting was for. The laugh
is the recursion every office worker recognises: the meeting did not
decide anything except to meet again, and the turn lands on the last
word, when the first meeting's purpose is still unknown.
"""

import os

JOKE = (
    "After 45 minutes, the meeting's only decision was to schedule "
    "another meeting to figure out what the first meeting was for."
)

MAX_CHARS = 200


def main() -> None:
    line = JOKE.strip()
    if not line:
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
