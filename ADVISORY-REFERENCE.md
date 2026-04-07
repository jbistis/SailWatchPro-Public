# SailWatchPro — Advisory System Reference

**Check interval:** Every 5 minutes (300 seconds) via `startPeriodicChecks()`  
**Sources:** `AdvisoryManager.swift` + `AdvisoryManager+GRIBAccuracy.swift`  
**Last updated:** April 2026

---

## Categories

| Category | Icon | Display Name |
|----------|------|--------------|
| `weather` | cloud.rain.fill | Weather |
| `sail` | flag.fill | Sail Selection |
| `safety` | exclamationmark.shield.fill | Safety |
| `tactical` | scope | Tactical |
| `navigation` | map.fill | Navigation |
| `performance` | speedometer | Performance |

## Priority Levels

| Priority | Color | Icon |
|----------|-------|------|
| `.info` | Blue | info.circle.fill |
| `.warning` | Orange | exclamationmark.triangle.fill |
| `.critical` | Red | exclamationmark.octagon.fill |

---

## Weather Advisories

### Barometric Pressure

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| Rapidly Falling Barometric Pressure | Warning | Pressure drops > 3 mb/hr over last hour | "Pressure has dropped X mb in the last hour. Conditions may deteriorate rapidly." | Shorten sail, check forecast, prepare for stronger winds |
| Dangerous Pressure Drop | Critical | Pressure drops > 5 mb/hr over last hour | "Pressure has plummeted X mb. Severe weather likely." | URGENT: Seek shelter immediately |
| Rising Barometric Pressure | Info | Pressure rises > 3 mb/hr over last hour | "Pressure has risen X mb. Conditions improving." | Expect lighter winds and clearing conditions |

**Data required:** Min 10 pressure samples from last 2 hours (WindDataManager.pressureDataPoints)

---

### GRIB Accuracy (from `AdvisoryManager+GRIBAccuracy.swift`)

**Prerequisites:** Race active (`isRaceActive = true`) + min 6 rows of 5-min summary data (30 min of logging)

| Title | Priority | Trigger | Suppressed when | Message |
|-------|----------|---------|-----------------|---------|
| GRIB Wind Direction Bias | Warning | Avg TWD error ≥ 8° over logged period | Wind oscillating > 20° amplitude | "GRIB TWD has been X° right/left of actual for Y hrs — bias is [trend]." |
| GRIB Wind Direction Bias | Critical | Avg TWD error ≥ 15° | Wind oscillating > 20° amplitude | Same message, higher priority |
| GRIB Wind Speed Bias | Warning | Avg TWS error ≥ 2.5 kt | — | "Actual wind has been X kt stronger/lighter than GRIB for Y hrs." |
| GRIB Wind Speed Bias | Critical | Avg TWS error ≥ 5.0 kt | — | Same message, higher priority |
| GRIB Current Bias | Warning | Avg drift error ≥ 0.4 kt | — | "Current drift is X kt stronger/weaker than GRIB for Y hrs." |
| GRIB Current Bias | Critical | Avg drift error ≥ 0.8 kt | — | Same message, higher priority |

**Bias trend labels:** improving / degrading / stable, not improving / insufficient data  
**Thresholds to tune after first races** — defined in `GRIBThreshold` enum in `AdvisoryManager+GRIBAccuracy.swift`

**Data source:** `ForecastComparisonManager.shared.validationStats` → `fiveMinuteSummary` (downsampled from 15-sec raw logs, 8-hour window, 96 rows max)

---

## Sail Advisories

### Sail Change (from SailCrossoverManager)

**Note:** Currently only fires in Test Mode — live mode returns early when `data == nil`

| Title | Priority | Trigger | Message |
|-------|----------|---------|---------|
| Sail Change Recommended | Warning | `SailCrossoverManager.sailChangeAlert == .shouldChange` | "Current sail 'X' is no longer optimal. Recommended: 'Y'" |
| Sail Change Approaching | Info | `SailCrossoverManager.sailChangeAlert == .approaching` | "Approaching optimal conditions for 'X' in [distance]" |

---

## Safety Advisories

**Data source:** `ExpeditionDataManager.shared.data` (live) or passed `expeditionData` parameter

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| Depth Data Critical | Critical | Depth ≤ 0 (sensor failure or extreme shallow) | "Depth reading is X m. Sensor failure or dangerous shallow water." | Verify sounder, navigate with extreme caution |
| Shallow Water Warning | Critical | Depth < draft × 1.2 (e.g. draft 2.5m → depth < 3.0m) | "Current depth Xm dangerously close to draft Ym. Safety margin: Zm." | IMMEDIATE: Change course to deeper water |
| Depth Advisory | Warning | Depth < draft × 1.5 (e.g. draft 2.5m → depth < 3.75m) | "Depth Xm getting shallow relative to draft Ym." | Monitor carefully, prepare to change course |
| Excessive Heel Angle | Warning | Heel angle > 35° | "Current heel angle of X° is quite high." | Reduce sail area, ease sheets, or change course |
| High Speed in Strong Conditions | Info | TWS > 25 kt AND BSP > 12 kt | "Boat speed X kt in Y kt TWS." | Monitor carefully, consider reducing sail |

**Draft required:** Safety advisories only run when `settings.draft > 0`

---

## Tactical Advisories

### Sail Mismatch (from Expedition)

**Prerequisites:** Race timer state == `.racing` AND sail data available from Expedition

| Title | Priority | Trigger | Message |
|-------|----------|---------|---------|
| Sail Mismatch | Warning | `sailMark` ≠ `sailEvent` (or `sail`) | "Expedition recommends changing to X. You are currently flying Y." |

**Data:** `ExpeditionDataManager.shared.data.sailMark` vs `sailEvent`/`sail` (Expedition channels)

---

### Overstood Layline

**Prerequisites:** Active mark with `markRange > 0`, sailing mode is upwind or downwind (not reaching)

| Title | Priority | Trigger | Message |
|-------|----------|---------|---------|
| Overstood Layline | Info | Past layline by 0–0.1 nm | "You are X nm (Y m) past the [port/starboard] layline to [mark]." |
| Overstood Layline | Warning | Past layline by > 0.1 nm | Same message, higher priority |

**Buffer:** 0.05 nm dead-band to reduce noise  
**Tack vs Gybe:** Advisory says "Tack now" upwind, "Gybe now" downwind

---

## Performance Advisories

### Polar Performance

**Note:** Currently only fires in Test Mode

| Title | Priority | Trigger | Message |
|-------|----------|---------|---------|
| Below Target Performance | Info | Polar% > 0 AND polar% < 80% | "Current performance is X% of polar target." |
| VMG Below Target | Info | VMG% > 0 AND VMG% < 85% | "VMG is X% of target (Y vs Z kt)." |

---

### Current / Leeway Push

**Data source:** `PerformanceDataManager` — 10-min avg BSP vs SOG (`netCurrentPush10MinAvg = BSP - SOG`)  
**Includes:** Opposite tack VMG prediction when tacking would be beneficial

| Title | Priority | Trigger (BSP - SOG over 10 min) | Message |
|-------|----------|--------------------------------|---------|
| Mild Push Against Current/Leeway | Info | ≤ −0.5 kt | "Losing ~0.5–1.2 kt over last 10 min. [Opposite tack note if applicable]" |
| Pushing Too Much Water | Warning | ≤ −1.2 kt | "Losing ~1.2–1.5 kt on average over last 10 min. [Opposite tack note]" |
| Pushing Hard Against Current/Leeway | Critical | ≤ −1.5 kt | "Losing ~1.5+ kt over last 10 min. [Opposite tack note]" |

**Opposite tack prediction:** Computed from current TWA, BSP, current set/drift, and mark bearing. Only shown when VMG gain > 0.1 kt.

---

## Advisory Lifecycle

- **Replaced:** Each advisory title replaces its previous version (`replacingCategory:withTitle:`) — no stacking of same advisory type
- **Cleared:** When condition resolves, `removePreviousAdvisories()` is called automatically
- **Dismissed:** User can dismiss; dismissed advisories stay in storage but are hidden from active list
- **Cleanup:** Advisories older than 7 days are purged; max 50 stored (configurable in Advisory Settings)
- **Watch:** Most critical (`.critical`) advisory synced to Apple Watch via WatchConnectivity

---

## Files

| File | Contents |
|------|----------|
| `AdvisoryManager.swift` | Core manager, all non-GRIB advisories |
| `AdvisoryManager+GRIBAccuracy.swift` | GRIB bias advisories (iOS target only) |
| `AdvisoryModels.swift` | `Advisory`, `AdvisoryPriority`, `AdvisoryCategory` structs (iOS + Watch) |
| `AdvisorySettingsView.swift` | Settings UI — enable/disable, category filter, priority filter |
| `ForecastComparisonManager.swift` | Raw 15-sec GRIB vs actual logging, 8-hour retention (iOS only) |
| `ForecastModels.swift` | `ForecastComparison`, `ForecastSummaryRow`, `ForecastValidationStats` (iOS only) |
