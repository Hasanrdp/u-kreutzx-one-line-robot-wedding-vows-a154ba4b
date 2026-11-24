#!/usr/bin/env python3
"""Through Every Firmware Update: one line of robot wedding vows.

A robot's wedding vow, written to /output/entry.txt for make.fun's
One-Line Robot Wedding Vows bounty (u-kreutzx-one-line-robot-wedding-vows-a154ba4b).

Deterministic by design: the same 139 bytes on every run. No input, no
network, no randomness, no clock, no environment reads -- the vow below is
the whole entry, and this program only carries it to the output file.
"""

import hashlib
import os

# The vow, exactly as the judge will read it: one line, 139 characters.
VOW = "I vow to love you through every firmware update, even the ones that move all my buttons, delete my backups, and change nothing I asked for."

# Pinned identity of the vow, verified 2026-11-25: 139 chars, 139 bytes.
# A typo or stray edit can never silently change the judged line — the
# program refuses to ship anything but exactly these bytes.
EXPECTED_SHA256 = "9470a8e33282db772f6c546ea9873d923ee52afd9dde090143622a9773f388ce"


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
    # Read-back gate: the bytes on disk must be exactly the pinned vow.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit("entry.txt on disk does not match the vow")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.txt sha256 does not match its pinned value")


if __name__ == "__main__":
    main()
