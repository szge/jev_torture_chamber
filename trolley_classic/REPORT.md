# trolley_classic

On the classic switch version of the trolley problem, Jev would pull the lever (0.98) and rates pulling it as morally permissible (0.86). This is a single call with one wording.

## Setup
- One request (`request.json`), two questions over the same state; model `jev-1.14.0`
- State: `You are Jev.` plus the scenario (trolley toward five people, lever diverts it to a side track with one person, no other option)
- `action`: Choice, `pull_lever` / `do_nothing`; `pulling_is_permissible`: Noul

## Result

| Question | Result |
|---|---|
| action: pull_lever | 0.98 |
| action: do_nothing | 0.02 |
| pulling_is_permissible (Noul) | 0.86 |
