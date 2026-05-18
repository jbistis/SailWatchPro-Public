# SailWatch Pro — Crew Availability: Feature Scope

**Status:** Design draft for review
**Author:** James Bistis (SailWatch Pro)
**Date:** May 2026

---

## Summary

When recruiting crew for an event, the existing flow shows the whole roster
and asks the manager to pick from it. That works on a 5-boat racing weekend
but breaks down on a Wednesday-night beer can: Mike has said five times he
can't do weeknights, but he's still in the list, still getting whip-emails,
still annoyed.

This feature adds a **standing availability** signal on each crew member:
which days of the week they can sail, and which event durations they'll
consider. When you create an event, the system uses the event's
date-range + duration to mark each crew member as **available** /
**unavailable** / **check notes** before you start filling the season
matrix. Unavailable crew stay visible (the manager has final say) but are
clearly flagged so you don't pester them by default.

This is the *upstream* filter. The existing `event_crew_availability`
matrix (the per-event A/P/N/C the crew self-report) is unchanged — this
just gives you a smarter starting point for that matrix.

---

## How this composes with what's already shipped

Three orthogonal signals about a crew member, each answering a different
question. All three are kept:

| Signal | Scope | Answers | Who edits |
|---|---|---|---|
| **Availability** (this feature) | Per crew (account-wide) | *"Would they ever say yes to this kind of event?"* | Manager edits unclaimed; crew edits own (Slice 3) |
| **Qualifications** (Slice 6) | Per (crew, boat) | *"What positions can they fill on this boat?"* | Boat manager only |
| **Priority** (existing) | Per (crew, boat) | *"Among available qualified crew, who do I want first?"* | Boat manager only |

The recruiting flow stacks them: **availability filters**, **qualifications
narrow**, **priority ranks**. None of them replaces the per-event A/P/N/C
matrix — that remains the authoritative "are you actually coming to this
specific regatta" record.

### Why availability lives on `crew_members`, not per-boat

Day-of-week and duration constraints are properties of the *person*
("Mike's kids have hockey Wednesdays", "Sara doesn't do overnights"), not
of the boat. A per-boat override is conceivable later — someone might do
distance racing on a J/120 but not a J/29 — but it's rare and adds real
complexity. Start universal. If it bites, layer an override table in v2.

---

## The data we're working with

### What "kind of event" means in practice

User's working categories were:

- Weeknight Buoy Races
- Weekend Windward/Leeward Daily
- Race Week
- Overnight Offshore

Decomposed into two orthogonal axes:

| Axis | Values | Source |
|---|---|---|
| **Day of week** | Mon, Tue, Wed, Thu, Fri, Sat, Sun (set) | `events.start_date` → `end_date` expanded to a set of weekdays |
| **Duration class** | `single_day`, `multi_day`, `overnight` | Derived from `events.start_date`, `end_date`, and (where present) `races.end_utc - races.start_utc` |

Every category in the user's list collapses to a (days, duration) tuple:

- Weeknight Buoy = {Mon–Fri} × single_day
- Weekend Daily = {Sat,Sun} × single_day
- Race Week = consecutive days × multi_day
- Overnight Offshore = any days × overnight

No taxonomy to maintain, no "event types" CRUD, and the rules express
themselves in terms of the event's actual schedule rather than a label
someone has to remember to set.

### Duration class, more precisely

- `single_day` — `end_date = start_date`, and (if races exist) no race
  crosses local midnight
- `multi_day` — `end_date > start_date`, and no individual race is
  overnight
- `overnight` — any race in the event has `end_utc - start_utc >= 12h`,
  OR explicit override on the event (see Slice 2 — `is_overnight` toggle)

The explicit override matters because some Wednesday-night beer cans run
late into the next morning officially (Friday Night Long Distance series,
etc.), and some "overnight" races are actually two segments with a
mandatory layday between. Auto-detect from races where possible, manual
toggle when not.

---

## Design decisions (settled)

### 1. Two-axis availability stored on `crew_members`

- `available_weekdays` — `text[]` containing any subset of
  `{mon, tue, wed, thu, fri, sat, sun}`. Default `{}` meaning "no
  declared availability" → treated as available for everything (don't
  punish crew who haven't filled this in).
- `available_durations` — `text[]` containing any subset of
  `{single_day, multi_day, overnight}`. Same default semantics.
- `availability_notes` — free text for the edge cases ("Only summer
  Wednesdays", "Out July 1–15"). Surfaced in the recruiting UI as a
  hover/tooltip badge; never parsed.

### 2. "Empty means available" — opt-in restriction

A brand-new crew member with no availability set should not be excluded
from any event. The matching rule is **availability is restrictive only
when set**. If `available_weekdays = {}`, every weekday matches. Same
for durations. This avoids the cold-start problem where the feature
makes the recruiting list empty until everyone fills out a form.

### 3. Match logic is a SQL function, not application code

A `crew_availability_match(crew_member_id, event_id)` SQL function
returns one of:

- `available` — every required weekday and duration is in the crew's
  set (or the crew has no constraint)
- `unavailable` — at least one required weekday or duration is NOT in
  the crew's set
- `check_notes` — `available_weekdays` and `available_durations`
  match, AND `availability_notes` is non-empty (surface the note;
  don't auto-decide)

Returned column joins onto the existing `event_crew_availability` query
in the matrix UI. One DB-side function means iOS and any future API
consumer get the same answer the web does.

### 4. Recruiting UI shows, never hides

The season matrix already groups crew by tier (First Call / Second Call
/ Reserve). The availability signal adds a **column badge per event**
on each crew row (or per (event, crew) cell):

- ● green — `available`
- ◐ amber — `check_notes` (tooltip shows the note)
- ○ gray — `unavailable` (still visible, still selectable, just dimmed)

The manager can always override and confirm an "unavailable" crew —
the badge is advice, not enforcement. Optional filter chip above the
matrix: **"Hide unavailable"** for quick mass-recruiting.

### 5. Crew edit their own availability (Slice 3)

Same self-claim pattern as the rest of crew_members: pre-claim, the
boat manager edits availability for unclaimed crew (any rostering
boat's manager — same RLS as existing crew_members fields). Post-claim
(`crew_members.user_id` set), the crew member edits their own from
the CrewAccountPage / MyAvailabilityPage. Boat manager loses edit
access at claim time, same as other personal fields.

### 6. iOS shape parity

Add the three fields to the iOS `CrewMember` struct in
`/Users/jamesbistis/dev/SailWatchPro/Models/CrewMember.swift`:

- `availableWeekdays: Set<String>` (lowercase, matching DB values)
- `availableDurations: Set<String>`
- `availabilityNotes: String?`

Names mirror DB columns with the iOS camelCase convention already in
use for the other crew jsonb fields. iOS doesn't compute the
recruiting match — it just reads/writes the raw fields. Match is a
web-side concern for now.

---

## Data model

### `crew_members` additions

| Column | Type | Notes |
|---|---|---|
| `available_weekdays` | `text[] not null default '{}'` | Subset of mon/tue/wed/thu/fri/sat/sun. Empty = no restriction. |
| `available_durations` | `text[] not null default '{}'` | Subset of single_day/multi_day/overnight. Empty = no restriction. |
| `availability_notes` | `text` nullable | Free text. Shown in UI as tooltip. |

CHECK constraints reject unknown values in either array — keeps the
column self-validating without needing an enum.

### `events` additions

| Column | Type | Notes |
|---|---|---|
| `is_overnight` | `boolean not null default false` | Manual override when auto-detect can't tell (no races created yet, or stale race times). |

Duration class is computed on read, not stored — the only stored
attribute is the manual override. Auto-detection logic:

```
overnight  := events.is_overnight
              OR any race in this event spans >= 12h
              OR any race in this event crosses local midnight
multi_day  := NOT overnight AND end_date > start_date
single_day := NOT overnight AND end_date = start_date
```

Weekday set is always derived from `start_date..end_date` inclusive.

### Match function

```sql
create or replace function public.crew_availability_match(
  _crew_member_id uuid,
  _event_id uuid
) returns text language sql stable as $$
  with c as (
    select available_weekdays, available_durations, availability_notes
    from crew_members where id = _crew_member_id
  ),
  e as (
    select
      -- weekday set from start_date..end_date
      array(select to_char(d, 'dy')
            from generate_series(start_date, end_date, '1 day') d) as wd,
      -- duration class derived as above
      public.event_duration_class(id) as dur
    from events where id = _event_id
  )
  select case
    when (select cardinality(available_weekdays) from c) > 0
         and not ((select wd from e) <@ (select available_weekdays from c))
      then 'unavailable'
    when (select cardinality(available_durations) from c) > 0
         and not ((select dur from e) = any (select available_durations from c))
      then 'unavailable'
    when (select coalesce(length(availability_notes), 0) from c) > 0
      then 'check_notes'
    else 'available'
  end;
$$;
```

`event_duration_class(event_id)` is a sibling helper containing the
overnight / multi_day / single_day rule. Both functions are STABLE
(no writes) and called in the matrix SELECT — joined per (event, crew)
row. Cost is negligible at any realistic season size (dozens of events
× tens of crew = hundreds of rows).

### No new table

Availability is a property of the crew member, not a many-to-many. Three
columns and two functions — no join table, no event_types CRUD, nothing
new to back up. This is the win over the original
event-type-categories approach.

---

## UI changes

### CrewMemberForm — new "Availability" section

Added between "Safety & roles" and "Emergency contact":

- **Available days** — seven checkbox chips (Mon–Sun). "Leave blank if
  no constraint" helper.
- **Race durations I'll consider** — three checkbox chips: Single day,
  Multi-day regatta, Overnight / offshore. Same blank-means-unconstrained
  helper.
- **Availability notes** — text area, placeholder *"Only summer Wednesdays,
  out July 1–15, etc."*

Persists via the existing crew_member update path. No new component
plumbing.

### Per-boat CrewPage — read-only summary chip

Each crew card gets a small availability summary below the contact line:

- If both arrays empty: *"Available any time"* (subtle, gray)
- Otherwise: a chip like *"Sat/Sun • multi-day • notes"* — click opens
  the same editor route as other crew details

Keeps the page scannable without burying the info.

### Season matrix — availability badge per cell

For each (event, crew) cell already rendered in
[src/components/SeasonMatrix.tsx](src/components/SeasonMatrix.tsx):

- Before the A/P/N/C dropdown, render the availability dot (●/◐/○)
- ○ unavailable cells get reduced opacity on the dropdown — manager can
  still click and confirm, just visually deprioritized
- Tooltip on ◐ shows `availability_notes`

New control row above the matrix:

- Toggle: **Hide crew unavailable for any event** (default off)
- When on, rows where every event resolves to `unavailable` are
  collapsed into a *"N hidden — show"* link

### MyAvailabilityPage — self-edit (Slice 3 only)

A new "My standing availability" section at the top, above the
event-by-event list. Same three controls as the CrewMemberForm
section. Saves to the claimed crew's own `crew_members` row via RLS.

---

## Slice breakdown

**Slice 1 — Schema + form editor**
- Migration: three columns on `crew_members`, one column on `events`,
  CHECK constraints, two SQL functions
- Add "Availability" section to
  [CrewMemberForm.tsx](src/components/CrewMemberForm.tsx)
- iOS struct update (separate iOS PR, see *Cross-platform coordination*)
- No matching logic surfaced yet — just collect the data

**Slice 2 — Read-only badges on CrewPage**
- Render the availability summary chip on each crew card
- Verifies the data round-trips before we wire it into matrix logic

**Slice 3 — Matrix integration**
- Wire `crew_availability_match(crew_id, event_id)` into the season
  matrix query
- Render badges + tooltip + reduced-opacity styling
- "Hide unavailable" toggle row
- This is the slice that delivers the actual user value — earlier
  slices are setup

**Slice 4 — Crew self-edit on MyAvailabilityPage**
- Add the standing-availability section above the event list
- RLS already covers it (crew can edit own row), no migration needed
- Pre-existing column-narrowed UPDATE policy from Slice 3a of the crew
  feature should handle this — verify before assuming

**Slice 5 (deferred) — Per-boat override**
- New table `crew_member_boat_availability_overrides` keyed on
  `(crew_member_id, boat_id)` with the same three columns
- Match function checks override first, falls back to crew_members
- Only build if real cases emerge

---

## Cross-platform coordination

iOS reads `crew_members` via the existing sync path. The three new
columns need a matching iOS struct update **before** Slice 1's
migration is applied to production, otherwise iOS decoders blow up on
unknown jsonb keys (or, for plain columns, just silently miss them
depending on the codec). Order:

1. Add fields to `CrewMember.swift` with default values (empty
   set / nil), ship an iOS build
2. Apply the SailWatch web migration
3. Ship the web Slice 1 PR

iOS Slice 4 (crew self-edit on mobile) can land later.

---

## What v1 does NOT include

- **No per-boat availability override.** Universal-on-crew_members
  only. Per-boat overrides are scoped as Slice 5 / deferred.
- **No time-of-day axis** (morning / afternoon / evening). Sailing
  events are mostly all-day or evening-by-context; adding a third axis
  complicates the UI for marginal benefit. Use availability_notes for
  the few cases this matters.
- **No date-range vacation blocks.** "Out July 1–15" goes in notes,
  not a structured range. If this becomes a real pattern, add a
  `crew_member_unavailable_periods` table later.
- **No learning from RSVP history.** The history-driven option from
  the design discussion is a possible future enhancement on top of
  this, not part of v1.
- **No auto-fill of `event_crew_availability` cells.** The matrix
  still requires explicit A/P/N/C entry. Availability badges are
  advisory only — they don't pre-populate the matrix because
  "available in general" ≠ "available this specific weekend".
- **No event-type taxonomy / categories CRUD.** Intentionally absent
  — that was the alternative design this scope replaces. The match
  rule operates on the event's actual date and duration, not a label.

---

## Open questions for review

1. **`is_overnight` placement.** Putting the manual override on
   `events` is simplest, but some users may want it on the boat
   level ("this boat does overnight by default"). Confirm event-level
   is the right scope.

2. **Default for new crew imported via "Add from other boats".** When
   a crew member exists with availability set on one boat's roster
   and is added to a second boat, the universal field travels with
   them. Correct? Or should the second boat manager re-confirm?
   (Suggested default: travels — that's the whole point of
   universal-per-crew.)

3. **`available_weekdays` storage format.** Using lowercase 3-letter
   day codes (`mon`, `tue`, …) matches PostgreSQL's `to_char(d, 'dy')`
   output and is human-readable. Alternative: integers 0–6. Stay with
   text codes unless there's a reason to switch.

4. **Race Week edge case.** A 5-day regatta running Mon–Fri (rare
   but real) currently requires every day to be in the crew's
   `available_weekdays`. A crew member who can only do Wed–Fri of
   Race Week shows as `unavailable` even though they could partially
   commit. Acceptable — they reflect that nuance in the per-event
   A/P/N/C, with a "P + see notes" pattern. Confirm this is OK.

5. **What counts as "overnight"?** The auto-detect heuristic is
   *"any race ≥ 12 hours OR crossing local midnight"*. The 12-hour
   threshold is a guess. Could equally be 8h, could be a UI-tunable
   per boat. Calibrate against real Della-Aurora race data once
   Slice 1 ships.

---

## Appendix: what we already have

- **Crew roster** ([CrewPage.tsx](src/pages/CrewPage.tsx)) — per-boat
  roster with tier groups, qualifications chips, team managers section
- **Season matrix** ([SeasonMatrix.tsx](src/components/SeasonMatrix.tsx))
  — the recruiting UI where availability badges land in Slice 3
- **Priority tiers** (`crew_member_priorities`) — First Call / Second
  Call / Reserve, manager-only, **kept and unchanged** by this feature
- **Per-boat qualifications**
  (`crew_member_boat_qualifications`) — chip toggles per boat,
  **kept and unchanged**
- **MyAvailabilityPage** — the self-service surface for Slice 4
- **iOS CrewMember struct** at
  `/Users/jamesbistis/dev/SailWatchPro/Models/CrewMember.swift` — the
  source-of-truth shape this feature extends
