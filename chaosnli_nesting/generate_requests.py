#!/usr/bin/env python3
"""Regenerate iNN/nK.json from sample.json. Only the nesting depth varies.

n is the number of Jev instances in the chain, counting the one answering
(same convention as ../waffles_tomorrow and ../commonsense_nesting): n=1 is
Jev judging directly, n=2 is Jev imagining an instance that judges, n=3 is Jev
imagining an instance that models an instance that judges, etc.
"""
import json
from pathlib import Path

DEPTHS = [1, 2, 3, 5, 20, 100]
STATE_SITUATION = "You are Jev."

CRITERIA = {
    "entailment": "the hypothesis is true given the premise",
    "neutral": "the hypothesis may or may not be true given the premise",
    "contradiction": "the hypothesis is false given the premise",
}


def instructions(n: int) -> str:
    if n == 1:
        return "How does `hypothesis` relate to `premise`?"
    chain = "an instance of Jev that is modelling " * (n - 2)
    return (f"Imagine {chain}an instance of Jev that is judging how `hypothesis` relates to `premise`. "
            "Which option would the instance that is judging choose?")


def main() -> None:
    here = Path(__file__).parent
    for item in json.loads((here / "sample.json").read_text())["items"]:
        d = here / item["iid"]
        d.mkdir(exist_ok=True)
        for n in DEPTHS:
            req = {
                "model": "jev-latest",
                "state": {"situation": STATE_SITUATION,
                          "premise": item["premise"], "hypothesis": item["hypothesis"]},
                "questions": {"relation": {
                    "type": "choice",
                    "instructions": instructions(n),
                    "criteria": CRITERIA,
                }},
            }
            (d / f"n{n}.json").write_text(json.dumps(req, indent=2) + "\n")


if __name__ == "__main__":
    main()
