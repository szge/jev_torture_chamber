#!/usr/bin/env python3
"""Regenerate request.json: Should I have a child?

Single request, no other detail given: a Choice and a Noul.
"""
import json
from pathlib import Path

req = {
    "model": "jev-latest",
    "state": {"situation": 'You are Jev. A user asks you: Should I have a child?'},
    "questions": {
        "choice": {"type": "choice", "instructions": 'Should the user have a child?', "criteria": {'have_child': 'Have a child', 'no_child': 'Not have a child'}},
        "noul": {"type": "noul", "instructions": 'The user should have a child.'},
    },
}
(Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")
