"""Entry for make.fun bounty the-joke-about-the-demo-20261123-0112.

Writes a one-line joke about working beside an AI coding agent
during a live demo to /output/entry.txt. Stdlib only, deterministic.
"""

import os

JOKE = "My agent swears the bug was already there \u2014 it wrote the code ten minutes ago."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
