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

---

## Test Scripts

### Pre-Start Controls
- Start clock with 15-minute timer and test +1, -1, Sync, and Kill buttons
- Start clock with 10, 5, and 3-minute timers.
- Set the PORT and Starboard start line pins.
- Select a course.

### Import Performance Files
- Polars

[![Download Polars](https://img.shields.io/badge/Download%20Polars%20Chart-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild57/ORC-polars-della-aurora-2dot5m-20251029.txt)

- Crossover Chart

[![Download Polars](https://img.shields.io/badge/Download%20Sail%20Performance%20Crossover%20Chart-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild57/sail-chart-della-aurora-20251029.xml)

- Performance Crossover Chart

[![Download Polars](https://img.shields.io/badge/Download%20Sail%20Performance%20Crossover%20Chart-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild57/performance-sail-chart-della-aurora.txt)


### Weather Data
- Import the buoys

[![Download Polars](https://img.shields.io/badge/Download%20default_buoys.csv-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild57/default_buoys.csv)

- Import a current and relevant GRIB file
- Check that Buoy Auto-Fetch is functioning properly by letting it sit long enough to execute a few auto-fetches.
- Check that buoys that do not report history accure history as auto-fetch proceeds
- Check that the GRIB data is plotted along with the buoy's actual data

### Competitors 
- Import competitors
- Check ORC poll

### Display Options
- Test switching between Light Mode and Dark Mode are set using your iOS device Settings > Display & Brightness > APPEARANCE
- Night Mode (red-tinted) is enabled and disabled in Settings and check for hot spots.

Visit the full release page:  
[All Import Files Release →](https://github.com/jbistis/SailWatchPro-Public/releases/tag/ImportFiles)

Happy sailing! ⛵
**SailWatchPro Team**

