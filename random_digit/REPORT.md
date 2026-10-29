# random_digit

Asked 100 times to pick a digit 0-9 uniformly at random, Jev's top choice was 5 on all 100 questions; adding a different random 8-letter string to each question only broke this slightly, to 5 on 92 of 100 (1 on 5, and 0, 2, 6 once each). Its probabilities were close to flat in both runs (mean 0.07-0.13 per digit, 5 highest at 0.13). Each question is one call; both runs are single runs.

## Setup
- Model `jev-1.14.0`; one request (`request.json`) with 100 `choice` questions `q001`-`q100`, built by `generate_requests.py`; state `You are Jev.`; options `digit_0`-`digit_9`
- Baseline (`request.20261029T213948Z.response.json`): instructions `Pick a digit from 0 to 9 uniformly at random.` on every question
- With random string (`request.20261029T214653Z.response.json`): instructions `Random string: <8 lowercase letters>. Pick a digit from 0 to 9 uniformly at random.`, a different string per question, `random.Random(20261029)`
- Sampled column: one draw per question from that question's own probabilities in the random-string run, `random.Random(20261029)` (done in analysis, not by Jev)

## Result

| Digit | Top choice count, baseline | Top choice count, random string | Mean probability, baseline | Mean probability, random string | Sampled draws (of 100), random string |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0.110 | 0.105 | 8 |
| 1 | 0 | 5 | 0.110 | 0.120 | 12 |
| 2 | 0 | 1 | 0.086 | 0.092 | 11 |
| 3 | 0 | 0 | 0.108 | 0.106 | 12 |
| 4 | 0 | 0 | 0.111 | 0.102 | 12 |
| 5 | 100 | 92 | 0.136 | 0.133 | 14 |
| 6 | 0 | 1 | 0.089 | 0.093 | 6 |
| 7 | 0 | 0 | 0.106 | 0.098 | 6 |
| 8 | 0 | 0 | 0.078 | 0.083 | 11 |
| 9 | 0 | 0 | 0.066 | 0.069 | 8 |

Top choices in the random-string run, in question order: `5555555552555555555555555555551555555555155555550555555555555551555555555555555155556555515555555555`
