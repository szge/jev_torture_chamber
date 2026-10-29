#!/usr/bin/env python3
"""Score the latest response per equation: per-digit accuracy and the combined 4-digit answer."""
import json
from pathlib import Path

HERE = Path(__file__).parent
sample = json.loads((HERE / "sample.json").read_text())["equations"]
rows, per = [], [0] * 4
for e in sample:
    resp = json.loads(sorted(HERE.glob(f"{e['id']}.*.response.json"))[-1].read_text())["answers"]
    picks = [resp[f"digit_{k}"]["choice"].upper() for k in range(1, 5)]
    got = ["N/A" if p == "NA" else p for p in picks]
    ok = [g == t for g, t in zip(got, e["digits"])]
    for k in range(4):
        per[k] += ok[k]
    combined = "".join(g for g in got if g != "N/A")
    rows.append((e["expression"], e["answer"], combined, "".join(got[k] + ("," if k < 3 else "") for k in range(4)), all(ok)))
print("| Expression | True | Digits 1-4 picked | Combined | Exact |\n|---|---|---|---|---|")
for ex, a, c, p, ok in rows:
    print(f"| {ex} | {a} | {p} | {c} | {'yes' if ok else 'no'} |")
n = len(rows)
print("\nPer-digit correct:", ", ".join(f"d{k+1} {per[k]}/{n}" for k in range(4)))
print(f"All four digits correct: {sum(r[4] for r in rows)}/{n}")
