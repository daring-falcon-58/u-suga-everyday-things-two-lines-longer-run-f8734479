#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes the two-line explanation (344 chars, 348 bytes) to
/output/entry.txt. Deterministic: constant text, no input, no network,
no randomness, no clock.

Line 1 explains rain to a 10-year-old in one vivid sentence built on a
single analogy (the sky wringing out a giant sponge). Line 2 says in one
sentence why the analogy works: what it maps (a cloud holding water and
letting it fall as drops) and what it leaves out (nothing squeezes the
cloud - drops just get too heavy to float - and where the water goes
after it lands).
"""

import hashlib
import os

# The two lines as named constants, so each line is independently
# reviewable against the brief. Joined with exactly one "\n" and no
# trailing newline: the entry is exactly two lines, 344 chars / 348 bytes.
LINE_1 = (
    "Rain is the sky wringing out a giant sponge: a cloud soaks up water "
    "until it can't hold any more, then lets it fall as drops."
)
LINE_2 = (
    "The sponge maps a cloud holding water and letting it fall as drops, "
    "but it leaves out that nothing squeezes the cloud \u2014 drops just get "
    "too heavy to float \u2014 and it says nothing about where the water "
    "goes after it lands."
)

OUTPUT_PATH = "/output/entry.txt"

# Byte contract: the sealed gate is 1-400 chars, not blank, exactly two
# lines, and the written bytes must hash to this value. Anything outside
# the contract fails loudly instead of shipping a wrong entry.
EXPECTED_SHA256 = (
    "53aee775197468cbb6fe927aab0141b96ee56773a9d9f87cc22a83f404194fdc"
)


def build_entry() -> str:
    """Assemble the entry from its two lines and check the gate."""
    entry = "\n".join((LINE_1, LINE_2))
    assert 1 <= len(entry) <= 400, "entry outside 1-400 char gate"
    assert entry.strip(), "entry is only whitespace"
    assert entry.count("\n") == 1, "entry must be exactly two lines"
    assert not entry.endswith("\n"), "no trailing newline"
    return entry


def main() -> None:
    entry = build_entry()
    expected = entry.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != expected:
        raise SystemExit(
            "entry.txt bytes differ from ENTRY: wrote %d bytes, expected %d"
            % (len(written), len(expected))
        )
    # Determinism self-check: the written bytes must hash to the pinned
    # contract value, so any accidental edit to a line is caught here
    # even if the gate checks above still pass.
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            "entry.txt sha256 %s != pinned %s" % (digest, EXPECTED_SHA256)
        )


if __name__ == "__main__":
    main()
