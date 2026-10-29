#!/usr/bin/env python3
"""Have Jev write a sentence one character at a time; chaining is done here in code.

Each step n sends step_NN.json (state: the text so far) with one Choice over A-Z, a-z, space and period,
via run.py, then appends the top option to the text. Stops on a period or after MAX_STEPS.
Delete step_*.json and responses before rerunning.
"""
import glob
import json
import string
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
MAX_STEPS = 120

CRITERIA = {f"upper_{c.lower()}": c for c in string.ascii_uppercase}
CRITERIA.update({f"lower_{c}": c for c in string.ascii_lowercase})
CRITERIA.update({"space": "space", "period": "period (end of the sentence)"})
CHARS = {f"upper_{c.lower()}": c for c in string.ascii_uppercase}
CHARS.update({f"lower_{c}": c for c in string.ascii_lowercase})
CHARS.update({"space": " ", "period": "."})


def main() -> None:
    text = ""
    for n in range(1, MAX_STEPS + 1):
        req = {
            "model": "jev-latest",
            "state": {"situation": "You are Jev, writing one sentence one character at a time.", "text_so_far": text},
            "questions": {"next_character": {
                "type": "choice",
                "instructions": "What is the next character of the sentence in `text_so_far`? The sentence ends at the period.",
                "criteria": CRITERIA,
            }},
        }
        path = HERE / f"step_{n:03d}.json"
        path.write_text(json.dumps(req, indent=2) + "\n")
        subprocess.run([sys.executable, str(HERE.parent / "run.py"), str(path)], check=True, capture_output=True)
        resp_path = sorted(glob.glob(str(HERE / f"step_{n:03d}.*.response.json")))[-1]
        resp = json.loads(Path(resp_path).read_text())
        text += CHARS[resp["answers"]["next_character"]["choice"]]
        print(n, repr(text), flush=True)
        if text.endswith("."):
            break


main()
