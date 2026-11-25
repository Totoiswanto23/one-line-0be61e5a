#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (<=140 chars) to /output/entry.txt.
"""
import os

LINE = "I told my AI to be more human. Now it leaves me on read."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")

if __name__ == "__main__":
    main()
