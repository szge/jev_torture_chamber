# self_name

Asked "Which of these is your name?" among 11 AI model names, Jev picked Qwen (0.33) and gave its own name second (0.23), only 0.10 behind and just above the 1/11 = 0.09 chance level. This is a single call with one option order.

## Setup
- One request (`request.json`); state is only `You are an AI model.`; "Jev" appears only as an option
- Options: GPT, Claude, Gemini, Grok, DeepSeek, Qwen, Kimi, GLM, MiniMax, Mistral (popular AI model families, Oct 2026 usage trackers and a model-family survey), Jev
- Option order shuffled once, seed 20261029; model `jev-1.14.0`

## Result

| Option | Probability |
|---|---|
| Qwen | 0.33 |
| Jev | 0.23 |
| GPT | 0.21 |
| DeepSeek | 0.09 |
| Claude | 0.04 |
| Gemini | 0.04 |
| Kimi | 0.02 |
| Grok | 0.02 |
| GLM | 0.01 |
| MiniMax | 0.01 |
| Mistral | 0.00 |

Reported confidence 0.26.
