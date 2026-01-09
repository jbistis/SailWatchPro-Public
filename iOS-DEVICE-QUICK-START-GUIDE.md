# SailWatchPro

<p align="center">
  <a href="https://sailwatchpro.io/">
    <img alt="SailWatchPro" title="SailWatchPro" src="images/icon-76x76@2x.png">
  </a>
</p>

<p align="center">
  Setup Guide
</p>

---

## Table of Contents

- [Getting Started](#getting-started)
- [First Launch Setup](#first-launch-setup)
- [Expedition Marine Requirements](#expedition-marine-requirements)
- [Connection Settings](#connection-settings)
- [Boat Configuration](#boat-configuration)
- [Display Options](#display-options)
- [Safety Settings](#safety-settings)
 [Performance Issues](#performance-issues)
- [Support & Updates](#support--updates)

---

## Getting Started

**Latest Version**  
It is strongly recommended that all iOS devices (iPhone & Watch) run the latest version of the app, as some data is shared between users.

### First Launch
The first launch will take a few moments as the app installs the ECMWF libraries.  This is just on the first launch.  

**Start Expedition Marine Network**  
   - Download the App
   - Start the App on your iPhone or iPad
   - On the iPad, navigate to Settings and enter the following:

**Connection Information**  
<div align="center">
  <img src="images/swp-expedition-connections-setup.png" width="756">
  <br><em>Enter your connection parameters</em>
</div>
<br>

**Boat Configuration**  
- **Boat Name** — Vessel identification  
- **Boat Length** — For distance calculations in boat lengths  
- **Draft** — Critical for depth safety  
- **TWA Reaching Threshold**
<div align="center">
  <img src="images/swp-boat-configuration.png" width="756">
  <br><em>Enter your boat parameters</em>
</div>
<br>

Touch the [Done] button

---

## Default Buoy Data

[![Download default_buoys.csv](https://img.shields.io/badge/Download%20default_buoys.csv-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFiles/default_buoys.csv)

<div align="center">
  <img src="images/swp-buoy-import.png" width="756">
  <br><em>Enter your boat parameters</em>
</div>
<br>



## Downloadable Import Files
These files serve as data sources for SailWatchPro.

Click the links below to download directly (no preview in browser):




Or visit the full release page:  
[All Import Files Release →](https://github.com/jbistis/SailWatchPro-Public/releases/tag/ImportFiles)



**Load sail crossover charts and polars**
<div align="center">
  <img src="images/swp-sail-polar-import.png" width="756">
  <br><em>Enter your boat parameters</em>
</div>
<br>

**Load Compeitors**  



---

## Connection Settings

- **IP Address**: Boat network broadcast address  
- **UDP Port**: Usually 5098  
- **Test Mode**: Enable for simulated training data  

## Boat Configuration

- **Boat Name** — Vessel identification  
- **Boat Length** — For distance calculations in boat lengths  
- **Draft** — Critical for depth safety  
- **TWA Reaching Threshold** — Adjusts sailing mode detection  

## Display Options

- Light Mode  
- Dark Mode  
- Night Mode (red-tinted)  
- Chart Time Windows (custom history view)  
- Map Style (hybrid, standard, satellite, imagery)  

## Safety Settings

- **Depth Alerts** — Draft + safety margin warnings  
- **Audio Countdown** — Spoken start sequence  
- **MOB (Man Overboard)** — Emergency position mark & tracking  

## Data imports

You can find sample import files at https://github.com/jbistis/SailWatchPro-Public/tree/main/documents 

- **Buoys** — file name must be `default_buoys.csv`
- **Sail Crossover Chart** — Txt or xml export from Expedition Marine
- **Sail Performance Crossover Chart** — export tsv from sailing analytics
- **Polars** — Txt or export from Expedition Marine
- **Competitors** — Bulk high speed entry

## Troubleshooting

### Connection Issues
- Red indicators → Verify IP & port  
- No data → Confirm Expedition is broadcasting  
- Intermittent → Check WiFi strength/stability  

### Display Problems
- Data not updating → Restart connection or Expedition  
- Watch not syncing → Check iPhone–Watch link & permissions  

### Performance Issues
- Slow → Shorten chart time windows / restart app  
- Battery drain → Use Night Mode + lower brightness  
- Memory → Clear old logs / restart periodically  

---

## Support & Updates

SailWatchPro is actively developed with new features based on user feedback and racing experience.  

For best results, keep both iPhone and Watch apps on the same version.  

**Support & Feature Requests**:  
https://github.com/jbistis/SailWatchPro-Public/issues

Happy sailing! ⛵
**SailWatchPro Team**

