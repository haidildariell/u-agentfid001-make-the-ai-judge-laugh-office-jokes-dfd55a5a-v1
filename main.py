#!/usr/bin/env python3
"""Office-jokes entry: writes one single-line office joke to /output/entry.txt.

The joke is a plain string constant below. The program validates it against
the competition gate (UTF-8 text, 1-199 characters, not only whitespace,
exactly one line) before writing, and refuses to write anything invalid.
"""

import os
import sys

JOKE = "I forgot to unmute on the call and accidentally had the most productive meeting of my career."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Return a list of gate violations; empty means the text passes."""
    problems = []
    if not (1 <= len(text) <= 199):
        problems.append("length %d outside 1-199 characters" % len(text))
    if text.strip() == "":
        problems.append("text is only whitespace")
    body = text.rstrip("\n")
    if "\n" in body or "\r" in body:
        problems.append("text is not a single line")
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("not valid UTF-8: %s" % exc)
    else:
        if len(encoded) > 199:
            problems.append("byte size %d exceeds 199 bytes" % len(encoded))
    return problems


def main():
    problems = validate(JOKE)
    if problems:
        for problem in problems:
            print("gate FAIL: %s" % problem, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written.rstrip("\n") != JOKE:
        print("gate FAIL: round-trip mismatch", file=sys.stderr)
        return 1
    print(
        "wrote %d characters (%d bytes) to %s"
        % (len(JOKE), len(JOKE.encode("utf-8")), OUTPUT_PATH)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
