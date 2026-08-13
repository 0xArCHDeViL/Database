# Gateway Tracker UI/UX Functional Audit

The overhaul uses one test for every visible surface: it must either initiate an action, collect essential input, explain a decision, or provide feedback that changes the next action. Surfaces that did not meet that test were removed or demoted.

| Component | Functional responsibility | User outcome | Decision / feedback source |
|---|---|---|---|
| Daily Pilot | Names the next Japanese category and smallest useful focus block. | The user knows what to do without interpreting a chart. | Adaptive plan from target, 7-day rhythm, 14-day allocation, and current progress. |
| Local Focus Alarm | Starts, persists, and ends the current focus block while the app is active. | A timer has a clear beginning/end and optional notification. | Browser permission, persisted end time, visual countdown, optional audio. |
| Daily Nudge | Provides a configurable check-in time with an honest active-app limitation. | Reminder is predictable instead of ambient decoration. | Jakarta-time schedule, one firing per date, remaining Japanese minutes. |
| Workout input | Captures only completed Ladder/Cindy work and its duration. | Physical work contributes truthfully to daily totals. | Selected workout state and entered rounds/minutes. |
| Japanese batch capture | Converts a large paste into one validated, deduplicated study session. | Hundreds of items can be recorded in seconds. | Parser count, suggested minutes, category/JLPT selection, batch summary. |
| Manual Japanese detail | Keeps sentence/reading input available but optional. | Detail is added only where it aids learning. | User-opened disclosure, not a mandatory row factory. |
| Decision signal | States remaining minutes and current category priority. | The user gets a concise intervention cue. | Daily plan and current-day aggregation. |
| Target rationale | Explains target and re-entry behaviour. | The target is inspectable rather than arbitrary. | Bounded baseline, stability adjustment, missed-session re-entry discount. |
| Rhythm | Shows consistency, load, and allocation by category. | Historic data changes the next priority instead of becoming decoration. | 12-week minutes, 14-day load, selected range aggregation. |
| Export / backup | Produces a portable audit trail and optional append-only snapshot. | The user can retain or inspect data outside the app. | Current store, selected date range, direct branch snapshot. |

## Removed or demoted patterns

The large decorative hero, imagery-only panel, duplicate mobile navigation, and always-visible Japanese row stack were removed. The design now reserves strong colour for the active focus alarm, uses the remaining panels as either input or evidence, and moves manual detail behind an explicit disclosure.
