#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry.

Writes a single funny line (setup + turn, punchline last) to
/output/entry.txt. Pure standard library only.
"""

import os

# The line: a parrot that has learned the most passive-aggressive
# sentence in office English -- and the HR meeting that inevitably
# follows once it starts using it on the boss.
LINE = "I taught my parrot to say 'per my last email'. HR has never been faster at scheduling a meeting about me."

MAX_CHARS = 200


def main():
    # One line, one laugh: strip stray whitespace, enforce the
    # competition's 1-200 character gate, then write it out.
    line = LINE.strip()
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
