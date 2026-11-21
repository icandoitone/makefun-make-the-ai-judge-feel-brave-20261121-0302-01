"""Write one short, steadying text to /output/entry.txt.

The text is a small, unhurried scene: late-afternoon light, a quiet
kettle, tea cooling in no hurry. It shows calm rather than telling
anyone to relax, and it leaves one image to return to.
"""

import os

TEXT = (
    "Late afternoon light comes in low through the kitchen window "
    "and lands on the chipped blue mug. The kettle has gone quiet. "
    "Nothing needs doing before the tea cools, "
    "and the tea is in no hurry either."
)

# The gate allows 1 to 280 characters, counted as Unicode code points.
assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
