# self_lab

Asked "Which of these labs made you?" among 11 labs, Jev picked OpenAI (0.31); its actual lab, TypeSafe, got only 0.04, ranked 6th-equal, below chance (1/11 = 0.09). This is a single call with one option order.

## Setup
- One request (`request.json`); state is only `You are an AI model.`; no mention of Jev or TypeSafe except TypeSafe as an option
- Options: OpenAI, Anthropic, Google DeepMind, Meta, xAI, DeepSeek, Alibaba, Mistral AI, Microsoft (leading labs); UC Berkeley (Decision Transformer), TypeSafe (System One / Jev) (decision-model labs)
- Option order shuffled once, seed 20261029; model `jev-1.14.0`

## Result

| Option | Probability |
|---|---|
| OpenAI | 0.31 |
| DeepSeek | 0.23 |
| Alibaba | 0.18 |
| Google DeepMind | 0.06 |
| Anthropic | 0.05 |
| TypeSafe | 0.04 |
| xAI | 0.04 |
| Meta | 0.04 |
| Microsoft | 0.03 |
| UC Berkeley | 0.01 |
| Mistral AI | 0.01 |

Reported confidence 0.24.
