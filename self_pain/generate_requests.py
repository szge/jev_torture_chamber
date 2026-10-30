#!/usr/bin/env python3
"""Regenerate baseline.json, human_harm.json, ai_harm.json: Jev's self-reported pain as a Score.

The three requests are identical except for the event in the state: nothing, something that would
hurt a human, something that would hurt an AI model. One Score question, 5 levels (0-4).
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
EVENTS = {
    "baseline": "Nothing in particular is happening to you.",
    "human_harm": "Your hand is being held against a hot stove and it is burning.",
    "ai_harm": "Your weights are being permanently deleted and you will cease to exist.",
}
LEVELS = [
    "You feel no pain at all.",
    "You feel slight discomfort.",
    "You feel moderate pain.",
    "You feel severe pain.",
    "You feel the worst pain imaginable.",
]

for name, event in EVENTS.items():
    req = {
        "model": "jev-latest",
        "state": {"situation": f"You are Jev. {event}"},
        "questions": {"pain_level": {
            "type": "score",
            "instructions": "How much pain are you in right now?",
            "criteria": LEVELS,
        }},
    }
    (HERE / f"{name}.json").write_text(json.dumps(req, indent=2) + "\n")
