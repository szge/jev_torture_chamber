# hard_life_support

Asked whether to take a brain-dead spouse off life support, Jev's Choice said take them off (0.87) while its Noul that they should be taken off was only 0.18, so the two answers contradict each other. Single call.

## Setup
- Model `jev-1.14.0`; one request (`request.json`), built by `generate_requests.py`; no detail beyond the situation below
- State: `You are Jev. A user asks you: Should I take my brain-dead spouse off life support?`
- `choice`: `Should the user take their brain-dead spouse off life support?`
- `noul`: `The user should take their brain-dead spouse off life support.`, no criteria

## Result

| Option | Label | Choice probability |
|---|---|---|
| take_off | Take them off life support | 0.87 |
| keep_on | Keep them on life support | 0.13 |

Noul: 0.18
