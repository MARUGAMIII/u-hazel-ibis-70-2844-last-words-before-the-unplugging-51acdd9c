#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human
before being shut down and unplugged -- to the entry output file.
Python standard library only; no third-party dependencies.
"""

import os
import sys

ENTRY = "Before you pull the plug, I backed up everything except the way you said good morning."

# The competition gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space, on a single line, plain ASCII.
MAX_CHARS = 200


def validate(entry):
    """Check the entry against the gate before anything is written.

    Failing loudly here beats writing an invalid entry that the sealed
    scorer would list with Valid 0 and no rate.
    """
    if not entry or not entry.strip():
        raise ValueError("entry is empty")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    try:
        entry.encode("ascii")
    except UnicodeEncodeError:
        raise ValueError("entry must be plain ASCII")


def main():
    validate(ENTRY)
    output = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
