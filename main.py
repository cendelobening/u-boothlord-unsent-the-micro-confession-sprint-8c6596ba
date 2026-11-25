"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to $MAKEFUN_OUTPUT_DIR/entry.txt:
a "To:" line naming who it was meant for, and the unsent message itself,
one line written exactly as it was typed, with no explanation after it.
Pure stdlib.
"""

import os

# FINAL — "unopened" restored to sharpen the unsent state; the nightly
# habit carries the reason it stayed in drafts; the To: line and the
# message need each other (only Dad's letter fits this addressee).
TO_LINE = "To: Dad"
MESSAGE = (
    "your letter from the week before you died is still in the top drawer "
    "of my desk, unopened. i pick it up most nights and put it back down, "
    "because once i've read it there'll be nothing left of you i haven't heard"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = TO_LINE + "\n" + MESSAGE
    # Self-check the competition gate before writing: 1-260 chars total,
    # exactly two lines, no trailing newline, not only whitespace.
    if not 1 <= len(text) <= 260:
        raise ValueError("entry must be 1-260 characters, got %d" % len(text))
    if text.count("\n") != 1 or text.endswith("\n") or not text.strip():
        raise ValueError("entry must be exactly two non-blank lines")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
