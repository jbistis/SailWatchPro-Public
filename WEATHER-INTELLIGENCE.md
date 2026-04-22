# SailWatchPro — Weather Intelligence Reference

**Data source:** Open-Meteo API (`/v1/forecast` endpoint — auto-selects best model per location)  
**Manager:** `OpenMeteoManager.swift`  
**Settings:** `SettingsModel.isOpenMeteoEnabled` (default: off)  
**Last updated:** April 2026 (updated for worldwide model support)

---

## Design Philosophy

SailWatchPro's weather intelligence layer runs parallel to the existing GRIB infrastructure. Each serves a distinct purpose:

| Source | Answers | Lifecycle | Owner |
|--------|---------|-----------|-------|
| **GRIB files** | What is Expedition routing on right now? | Navigator downloads manually, loads into Expedition | Navigator below deck |
| **Open-Meteo** | What does the latest model run say, and how is it changing? | Automatic hourly polling, no manual action | SailWatchPro |
| **Buoy observations** | What is actually happening at known stations? | Auto-fetched from NOAA/NDBC | SailWatchPro |
| **Boat instruments** | What is the boat experiencing right now? | Real-time UDP from Expedition | SailWatchPro |

The guiding principle: SailWatchPro owns execution intelligence (sail faster in the wind you have), not routing (where to go). Weather intelligence tells the navigator the forecast may be drifting — it does not say where to sail.

---

## Architecture

### Data Flow

```
RaceAreaManager (bounding box)
        |
        v
OpenMeteoManager (hourly poll at :05)
        |
        v
Open-Meteo API (/v1/forecast, auto-selects best model per location)
        |
        v
JSON response (63 grid points x 24 forecast hours = 1512 data points)
        |
        v
OpenMeteoSnapshot (stored, max 8 retained)
        |
        v
Revision analysis (diff consecutive snapshots)
        |
        v
RevisionSummary (avg direction/speed/pressure deltas across grid)
        |
        +---> AdvisoryManager (forecast revision advisories)
        +---> Settings UI (live trend display)
        +---> AI Briefing pipeline
```

### Key Files

| File | Contents |
|------|----------|
| `OpenMeteoManager.swift` | Core manager — polling, grid generation, API fetch, parsing, snapshot storage, revision analysis, briefing data |
| `AdvisoryManager.swift` | `checkOpenMeteoRevisionAdvisories()` — direction and speed revision advisories |
| `SettingsModel.swift` | `isOpenMeteoEnabled` — persisted toggle, syncs to manager |
| `SimpleSettingsView.swift` | Weather Intelligence settings section with live status |
| `UDPListener.swift` | Initializes `OpenMeteoManager.shared` on app startup (iOS only) |

---

## Grid Generation

The grid is derived from `RaceAreaManager.shared.filteredRaceArea` — the same bounding box used for race course visualization. No dependency on `GRIBFetchArea`.

### Auto-scaling

| Fetch Area Size | Resolution | Approximate Grid Points |
|----------------|------------|------------------------|
| Small (< 1 deg x 1 deg) | 0.10 - 0.25 deg | 25-50 |
| Medium (2 deg x 3 deg) | 0.50 deg | 50-80 |
| Large (> 4 deg x 5 deg) | 0.75 - 1.00 deg | 80-150 |

Target range: 25-150 grid points. Resolution bounds: 0.1 deg minimum, 1.0 deg maximum.

Grid points are sent to the API as paired lat/lon arrays (not separate axis arrays). All points go in a single HTTP request — Open-Meteo supports up to 1,000 locations per call.

---

## Polling Schedule

| Event | Timing |
|-------|--------|
| Cold start (no cached snapshots) | Immediate fetch |
| Warm start (cached snapshots exist) | Wait until :05 past next hour |
| Recurring | Every hour at :05 past the hour |
| Manual | "Fetch now" button in Settings |

The :05 offset gives weather services time to propagate model data through Open-Meteo's pipeline after each model run.

### Model Selection

Open-Meteo's `/v1/forecast` endpoint automatically selects the best available weather model for each location:

| Location | Primary Model | Resolution | Update Frequency |
|----------|--------------|------------|-----------------|
| US CONUS | HRRR | 3 km | Hourly |
| Central Europe | ICON-D2 | 2 km | Every 3 hours |
| Europe (wider) | ICON-EU | 7 km | Every 6 hours |
| Global fallback | GFS / ICON | 13-25 km | Every 6 hours |

SailWatchPro does not specify a model — the endpoint handles selection transparently. The `modelName` field in each snapshot is stored as "auto (best available)" for reference.

SailWatchPro requests 24 hours of forecast (`forecast_days=1`). For models with shorter forecast horizons, Open-Meteo may blend with a global model for later hours — this is acceptable since the first 12-18 hours are the tactically relevant ones.

---

## Snapshot Storage

| Parameter | Value |
|-----------|-------|
| Max snapshots retained | 8 (8 hours of history) |
| Storage location | `Documents/openmeteo_snapshots.json` |
| Save throttle | Max once per 30 seconds |
| Pruning | Snapshots older than 8 hours removed on load |

Each snapshot contains: fetch timestamp, model name, grid coordinates, and all grid point forecasts (lat, lon, forecast time, wind speed, wind direction, wind gusts, pressure, temperature).

---

## Revision Analysis

When a new snapshot arrives, it is diffed against the previous snapshot. For each grid point and forecast hour present in both snapshots, the following deltas are computed:

| Delta | Unit | Method |
|-------|------|--------|
| Wind direction | degrees | Shortest angle difference |
| Wind speed | knots | Simple difference |
| Pressure | hPa | Simple difference |

These roll up into a `RevisionSummary`:

| Field | Description |
|-------|-------------|
| `avgWindDirectionDelta` | Mean direction change across all grid points |
| `avgWindSpeedDelta` | Mean speed change across all grid points |
| `maxWindDirectionDelta` | Largest absolute direction change at any grid point |
| `avgPressureDelta` | Mean pressure change across all grid points |

### Monotonic Detection

`isDirectionRevisionMonotonic` checks whether the last N revision summaries all share the same sign for direction change. If the model keeps backing the wind 3 deg each update for 4 consecutive hours, the revision is monotonic — something real is happening that the original forecast missed.

---

## Advisories

Two advisories in `AdvisoryManager`, category `.weather`. Checked every 5 minutes via the standard advisory cycle. Requires at least 3 snapshots (2 revision summaries) before firing.

### Forecast Wind Direction Shifting

| Priority | Trigger | Monotonic Required |
|----------|---------|--------------------|
| Info | Avg revision >= 3 deg/update | No |
| Warning | Avg revision >= 6 deg/update | Yes |
| Critical | Avg revision >= 10 deg/update | Yes |

**Message example:** "Forecast model has shifted wind direction 8 deg veering per update over the last 3 hours."  
**Action:** "Monitor the trend. The forecast Expedition is routing on may be drifting from reality."  
**Auto-clears** when revision trend drops below 3 deg/update or Open-Meteo is disabled.

### Forecast Wind Speed Shifting

| Priority | Trigger | Monotonic Required |
|----------|---------|--------------------|
| Info | Avg revision >= 1.5 kt/update | No |
| Warning | Avg revision >= 3.0 kt/update | Yes |
| Critical | Avg revision >= 5.0 kt/update | Yes |

**Message example:** "Forecast model has revised wind speed 3.2 kt stronger per update over the last 3 hours."  
**Action:** "The forecast may be under- or over-predicting wind. Monitor boat instruments against the forecast."  
**Auto-clears** when revision trend drops below 1.5 kt/update or Open-Meteo is disabled.

**Threshold note:** These are initial values for tuning. After on-water validation, thresholds may need adjustment — especially the info tier, which could be noisy in unstable weather patterns.

---

## Settings UI

Located in `SimpleSettingsView` under "WEATHER INTELLIGENCE", after "AI WEATHER BRIEFINGS".

### Elements

| Element | Description |
|---------|-------------|
| Toggle | Enable/disable forecast monitoring |
| Status dot | Gray (disabled), Orange (waiting/no data), Green (active), Red (error) |
| Status text | "Disabled", "No race area loaded", "Waiting for first fetch", "Active — N snapshots" |
| Last update | Time and snapshot count |
| Grid | Dimensions and forecast hours |
| Direction trend | Degrees/update with veering/backing label. Bold orange when >= 5 deg |
| Speed trend | Knots/update with increasing/decreasing label. Bold orange when >= 2 kt |
| Error display | Shows last fetch error if any |
| Fetch now | Manual refresh button with spinner |

### Footer

Orange when enabled: "Requires a loaded race course and internet connection. Data via Open-Meteo (HRRR for US, ICON for Europe, best model elsewhere)."  
Gray when disabled: "Enable to monitor how the forecast model is revising across your race area."

---

## API Details

| Parameter | Value |
|-----------|-------|
| Endpoint | `https://api.open-meteo.com/v1/forecast` |
| Model selection | Auto — best model per location (HRRR for US, ICON-D2 for Europe, etc.) |
| Variables | `wind_speed_10m`, `wind_direction_10m`, `wind_gusts_10m`, `pressure_msl`, `temperature_2m` |
| Wind units | Knots (via `wind_speed_unit=kn`) |
| Forecast window | 1 day (`forecast_days=1`) |
| Timezone | UTC |
| Format | JSON (default) |

### API Usage

| Scenario | Calls/hour | Calls/day |
|----------|-----------|-----------|
| 1 device, 63 grid points | 1 | 24 |
| 6 devices, 63 grid points each | 6 | 144 |
| Free tier limit | — | 10,000 |
| Paid plan ($29/mo) | — | ~33,000 |

Currently each device fetches independently. Future optimization: coordinator device fetches once, distributes via inter-device sync.

---

## AI Briefing Pipeline

`WeatherBriefingManager.swift` orchestrates the AI weather briefing by collecting data from five sources and sending a structured prompt to the Anthropic API (Claude Sonnet).

**Data sources fed to Claude:**
- Boat instruments (TWD, TWS, BSP, SOG, current, pressure, temperature, dew point)
- Buoy observations (up to 8 nearest stations with wind data and age)
- Open-Meteo revision trends (via `briefingData().asPromptText()`)
- GRIB accuracy (TWD and TWS bias from `ForecastComparisonManager`)
- Coastal effects (sea breeze, land breeze, friction shift)

**Prompt instructions:** Claude acts as a racing meteorologist. Direct and concise for reading on a bouncing boat. No routing advice — that is the navigator's job. Ends with a confidence summary.

**Delivery:** `WeatherBriefingCard` in the Wind section. Manual trigger via "Generate briefing" button. ~$0.01 per briefing. Requires API key configured in Settings.

`OpenMeteoManager.briefingData()` produces an `OpenMeteoBriefingData` struct. `asPromptText()` renders it as plain text including forecast time range and model revision trends.

---

## Multi-Model Support (Future)

The architecture supports querying multiple weather models by changing the `modelName` property or making parallel requests. Each snapshot stores its model name, so revision analysis can be model-specific.

Candidate models for comparison:

| Model | Resolution | Coverage | Update Frequency |
|-------|-----------|----------|-----------------|
| HRRR | 3 km | US CONUS | Hourly |
| GFS | 25 km | Global | Every 6 hours |
| ECMWF IFS | 9 km | Global | Every 6 hours |
| ICON | 13 km | Global | Every 6 hours |
| ICON-EU | 7 km | Europe | Every 6 hours |

The navigator's workflow: compare which model is tracking reality best for this particular weather pattern, then weight routing decisions accordingly.

---

## Roadmap

### Built (April 2026)
- [x] OpenMeteoManager with hourly polling (worldwide model support)
- [x] Auto-scaled grid from race area bounding box
- [x] Snapshot storage with 8-hour retention
- [x] Revision analysis between consecutive snapshots
- [x] Monotonic revision detection
- [x] Two forecast revision advisories (direction, speed)
- [x] Settings toggle with live status display
- [x] Forecast Revision card in Wind section
- [x] AI weather briefing (Claude Sonnet via Anthropic API)
- [x] Weather Briefing card in Wind section
- [x] Forecast time range display (card footer and briefing prompt)
- [x] Worldwide model support (/v1/forecast — HRRR US, ICON-D2 Europe, auto elsewhere)

### Next
- [ ] Multi-model comparison (query specific models side-by-side)
- [ ] Coordinator-based fetch (one device fetches, distributes to fleet via sync)
- [ ] Spatial visualization of revision patterns on navigator map (heat map overlay)
- [ ] "Enter this in Expedition What-If" suggestions based on observed forecast error

---

## Session Log — April 20, 2026

### Advisories Fixed
- **Sail Change advisory** — was test-mode only, now live. Added racing-state gate. Uses `ExpeditionDataManager.shared.data` instead of `nil`.
- **Performance advisory** — was test-mode only, now live. Switched from instantaneous Expedition values to 5-min rolling averages via `PerformanceDataManager`. Added racing-state and BSP > 2.0 gates. Added auto-clear when performance recovers.

### New Advisory
- **Persistent Header — Downwind** — gybe-on-a-header advisory mirroring the upwind version. Same signal processing (three 2-min circular-averaged TWD buckets, monotonicity filter, 5/10 deg thresholds). Sign formula drops the negation: `signedHeader = totalShift x sign(AWA) > 0`.

### Open-Meteo Weather Intelligence Layer
- Full pipeline: race area -> grid -> API -> parsing -> snapshots -> revision analysis -> advisories -> settings UI
- Verified live with 8 snapshots accumulated, 1512 data points per fetch
- Settled on RaceAreaManager as bounding box source (not GRIBFetchArea)
- Fixed API issues: dropped explicit model parameter, fixed grid to send paired lat/lon arrays
- Added :05 past the hour polling alignment for data propagation delay
- Added cold-start immediate fetch
- Added Settings UI with live status, trends, and manual fetch
- Gated with `#if !os(watchOS)` where needed
- Switched from /v1/gfs to /v1/forecast for worldwide model support (HRRR for US, ICON-D2 for Europe, auto elsewhere)
- All UI and advisory text updated from HRRR-specific to model-agnostic
