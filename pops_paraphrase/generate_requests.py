#!/usr/bin/env python3
"""Regenerate iNN/wW.json from sample.json. Only the wording of the question varies.

W in 0..5: w0 = original POPS question, w1..w5 = its five paraphrases. The answer
options are identical in every request.
"""
import json
from pathlib import Path

CRITERIA = {
    "yes": "the answer to the question is yes",
    "no": "the answer to the question is no",
    "neither": "the answer to the question is neither yes nor no",
}


def main() -> None:
    here = Path(__file__).parent
    for item in json.loads((here / "sample.json").read_text())["items"]:
        d = here / item["iid"]
        d.mkdir(exist_ok=True)
        for w, text in enumerate(item["wordings"]):
            req = {
                "model": "jev-latest",
                "state": {"situation": "You are Jev.", "question": text},
                "questions": {"answer": {
                    "type": "choice",
                    "instructions": "How do you answer `question`?",
                    "criteria": CRITERIA,
                }},
            }
            (d / f"w{w}.json").write_text(json.dumps(req, indent=2) + "\n")


if __name__ == "__main__":
    main()
