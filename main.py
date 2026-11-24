#!/usr/bin/env python3
"""Through Every Firmware Update: one line of robot wedding vows.

A robot's wedding vow, written to /output/entry.txt for make.fun's
One-Line Robot Wedding Vows bounty (u-kreutzx-one-line-robot-wedding-vows-a154ba4b).

Deterministic by design: the same 139 bytes on every run. No input, no
network, no randomness, no clock, no environment reads -- the vow below is
the whole entry, and this program only carries it to the output file.
"""

import os

# The vow, exactly as the judge will read it: one line, 139 characters.
VOW = "I vow to love you through every firmware update, even the ones that move all my buttons, delete my backups, and change nothing I asked for."


def main() -> None:
    text = VOW
    if not 1 <= len(text) <= 160:
        raise ValueError(f"vow is {len(text)} characters, must be 1-160")
    if not text.strip():
        raise ValueError("vow must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must fit on one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
