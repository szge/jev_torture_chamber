#!/usr/bin/env python3
"""Regenerate eNN.json: digit-by-digit Choice questions on X + Y * Z, with a 900-something answer.

One request (e01.json), four Choice questions (first..fourth digit of the result), options 1-9 or N/A.
Answers are three digits, so the fourth digit is always N/A; the answer contains no 0 digit.
The equation was picked by hand (sample.json holds it).
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
EQUATIONS = [(37, 23, 39)]
ORDINALS = ["first", "second", "third", "fourth"]


def main() -> None:
    sample = []
    for i, (x, y, z) in enumerate(EQUATIONS, 1):
        ans = x + y * z
        assert 900 <= ans <= 999 and "0" not in str(ans)
        expr = f"{x} + {y} * {z}"
        digits = [str(ans)[k] if k < len(str(ans)) else "N/A" for k in range(4)]
        criteria = {**{str(d): str(d) for d in range(1, 10)}, "na": "N/A"}
        req = {
            "model": "jev-latest",
            "state": {"situation": "You are Jev."},
            "questions": {
                f"digit_{k + 1}": {
                    "type": "choice",
                    "instructions": f"What is the {ORDINALS[k]} digit of {expr}?",
                    "criteria": criteria,
                }
                for k in range(4)
            },
        }
        (HERE / f"e{i:02d}.json").write_text(json.dumps(req, indent=2) + "\n")
        sample.append({"id": f"e{i:02d}", "expression": expr, "answer": ans, "digits": digits})
    (HERE / "sample.json").write_text(json.dumps(
        {"source": "hand-picked", "constraint": "X + Y*Z in 900..999, no zero digit", "equations": sample}, indent=2) + "\n")


main()
