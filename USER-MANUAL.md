# SailWatchPro

<p align="center">
  <a href="https://sailwatchpro.com/">
    <img alt="SailWatchPro" title="SailWatchPro" src="images/icon-76x76@2x.png">
  </a>
</p>

<p align="center">
  <strong>User Manual</strong>
</p>

---

## Table of Contents

- [Introduction](#introduction)
- [Getting Around](#getting-around)
- [Dashboards](#dashboards)
- [Pre-Start](#pre-start)
- [Start](#start)
- [Navigator](#navigator)
- [Competitors](#competitors)
- [Advisories](#advisories)
- [Wind](#wind)
- [Weather](#weather)
- [Sails](#sails)
- [Crew](#crew)
- [The Boat's Devices](#the-boats-devices)
- [Events, Expedition Control and Incoming Data](#events-expedition-control-and-incoming-data)
- [MOB](#mob)
- [Apple Watch](#apple-watch)
- [Apple Watch Tips](#apple-watch-tips)
- [Settings Reference](#settings-reference)
- [What Needs a Plan](#what-needs-a-plan)
- [System Requirements](#system-requirements)
- [Support & Updates](#support--updates)

---

## Introduction

SailWatchPro is a racing app for iPad, iPhone and Apple Watch. It reads the boat's instruments, from Expedition Marine, an NMEA 2000 gateway, a B&G display network or the iPad's own GPS, and turns them into the numbers and calls a crew needs on deck: dashboards, the start, the course, competitors, wind and weather, sails and advisories. Expedition Marine is optional: the app works from a gateway or the iPad's GPS alone, and where Expedition is aboard it adds the integration, sending pings, the gun, sail and crew events and MOB to it and taking its marks and courses.

The boat is set up once on the web at [sailwatchpro.com](https://sailwatchpro.com) and imported to each device. The app is free; a plan unlocks its paid half. This manual describes what each screen does. It deliberately has no screenshots, so it stays true from build to build; the [README](README.md) carries a gallery.

- For installation, network, Expedition and first-time configuration, see the [Setup Guide](SETUP-GUIDE.md).
- For plans, the licence and crew access, see the [Subscription & Licensing Guide](SUBSCRIPTION-AND-LICENSING.md).
- For connection problems, see the [Troubleshooting Guide](TROUBLESHOOTING.md).
- For every advisory's trigger and wording, see the [Advisory Reference](ADVISORY-REFERENCE.md).

---

## Getting Around

On iPad the sections are in the sidebar: Dashboard, Pre-Start, Start Line, Navigator, Competitors, Wind, Barometer, Weather Data, Advisories, Sails, Sail Control, Sail Crossover, Polars, Crew, Crew Positions, Events, Expedition Control, GRIB Files, Incoming Data and Settings.

On iPhone the main sections are tabs, and the rest are under **More**: Advisories, Sail Control, Sail Crossover, Sail Inventory, Buoy Weather Data, Crew Positions, Crew Members, Events, GRIB Files, Polars and Settings.

Every screen shares a toolbar that shows the connection state of the boat's data sources. Green means data is arriving.

---

## Dashboards

Dashboards show the boat's numbers, large, in a grid you lay out yourself. Layouts run from a single field (1×1) through 2×1, 2×2, 2×3 and 3×2 to a 3×3 grid, plus a 3×2 layout with a wind chart in it. Each field can hold any channel the boat sends or any value the app computes.

**Computed channels.** COG, SOG, VMG, VMG%, VMC, VMC%, Polar% and Target Boat% are available as live values and as 5, 10 and 15-minute rolling averages.

**Context switching.** Many fields change what they show by sailing mode, upwind, reaching or downwind, so one layout serves the whole race. Fields colour themselves when a value is out of bounds.

Dashboards can be renamed and reordered.

---

## Pre-Start

Pre-Start is where the course is chosen, the line is pinged and the timer is set.

**Timer.** Tap 15, 10, 5, 3 or 1 to set the countdown. **SYNC** rounds the running timer to the nearest whole minute, **KILL** stops it, and the plus and minus buttons nudge it by a second. **Set Custom Start Time** sets the gun to a clock time. A class flag indicator and **P Flag** follow the sequence.

**Start line.** Long-press **SET** at **Port Pin** and **Starboard Pin** to ping the ends as the boat passes them. Pings are taken at the bow when **Bow to GPS** is set. The line length and bias are shown, with a warning if the two ends are almost on top of each other. **Swap ends** fixes a line pinged the wrong way round. **Edit Line** lets you set an end from a mark or an entered position instead of a ping.

**Courses.** **Race Courses** lists courses from two places: Expedition Marine, requested with **Refresh**, and the boat's marks and courses on the web, as of the last Import Setup. Select one and the Navigator takes it up. The course the boat is racing is shared between the boat's iPads, so an iPad that joins late is told which course the others are on.

**Windward-leeward setup.** For a W/L course without a published mark list, enter the windward mark's bearing and range, the leeward mark range, laps, gate width, an offset mark and a finish line, and the app builds the course.

**Expedition.** Pings and the start time are sent to Expedition when it is aboard, so both keep the same line and the same gun. With a B&G display network and the setting on, the start line and start time are pushed to the displays as well.

---

## Start

The Start view is the start box. It draws your boat against the line and the pin laylines, with time to the line and time to burn for the port end, the middle and the starboard end, the distance below the line, the wind and the current as the instruments see them, and the heading to the first mark. Wind strip charts under the box show what the breeze has done over the last minutes.

---

## Navigator

The Navigator shows the course and the boat on a map, with a table view of the marks and the tactical numbers for the leg.

**Map and table.** Switch between **Show map view** and **Show table view**. **PREV MARK** and **NEXT MARK** move the active mark; **Auto Mark Detection** in Settings advances it as you approach. The table lists every mark with bearing, range and the expected wind angle on each leg.

**Tactical Data.** A card alongside the map carries the leg's numbers: TWD and TWS, target speed and angle, VMG, performance against the polar, and the rounding. The **Rounding** cell says what happens at the next mark, whether you arrive and leave on the same tack or a gybe is in the rounding, and whether it leads into or out of a run. Its info button opens the crew's own procedure for that drop, written on the web under Playbook.

**Favored Side.** Which half of the beat or the run pays, and on what evidence: the forecast shift, the current, or the buoys. It hides itself on a reach or in light air rather than show a number it cannot stand behind.

**Tidal Gate.** When a tidal gate is within range, which way to take it and whether that answer still holds when you get there. Hidden the rest of the time.

**Douse card.** The crew's drop procedures gathered in one place to read on the way out to the course.

**Buoys.** Weather buoys near the course are drawn on the map with their latest wind. Tap one for the 24-hour chart of what it measured against what each forecast model said, graded by how close each model has been.

**Chart map.** Behind **Chart map (beta)** in Settings, the Navigator draws on SailWatchPro's own chart: NOAA depths, contours, soundings and buoys. It adds:

- **Forecast wind**, drawn as barbs for the chosen model and hour, with a slider through the forecast.
- **Current**, as a coloured speed field with streamlines, from Current Lab where the boat has it or from the public current model otherwise.
- **Depth**, the water a routing depth grid closes to this boat shown in red, so the grid can be trusted before a route depends on it.
- **Routing**, the fastest route from the boat to the next mark from the polar, the shown forecast, the current and the depth grid, worked out on the device from data already aboard. A line under the map says how long it takes, what to sail now, and what it was worked from.
- **Long-press** anywhere on open water for the forecast wind and current at that point for the hour shown.
- **Saved for offline.** The race area, the course with a margin for laylines and a wide tack, can be downloaded at the dock and used with no signal.

The chart map is marked not for navigation. It is a thinned copy of the chart under the tactics, not a replacement for the boat's plotter.

**GPX routes.** Routes exported from other software can be imported and shown.

---

## Competitors

The Competitors screen is the fleet: who is racing, where they are, and how you stand against them.

**Where competitors come from.** The fleet for an event is set up on the web and imported with **Import Crew & Competitors for Event**. Boats can also be added by hand with **Add Competitor**, or taken from **Detected Vessels**, the AIS targets the boat's receiver is hearing. Positions come from AIS and from other SailWatchPro boats on the network.

**Own boat.** **Choose my boat** marks which entry is yours, so the app can score you against the others.

**Cards.** Each racing competitor shows bearing, range, course and speed, how fresh its AIS is, elapsed and corrected times, VMC, lateral separation, and whether it is on a different leg. **OUR LEAD** and **CORR. LEAD** give the gap on the water and on corrected time.

**Scoring.** **Race Setup** holds the class flag, class type and scoring system, PHRF or ORC, with the ORC options the certificate allows, and a link to the regatta page. The finish card lets you tap each boat as it crosses to record its time, and shows the finish margins.

**Sorting and filters.** Sort by name, distance, threat and more; search by name or MMSI; hide boats with no AIS.

---

## Advisories

Advisories are the app's calls: conditions it watches so the crew does not have to. They are checked every five minutes, each new advisory replaces the previous one of its type, and a cleared condition clears its advisory. The most important active advisory is pushed to the Apple Watch.

| Category | Examples |
|----------|----------|
| Weather | Barometric pressure trend, frontal passage, dew point, forecast accuracy |
| Sail | Sail change recommended, approaching a crossover |
| Safety | Shallow water, depth sensor failure, excessive heel |
| Tactical | Sail mismatch, layline, mark reachable, board to the mark, persistent header, wind shift approaching, forecast shift |
| Performance | Below polar target, target angle, rudder angle, current or leeway push |
| Calibration | TWD and AWA bias tack to tack, TWS bias upwind against downwind |

The Advisories screen shows what is active, a history, and settings: which categories to receive, a priority filter, and a test mode that raises sample advisories. Safety advisories are free; the other categories need a plan.

Triggers, thresholds and wording for every advisory are in the [Advisory Reference](ADVISORY-REFERENCE.md).

---

## Wind

The Wind screen treats the boat as a moving weather station.

**Trend.** TWD and TWS over a chosen time window, with rolling averages, the current pattern, the expected next shift and where the centre is heading, each with a confidence. The wind history syncs between the boat's devices, so every iPad sees the same breeze.

**Weather Models.** How each forecast model has done against the boat's own instruments, graded over the recent window, and which one to believe today. The same grading appears for every weather buoy.

**Forecast Revision.** How the forecast for the current hour has changed across the race area from one model run to the next.

**Coastal Effects.** Where the shore bends or lifts the breeze along the course, from the forecast and the coastline. Needs an internet connection.

**AI Weather Briefing.** A written briefing for the race from the forecasts and the boat's position, generated with Claude when the owner has switched briefings on. See [Settings](#settings-reference).

**Strip chart.** A time-series view of any channel against the forecast, with the forecast line drawn inside the chart's natural range or as a badge at the edge when it falls outside it.

---

## Weather

**Buoy Weather Data.** The weather stations near the race area, fetched on a schedule. The list is seeded from SailWatchPro's buoy catalog and can be synced from the cloud as stations are added. Each station shows the latest wind and gust, its trend, the range from the boat, and a 24-hour chart of measured wind against every forecast model, with each model graded on how close it has been. Fetch interval and search radius are set from the screen.

**Barometer.** The boat's pressure, its rate of change and a forecast hint, with a chart over a chosen window.

**GRIB Files.** Import GRIB files and choose the active one. Its wind is drawn on the Navigator and compared with the buoys. Downloads need a weather coverage area to be defined in Settings.

**Weather Intelligence.** With forecast monitoring on, the app polls the weather models hourly across the race area to track revisions, and drives the forecast barbs, the model grading and the routing. It needs an internet connection to update, and keeps the last snapshot offline.

---

## Sails

**Sail Control.** The sails aboard, and one-tap logging of hoists and drops. Each change is sent to Expedition and to the other devices on the boat, and the hoist log is uploaded to the web Logbook. The sail list comes from the web; **Sails aboard** lets you mark what was left on the dock so the crossover advice only names cloth you carry.

**Sail Crossover.** The sailmaker's crossover chart and a performance chart built from the boat's own logged sailing, showing the optimal sail for the current wind and the crossings nearby. The chart comes from the web.

**Polars.** The boat's polar tables, synced from the web: the navigation polar that drives targets and routing, and the performance, start, heel and tack-specific slots, each with its data points and status.

**Forestay Load Targets.** Target forestay load by wind speed, with the rig's maximum as a cap, synced from the web.

**Tuning Guide.** The boat's tuning table from the web.

**Sail Inventory.** The sails on file with area, weight, colour and group.

---

## Crew

**Crew Members.** The roster for the event, imported with **Import Crew & Competitors for Event**. The roster is kept on the web.

**Crew Positions.** The boat's positions and who is in each. Positions are filled from the roster, and a change of position is logged with one tap and sent to Expedition and the other devices. Filters show only assigned positions or only crew on board. Positions are uploaded to the web for the race record.

---

## The Boat's Devices

Every SailWatchPro device on the boat's WiFi talks to the others on a channel of its own, separate from Expedition and the gateway. Nothing needs to be set up for it; devices on the same network find each other.

**What travels between all devices.** Decisions a person made, each stamped with when it was made, so the newest wins and two iPads editing the same thing seconds apart end up agreeing: sail hoists and drops, crew position changes, which sails are aboard, a KILL on the timer, the answer to "is this a new race?", and the race setup. When Expedition is not aboard, the start line, the gun and the chosen course travel this way too, so five iPads keep one line rather than five.

**The coordinator.** The devices elect one of their number as the boat's coordinator: the one that has been running longest, among those allowed the role. The coordinator answers for the boat where there has to be exactly one answer:

- It hands the boat's plan to any device aboard that has not imported it, with a 45-day lease.
- It holds the authoritative sail and crew state for a device that joins mid-race and asks.
- It alone writes to a B&G display network: the display outputs once a second, and the race timer.
- It alone records the start line and the boat track for the web Logbook, so the race has one record.

If the coordinator goes quiet for a minute the others elect again, so a coordinator that is switched off or leaves the boat is replaced on its own.

**Which iPad should coordinate.** In Settings, under Data Sources, **Allow Coordinator Role** says whether this device may be elected. Leave it on for the nav-station iPad and any device that stays aboard and powered. Turn it off on a crew iPhone or iPad that comes and goes, so the boat is never coordinated by a device that is about to leave. Settings shows **This iPad is the boat's coordinator** when it is.

**Taking it over.** **Make this iPad the coordinator**, in the same place, is for the case the election cannot fix: the longest-running device is an iPad in a bag below, or one nobody can find. The claim holds for twelve hours.

**Keep every device on the same build.** A device on an older build than the others is heard but not trusted with anything that changes the boat's state, and cannot become coordinator.

---

## Events, Expedition Control and Incoming Data

**Events.** A log of what happened and when: the gun, the finish, line pings, sails up, race legs, MOB, photos, tech problems and notes. Events can be added by hand, searched, and exported as a CSV.

**Expedition Control.** Sends commands to Expedition Marine: **Set Race Start Time** overwrites Expedition's timer with the gun this iPad recorded, to the second, and a past time sets a race already under way. The **Response Log** shows what Expedition answered.

**Incoming Data.** The raw lines arriving from each data source, as a check that the boat is being heard. A source that is not set to provide something on the web is shown as ignored for it.

---

## MOB

The MOB button marks a person in the water. The MOB view then shows the marked position, the time in water, the estimated position as the current carries the person, the set and drift it is using, navigation guidance back to them, and an estimate of hypothermia risk and survival time from the water temperature. The incident is sent to Expedition Marine, and from there to the boat's plotters. **Clear MOB** ends it, with a confirmation.

---

## Apple Watch

The Watch app shows the numbers that matter on the rail, fed by the paired iPhone.

| View | What it shows |
|------|---------------|
| Race Timer | The start sequence |
| Next Mark | Bearing and range to the active mark, with mark ETA and the recommended sail |
| Boat speed, heel, VMG, TWA and AWA | Split boxes with performance indicators |
| Depth | Depth with automatic switching to it when the water gets thin |
| Wind state | The current pattern and trend |
| Strip chart | A channel over a chosen window |
| Custom field | Any dashboard field |
| Advisories | The active advisories, with the most important pushed as it arrives |

Watch settings cover draft, the TWA threshold, display mode including a night-vision red, and audio. The Watch does not need a plan of its own.

---

## Apple Watch Tips

These are iPhone and Watch system settings, not app settings. They control how watchOS behaves and how the iPhone delivers data to the Watch.

### Keep SailWatchPro on the Watch Face

By default the Watch returns to the clock after a couple of minutes, which means SailWatchPro disappears mid-race.

**On the iPhone:** open the **Watch** app, tap **General → Return to Clock**, find **SailWatchPro** and select **Don't Return to Clock**.

**On the Watch:** **Settings → General → Return to Clock**, scroll to **SailWatchPro** and turn off **Return to Clock**.

Also enable **Wake Screen on Wrist Raise** and, on a Watch that has it, **Always On**.

### Keep iPhone Data Flowing to the Watch

When the iPhone locks or enters a low-power state, iOS can throttle Bluetooth and suspend background apps, which stops data reaching the Watch.

| Setting | Path | During racing |
|---------|------|---------------|
| Auto-Lock | Settings → Display & Brightness → Auto-Lock | **Never** |
| Low Power Mode | Settings → Battery | **Off** |
| Background App Refresh | Settings → General → Background App Refresh | **On** for SailWatchPro |
| Location Services | Settings → Privacy & Security → Location Services → SailWatchPro | **Always**, with **Precise Location** on |

Keep the iPhone on power when possible, and close to the Watch: a cockpit pocket beats the nav station, since rigging, wet sails and the deck all cut Bluetooth range. Restore Auto-Lock after sailing.

### Checking Watch Battery

Swipe up for Control Center, add the **Battery** complication to the watch face, or add the **Batteries** widget to the iPhone's Today View.

---

## Settings Reference

Settings is one long screen in sections. The sections you touch once, on day one, are covered step by step in the [Setup Guide](SETUP-GUIDE.md); this table says what each section is for.

| Section | What it does |
|---------|--------------|
| **Account** | Sign in and out, **Import Setup** to pull the boat's configuration from the web, and **Switch boat from web** for a device that moves between boats. See the Setup Guide. |
| **Data Sources** | What the boat's sources are and whether this device hears them. Sources are defined on the web; here you switch **Receive gateway data** off on iPads that do not need AIS, see which Expedition machine commands go to, **Allow Coordinator Role** and **Make this iPad the coordinator** (see [The Boat's Devices](#the-boats-devices)), and enable the B&G display outputs and timer start. |
| **Boat Configuration** | Boat name, MMSI, length, bow to GPS, draft, mast height, maximum forestay load, reaching threshold and minimum tactical wind. Filled from the web on Import Setup; change them there. |
| **Wind Calculation Options** | Let the app derive TWA and TWS, or TWD, from apparent wind and boat data when the instruments do not send them. |
| **AI Weather Briefings** | On or off. Briefings use the boat owner's Anthropic key, set on the web under Documents & config. Nothing is stored on the device. Switch off for races that prohibit paid services. |
| **Weather Intelligence** | **Enable forecast monitoring** polls the weather models hourly across the race area. Shows the active model, the last update, the grid and the trends, with **Fetch now**. |
| **Weather Coverage** | The bounding box for GRIB downloads and forecast polling. With none set, the race course plus 30 NM is polled; add an area to widen the horizon or to enable GRIB downloads. |
| **Instrument Log** | Records every channel once a second to a file in Expedition's format. Switch on at the dock; the iPad can lock while it records. Share the file to the web Logbook after the race. |
| **Buoys** | Your personal buoy list, and a sync of the catalog from the cloud. |
| **Advisory Events** | Uploads advisory events to the web for post-race analysis. Queued locally and sent when there is a connection. |
| **Sail Hoists**, **Boat Track**, **Heard AIS**, **Crew Positions** | What this device has recorded for the web Logbook, what is queued and when it last uploaded. |
| **Uploads** | Status of all uploads to the web. |
| **Channel Health** | Learns which Expedition channels this boat normally sends and flags the ones that have gone silent. Learned per boat. **Run Check Now** and **Reset Learned Channels**. |
| **Display & Navigation** | **Auto Mark Detection**, **Night Vision** (red for night sailing; light and dark otherwise follow iOS), **Throttle Interval** for the update rate from 20 Hz to 1 Hz, **Chart map (beta)** with its depths in feet or metres, and **Map Style**. |
| **Development** | **Test Mode** runs the app on a recorded race instead of the live listener, for training and demos off the boat. Some screens freeze while it is on. |
| **Licenses** | Read-only. Expedition Marine's status and Site Code, with **Refresh**. SailWatchPro's plan, where it came from (sign-in or another device on this boat), who granted it and when it renews. **Remove plan from this device**. The Device ID for support. |
| **Debug** | Password-protected developer tools and the Sync ID. |

---

## What Needs a Plan

The app is free. Four features need the boat to be on a plan, Instruments or Expedition:

1. Advisories in every category except Safety
2. The chart map, and with it routing, the forecast overlay, Current Lab and the depth grid
3. Competitors, on the map and in their own screen
4. The instrument log recorder, and log upload and analysis on the web

A locked feature says "Available on the Instruments plan." and nothing more. Plans are chosen and managed on the web; see the [Subscription & Licensing Guide](SUBSCRIPTION-AND-LICENSING.md).

---

## System Requirements

| Platform | Minimum |
|----------|---------|
| iPad / iPhone | iOS 18.5 |
| Apple Watch | watchOS 11.5 |
| Expedition Marine | Optional. A current release if the boat runs it; Expedition updates often. |

A reliable boat WiFi is required. An NMEA 2000 gateway or AIS source is required for competitor positions from AIS; Expedition does not forward them. An internet connection is required for sign-in, Import Setup, buoy data, forecasts and briefings; the app runs offline on the water once set up.

---

## Support & Updates

Keep every device on the same version. Builds are announced through TestFlight.

- **Support:** support@sailwatchpro.com
- **Bugs and feature requests:** https://github.com/jbistis/SailWatchPro-Public/issues

Happy sailing! ⛵
**SailWatchPro Team**
