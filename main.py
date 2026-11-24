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

import os

ENTRY = (
    "Rain is the sky wringing out a giant sponge: a cloud soaks up water "
    "until it can't hold any more, then lets it fall as drops.\n"
    "The sponge maps a cloud holding water and letting it fall as drops, "
    "but it leaves out that nothing squeezes the cloud \u2014 drops just get "
    "too heavy to float \u2014 and it says nothing about where the water "
    "goes after it lands."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check (revision pass): the written bytes must equal the entry
    # exactly, and must pass the sealed gate (1-400 chars, not blank,
    # exactly two lines). Any mismatch fails loudly instead of shipping
    # a wrong entry.
    expected = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 400, "entry outside 1-400 char gate"
    assert ENTRY.strip(), "entry is only whitespace"
    assert ENTRY.count("\n") == 1, "entry must be exactly two lines"
    assert not ENTRY.endswith("\n"), "no trailing newline"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != expected:
        raise SystemExit(
            "entry.txt bytes differ from ENTRY: wrote %d bytes, expected %d"
            % (len(written), len(expected))
        )


if __name__ == "__main__":
    main()
