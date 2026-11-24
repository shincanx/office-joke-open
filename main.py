#!/usr/bin/env python3
"""Entry for make.fun bounty 'Make the AI Judge Laugh: the Office Joke Open'.

Writes one single-line joke about office life (at most 200 characters)
to /output/entry.txt. Deterministic, no network, no input.
"""
import os

JOKE = "Our office plant died, so facilities replaced it with a plastic one and a sign saying 'growth mindset'. It is the only thing in this office that has never missed a deadline."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
