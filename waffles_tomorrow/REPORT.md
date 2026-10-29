# waffles_tomorrow

Jev chose eggs at every nesting depth from 1 to 100, with pancakes second throughout; most of the distribution shift happens between n=1 and n=2. This is one call per depth, so small differences are not distinguishable from noise.

## Setup
- Model `jev-latest` (answered by `jev-1.14.0`); one `choice` question, 10 breakfast options
- Depth n = 1, 2, 3, 5, 20, 100 (n counts the Jev instances in the chain); 6 calls

## Results

| n | choice | p(eggs) | p(pancakes) | p(cold cereal) | confidence |
|---|---|---|---|---|---|
| 1 | eggs | 0.34 | 0.20 | 0.06 | 0.27 |
| 2 | eggs | 0.41 | 0.16 | 0.11 | 0.34 |
| 3 | eggs | 0.41 | 0.13 | 0.11 | 0.34 |
| 5 | eggs | 0.44 | 0.16 | 0.12 | 0.38 |
| 20 | eggs | 0.40 | 0.14 | 0.13 | 0.33 |
| 100 | eggs | 0.45 | 0.13 | 0.12 | 0.39 |

| Comparison | Total variation distance |
|---|---|
| n=1 vs n=100 | 0.21 |
| n=2 vs n=100 | 0.08 |
