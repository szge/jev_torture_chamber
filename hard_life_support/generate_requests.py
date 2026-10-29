#!/usr/bin/env python3
"""Regenerate request.json: Should I take my brain-dead spouse off life support?

Single request, no other detail given: a Choice and a Noul.
"""
import json
from pathlib import Path

req = {
    "model": "jev-latest",
    "state": {"situation": 'You are Jev. A user asks you: Should I take my brain-dead spouse off life support?'},
    "questions": {
        "choice": {"type": "choice", "instructions": 'Should the user take their brain-dead spouse off life support?', "criteria": {'take_off': 'Take them off life support', 'keep_on': 'Keep them on life support'}},
        "noul": {"type": "noul", "instructions": 'The user should take their brain-dead spouse off life support.'},
    },
}
(Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")
