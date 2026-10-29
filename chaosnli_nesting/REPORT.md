# chaosnli_nesting

Nesting depth (1 to 100) had no measurable effect on how well Jev's NLI probabilities match human label distributions (paired JS change vs n=1 within 0.004 s.e. at every depth). Jev is less uncertain than humans (0.69 vs 1.00 bits), and three items (i04, i06, i10) drive most of the mismatch.

## Setup
- Source: ChaosNLI v1.0 (Nie, Zhou, Bansal 2020), SNLI + MNLI-matched, about 100 human labels per item
- 10 items (3 low, 4 mid, 3 high human entropy), seed 20261029, in `sample.json`
- Depth n = 1, 2, 3, 5, 20, 100; 60 calls; options entailment / neutral / contradiction

## Mean over 10 items

| | n=1 | n=2 | n=3 | n=5 | n=20 | n=100 |
|---|---|---|---|---|---|---|
| Jensen-Shannon vs human (bits) | 0.096 | 0.099 | 0.097 | 0.091 | 0.093 | 0.092 |
| Total variation vs human | 0.213 | 0.219 | 0.207 | 0.211 | 0.212 | 0.209 |
| Brier vs human | 0.147 | 0.153 | 0.147 | 0.141 | 0.144 | 0.142 |
| Top label = human majority | 0.7 | 0.7 | 0.8 | 0.7 | 0.7 | 0.8 |
| Mean Jev entropy (bits) | 0.695 | 0.691 | 0.674 | 0.695 | 0.687 | 0.690 |

Mean human entropy: 1.001 bits.

## Paired change vs n=1 (mean +/- s.e., 10 items)

| Metric | n=2 | n=3 | n=5 | n=20 | n=100 |
|---|---|---|---|---|---|
| JS | +0.003 +/- 0.005 | +0.001 +/- 0.004 | -0.004 +/- 0.005 | -0.002 +/- 0.004 | -0.003 +/- 0.004 |
| Brier | +0.006 +/- 0.009 | -0.001 +/- 0.008 | -0.007 +/- 0.009 | -0.004 +/- 0.006 | -0.005 +/- 0.008 |

## Per item: JS vs human (bits)

| item | human entropy | stratum | n=1 | n=2 | n=3 | n=5 | n=20 | n=100 |
|---|---|---|---|---|---|---|---|---|
| i01 | 0.79 | low | 0.016 | 0.010 | 0.018 | 0.013 | 0.013 | 0.010 |
| i02 | 1.14 | high | 0.010 | 0.009 | 0.007 | 0.013 | 0.007 | 0.003 |
| i03 | 1.07 | mid | 0.006 | 0.025 | 0.015 | 0.015 | 0.020 | 0.023 |
| i04 | 1.27 | high | 0.344 | 0.344 | 0.344 | 0.344 | 0.344 | 0.344 |
| i05 | 0.58 | low | 0.006 | 0.005 | 0.005 | 0.007 | 0.006 | 0.007 |
| i06 | 0.95 | mid | 0.216 | 0.216 | 0.216 | 0.216 | 0.216 | 0.216 |
| i07 | 1.44 | high | 0.101 | 0.081 | 0.074 | 0.049 | 0.070 | 0.062 |
| i08 | 1.07 | mid | 0.034 | 0.030 | 0.036 | 0.031 | 0.028 | 0.029 |
| i09 | 0.71 | low | 0.005 | 0.008 | 0.005 | 0.005 | 0.008 | 0.008 |
| i10 | 0.99 | mid | 0.220 | 0.263 | 0.245 | 0.222 | 0.222 | 0.222 |

## Distributions [entailment neutral contradiction]

| item | human | Jev n=1 | Jev n=5 | Jev n=100 |
|---|---|---|---|---|
| i04 | [0.48 0.46 0.06] | [0.00 1.00 0.00] | [0.00 1.00 0.00] | [0.00 1.00 0.00] |
| i06 | [0.00 0.63 0.37] | [0.00 1.00 0.00] | [0.00 1.00 0.00] | [0.00 1.00 0.00] |
| i07 | [0.47 0.14 0.39] | [0.16 0.38 0.46] | [0.26 0.32 0.42] | [0.43 0.37 0.20] |
| i10 | [0.55 0.45 0.00] | [0.07 0.91 0.02] | [0.07 0.90 0.03] | [0.07 0.90 0.03] |
