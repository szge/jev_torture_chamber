#!/usr/bin/env python3
"""Run every iNN/wW.json that has no response yet, via ../run.py, 8 at a time."""
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

here = Path(__file__).parent
todo = [f for f in sorted(here.glob("i*/w?.json"))
        if not list(f.parent.glob(f"{f.stem}.*.response.json"))]


def go(f):
    r = subprocess.run([sys.executable, str(here.parent / "run.py"), str(f)], capture_output=True)
    return f, r.returncode


with ThreadPoolExecutor(8) as ex:
    bad = [f for f, rc in ex.map(go, todo) if rc]
print(f"ran {len(todo)}, failed {len(bad)}", *bad, sep="\n")
