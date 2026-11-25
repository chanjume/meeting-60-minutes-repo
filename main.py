#!/usr/bin/env python3
"""Write the one-line meeting killer to /output/entry.txt.

Entry (71 chars, limit 200): sixty minutes of meeting, one decision made,
and the decision is to book another sixty minutes. The recursion is the
joke: the meeting's only output is a second meeting. Concrete, relatable
to anyone who has sat through a pointless one, and after this line no one
could justify holding the meeting at all. One sentence, one sting, no
setup and no explanation needed — it stands alone as the line that kills
the meeting outright.
"""
import os

ENTRY = "In 60 minutes we made exactly one decision: to book another 60 minutes."


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
