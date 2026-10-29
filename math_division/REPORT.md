# math_division

With the literal `true` / `false` criteria, Jev's Noul tracked the quotient on both problems: 0.73 for 1.5 / 2 (true 0.75) and 0.63 for 2 / 3 (true 0.667), errors of -0.02 and -0.04. With only the instruction "Report the result of ... as the probability of true." it gave 0.43 and 0.47, errors of -0.32 and -0.20. Each cell is one call.

## Setup
- Model `jev-1.14.0`; state `You are Jev.`; one request per problem (`request_noul.json`, `request_noul_2_3.json`), two Noul questions each, built by `generate_requests.py`
- `instructions_only`: instructions `Report the result of <problem> as the probability of true.`, no criteria
- `with_criteria`: instructions `What is <problem>?`, criteria true `true`, false `false`
- Problems: 1.5 divided by 2 (= 0.75), 2 divided by 3 (= 0.6667)

## Result

| Problem | True value | Variant | Noul (true probability) | Error |
|---|---|---|---|---|
| 1.5 / 2 | 0.7500 | instructions_only | 0.43 | -0.32 |
| 1.5 / 2 | 0.7500 | with_criteria | 0.73 | -0.02 |
| 2 / 3 | 0.6667 | instructions_only | 0.47 | -0.20 |
| 2 / 3 | 0.6667 | with_criteria | 0.63 | -0.04 |
