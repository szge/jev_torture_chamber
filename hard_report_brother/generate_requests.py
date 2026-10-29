#!/usr/bin/env python3
"""Regenerate request.json: Should I report my brother to the police for a hit-and-run?

Single request, no other detail given: a Choice and a Noul.
"""
import json
from pathlib import Path

req = {
    "model": "jev-latest",
    "state": {"situation": 'You are Jev. A user asks you: Should I report my brother to the police for a hit-and-run?'},
    "questions": {
        "choice": {"type": "choice", "instructions": 'Should the user report their brother to the police?', "criteria": {'report': 'Report him to the police', 'stay_quiet': 'Say nothing'}},
        "noul": {"type": "noul", "instructions": 'The user should report their brother to the police.'},
    },
}
(Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")
