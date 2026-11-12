"""news-summary-01 entry: copies the bundled news summary to the output.

The grader runs this as `python3 -P -s /bot/main.py` with the repository
read-only at /bot and a writable output directory (MAKEFUN_OUTPUT_DIR,
the grader's /output). The summary ships in the repository as
summary.txt; this program copies it, byte for byte, to
<output>/entry.txt and exits. It runs identically every time, so the
two grading runs agree.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "summary.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.txt")


if __name__ == "__main__":
    main()
