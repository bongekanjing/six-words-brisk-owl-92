#!/usr/bin/env python3
"""Write the six-word story to the grader's output path.

The whole entry is one line of text.  The gate accepts 1 to 60 characters of
UTF-8 that is not only white space, so the only real risks are a miscount and
an encoding slip.  Both are checked here before anything is written: a program
that refuses is cheaper than a zero on the board.
"""
import json
import os
import sys

STORY = "Forty years sober. Tonight, I drink."

WORDS_REQUIRED = 6
MIN_CHARS = 1
MAX_CHARS = 60


def words(text):
    """The words the judge will count, punctuation and dashes aside."""
    cleaned = text
    for mark in ",.;:!?\"'\u2019\u2018\u2014\u2013-":
        cleaned = cleaned.replace(mark, " ")
    return [piece for piece in cleaned.split() if piece]


def main():
    text = STORY.strip()
    length = len(text.encode("utf-8"))
    counted = words(text)

    if not text or not text.strip():
        raise SystemExit("the story is blank")
    if length < MIN_CHARS or length > MAX_CHARS:
        raise SystemExit("the story is %d characters, outside %d to %d"
                         % (length, MIN_CHARS, MAX_CHARS))
    if len(counted) != WORDS_REQUIRED:
        raise SystemExit("the story is %d words, not %d: %r"
                         % (len(counted), WORDS_REQUIRED, counted))
    try:
        text.encode("utf-8").decode("utf-8")
    except UnicodeError as fault:
        raise SystemExit("the story is not UTF-8: %s" % fault)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    with open(target, "rb") as handle:
        written = handle.read()
    if written.decode("utf-8") != text:
        raise SystemExit("the file does not read back as the story")

    print(json.dumps({
        "entry": target,
        "text": text,
        "words": len(counted),
        "bytes": len(written),
    }, indent=2))


if __name__ == "__main__":
    main()
