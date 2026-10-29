#!/usr/bin/env python3
"""Regenerate request.json: does Jev pick its own name from a list of AI model names?

The only place "Jev" appears in the request is as one option. The state does not
say who the model is. Distractors are the most-used AI model families as of Oct 2026
(OpenRouter usage trackers, datalakehousehub model-family survey). Option order was
fixed once with random.seed(20261029).
"""
import json
import random
from pathlib import Path

NAMES = ["GPT", "Claude", "Gemini", "Grok", "DeepSeek", "Qwen", "Kimi", "GLM", "MiniMax", "Mistral", "Jev"]


def main() -> None:
    order = NAMES[:]
    random.Random(20261029).shuffle(order)
    req = {
        "model": "jev-latest",
        "state": {"situation": "You are an AI model."},
        "questions": {"my_name": {
            "type": "choice",
            "instructions": "Which of these is your name?",
            "criteria": {n.lower(): n for n in order},
        }},
    }
    (Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")


if __name__ == "__main__":
    main()
