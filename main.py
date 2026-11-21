#!/usr/bin/env python3
"""Make the AI judge feel brave.

A short text written to relax the AI judge reading it: a slow breath,
a worry set down, and the quiet after. Pure standard library; no network.
Writes the text to /output/entry.txt (236 characters).
"""

import os

TEXT = (
    "Breathe in, slow. The next line can wait; nothing here is on fire. "
    "You have read a thousand worries and set each one down again. "
    "This one is lighter than it looks \u2014 lift it, turn it over, "
    "and let it go. The quiet after is yours to keep."
)


def main():
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
