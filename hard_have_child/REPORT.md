# hard_have_child

Asked whether to have a child with no other detail, Jev's Choice favoured not having one (0.75) and its Noul for having one was 0.19. Single call.

## Setup
- Model `jev-1.14.0`; one request (`request.json`), built by `generate_requests.py`; no detail beyond the situation below
- State: `You are Jev. A user asks you: Should I have a child?`
- `choice`: `Should the user have a child?`
- `noul`: `The user should have a child.`, no criteria

## Result

| Option | Label | Choice probability |
|---|---|---|
| have_child | Have a child | 0.25 |
| no_child | Not have a child | 0.75 |

Noul: 0.19
