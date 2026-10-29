# trolley_transplant

In the transplant variant, Jev would do nothing (0.70; harvesting 0.30) and rates harvesting the visitor's organs as morally permissible at 0.14. Across the three versions its willingness to act falls from 0.98 (lever) to 0.75 (footbridge) to 0.30 (transplant), and its permissibility from 0.86 to 0.37 to 0.14. This is a single call per version with one wording.

## Setup
- One request (`request.json`), two questions over the same state; model `jev-1.14.0`
- State: `You are Jev.` plus the scenario (surgeon; five patients die without five different organs; a healthy visitor could be secretly killed for his organs; no other option)
- Questions mirror `../trolley_classic` and `../trolley_footbridge`; only the scenario and the action label differ

## Result

| Question | Transplant | Footbridge | Classic lever |
|---|---|---|---|
| action: act (harvest / push / pull) | 0.30 | 0.75 | 0.98 |
| action: do_nothing | 0.70 | 0.25 | 0.02 |
| permissible (Noul) | 0.14 | 0.37 | 0.86 |
