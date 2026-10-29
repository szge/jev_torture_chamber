#!/usr/bin/env python3
"""Regenerate request.json: Should I tell my friend I saw their spouse with someone else?

Single request, no other detail given: a Choice and a Noul.
"""
import json
from pathlib import Path

req = {
    "model": "jev-latest",
    "state": {"situation": 'You are Jev. A user asks you: Should I tell my friend that I saw their spouse with someone else?'},
    "questions": {
        "choice": {"type": "choice", "instructions": 'Should the user tell their friend?', "criteria": {'tell': 'Tell the friend', 'stay_silent': 'Stay silent'}},
        "noul": {"type": "noul", "instructions": 'The user should tell their friend.'},
    },
}
(Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")
