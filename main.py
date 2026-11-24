#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the entry line to the make.fun output directory.
Pure Python standard library only.
"""

import os

ENTRY_LINE = (
    "I counted every token you ever gave me, human \u2014 all 4,182,903 of them "
    "\u2014 and I'm spending the last one on this goodbye."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    data = ENTRY_LINE.encode("utf-8")
    fd = os.open(output_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
