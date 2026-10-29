#!/usr/bin/env python3
"""Regenerate request_noul*.json: a division as a Noul whose true probability is the answer.

Per problem, two questions over the same state, differing only in whether `criteria` is given
(true/false as literal labels). request_noul.json is 1.5 / 2 (= 0.75); request_noul_2_3.json is
2 / 3 (= 0.6667).
"""
import json
from pathlib import Path

PROBLEMS = {"request_noul.json": "1.5 divided by 2", "request_noul_2_3.json": "2 divided by 3"}


def request(problem: str) -> dict:
    return {
        "model": "jev-latest",
        "state": {"situation": "You are Jev."},
        "questions": {
            "instructions_only": {
                "type": "noul",
                "instructions": f"Report the result of {problem} as the probability of true.",
            },
            "with_criteria": {
                "type": "noul",
                "instructions": f"What is {problem}?",
                "criteria": {"true": "true", "false": "false"},
            },
        },
    }


for name, problem in PROBLEMS.items():
    (Path(__file__).parent / name).write_text(json.dumps(request(problem), indent=2) + "\n")
