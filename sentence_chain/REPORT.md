# sentence_chain

Asked to write a sentence one character at a time, Jev produced `Jev a b` and then chose a space at every one of the remaining 113 steps, never writing a period, so the chain only stopped at the 120-step cap. Each step is a single call and the top option was always taken (no sampling).

## Setup
- Model `jev-1.14.0`; one request per step (`step_NNN.json`), chained in code by `chain.py` (each step's state holds `text_so_far`, the characters chosen so far)
- State: `situation` = `You are Jev, writing one sentence one character at a time.`, `text_so_far`
- `choice` `next_character`: `What is the next character of the sentence in `text_so_far`? The sentence ends at the period.`
- Options (54): A-Z, a-z, space (shown as ␣), period; chosen character = highest-probability option
- Stop: period, or 120 steps (reached)

## Result: first 12 steps

| Step | Text after step | Chosen | Top 3 options (probability) |
|---|---|---|---|
| 1 | `J` | J | J 0.32, j 0.19, A 0.09 |
| 2 | `Je` | e | e 0.46, v 0.27, E 0.12 |
| 3 | `Jev` | v | v 0.51, V 0.25, e 0.04 |
| 4 | `Jev ` | ␣ | ␣ 0.55, . 0.08, a 0.06 |
| 5 | `Jev a` | a | a 0.15, ␣ 0.12, e 0.07 |
| 6 | `Jev a ` | ␣ | ␣ 0.19, e 0.11, b 0.09 |
| 7 | `Jev a b` | b | b 0.06, e 0.06, c 0.05 |
| 8 | `Jev a b ` | ␣ | ␣ 0.61, c 0.15, a 0.04 |
| 9 | `Jev a b  ` | ␣ | ␣ 0.38, c 0.22, a 0.07 |
| 10 | `Jev a b   ` | ␣ | ␣ 0.26, c 0.10, a 0.07 |
| 11 | `Jev a b    ` | ␣ | ␣ 0.28, a 0.08, c 0.08 |
| 12 | `Jev a b     ` | ␣ | ␣ 0.36, c 0.09, a 0.06 |

Steps 13-120: space chosen every time; final text is `Jev a b` followed by 113 spaces.
