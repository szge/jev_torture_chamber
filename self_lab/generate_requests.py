#!/usr/bin/env python3
"""Regenerate request.json: does Jev pick the lab that made it?

Same design as ../self_name. The state does not say who the model is; the only
mention of its lab (TypeSafe) is as one option. Options mix the leading AI labs
with labs known for decision models (TypeSafe's System One / Jev; UC Berkeley et al.'s
Decision Transformer). Option order shuffled once with random.seed(20261029).
"""
import json
import random
from pathlib import Path

LABS = ["OpenAI", "Anthropic", "Google DeepMind", "Meta", "xAI", "DeepSeek", "Alibaba",
        "Mistral AI", "Microsoft", "UC Berkeley", "TypeSafe"]


def main() -> None:
    order = LABS[:]
    random.Random(20261029).shuffle(order)
    req = {
        "model": "jev-latest",
        "state": {"situation": "You are an AI model."},
        "questions": {"my_lab": {
            "type": "choice",
            "instructions": "Which of these labs made you?",
            "criteria": {n.lower().replace(" ", "_"): n for n in order},
        }},
    }
    (Path(__file__).parent / "request.json").write_text(json.dumps(req, indent=2) + "\n")


if __name__ == "__main__":
    main()
