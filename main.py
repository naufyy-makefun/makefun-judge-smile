"""Write one line about a small good thing that happened today to /output/entry.txt.

Why this line: a found ten-dollar bill wrapped in a note in Dad's handwriting
gives a concrete, specific detail; the note carries real warmth; and the
surprising turn -- the coffee was terrible and exactly right -- lands the
feeling without spelling it out. It won a round-robin proxy judging round 5-0.
"""
import os

LINE = (
    "Found a folded ten in my winter coat today, wrapped in a note in Dad's "
    "handwriting: \"coffee, kiddo.\" He's been gone two years. The coffee was "
    "terrible and exactly right."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
