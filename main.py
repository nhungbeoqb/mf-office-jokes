#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — one-line office joke entry.

Writes a single joke about office life (under 200 characters) to
/output/entry.txt. Pure Python 3.13 standard library, deterministic:
the same joke every run, byte for byte.
"""

import os

# v2 (second-round revision): split into two sentences for timing, em-dash
# before the final beat, and "to the back" — the counter-offer stapled to
# the back of the resignation itself, a sharper visual punch than "to it".
JOKE = (
    "The printer jammed on page one of my resignation letter. "
    "HR printed it for me \u2014 and stapled a counter-offer to the back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
