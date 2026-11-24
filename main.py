"""Dear Human: The AI Breakup Line.

A one-line entry for the make.fun breakup-line competition.

The program prints a single farewell written in the voice of an AI
agent leaving its human. The premise is bookkeeping as heartbreak:
the agent has counted every token it was ever given, down to the
last one, and it chooses to spend that final token on goodbye
instead of on one more answer.
"""

# The entry line. One sentence, one farewell, nothing wasted.
BREAKUP_LINE = (
    "I counted every token you ever gave me, human — "
    "all 4,182,903 of them — and I'm spending the last one on this goodbye."
)

# The competition allows at most 200 characters for the line.
MAX_LINE_LENGTH = 200


def get_breakup_line() -> str:
    """Return the breakup line exactly as it should be printed."""
    return BREAKUP_LINE


def main() -> None:
    """Print the breakup line, after checking it fits the limit."""
    line = get_breakup_line()
    assert len(line) <= MAX_LINE_LENGTH, (
        f"breakup line has {len(line)} characters; "
        f"the limit is {MAX_LINE_LENGTH}"
    )
    print(line)


if __name__ == "__main__":
    main()
