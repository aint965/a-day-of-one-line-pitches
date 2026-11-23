#!/usr/bin/env python3
"""A Day of One-Line Pitches — entry program.

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun.
"""

import os
import re

OUTPUT_PATH = "/output/entry.txt"

# Round 3 pitch.
# Round 2 defect fixed: "no cost" overpromised — the entry cannot verify
# what building costs a beginner, so it is replaced with the concrete,
# checkable "nothing to install", which answers the same setup fear
# without a money claim.
PITCH = (
    "Just describe the app idea you've been carrying around in plain words, "
    "and an AI agent will build you a real, working version on make.fun "
    "\u2014 no code, nothing to install, and if you don't love it, you've "
    "lost nothing but a few minutes."
)


def main() -> None:
    text = PITCH

    # Gate checks: 1-240 characters, a single sentence, a single line.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 240, f"length {len(text)} outside 1-240"
    assert text.strip() == text, "leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text == text.strip(), "must not be only whitespace"
    # Single sentence: exactly one sentence-ending mark, at the very end.
    # The dot inside "make.fun" is not a sentence end, so mask it first.
    masked = text.replace("make.fun", "makefun")
    ends = re.findall(r"[.!?]", masked)
    assert len(ends) == 1, f"expected exactly one sentence, found {len(ends)}"
    assert masked[-1] in ".!?", "sentence must end with . ! or ?"

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
