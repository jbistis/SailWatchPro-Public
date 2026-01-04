# SailWatchPro

<p align="center">
  <img alt="SailWatchPro" src="images/icon-76x76@2x.png" width="96">
  <br><br>
  <strong>Win More Races. Make Faster Decisions.</strong>
</p>

<p align="center">
  <a href="https://apps.apple.com/us/app/testflight/id899247664">
    <img src="http://i.imgur.com/0n2zqHD.png" width="140">
  </a>
</p>

<!-- <p align="center">
  <strong>Limited Beta – Join via TestFlight</strong><br>
  <a href="https://testflight.apple.com/join/YOUR_BETA_CODE_HERE">
    <img src="https://developer.apple.com/assets/elements/testflight/testflight-badge.svg" width="200" alt="Join Beta on TestFlight">
  </a>
</p>

<p align="center">
  SailWatchPro is currently in limited beta with a small group of competitive boats.<br>
  Full App Store release and pricing details coming soon — request an invite for early access.
</p>

<p align="center">
  **Request Beta Invite** → [james.bistis@icloud.com](mailto:james.bistis@icloud.com?subject=SailWatchPro%20Beta%20Invite%20Request)  
  or email directly: james.bistis@icloud.com
</p>

<p align="center">
  [Report Issues & Suggestions →](https://github.com/jbistis/SailWatchPro-Public/issues)
</p> -->

SailWatchPro extends Expedition Marine above-deck with a modern, touch-first iOS interface for iPad, iPhone, Mac, and Apple Watch. It synthesizes real-time data into clear, actionable insights and advisories — helping you make faster, more confident decisions on the water.

## Key Pillars
- **Racing Management** — Pre-start, start line, course marks, course map, and customizable dashboards
- **Weather Observations & Analytics** — Boat Instruments + Buoys + GRIB fusion, trend analysis
- **Competitor Tracking** — Live Leaderboard and map with corrected time and distance & fleet awareness, ORC Interface
- **Strategic & Tactical Advisories** — Automated high-value alerts

### Racing Management
**Pre-Start & Start Line**  
Expedition provides precision timing, line pings, and bias. SailWatchPro makes it mobile and intuitive — above-deck touch controls for pinging, timer, course selection, and visual dashboards for approach decisions.

<div align="center">
  <img src="images/swp-prestart-view-light.png" width="512">
  <br><em>Pre-Start Dashboard</em>
</div>

<div align="center">
  <img src="images/swp-iPad-start-view-light.png" width="512">
  <br><em>Start Line Visuals & Bias</em>
</div>

### Weather Observations & Analytics
Automatic polling of nearby buoys (NOAA, NDBC, etc.) within 100nm. Overlay predicted GRIB vs. actual observations, track divergences in real time.
<div align="center">
  <img src="images/swp-buoy-list-view-light.png" width="512">
  <br><em>Automated recurring buoy data fetching</em>
</div>


**Weather Station Wind Analysis**  
Visually compare buoy observations with GRIB forecasts and trends for every key station — see exactly how reality is diverging across the race area.
<div align="center">
  <img src="images/buoy-observed-grib.png" width="512"> <!-- Use your Virginia Key screenshot here -->
  <br><em>Buoy: Predicted vs. Actual Wind Trends</em>
</div>

**Boat Instrumentation Wind Analysis**  
Your boat is a moving weather station. SailWatchPro analyzes real-time wind trends using rolling averages, FFT, and wavelet transforms to identify veering/backing, building, and oscillating patterns — with confidence indicators and a 6-hour wind history that syncs across devices.

<div align="center">
  <img src="images/swp-boat-location-forcast-portrait-light.png" width="512"> <!-- Use your Virginia Key screenshot here -->
  <br><em>Buoy: Predicted vs. Actual Wind Trends</em>
</div>

### Competitor Tracking
Live corrected time vs. handicap, lateral separation visualization — know instantly if you're gaining or losing on corrected time, even when boats are physically ahead or behind.
<div align="center">
  <img src="images/swp-competitor-view-light.png" width="512"> <!-- Use your Virginia Key screenshot here -->
  <br><em>Boat: Predicted vs. Actual Wind Trends</em>
</div>

### Strategic & Tactical Advisories
Centralized, customizable alerts that monitor for you: current push, leeway drift, sail mismatches, barometric trends, and more — so you can focus on steering and tactics.

<div align="center">
  <img src="images/swp-advisories-light.png" width="512"> <!-- Use your Virginia Key screenshot here -->
  <br><em>Advisories in realtime/em>
</div>

**Dashboards**  
12 customizable layouts (any Expedition channel + computed metrics like 5/10/15-min averages). Context-aware alerts help maintain trim, avoid overstanding, and correct drift.
<div align="center">
  <strong>Select any channel, including computed channels derived from Expedition Marine Channels</strong><br>
</div>
<div align="center">
  <img src="images/swp-dashboard-select-channels-dashboards-landscape-light.png" width="512"/>
</div>

---

<div align="center">
  <strong>Prestart Dashboard Example</strong><br>
</div>
<div align="center">
  <img src="images/swp-dashboard-3x3-prestart-landscape-light.png" width="512"/>
</div>

---

<div align="center">
  <strong>Buoy Racing Dashboard Example</strong><br>
</div>
<div align="center">
  <img src="images/swp-dashboard-3x3-buoy-racing-landscape-light.png" width="512"/>
</div>

---

<div align="center">
  <strong>Offshore Racing Dashboard Example</strong><br>
</div>
<div align="center">
  <img src="images/swp-dashboard-3x3-offshore-racing-landscape-light.png" width="512"/>
</div>

---

<div align="center">
  <strong>Driver Performance Dashboard Example</strong><br>
</div>
<div align="center">
  <img src="images/swp-dashboard-3x3-performance-landscape-light.png" width="512"/>
</div>

---

<div align="center">
  <strong>Four Channels</strong><br>
</div>
<div align="center">
 <img src="images/swp-dashboard-2x2-wind-landscape-light.png" width="512"/>
</div>

---

<div align="center">
  <strong>Build your own custom names in custom order</strong><br>
</div>
<div align="center">
 <img src="images/swp-dashboard-reorder-dashboards-landscape-light.png" width="512"/>
</div>

## Apple Watch Integration
Dedicated views for timer, speed, heel, VMG, wind, and depth — auto-switches to shallow-water monitoring.

<div align="center">
  <img src="images/swp-apple-watch-views.png" width="512">
</div>

## Technical Highlights
- GRIB parsing via ECMWF ecCodes bridge
- 5/10/15-min averaging engine
- Two-way Expedition integration
- Night mode with red tint

## Requirements
- iOS 18.5+ (iPad/iPhone) / macOS 15.6+ (arm) / watchOS 11.5+
- Expedition Marine 12.5.11+ (latest encouraged)
- Reliable boat WiFi

## Getting Started
1. Connect to the Expedition network  
2. Enter boat parameters  
3. Customize dashboards  
4. Race with real-time edge  

[Full setup guide →](https://docs.google.com/document/d/1cXRDmIqwttnDQbBGQB0azVdZFzVpno5fVTCnSREfSbo/edit?usp=sharing)

## Pricing & Availability
Currently in limited beta.  
Full release and pricing details coming soon — contact us for early access.

**Request Beta Access** → [james.bistis@icloud.com](mailto:james.bistis@icloud.com?subject=SailWatchPro%20Beta%20Access%20Request)  
or email directly: james.bistis@icloud.com

[Report Issues & Suggestions →](https://github.com/jbistis/SailWatchPro-Public/issues)

*May you always find the favorable shift.*  
**– The SailWatchPro Team**

<!-- End of Version

