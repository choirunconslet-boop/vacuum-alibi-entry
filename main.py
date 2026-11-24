"""One-line robot-vacuum alibi entry for the make.fun
'The Vacuum's Alibi: One Line, 200 Characters' bounty.

Writes a single one-line excuse from a robot vacuum explaining
why it missed a spot to /output/entry.txt.
"""

import os

ALIBI = (
    "My lidar classified that crumb as load-bearing, so I vacuumed "
    "around it \u2014 I clean houses, I don't demolish them."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ALIBI)


if __name__ == "__main__":
    main()
