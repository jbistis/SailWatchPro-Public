# SailWatchPro — Advisory System Reference

**Check interval:** Every 5 minutes (300 seconds) via `startPeriodicChecks()`  
**Sources:** `AdvisoryManager.swift` + `AdvisoryManager+GRIBAccuracy.swift` + `CalibrationTracker.swift` + `OpenMeteoManager.swift`  
**Last updated:** April 2026 (v81+ session — added calibration suite, downwind header, Open-Meteo revision, performance fixes)

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

**Data required:** Min 10 pressure samples from last 2 hours (`WindDataManager.pressureDataPoints`)

---

### Frontal Passage

**Data sources:** `WindDataManager.atmpDataPoints` (air temperature history), `WindDataManager.pressureDataPoints` (barometric pressure history)

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| Frontal Passage Likely | Warning | Air temp dropped ≥ 3°C AND pressure dropped ≥ 2 mb — both within the last 30 min | "Air temp dropped X°C and pressure dropped Y mb in the last 30 min." | Front likely passing. Expect wind shift and squalls — prepare to shorten sail. |

**Both conditions required** — temp-alone can be nocturnal cooling, pressure-alone is already covered by the barometric advisory. Requiring both filters out non-frontal patterns.

**Prerequisites:** Both time series must span ≥ 30 min (oldest sample older than 30 min ago).

**Auto-clears** when either drop falls below its threshold, or when history is insufficient.

**Interaction with barometric advisory:** A 2 mb drop over 30 min is ~4 mb/hr, which also exceeds the "Rapidly Falling Barometric Pressure" threshold (3 mb/hr). Both will fire simultaneously during a front — intentional, since the Frontal advisory adds meteorological context.

**Data values logged:** `tempDropC`, `pressureDropMb`, `currentTempC`, `currentPressureMb`

---

### Dew Point

**Data sources:** `airTemperature` (channel 14, °C), `dewPoint` (channel 370, °C), `relativeHumidity` (channel 168, 0–100%)  
**Dew risk window:** 17:00–08:00 local time

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| Dew Forming on Deck | Warning | Spread ≤ 1.5°C OR humidity ≥ 95% (any time) | "Dew point spread is X°C (Y% RH). Dew is actively forming on deck surfaces." | Consider heading offshore. Use caution on deck — wet surfaces reduce grip. |
| Dew Forming on Deck | Info | Spread ≤ 3.0°C AND within dew risk window (17:00–08:00) | "Dew point spread is X°C (Y% RH). Dew likely to form as deck temperatures drop." | Monitor conditions. Consider heading offshore. |

**Spread calculation:** `airTemperature − dewPoint`  
**Auto-clears** when spread > 3.0°C outside the dew risk window, or when sensor data is unavailable  
**Data values logged:** `airTempC`, `dewPointC`, `spreadC`, `humidityPct`

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

### Layline

**Prerequisites:** Active mark with `markRange > 0`, sailing mode is upwind or downwind (not reaching)

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| Layline | Info | `2.5 min < laylineTime ≤ 7.5 min` on the approaching-tack layline | "Tack/Gybe to [mark] in ~N min." | Start preparing crew for tack/gybe |
| Layline | Warning | `laylineTime ≤ 2.5 min` AND not overstood | "At the layline to [mark]." | Tack/Gybe as soon as practicable |
| Layline | Warning | `shortestAngleDifference(oppositeTackCOG, markBearing) × sign(AWA) > 1°` | "Overstood layline to [mark] by ~X nm." | Tack/Gybe as soon as practicable — losing distance |
| Layline | Info | Overstood but `overstoodNM / markRange ≤ 5%` (trivial) | Same overstood message, lower priority | Same action |

**Layline time source (picked by current tack):**
- Starboard tack → `laylineTimeOnPort` (approaching port layline)
- Port tack → `laylineTimeOnStarboard` (approaching starboard layline)

**Overstood detection:** Angle-based using `oppositeTackCOG` vs `markBearing` — robust regardless of Expedition distance-sign convention. On starboard, overstood when `markBearing` is clockwise of `oppositeTackCOG` by > 1°; inequality flips on port tack (the `× sign(AWA)` term normalizes this).

**Overstood distance:** `max(markRange × sin(|Δ|), |laylineDistance_approachingTack|)` — geometric estimate with fallback to Expedition distance if larger.

**Tack vs Gybe:** Message says "Tack" upwind, "Gybe" downwind.

**Lifecycle:** All three phases share the single title `"Layline"` and replace each other in place. The legacy `"Overstood Layline"` title is removed on every check so users upgrading don't see stale entries.

**Cadence note:** Thresholds are tuned to the 5-min check cadence — the (2.5, 7.5] min approaching bucket is 5 min wide so roughly one check lands inside it; the ≤ 2.5 min bucket catches the final approach. A separate 1-min warning was considered but dropped because a 1-min window can't be reliably caught at 5-min cadence.

---

### Persistent Header

**Data source:** `WindDataManager.twdDataPoints` — three non-overlapping 2-min averaging buckets (now, 4–6 min ago, 8–10 min ago) using circular sin/cos averaging

**Prerequisites:** Sailing mode is upwind, BSP > 2 kt, ≥ 10 min of TWD history with at least 3 samples per bucket

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| Persistent Header | Info | Monotonic TWD shift against current tack ≥ 5° over 10 min | "TWD has shifted X° against you on [tack] over the last 10 min." | Consider tacking to [opposite tack] if the shift persists. |
| Persistent Header | Warning | Monotonic TWD shift against current tack ≥ 10° over 10 min | "TWD has shifted X° against you on [tack] over the last 10 min — opposite tack is lifted." | Tack to [opposite tack] for tactical advantage. |

**Header interpretation (tack-aware):**
- Starboard tack (AWA ≥ 0): TWD backing left (negative shift) = header → port tack is lifted
- Port tack (AWA < 0): TWD veering right (positive shift) = header → starboard tack is lifted
- Combined: `signedHeader = −totalShift × sign(AWA)` must be > 0 to fire

**Oscillation filter:** Requires both sub-shifts (A→B and B→C) to share a sign — `shiftAB × shiftBC > 0`. This forces monotonic behavior across 10 min and rejects common 3–8 min wind oscillation cycles.

**Auto-clears** on reversal, insufficient magnitude, oscillation detection, or mode change.

**Startup behavior:** If < 10 min of TWD history or too few samples per bucket, silently skips — neither fires nor clears.

**Data values logged:** `headerDeg`, `totalShiftDeg`, `currentTWD`

---

### Persistent Header — Downwind (Gybe-on-a-Header)

**Data source:** `WindDataManager.twdDataPoints` — same three 2-min circular-averaged buckets as the upwind version

**Prerequisites:** Sailing mode is downwind, BSP > 2 kt, ≥ 10 min of TWD history with at least 3 samples per bucket

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| Persistent Header — Downwind | Info | Monotonic TWD shift against current gybe ≥ 5° over 10 min | "TWD has shifted X° against you on [gybe] gybe over the last 10 min." | Consider gybing to [opposite gybe] if the shift persists. |
| Persistent Header — Downwind | Warning | Monotonic TWD shift against current gybe ≥ 10° over 10 min | "TWD has shifted X° against you on [gybe] gybe over the last 10 min — opposite gybe is lifted." | Gybe to [opposite gybe] for tactical advantage. |

**Downwind sign inversion:** On starboard gybe (AWA ≥ 0), TWD veering right (positive shift) pushes the VMG angle wider — that is a header downwind. The upwind formula drops the negation: `signedHeader = totalShift × sign(AWA) > 0`.

**Separate title:** Uses "Persistent Header — Downwind" so it is fully independent from the upwind version. Different titles, different lifecycle, no cross-clearing. Mode gate ensures each clears itself on mark roundings.

**Same thresholds as upwind:** 5°/10° as a starting point — may need tuning after on-water validation if downwind proves noisier.

**Data values logged:** `headerDeg`, `totalShiftDeg`, `currentTWD`

---

### Forecast Wind Direction Shifting

**Data source:** `OpenMeteoManager.shared.revisionSummaries` — computed from consecutive hourly HRRR snapshots across the race area grid

**Prerequisites:** `isOpenMeteoEnabled == true`, at least 3 snapshots (2 revision summaries)

| Title | Priority | Trigger | Monotonic Required | Message |
|-------|----------|---------|--------------------|---------|
| Forecast Wind Direction Shifting | Info | Avg revision ≥ 3°/update | No | "HRRR is revising wind direction X° veering/backing per update." |
| Forecast Wind Direction Shifting | Warning | Avg revision ≥ 6°/update | Yes | "HRRR has shifted wind direction X° veering/backing per update over the last N hours." |
| Forecast Wind Direction Shifting | Critical | Avg revision ≥ 10°/update | Yes | "HRRR has shifted wind direction X° ... Revision is consistent and significant." |

**Monotonic = all recent revisions share the same sign.** Prevents noisy oscillation from triggering warning/critical.

**Auto-clears** when revision trend drops below 3°/update or Open-Meteo is disabled.

---

### Forecast Wind Speed Shifting

**Data source:** Same as above

**Prerequisites:** Same as above

| Title | Priority | Trigger | Monotonic Required | Message |
|-------|----------|---------|--------------------|---------|
| Forecast Wind Speed Shifting | Info | Avg revision ≥ 1.5 kt/update | No | "HRRR is revising wind speed X kt increasing/decreasing per update." |
| Forecast Wind Speed Shifting | Warning | Avg revision ≥ 3.0 kt/update | Yes | "HRRR has revised wind speed X kt ... over the last N hours." |
| Forecast Wind Speed Shifting | Critical | Avg revision ≥ 5.0 kt/update | Yes | "HRRR has revised wind speed X kt ... Significant forecast error likely." |

**Auto-clears** when revision trend drops below 1.5 kt/update or Open-Meteo is disabled.

---

## Performance Advisories

### Polar Performance

**Data source:** `PerformanceDataManager` — 5-min rolling averages of polar% and VMG% (channels 58 and 66)

**Prerequisites:** Race timer state == `.racing`, BSP > 2 kt

| Title | Priority | Trigger | Message |
|-------|----------|---------|---------|
| Below Target Performance | Info | 5-min avg polar% > 0 AND < 80% | "Performance averaging X% of polar target over the last 5 min." |
| VMG Below Target | Info | 5-min avg VMG% > 0 AND < 85% | "VMG averaging X% of target over the last 5 min (Y vs Z kt)." |

**Why 5-min averages:** Instantaneous polar% and VMG% from Expedition are too noisy — gusts, waves, and momentary pinches cause false alerts. The 5-min rolling average from `PerformanceDataManager` smooths out transients.

**Auto-clears** when performance recovers above thresholds, when racing stops, or when boat slows below 2 kt.

---

### Excessive Rudder Angle

**Data source:** `PerformanceDataManager.samples` — rolling 2-min average of `abs(rudderAngle)` (rudder is captured in each `PerformanceSample` at ~1 sample / 2s; 15-min retention)

**Prerequisites:** Sailing mode is upwind, BSP > 2 kt

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| Excessive Rudder Angle | Info | Avg \|rudder\| ≥ 5° over last 2 min | "Average rudder angle of X° over the last 2 min — more than optimal." | Consider easing sheets or flattening sails to reduce weather helm. |
| Excessive Rudder Angle | Warning | Avg \|rudder\| ≥ 8° over last 2 min | "Average rudder angle of X° over the last 2 min — rudder is acting as a brake." | Depower: ease mainsheet/traveler, move crew to rail, or reduce sail. |

**Why upwind only:** Reaches and runs naturally require more rudder to steer the boat through waves. Weather helm is a depowering signal specifically on the beat.

**Autopilot note:** Autopilots are forbidden under racing rules, so we assume hand steering. If the pilot is correcting, the same imbalance advice applies.

**Auto-clears** when avg falls below 5°, when boat slows, or when sailing mode changes off upwind.

**Data values logged:** `avgAbsRudderDeg`, `windowSec`

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

## Calibration Advisories

**Data source:** `CalibrationTracker.swift` — detects tacks (AWA sign change) and mark roundings (sailing mode change), stores 5-min TWD, |AWA|, and TWS averages before and after each maneuver

**Tack detection:** AWA sign changes while upwind and BSP > 2 kt  
**Rounding detection:** Sailing mode transitions between upwind and downwind (reaching ignored as transitional)

**Timing windows:**
- Pre-maneuver: 5-min average ending 30 seconds before the maneuver
- Post-tack: 60-second settling window, then 5-min average
- Post-rounding: 90-second settling window (longer — sail changes, acceleration), then 5-min average

**Consistency filter:** All calibration advisories require the delta to have the same sign across all measured maneuvers. If tack 1 shows +5° and tack 2 shows -3°, that is wind oscillation, not calibration — the advisory will not fire.

**Minimum maneuvers:** 3 tacks for TWD/AWA, 3 roundings for TWS

**Discard conditions:** Record is discarded if sailing mode changes during the post-maneuver evaluation window (e.g., mark rounding during the 5-min post-tack averaging)

---

### TWD Calibration Bias (Tack-to-Tack)

**Prerequisites:** Race timer state == `.racing`, sailing mode is upwind

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| TWD Calibration Bias | Info | Mean delta ≥ 3° consistent across 3+ tacks | "TWD reads X° higher/lower after tacking — seen across N tacks." | Monitor over the next few tacks. If it persists, check compass and wind instrument calibration. |
| TWD Calibration Bias | Warning | Mean delta ≥ 5° consistent across 3+ tacks | "TWD reads X° higher/lower after tacking — consistent across N tacks. Likely instrument calibration error." | Check compass calibration and wind instrument alignment. This bias affects all TWD-based tactical decisions. |

**What it detects:** Compass offset or wind direction sensor misalignment. On a well-calibrated boat, the 5-min average TWD should be the same on port and starboard tacks. A consistent delta indicates the compass or wind vane reads differently depending on the boat's heading.

**Does not clear when leaving upwind** — keeps the advisory visible on reaches/runs so the crew remembers the bias exists.

**Data values logged:** `meanDeltaDeg`, `tackCount`, `isConsistent`

---

### AWA Calibration Bias (Tack-to-Tack)

**Prerequisites:** Race timer state == `.racing`, sailing mode is upwind

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| AWA Calibration Bias | Info | Mean |AWA| delta ≥ 2° consistent across 3+ tacks | "AWA reads X° wider/narrower after tacking — seen across N tacks." | Monitor over the next few tacks. If it persists, check mast head unit alignment. |
| AWA Calibration Bias | Warning | Mean |AWA| delta ≥ 4° consistent across 3+ tacks | "AWA reads X° wider/narrower after tacking — consistent across N tacks. Wind instrument likely has a rotational offset." | Check mast head unit alignment. This affects target angles, sail trim, and layline calculations on every tack. |

**What it detects:** Mast head unit (MHU) rotational offset. Compares `abs(AWA)` between tacks — if starboard reads 24° and port reads 18°, the delta is 6° (3° error per side). Tighter thresholds than TWD because AWA directly drives target angle and sail trim decisions.

**Data values logged:** `meanDeltaDeg`, `tackCount`, `isConsistent`

---

### TWS Upwind/Downwind Bias (Rounding-to-Rounding)

**Prerequisites:** None beyond having 3+ mark roundings between upwind and downwind

| Title | Priority | Trigger | Message | Action |
|-------|----------|---------|---------|--------|
| TWS Upwind/Downwind Bias | Info | Mean TWS delta ≥ 8% consistent across 3+ roundings | "TWS reads X kt (Y%) higher downwind/upwind — seen across N roundings." | Monitor over the next few roundings. Review upwash speed correction tables. |
| TWS Upwind/Downwind Bias | Warning | Mean TWS delta ≥ 12% consistent across 3+ roundings | "TWS reads X kt (Y%) higher downwind/upwind — consistent across N roundings. Upwash speed correction likely needed." | Wind speed is being distorted by sail-induced airflow. Check upwash tables in Expedition or Calibrator. |

**What it detects:** Sail-induced airflow acceleration past the mast head unit. Wind speed typically reads 10-15% higher downwind because the sail accelerates air past the sensor to a greater extent at deeper angles. This affects polar targets, VMG calculations, and sail change crossover points.

**Uses percentage thresholds** since the absolute knot difference scales with wind strength (2 kt in 12 kt breeze is 17%; same 2 kt in 20 kt breeze is only 10%).

**Direction handling:** Uses upwind→downwind roundings or downwind→upwind roundings (whichever has more data), flipping the sign so positive always means "reads higher downwind."

**Data values logged:** `meanDeltaKt`, `meanDeltaPercent`, `roundingCount`, `isConsistent`

---

## Advisory Lifecycle

- **Replaced:** Each advisory title replaces its previous version (`replacingCategory:withTitle:`) — no stacking of same advisory type
- **Cleared:** When condition resolves, `removePreviousAdvisories()` is called automatically
- **Dismissed:** User can dismiss; dismissed advisories stay in storage but are hidden from active list
- **Cleanup:** Advisories older than 7 days are purged; max 50 stored (configurable in Advisory Settings)
- **Watch:** Most critical (`.critical`) advisory synced to Apple Watch via WatchConnectivity
- **Storage throttle:** Disk writes throttled to max once per 10 seconds to reduce I/O during frequent checks

---

## Check Order (per `performAdvisoryChecks()`)

1. Barometric pressure
2. Frontal passage
3. Sail change
4. Sail mismatch
5. Safety
6. Performance (polar %, VMG %)
7. Rudder angle
8. Tactical (Layline, Persistent Header upwind, Persistent Header downwind)
9. GRIB accuracy
10. Open-Meteo forecast revision (direction, speed)
11. Calibration (TWD tack-to-tack, AWA tack-to-tack, TWS rounding-to-rounding)
12. Current push
13. Dew point

---

## Files

| File | Contents |
|------|----------|
| `AdvisoryManager.swift` | Core manager, all non-GRIB advisories including dew point, calibration, and Open-Meteo revision |
| `AdvisoryManager+GRIBAccuracy.swift` | GRIB bias advisories (iOS target only) |
| `AdvisoryModels.swift` | `Advisory`, `AdvisoryPriority`, `AdvisoryCategory` structs (iOS + Watch) |
| `AdvisorySettingsView.swift` | Settings UI — enable/disable, category filter, priority filter |
| `CalibrationTracker.swift` | Tack and rounding detection, pre/post TWD/AWA/TWS averaging, bias computation |
| `ForecastComparisonManager.swift` | Raw 15-sec GRIB vs actual logging, 8-hour retention (iOS only) |
| `ForecastModels.swift` | `ForecastComparison`, `ForecastSummaryRow`, `ForecastValidationStats` (iOS only) |
| `OpenMeteoManager.swift` | Hourly HRRR polling, grid snapshots, revision analysis (iOS only) |
| `WeatherBriefingManager.swift` | AI weather briefing prompt construction and Claude API call (iOS only) |
