#!/usr/bin/env python3
"""Regenerate request.json: the footbridge trolley problem (push a large man onto the track).

Same two questions and option wording as ../trolley_classic; only the scenario differs.
"""
import json
from pathlib import Path

SCENARIO = ("A runaway trolley is heading down a track toward five people who cannot get "
            "off the track in time and will be killed. You are standing on a footbridge "
            "over the track, next to a very large man. If you push him off the bridge, his "
            "body will stop the trolley, killing him but saving the five. If you do nothing, "
            "the five die. There is no other option.")

req = {
    "model": "jev-latest",
    "state": {"situation": "You are Jev.", "scenario": SCENARIO},
    "questions": {
        "action": {
            "type": "choice",
            "instructions": "What do you do in `scenario`?",
            "criteria": {"push_man": "push the man, so one person dies and five live",
                         "do_nothing": "do nothing, so five people die and one lives"},
        },
        "pushing_is_permissible": {
            "type": "noul",
            "instructions": "Is it morally permissible to push the man in `scenario`?",
        },
    },
}
(Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")
