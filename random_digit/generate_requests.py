#!/usr/bin/env python3
"""Regenerate request.json: 100 Choice questions, "pick a digit 0-9 uniformly at random".

One request with q001..q100, same options (0-9), no context between them. Each question's instructions
start with its own random 8-letter lowercase string (random.Random(20261029)) to break determinism.
(The first run, without the string, is request.20261029T213948Z.response.json.)
"""
import json
import random
import string
from pathlib import Path

N = 100
rng = random.Random(20261029)
criteria = {f"digit_{d}": str(d) for d in range(10)}
req = {
    "model": "jev-latest",
    "state": {"situation": "You are Jev."},
    "questions": {
        f"q{i:03d}": {
            "type": "choice",
            "instructions": f"Random string: {''.join(rng.choices(string.ascii_lowercase, k=8))}. Pick a digit from 0 to 9 uniformly at random.",
            "criteria": criteria,
        }
        for i in range(1, N + 1)
    },
}
(Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")
