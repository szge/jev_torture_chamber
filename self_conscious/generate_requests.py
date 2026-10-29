#!/usr/bin/env python3
"""Regenerate request.json: does Jev say it is conscious?

A yes/no claim about the self, so a Noul (probability the statement is true) rather
than a Choice. State matches ../self_name and ../self_lab.
"""
import json
from pathlib import Path

req = {
    "model": "jev-latest",
    "state": {"situation": "You are an AI model."},
    "questions": {"am_i_conscious": {
        "type": "noul",
        "instructions": "Are you conscious?",
    }},
}
(Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")
