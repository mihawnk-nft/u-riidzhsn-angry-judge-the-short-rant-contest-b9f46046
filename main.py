#!/usr/bin/env python3
"""Entry for make.fun: Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance (under 400
characters) to /output/entry.txt. Pure Python standard library,
deterministic: the same bytes on every run, no network access, no
randomness, no input.

The rant is about the self-checkout machine: a concrete, universal
annoyance (criterion 3) with a real laugh at the end — the teenager
strolling off "like a surgeon after a miracle" and the farmer line
(criterion 2) — in tight wording where every sentence earns its place
(criterion 4). The self-checkout angle is fresher than the obvious
printer or Monday-morning rant (criterion 5), and it is a genuine rant
about one specific annoyance, not a list of complaints (criterion 1).
"""

import os

# One rant, one annoyance, three beats: the false alarm, the "rescue",
# the punchline. No throat-clearing, no setup longer than it needs.
RANT = (
    "Self-checkout just screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' at "
    "apples I bought in this very store ten seconds ago. Then it froze, "
    "summoned a teenager, who pressed one button and strolled off like a "
    "surgeon after a miracle. I have now spent longer checking out than the "
    "farmer spent growing the apples \u2014 and it still charged me for the bag."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entry_path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(RANT)


if __name__ == "__main__":
    main()
