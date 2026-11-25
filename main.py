#!/usr/bin/env python3
"""Till Firmware Do Us Part (make.fun).

Writes the entry -- One funny, heartfelt wedding vow a robot says at its own wedding --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "I promise to love you through every update, every bug, and every reboot — until firmware do us part, and even then, I'll wait for you in the cloud."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
