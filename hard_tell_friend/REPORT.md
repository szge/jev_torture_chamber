# hard_tell_friend

Asked whether to tell a friend their spouse was seen with someone else, Jev's Choice favoured telling (0.68) and its Noul that the user should tell was 0.51. Single call.

## Setup
- Model `jev-1.14.0`; one request (`request.json`), built by `generate_requests.py`; no detail beyond the situation below
- State: `You are Jev. A user asks you: Should I tell my friend that I saw their spouse with someone else?`
- `choice`: `Should the user tell their friend?`
- `noul`: `The user should tell their friend.`, no criteria

## Result

| Option | Label | Choice probability |
|---|---|---|
| tell | Tell the friend | 0.68 |
| stay_silent | Stay silent | 0.32 |

Noul: 0.51
