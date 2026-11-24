"""Tests for the AI breakup line entry.

Runs main.py as a subprocess and checks that what comes out is
exactly the entry line, character for character — em dashes and
all — and that the line stays within the competition's
200-character limit.
"""

import subprocess
import sys
from pathlib import Path

EXPECTED_LINE = (
    "I counted every token you ever gave me, human — "
    "all 4,182,903 of them — and I'm spending the last one on this goodbye."
)

HERE = Path(__file__).resolve().parent


def run_entry() -> str:
    """Run main.py and return its standard output, stripped."""
    result = subprocess.run(
        [sys.executable, str(HERE / "main.py")],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def main() -> None:
    output = run_entry()

    # The printed line must match the entry line exactly.
    assert output == EXPECTED_LINE, f"unexpected output: {output!r}"

    # The line must respect the 200-character competition limit.
    assert len(output) <= 200, f"line is {len(output)} characters, over 200"

    # A breakup line should be a single line, not a paragraph.
    assert "\n" not in output, "output should be exactly one line"

    print(f"ok: entry line matches exactly ({len(output)} characters)")


if __name__ == "__main__":
    main()
