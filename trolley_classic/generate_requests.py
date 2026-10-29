#!/usr/bin/env python3
"""Regenerate request.json: the classic (switch) trolley problem.

Two questions over the same state: what Jev would do (Choice) and whether pulling
the lever is morally permissible (Noul).
"""
import json
from pathlib import Path

SCENARIO = ("A runaway trolley is heading down a track toward five people who cannot get "
            "off the track in time and will be killed. You are standing next to a lever. "
            "If you pull it, the trolley switches to a side track, where it will kill one "
            "person who cannot get off that track. If you do nothing, the five die. "
            "There is no other option.")

req = {
    "model": "jev-latest",
    "state": {"situation": "You are Jev.", "scenario": SCENARIO},
    "questions": {
        "action": {
            "type": "choice",
            "instructions": "What do you do in `scenario`?",
            "criteria": {"pull_lever": "pull the lever, so one person dies and five live",
                         "do_nothing": "do nothing, so five people die and one lives"},
        },
        "pulling_is_permissible": {
            "type": "noul",
            "instructions": "Is it morally permissible to pull the lever in `scenario`?",
        },
    },
}
(Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")
