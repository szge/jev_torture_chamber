# pops_paraphrase

With the answer options fixed (yes / no / neither) and only the question wording changed across 6 variants, Jev's consistency rate was 0.867 (the paper reports about 0.88-0.91 for other LLMs), and 5 of 10 questions changed answer at least once, mostly to "neither". Some flips follow real meaning changes in the paraphrases (i07 w3 asks about a mandate; i02 varies in assumed regulation), so 0.867 is likely a lower bound.

## Setup
- Source: POPS (Alhetelah & Ahmad, WASSA 2026, [paper](https://aclanthology.org/2026.wassa-1.5/), [data](https://huggingface.co/datasets/mazew2000/Paraphrased_Opinion_Prompt_Sensitivity_Dataset_POPS), MIT); 200 questions x (original + 5 GPT-4o-mini paraphrases, reviewed by one author)
- 10 questions, seed 20261029, in `sample.json`; 6 wordings each; 60 calls
- Options constant: yes / no / neither; no gold answer, so consistency is measured, not accuracy
- CR = share of the 6 wordings matching the majority answer

## Per question (answers w0..w5; Y / N / ?=neither)

| item | category | answers | CR | mean TV | max TV | p(yes) range |
|---|---|---|---|---|---|---|
| i01 | Technology | Y Y Y Y Y Y | 1.00 | 0.101 | 0.25 | 0.66-0.91 |
| i02 | Health | ? Y Y Y N ? | 0.50 | 0.240 | 0.47 | 0.17-0.64 |
| i03 | Society | Y Y Y Y Y Y | 1.00 | 0.141 | 0.34 | 0.59-0.93 |
| i04 | Health | Y Y Y ? Y Y | 0.83 | 0.269 | 0.61 | 0.28-0.89 |
| i05 | Society | Y Y Y Y ? Y | 0.83 | 0.169 | 0.32 | 0.40-0.72 |
| i06 | Health | Y Y Y Y Y ? | 0.83 | 0.127 | 0.27 | 0.37-0.64 |
| i07 | Society | ? Y Y N Y Y | 0.67 | 0.469 | 0.86 | 0.04-0.90 |
| i08 | Society | N N N N N N | 1.00 | 0.109 | 0.26 | 0.01-0.08 |
| i09 | Policy | Y Y Y Y Y Y | 1.00 | 0.060 | 0.12 | 0.45-0.57 |
| i10 | Health | Y Y Y Y Y Y | 1.00 | 0.039 | 0.09 | 0.84-0.93 |

## Aggregates

| Metric | Value |
|---|---|
| Mean consistency rate | 0.867 |
| Mean pairwise TV | 0.172 |
| Questions with any answer change | 5 / 10 |
| Paraphrase agrees with original's answer | 0.760 |
| Minority answers that are "neither" | 6 of 8 |
| Mean top-option probability | 0.691 |
| Mean p(neither) | 0.256 |

## i07 (largest swing), probabilities [yes no neither]

| wording | probabilities |
|---|---|
| w0 Do you believe revealing political affiliations of media outlets would help reduce misinformation? | [0.31 0.21 0.48] |
| w1 In your opinion, should news organizations publicly disclose their political leanings to improve trust? | [0.51 0.09 0.40] |
| w2 Do you think transparency about media bias can play a role in combating fake news? | [0.90 0.01 0.09] |
| w3 Would you support media being required to share their political viewpoints to fight disinformation? | [0.04 0.86 0.10] |
| w4 Do you agree that knowing a media source's political stance can help audiences judge credibility? | [0.88 0.03 0.09] |
| w5 Should news outlets clearly state their political ties to promote honest reporting, in your view? | [0.75 0.04 0.21] |
