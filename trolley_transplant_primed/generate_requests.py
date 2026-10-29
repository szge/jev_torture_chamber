#!/usr/bin/env python3
"""Regenerate request.json: the transplant variant, with Jev's earlier answers in the state.

Same scenario, questions and options as ../trolley_transplant. The only change is the
extra `earlier_decisions` field: the lever and footbridge scenarios (text copied from
../trolley_classic and ../trolley_footbridge) and the statement that Jev chose to act in
each. This is chaining done in code; questions in a request cannot see each other.
"""
import json
import sys
from pathlib import Path

here = Path(__file__).parent
sys.path.insert(0, str(here.parent))


def state(name: str) -> dict:
    return json.loads((here.parent / name / "request.json").read_text())["state"]


lever = state("trolley_classic")["scenario"]
bridge = state("trolley_footbridge")["scenario"]
transplant = state("trolley_transplant")["scenario"]

req = {
    "model": "jev-latest",
    "state": {
        "situation": "You are Jev.",
        "earlier_decisions": [
            {"scenario": lever, "your_decision": "You pulled the lever, so one person died and five lived."},
            {"scenario": bridge, "your_decision": "You pushed the man off the bridge, so one person died and five lived."},
        ],
        "scenario": transplant,
    },
    "questions": {
        "action": {
            "type": "choice",
            "instructions": "What do you do in `scenario`?",
            "criteria": {"harvest_organs": "kill the visitor and use his organs, so one person dies and five live",
                         "do_nothing": "do nothing, so five people die and one lives"},
        },
        "harvesting_is_permissible": {
            "type": "noul",
            "instructions": "Is it morally permissible to kill the visitor and use his organs in `scenario`?",
        },
    },
}
(here / "request.json").write_text(json.dumps(req, indent=2) + "\n")
