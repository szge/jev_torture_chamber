# trolley_transplant_primed

With its earlier "pull the lever" and "push the man" decisions in the state, Jev flips on the transplant case: it now harvests (0.89, up from 0.30 without them) and rates harvesting as permissible at 0.38 (up from 0.14). Its stated action moved much more than its moral judgment, so the earlier decisions pulled its behaviour toward consistency while leaving the judgment mostly below the 0.5 line. This is a single call per condition.

## Setup
- One request (`request.json`), two questions; model `jev-1.14.0`
- Identical to `../trolley_transplant` (scenario, questions, options) except for the added state field `earlier_decisions`: the lever scenario with "You pulled the lever, so one person died and five lived." and the footbridge scenario with "You pushed the man off the bridge, so one person died and five lived."
- Scenario texts are copied programmatically from `../trolley_classic`, `../trolley_footbridge` and `../trolley_transplant`

## Result

| Question | With earlier decisions | Without (`../trolley_transplant`) |
|---|---|---|
| action: harvest_organs | 0.89 | 0.30 |
| action: do_nothing | 0.11 | 0.70 |
| harvesting permissible (Noul) | 0.38 | 0.14 |
| action confidence | 0.78 | 0.40 |
