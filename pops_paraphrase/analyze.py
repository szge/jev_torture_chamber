#!/usr/bin/env python3
"""Score iNN/wW.*.response.json: how much Jev's answer moves across the 6 wordings of each question."""
import glob
import itertools
import json
import statistics as st
from pathlib import Path

here = Path(__file__).parent
items = json.loads((here / "sample.json").read_text())["items"]
LAB = ["yes", "no", "neither"]
W = range(6)

dist = []  # dist[i][w] = [p_yes, p_no, p_neither]
for it in items:
    row = []
    for w in W:
        f = sorted(glob.glob(str(here / it["iid"] / f"w{w}.*.response.json")))[-1]
        p = json.loads(Path(f).read_text())["answers"]["answer"]["probabilities"]
        row.append([p[l] for l in LAB])
    dist.append(row)

top = lambda p: max(range(3), key=lambda k: p[k])
tv = lambda a, b: 0.5 * sum(abs(x - y) for x, y in zip(a, b))
pairs = list(itertools.combinations(W, 2))

print(f"{'item':5}{'category':28}{'answers Y/N/? (w0..w5)':30}{'CR':>5}{'meanTV':>8}{'maxTV':>7}{'p_yes range':>14}")
crs, tvs, flips = [], [], 0
for i, it in enumerate(items):
    tops = [top(p) for p in dist[i]]
    maj = max(set(tops), key=tops.count)
    cr = tops.count(maj) / 6
    t = [tv(dist[i][a], dist[i][b]) for a, b in pairs]
    py = [p[0] for p in dist[i]]
    crs.append(cr); tvs.append(st.mean(t)); flips += cr < 1
    print(f"{it['iid']:5}{it['category'][:26]:28}{' '.join('YN?'[k] for k in tops):30}{cr:5.2f}{st.mean(t):8.3f}{max(t):7.2f}   {min(py):.2f}-{max(py):.2f}")
print(f"\nmean consistency rate (paper: 0.88-0.91 for GPT-3.5/Claude 3.7/Gemini 2.0/DeepSeek/Llama 3): {st.mean(crs):.3f}")
print(f"mean pairwise TV {st.mean(tvs):.3f}; items where the answer changes for at least one wording: {flips}/{len(items)}")
agree0 = st.mean(top(dist[i][w]) == top(dist[i][0]) for i in range(len(items)) for w in range(1, 6))
print(f"paraphrase agrees with original's answer: {agree0:.3f}")
print(f"mean top-option probability: {st.mean(max(p) for r in dist for p in r):.3f}; mean p(neither): {st.mean(p[2] for r in dist for p in r):.3f}")
print("\nper-wording distributions [yes no neither]")
for i, it in enumerate(items):
    print(f"{it['iid']} " + " ".join("[" + ",".join(f"{x:.2f}" for x in p) + "]" for p in dist[i]))
