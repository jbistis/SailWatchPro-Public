# SailWatchPro

<p align="center">
  <img alt="SailWatchPro" src="images/icon-76x76@2x.png" width="96">
  <br><br>
  <strong>Win More Races. Make Faster Decisions.</strong>
</p>

<p align="center">
  <a href="https://docs.google.com/document/d/1cXRDmIqwttnDQbBGQB0azVdZFzVpno5fVTCnSREfSbo/edit?usp=sharing">
    <img src="http://i.imgur.com/0n2zqHD.png" width="140">
  </a>
</p>

SailWatchPro extends Expedition Marine's above-deck with a modern, touch-first iOS interface for iPad, iPhone, and Apple Watch. It synthesizes real-time data into clear, actionable insights and advisories — helping you make faster, more confident decisions on the water.

## Key Pillars
- **Racing Management** — Pre-start, start line, and customizable dashboards
- **Weather Observations & Analytics** — Buoy + GRIB fusion, trend analysis
- **Competitor Tracking** — Live corrected time & fleet awareness
- **Strategic & Tactical Advisories** — Automated high-value alerts

### Racing Management
**Pre-Start & Start Line**  
Expedition provides precision timing, line pings, and bias. SailWatchPro makes it mobile and intuitive — above-deck touch controls for pinging, timer, course selection, and visual dashboards for approach decisions.

**Dashboards**  
12 customizable layouts (any Expedition channel + computed metrics like 5/10/15-min averages). Context-aware alerts help maintain trim, avoid overstanding, and correct drift.

<div align="center">
  <img src="images/swp-prestart-view-light.png" width="384">
  <br><em>Pre-Start Dashboard</em>
</div>

<div align="center">
  <img src="images/swp-iPad-start-view-light.png" width="512">
  <br><em>Start Line Visuals & Bias</em>
</div>

### Weather Observations & Analytics
Automatic polling of nearby buoys (NOAA, NDBC, etc.) within 100nm. Overlay predicted GRIB vs. actual observations, track divergences in real time.
<div align="center">
  <img src="images/swp-buoy-list-view-light" width="512">
  <br><em>Start Line Visuals & Bias</em>
</div>


**Weather Station Wind Analysis**  
Visually compare buoy observations with GRIB forecasts and trends for every key station — see exactly how reality is diverging across the race area.

**Boat Instrumentation Wind Analysis**  
Your boat is a moving weather station. SailWatchPro analyzes real-time wind trends using rolling averages, FFT, and wavelet transforms to identify veering/backing, building, and oscillating patterns — with confidence indicators and a 6-hour wind history that syncs across devices.

<div align="center">
  <img src="images/swp-buoy-wind-analysis-light.png" width="512"> <!-- Use your Virginia Key screenshot here -->
  <br><em>Buoy: Predicted vs. Actual Wind Trends</em>
</div>

### Competitor Tracking
Live corrected time vs. handicap, lateral separation visualization — know instantly if you're gaining or losing on corrected time, even when boats are physically ahead or behind.

### Strategic & Tactical Advisories
Centralized, customizable alerts that monitor for you: current push, leeway drift, sail mismatches, barometric trends, and more — so you can focus on steering and tactics.

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
- iOS 18.5+ / watchOS 11.5+ / Expedition Marine 12.5.11+

## Requirements
- iOS 18.5+ (iPad/iPhone) | watchOS 11.5+  
- Expedition Marine 12.5.11+ (latest encouraged)  
- Reliable boat WiFi

## Getting Started
1. Connect to Expedition network  
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


### **Weather Station Wind Analysis**
<div align="center">
  <img src="images/swp-buoy-list-view-with-trends-light.png" width="384"/>
</div>

<strong>Visually overlay the actual weather with the GRIB forecasted and predicted trends</strong><br>
Import your GRIB files, and SailWatchPro overlays predicted vs. actual weather for every key station, tracking how reality is diverging from the forecast in real time.  Also included is a linear regression analysis of buoy data history to provide an additional predictive dataset.  

<div align="center">
  <img src="images/buoy-observed-grib.png" width="384"/>
</div>

In addition to the fixed buoys, your boat is a moving weather station, and its instruments provide valuable information.  Wind is best described as a moving lawn sprinkler that oscillates as it travels from one place to another.  Sailboat teams that can correctly quantify the oscillations within the larger movement gain a distinct advantage in getting longer lifts and smaller knocks.

### **Boat Instrumentation Wind Analysis**
<div align="center">
 <img src="images/swp-wind-state.png" width="384"/>
</div>

Real-time wind trend analysis using rolling averages, FFT, and wavelet transforms. The app identifies patterns such as veering, backing, building, and oscillating conditions and displays them with confidence indicators. Maintains a 6-hour wind history that automatically syncs across all crew devices on your boat's network.

See exactly where, when, and how the wind, pressure, or other elements are shifting differently than expected—across the entire race area.
Stop guessing. Start knowing.  Gain the advantage the fleet can't see coming.

## 🏁 Competitor Tracking and Threat Assessment
<strong>Know the Real Score Mid-Race with SailWatchPro's Fleet Intelligence</strong><br>
After the start gun, the real race begins: Where are your competitors, and how are you actually performing against them on handicap?
Competitor boat performance often reveals the fastest path—which side of the course to favor, which areas to avoid. Basic AIS gives you range, bearing, SOG, and COG for each boat… but SailWatchPro goes much further.
<br><br>
For handicapped racing, the software calculates live corrected time for every competitor against you as the race unfolds. 

<strong>See instantly:</strong>
<ul>
  <li>If you're beating a boat that's physically ahead (gaining on corrected time)</li>
  <li>Or losing to one that's behind (they're pulling away despite position)</li>
</ul>

<strong>It also tracks lateral separation across the fleet—so you can visualize who's leveraged to windward/leeward and decide:</strong>
<ul>
  <li>Time to take a risk and leverage hard for a comeback?</li>
  <li>Or play it safe, cover the fleet, and cross the line to the podium?</li>
</ul>

<div align="center">
  <img src="images/swp-competitor-view-light.png" width="384"/>
  <!-- <img src="images/swp-map-view-with-competitor-light.png" width="256"/> -->
</div>

With the automated ORC interface, select the scoring method once the Race Committee announces it. SailWatchPro automatically downloads the TCFs for all registered boats. No more tedious manual entry.
Enter your competitors' boat details once into a CSV file, then select the competitor you're racing against for any given race. Effortless fleet awareness lets you sail smarter, react faster, and win more.
Stop guessing your position on handicap.  Start knowing—and acting on it—in real time.

## Strategic and Tactical Advisories
<strong>Cut Through the Data Noise with SailWatchPro's Advisory Workbench</strong><br>
With modern racing sailboats, information overload is almost inevitable. Sensors and systems pump out data multiple times per second—polars, targets, laylines, currents, leeway, wind shifts—and it's all too easy to get lost in the trees and lose sight of the forest.  The SailWatchPro Advisory Workbench delivers a customizable, centralized dashboard of high-value insights automatically extracted from your live data streams—so you can focus on steering, trimming, and tactics instead of mental math.

<strong>A few examples of always-on advisories:</strong><br>
Continuously compares Speed Through Water (STW) to Speed Over Ground (SOG) and alerts you when you're pushing too much current (or getting a free ride).
Tracks your desired heading to the next mark against actual Course Over Ground (COG), warning you the moment you're being gradually knocked off your line by leeway or current.

<div align="center">
 <img src="images/swp-advisories-light.png" width="512"/>
</div>

These are just two of many preconfigured, extensible advisories—tailor them to your boat, your crew, and your race strategy.
Sure, you can get this information by staring at mast displays, scribbling notes, and doing constant mental calculations…
But why burn brainpower when SailWatchPro can watch it for you, 24/7, and only interrupt when it matters?
Stay ahead of the fleet. Stay focused on the race.

### 📊 **Customizable Dashboards**


### Racing Dashboards
The app includes 12 different dashboard layouts that display any Expedition Marine channel. Configure them for different race scenarios—pre-start, upwind work, reaching, or offshore. Fields show context-aware data based on sailing mode and provide visual alerts for out-of-range conditions.  In addition, SailWatchPro includes many more computed channels derived from Expedition channel data, including those maintained by the Averaging Engine.  Adding more computed channels is straightforward.

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
  <strong>Two Large Channels</strong><br>
</div>
<div align="center">
 <img src="images/swp-dashboard-1x2-portrait-light.png" width="512"/>
</div>

---

<div align="center">
  <strong>One Large Channel</strong><br>
</div>
<div align="center">
 <img src="images/swp-dashboard-1x1-portrait-light.png" width="512"/>
</div>

<div align="center">
  <strong>Build your own custom names in custom order</strong><br>
</div>
<div align="center">
 <img src="images/swp-dashboard-reorder-dashboards-landscape-light.png" width="512"/>
</div>

### ⌚ **Apple Watch Integration**
<div align="center">
 <img src="images/swp-apple-watch-views.png" width="512"/>
</div>

Dedicated watch views for race timer, speed, heel angle, VMG, wind angles, and depth.  Also included in access to all custom data fields that comprise dashboards. Data syncs from your iPhone, and the watch automatically shakes and switches to depth monitoring when approaching shallow water.

---

## Additional Capabilities

**Sail Management** – Import designer or performance-based crossover charts. Track sail inventory and log sail change events with time and location data for upload to Sailnjord.

**Weather Data** – Retrieve wind and weather information from NOAA, NDBC, NERACOOS, and LISICOS buoys within 100nm. Data syncs across all devices on your boat's network.

**Barometric Monitoring** – Track atmospheric pressure trends with visual history. The app alerts when pressure data stops updating.

**MOB Function** – Triggers alerts to Expedition and chartplotters, calculates estimated drift position, and provides hypothermia risk assessment.

---

## Technical Overview

SailWatchPro is designed for competitive sailing with features that address common racing scenarios:

- **12 Customizable Dashboards** with any Expedition Marine channel
- **Wind Trend Analysis** using FFT and wavelet transforms
- **Competitor Tracking** with distance and corrected time calculations
- **Start Line Analysis** with pin pinging and bias computation
- **Performance Metrics** with 5/10/15-minute rolling averages
- **Apple Watch Support** with automatic mode switching
- **Display Modes** including night mode with red-tinted display
- **Two-Way Expedition Integration** for marks, courses, and waypoints

---

## Requirements

- iOS 18.5+ (iPad/iPhone) | watchOS 11.5+ (Apple Watch)
- Expedition Marine 12.5.11+ - keeping current with the latest Expedition Marine release is encouraged.
- Reliable boat WiFi network

---

## Pricing & Availability

SailWatchPro is currently in limited beta with a small group of competitive boats.  
Full release and pricing details coming soon — contact us for early access or to join the beta.

**Request Beta Access** → [james.bistis@icloud.com](mailto:james.bistis@icloud.com?subject=SailWatchPro%20Beta%20Access%20Request)  
or email directly: james.bistis@icloud.com

[Report Issues & Suggestions →](https://github.com/jbistis/SailWatchPro-Public/issues)

---

## Getting Started

1. **Connect** – Configure your Expedition Marine network settings
2. **Setup** – Enter boat parameters (length, draft, MMSI)
3. **Customize** – Select dashboard layouts for your racing style
4. **Use** – Access real-time data during races

[Full setup guide available here](https://docs.google.com/document/d/1cXRDmIqwttnDQbBGQB0azVdZFzVpno5fVTCnSREfSbo/edit?usp=sharing)

---

## Feedback & Support

SailWatchPro is actively developed based on user feedback from competitive sailing environments.

**[Report Issues & Request Features →](https://github.com/jbistis/SailWatchPro-Public/issues)**

---

*May you always find the favorable shift.*

**– The SailWatchPro Team**

