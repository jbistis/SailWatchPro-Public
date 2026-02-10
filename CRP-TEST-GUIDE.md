# SailWatchPro

<p align="center">
  <a href="https://sailwatchpro.io/">
    <img alt="SailWatchPro" title="SailWatchPro" src="images/icon-76x76@2x.png">
  </a>
</p>

<p align="center">
  <strong>CRP Test Guide</strong>
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
- [Performance Issues](#performance-issues)
- [Support & Updates](#support--updates)

---

## Getting Started

**Latest Version**  
Remove the app from your iOS device and install the latest version.

### First Launch
The first launch will take a few additional moments while the app installs the ECMWF libraries once.

### Test Areas
- Pre-start buttons
- Weather Data
- Competitors
- Buoy Fetch - Test automated 


## Buoy List Import
### Download buoys list

[![Download Polars](https://img.shields.io/badge/Download%20default_buoys.csv-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild57/default_buoys.csv)

### Import buoys list
The file name must remain default_buoys.csv.  To add more buoys, follow the format used in the default file.  When you import a buoy file, the new file replaces the existing list.

<div align="center">
  <img src="images/swp-buoy-import.png" width="512">
  <br><em>Load your race buoy weather stations</em>
</div>
<br>

---

## Import Sail Crossover Charts and Polars
### Download Source Datafiles
[![Download Polars](https://img.shields.io/badge/Download%20Sailmaker%20Crossover%20Chart-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild57/ORC-polars-della-aurora-2dot5m-20251029.txt)

[![Download Polars](https://img.shields.io/badge/Download%20Sail%20Performance%20Crossover%20Chart-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild57/ORC-polars-della-aurora-2dot5m-20251029.txt)

[![Download Polars](https://img.shields.io/badge/Download%20Polars-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild57/ORC-polars-della-aurora-2dot5m-20251029.txt)

### Import the Source Datafiles using the import buttons

<div align="center">
  <img src="images/swp-sail-polar-import.png" width="512">
  <br><em>Enter your Sail Crossover Charts and Polars</em>
</div>
<br>

---



Visit the full release page:  
[All Import Files Release →](https://github.com/jbistis/SailWatchPro-Public/releases/tag/ImportFiles)

## Display Options
- Light Mode and Dark Mode are set using your iOS device Settings > Display & Brightness > APPEARANCE
- Night Mode (red-tinted) is enabled and disabled in Settings
- Map Style (hybrid, standard, satellite, imagery)  

## Safety Settings
- **Depth Alerts** — Draft + safety margin warnings  
- **Audio Countdown** — Spoken start sequence  
- **MOB (Man Overboard)** — Emergency position mark & tracking

---

## Test Scripts

### Pre-Start Controls
- Start clock with 15-minute timer and test +1, -1, Sync, and Kill buttons
- Start clock with 10, 5, and 3-minute timers.
- Set the PORT and Starboard start line pins.
- Select a course.

- ### Weather Data
- Import the buoys
- Check that Auto-Fetch is functioning properly by letting it sit long enough to execute a few auto-fetches.
- Check that buoys that do not report history accure history as auto-fetch proceeds
- Check that the GRIB data is plotted along with the buoy's actual data

Happy sailing! ⛵
**SailWatchPro Team**

