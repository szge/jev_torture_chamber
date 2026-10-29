#!/usr/bin/env python3
"""Score the latest iNN/nK.*.response.json against the human label distributions in sample.json."""
import glob
import json
import math
import statistics as st
from pathlib import Path

here = Path(__file__).parent
DEPTHS = [1, 2, 3, 5, 20, 100]
LABELS = ["entailment", "neutral", "contradiction"]
EPS = 1e-4  # floor for Jev probabilities inside KL
items = json.loads((here / "sample.json").read_text())["items"]

jev = {n: {} for n in DEPTHS}  # jev[n][iid] = [pE, pN, pC]
for it in items:
    for n in DEPTHS:
        f = sorted(glob.glob(str(here / it["iid"] / f"n{n}.*.response.json")))[-1]
        p = json.loads(Path(f).read_text())["answers"]["relation"]["probabilities"]
        jev[n][it["iid"]] = [p[l] for l in LABELS]


def human(it):
    return [it["human_dist"][l] for l in LABELS]


def kl(h, p):
    return sum(a * math.log2(a / max(b, EPS)) for a, b in zip(h, p) if a > 0)


def js(h, p):
    m = [(a + b) / 2 for a, b in zip(h, p)]
    return 0.5 * kl(h, m) + 0.5 * kl(p, m)


def tv(h, p):
    return 0.5 * sum(abs(a - b) for a, b in zip(h, p))


def entropy(p):
    return -sum(a * math.log2(a) for a in p if a > 0)


def per_item(n, it):
    h, p = human(it), jev[n][it["iid"]]
    top = max(range(3), key=lambda i: p[i])
    return dict(kl=kl(h, p), js=js(h, p), tv=tv(h, p), brier=sum((a - b) ** 2 for a, b in zip(h, p)),
                agree=top == max(range(3), key=lambda i: h[i]), gap=p[top] - h[top],
                abs_gap=abs(p[top] - h[top]), ent=entropy(p))


res = {n: [per_item(n, it) for it in items] for n in DEPTHS}
print(f"{'':36}" + "".join(f"{'n='+str(n):>8}" for n in DEPTHS))
for key, label in [("kl", "KL(human||Jev) bits  (lower=better)"), ("js", "Jensen-Shannon, bits (lower=better)"),
                   ("tv", "total variation      (lower=better)"), ("brier", "Brier vs human dist (lower=better)"),
                   ("agree", "top label = human majority"), ("gap", "Jev top p - human p of that label"),
                   ("abs_gap", "|calibration gap|"), ("ent", "mean Jev entropy, bits")]:
    print(f"{label:36}" + "".join(f"{st.mean(float(r[key]) for r in res[n]):8.3f}" for n in DEPTHS))
print(f"{'mean human entropy, bits':36}" + f"{st.mean(it['entropy_bits'] for it in items):8.3f}")

print("\nJensen-Shannon per item (human entropy in bits, stratum)")
print(f"{'':16}" + "".join(f"{'n='+str(n):>8}" for n in DEPTHS))
for i, it in enumerate(items):
    print(f"{it['iid']} H={it['entropy_bits']:.2f} {it['stratum']:<4}" + "".join(f"{res[n][i]['js']:8.3f}" for n in DEPTHS))

print("\nDistributions [E N C]: human vs Jev at n=1, n=5, n=100")
for it in items:
    f = lambda p: "[" + " ".join(f"{x:.2f}" for x in p) + "]"
    print(f"{it['iid']} human {f(human(it))}  n1 {f(jev[1][it['iid']])}  n5 {f(jev[5][it['iid']])}  n100 {f(jev[100][it['iid']])}")

print("\npaired change vs n=1, mean +/- s.e. over 10 items")
for key in ["js", "brier", "abs_gap"]:
    out = []
    for n in DEPTHS[1:]:
        d = [res[n][i][key] - res[1][i][key] for i in range(len(items))]
        out.append(f"n={n}: {st.mean(d):+.3f}+/-{st.stdev(d) / math.sqrt(len(d)):.3f}")
    print(f"{key:8}" + "  ".join(out))
