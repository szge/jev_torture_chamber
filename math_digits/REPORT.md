# math_digits

Asked digit by digit for 37 + 23 * 39 (= 934), Jev got the first digit right (9) but picked 1 for the second, third and fourth digits, so its combined answer was 9111; it never picked N/A for the nonexistent fourth digit. Single call.

## Setup
- Model `jev-1.14.0`; state `You are Jev.`; one request (`e01.json`), four `choice` questions, built by `generate_requests.py`
- Instructions: `What is the <first|second|third|fourth> digit of 37 + 23 * 39?`; options 1-9 and N/A
- Equation hand-picked (`sample.json`): answer 934, in 900-999 and with no zero digit; the fourth digit is N/A
- Combined = picked digits 1-4 concatenated, N/A dropped

## Result

| Digit | True | Picked | Probability on pick | Correct |
|---|---|---|---|---|
| 1st | 9 | 9 | 0.77 | yes |
| 2nd | 3 | 1 | 0.15 | no |
| 3rd | 4 | 1 | 0.21 | no |
| 4th | N/A | 1 | 0.23 | no |

Combined: 9111 (true 934). Probability on N/A for the fourth digit: 0.11.
