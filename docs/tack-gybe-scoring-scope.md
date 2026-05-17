# SailWatch Pro — Tack & Gybe Analysis: Feature Scope

**Status:** Design draft for skipper review
**Author:** James Bistis (SailWatch Pro)
**Date:** May 2026

---

## Summary

We're designing a tack and gybe analysis feature for SailWatch Pro that grades each maneuver in a race and tells the skipper, in plain English, *what went wrong and what to try next time* — not just how many seconds or metres were lost. The data we need (TWD, TWS, heading, BSP, TWA, heel) is already in the boat's instrument log; we don't require polar files in version 1.

We've reviewed how raceQs and Sailnjord present maneuver data and identified a gap neither tool fills: **coaching insight**. Numbers and clouds describe what happened. We want to also explain *why* and *what to do differently*, and to do it in a way that's aware of which wind regime you're sailing in.

---

## The gap we're trying to fill

| Tool | Strength | Weakness |
|---|---|---|
| **Expedition Marine** | Excellent live instrumentation | TackLossD / TackLossT only populate when the user clicks Start *and* Complete in the Tack Analysis dialog mid-maneuver — almost never happens during a real race. |
| **raceQs** | Beautiful "tacking pattern" cloud visualization on a half-polar; instant visual diagnosis of tight-groove vs. sprawl | Per-maneuver scalars are basic (tacking angle, duration, time lost). No written critique. |
| **Sailnjord** | Dense scalar table — two loss measures (geometric from COG, integral from VMG), 95%-recovery times for BSP and VMG | Wall of numbers; no diagnosis of *why* a tack was poor or what to change. Requires polars. |

**SailWatch's intent:** scalars on Sailnjord's level + visualization on raceQs's level + a coaching layer neither has — and polar-free in v1 so it works on any boat with reasonable instruments.

---

## What you'll see (user experience)

For each detected tack or gybe in a race, SailWatch will produce:

### 1. A maneuver card

A summary panel with the headline numbers:
- **Tacking angle** (degrees, pre-tack mean COG vs. post-tack mean COG)
- **Tack duration** (seconds bow-through-the-eye)
- **Min SOG**, **Min VMG** during the maneuver
- **VMG recovery time** (seconds to return to a settled groove, using the boat's own pre-tack baseline)
- **Time lost** — two numbers: from-COG (geometric) and from-VMG (integral)
- **Peak heel** during the maneuver

### 2. A "tacking pattern" view (half-polar cloud)

The raceQs-style cloud: half-polar chart with True Wind Direction at the top, concentric speed rings, one dot per second over the ±60s window around the maneuver, colored by time-since-tack. Lets the skipper see at a glance whether the post-tack cluster pulled tight or sprawled.

### 3. Stacked before/after histograms (our addition)

Beside the cloud, density bars for VMG, BSP, Heading, and TWA — but split into "30 seconds before the tack" and "30 seconds after the tack." Instantly answers: "did my groove come back?"

### 4. A plain-language critique

Two to four sentences identifying which phase of the maneuver was strong or weak. Example output for a poor tack:

> *Entered at 4.2 kt in 11 kt of wind — about 85% of your typical pre-tack speed in these conditions. After crossing the wind you came up to close-hauled within 2 seconds with only 4° of bear-off, which didn't give the boat time to rebuild speed. Try foot for speed an extra 10° for 4–5 seconds before squeezing back up to your line.*

The critique is generated from the scalars plus a sailing-mode classifier (see below).

### 5. A race-level rollup

Across all maneuvers in the race:
- Median and total time lost
- "Tack quality by mode" — your power-seeking, powered, and power-shedding tacks scored separately
- Best and worst tacks of the race linked to their cards

---

## What we measure

Per maneuver, computed from log data:

**Anchoring & Detection**
- Maneuver time anchored to TWA crossing 0° (tack) or 180° (gybe).
- Detection uses TWA-zone transitions with hysteresis to filter noise.

**Pre/post baselines** (the boat's own reference, no polars needed)
- 15-second mean BSP, HDG, VMG over `[t − 20s, t − 5s]` (before)
- 15-second mean BSP, HDG, VMG over `[t + 10s, t + 25s]` (after)
- "Exclusion period" of ±5–10s around the maneuver to skip the noisy moment of the turn itself.

**Maneuver scalars**
- Tacking angle (deg, COG-based)
- Over-steering (deg) — how far past the post-tack heading the boat went on exit
- Tack duration (sec)
- Min SOG, Min VMG
- VMG recovery time (sec until VMG returns to ≥95% of pre-tack mean and holds 3+ sec in a tight groove)
- BSP recovery time (sec, same logic)
- Peak heel (deg)
- Loss from COG (m) — how far behind a hypothetical straight-line ghost boat you are 10s after the tack
- Loss from VMG (m, derived sec) — integral of VMG deficit across the maneuver window

**The "groove" gate**
A maneuver is only *scored* if either the 30s before or the 30s after has settled HDG and BSP (low standard deviation). Tacks during chop, gusts, or chaotic boat-handling are detected but labeled "rough conditions — not scored," to keep us from publishing garbage numbers.

---

## Mode-aware coaching (our differentiator)

Sailboats operate in three wind regimes, and a "good tack" looks different in each:

| Mode | TWS (kt) | Tactic | Healthy oversteer band | Canonical failure |
|---|---|---|---|---|
| **Power-seeking** | 0–8 | Find power; long S-curve; aggressive foot for speed | 15–30° | Under-steering — no speed build, boat stalls on new tack |
| **Powered** | 8–16 | Standard fast tack | 5–15° | Mixed — either under-steering or over-rotation |
| **Power-shedding** | 16+ | Control; minimal bear-off; sometimes pinch on exit | 0–8° | Over-steering — overpowers boat, broach risk |

Every critique rule is mode-gated: the same oversteer degrees, recovery time, or VMG dip mean different things by mode, so the language of the critique changes accordingly. The bands above are starting estimates and would be tuned per boat class.

**Mode breakpoints are tunable per boat** — defaults are 8 kt and 16 kt for a typical keelboat, but a foiler or a heavy-displacement boat would shift them.

---

## The "perfect tack" model we'll score against

Three phases, each generating its own scalars and contributing to the critique:

1. **Entry (head up).** Were you carrying enough speed and heel to tack? Pre-tack BSP ratio vs. recent groove tells us. A tack from 85% of your typical speed is often doomed regardless of how cleanly the rest is executed — and the skipper deserves to be told that.
2. **Apex (crossing the eye of the wind).** Was the turn rate smooth and bell-shaped (good), or spiky/flat-spin (rudder dragged speed away)? Total course change in the expected band for the mode?
3. **Exit (build speed, then round up).** Did you bear off for the speed-build phase by the right amount for the mode, or did you immediately squeeze to close-hauled and stall the recovery? Did VMG return to a tight groove, or did the cloud sprawl?

We can locate which phase failed and write the critique sentence to point at that phase.

---

## What v1 explicitly does NOT include

Calling these out so they don't creep into the build:

- **No polar files.** We're self-referenced (your own pre-tack groove is the target). When polars are added later, the same metrics get a sharper external reference, but the design doesn't depend on them.
- **No multi-boat comparison.** raceQs shows you side-by-side with competitors. That requires multi-boat GPS upload to a shared regatta — out of scope for v1.
- **No live mode.** We're a post-mortem tool, not a tactical live overlay. Race ends, log uploads, analysis appears.
- **No coaching of *tactical* decisions** — e.g., we won't tell you that the tack was the wrong tactical call given lane and wind shift. Only the *execution* of the tack you did make.

---

## Questions we'd value your input on

Two lenses are valuable here — your coaching view of the scoring model, and your user view of how this would actually fit into how a sailor reviews a race. Questions 1–7 are coach-lens; questions 8–10 are user-lens.

### Coach-lens

1. **Mode breakpoints.** Are 0–8 / 8–16 / 16+ kt the right defaults, or do you draw them differently? Different upwind vs. downwind? Different by boat class in ways we should encode?
2. **Healthy oversteer bands.** Do the 15–30 / 5–15 / 0–8° ranges match what you actually coach? Where would you put them?
3. **Recovery definition.** We're treating "recovery complete" as "VMG returns to ≥95% of pre-tack mean *and* the boat is back in a tight HDG/BSP groove for 3+ seconds." Is the 95% threshold right? Is "groove tightness" the right additional gate, or is plain VMG-return enough?
4. **The critique sentence format.** Two-to-four sentences pointing at the failure phase plus a specific lever to pull. Is this useful coaching language, or would you frame it differently?
5. **What scalars are missing?** We deliberately kept the list short. Anything important to a coach that we've left off?
6. **Entry quality.** We're scoring the *decision to tack* (entry speed and heel vs. recent groove). Is this useful, or does it cross the line into tactical second-guessing the helm shouldn't see?
7. **Gybes.** This document focuses on tacks. We expect most of the framework transfers to gybes but with different phase emphases (depower, asymmetric vs. symmetric kite, broach risk on exit). Where would you split the gybe analysis differently from tacks?

### User-lens

8. **When would you actually open this?** Same evening after racing, next morning, days later — or would you mostly want headline numbers in a feed/notification and only dig in for tacks that looked bad? This drives whether we lead with the rollup, the worst-tack-of-the-race card, or the per-tack cloud.
9. **What gets you to click into a specific maneuver?** Should the worst tack of the race be auto-surfaced? Would you sort by time-lost, by mode, by leg? Would a "compare this tack to my best tack of the race" view be useful?
10. **Crew sharing.** Would you want to send a single maneuver card to a tactician or trimmer (text, email, image) — or is this purely a private skipper view? If sharing is useful, what should the shareable artifact look like?

---

## Appendix: data we already have to work with

From a standard Expedition log:
- True Wind Direction (TWD)
- True Wind Speed (TWS)
- Boat speed (BSP)
- Speed over ground (SOG)
- Heading (HDG)
- Course over ground (COG)
- True Wind Angle (TWA, signed)
- Heel
- VMG (derivable: BSP × cos(TWA))
- GPS position

We do **not** need:
- Polar files
- Target boat speed channels
- Manual annotation by the navigator (i.e., clicking buttons during the tack)
