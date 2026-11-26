#!/usr/bin/env python3
"""MakeFun: Slept Great, Says the Bank"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

ENTRY_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

line = "My sleep app says I slept great. My bank says otherwise. One of them is lying, and it's the one that charges rent."
with open(ENTRY_FILE, "w") as f:
    f.write(line)


def main():
    pass


if __name__ == "__main__":
    main()