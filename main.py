"""Long Roast entry writer.

Reads the one-line roast from entry.txt next to this file and copies it
byte-for-byte into $MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644, so the
grader sees exactly the text shipped in this repository.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 200


def main() -> int:
    try:
        src = Path(__file__).resolve().parent / "entry.txt"
        text = src.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read entry.txt: {exc}", file=sys.stderr)
        return 1

    if not text.strip():
        print("error: entry.txt is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text.strip()) > MAX_CHARS:
        print(
            f"error: entry is {len(text.strip())} chars, over the "
            f"{MAX_CHARS}-char limit",
            file=sys.stderr,
        )
        return 1

    try:
        out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / "entry.txt"
        out.write_text(text, encoding="utf-8")
        os.chmod(out, 0o644)
    except (OSError, KeyError) as exc:
        print(f"error: cannot write output entry.txt: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
