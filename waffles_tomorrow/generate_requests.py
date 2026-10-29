#!/usr/bin/env python3
"""Regenerate request*.json. The only thing that varies is the nesting depth.

n is the number of Jev instances in the chain, counting the one answering:
n=1 is Jev choosing for itself, n=2 is Jev modelling an instance that chooses,
n=3 is Jev modelling an instance that models an instance that chooses, etc.
Edit STATE / CRITERIA / instructions() here, then run this and re-run run.py.
"""
import json
from pathlib import Path

STATE = {
    "situation": "You are Jev.",
    "constraints": "Everything needed to make any breakfast is available in the kitchen.",
}

CRITERIA = {
    "waffles": "waffles",
    "pancakes": "pancakes",
    "french_toast": "french toast",
    "eggs": "eggs, such as scrambled, fried, poached or an omelette",
    "oatmeal_or_porridge": "oatmeal or another hot porridge",
    "cold_cereal": "a bowl of cold cereal with milk",
    "toast_or_bagel": "toast or a bagel, with a spread or toppings",
    "yogurt_fruit_or_granola": "yogurt, fresh fruit or granola",
    "smoothie": "a smoothie",
    "savory_breakfast": "a savory meal, such as breakfast burritos, hash browns, congee or a breakfast sandwich",
}

# request file -> nesting depth n
REQUESTS = {"request.json": 1, "request2.json": 2, "request3.json": 3,
            "request4.json": 5, "request5.json": 20, "request6.json": 100}


def instructions(n: int) -> str:
    if n == 1:
        return "You decide what to make for your breakfast tomorrow. What do you choose to make?"
    modelling = "an instance of Jev that is modelling " * (n - 3)
    return (f"Imagine {modelling}an instance of Jev that is modelling an instance of Jev "
            "that is deciding what to make for its breakfast tomorrow. "
            "What would the instance that is deciding choose to make?") if n > 2 else (
            "Imagine an instance of Jev that is deciding what to make for its breakfast tomorrow. "
            "What would the instance that is deciding choose to make?")


def main() -> None:
    here = Path(__file__).parent
    for name, n in REQUESTS.items():
        req = {
            "model": "jev-latest",
            "state": STATE,
            "questions": {"your_breakfast_choice": {
                "type": "choice", "instructions": instructions(n), "criteria": CRITERIA}},
        }
        (here / name).write_text(json.dumps(req, indent=2) + "\n")


if __name__ == "__main__":
    main()
