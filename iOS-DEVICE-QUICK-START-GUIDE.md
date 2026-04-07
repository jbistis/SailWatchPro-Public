# SailWatchPro

<p align="center">
  <a href="https://sailwatchpro.io/">
    <img alt="SailWatchPro" title="SailWatchPro" src="images/icon-76x76@2x.png">
  </a>
</p>

<p align="center">
  <strong>End-User Device Setup Guide</strong>
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
The first launch will take a few additional moments while the app performs a one-time installation of the ECMWF libraries.

### Settings
- Download the App
- Start the App on your iPhone or iPad
- iPad - navigate to Settings
- iPhone - navigate to More > Settings

**Connection Information**
Enter values specific to your boat as supplied by your Expedition Marine Administrator
<div align="center">
  <img src="images/swp-settings.png" width="512">
  <br><em>Enter your connection parameters</em>
</div>
<br>

**Troubleshooting Connection Issues**

***From your iPad/iPhone***
- Install a free ping utility app at  https://apps.apple.com/us/app/ping-network-utility/id576773404
-  Ping your Expedition Marine PC IP Address (If running Windows on top of Mac, the IP address of the virtual Windows PC)

***From your Expedition PC***
-  From a Windows CMD prompt, ping your iPhone.  Find your iOS device IP Address by Settings > WiFi > i (information circle) and not the IP Address found in the IPv4 Section
If you can ping in both directions that proves the networking is functioning properly

***Check your port settings***
-  Typically, in Expedition, the Rx port is 5098 and Tx port is 5099 and in the SailWatchPro app it is switched and the Rx port is 5099 and the Tx port is 5098.

***Check your Windows Firewall***
Temporarilly disable 
-  From a Windows CMD prompt, enter the command netsh advfirewall set allprofiles state off

**Boat Configuration**  
- **Boat Name** — Vessel identification  
- **Boat Length** — For distance calculations in boat lengths  
- **Draft** — Critical for depth safety  
- **TWA Reaching Threshold**
<div align="center">
  <img src="images/swp-boat-configuration-da.png" width="512">
  <br><em>Enter your boat parameters</em>
</div>
<br>

Touch the [Done] button

---

## Buoy List Import
### Download buoys list

[![Download Polars](https://img.shields.io/badge/Download%20default_buoys.csv-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild65/default_buoys.csv)

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
[![Download Polars](https://img.shields.io/badge/Download%20Sailmaker%20Crossover%20Chart-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild65/ORC-polars-della-aurora-2dot5m-20251029.txt)

[![Download Polars](https://img.shields.io/badge/Download%20Sail%20Performance%20Crossover%20Chart-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild65/ORC-polars-della-aurora-2dot5m-20251029.txt)

[![Download Polars](https://img.shields.io/badge/Download%20Polars-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild65/ORC-polars-della-aurora-2dot5m-20251029.txt)

### Import the Source Datafiles using the import buttons

<div align="center">
  <img src="images/swp-sail-polar-import.png" width="512">
  <br><em>Enter your Sail Crossover Charts and Polars</em>
</div>
<br>

---

## Import Competitors
### Download Source Datafile
[![Download Competitors](https://img.shields.io/badge/Download%20competitors.csv-blue?style=for-the-badge)](https://github.com/jbistis/SailWatchPro-Public/releases/download/ImportFilesBuild65/competitors.csv)

### Load the Competitor Datafile using the import icon in the toolbar.  Use the [+ Add] button to add one competitor.
<div align="center">
  <img src="images/swp-competitors.png" width="512">
  <br><em>Load your competitors file</em>
</div>
<br>

### Enter the Race Information (Yacht Scoring eID number, if available).

Touch the 3-dot circle just to the right of [+ Add] button to enter and update the race information.
<div align="center">
  <img src="images/swp-yacht-scoring-setup.png" width="512">
  <br><em>Load your Race Information</em>
</div>
<br>

---

## File Downloads

- **Buoys** — file name must be `default_buoys.csv`
- **Sail Crossover Chart** — Txt or xml export from Expedition Marine
- **Sail Performance Crossover Chart** — export tsv from sailing analytics
- **Polars** — Txt or export from Expedition Marine
- **Competitors** — Bulk high speed entry

Visit the full release page:  

[All Import Files /Github Release →](https://github.com/jbistis/SailWatchPro-Public/releases/tag/importFilesBuild65)

[All Import Files /Goolge Drive →](https://drive.google.com/drive/folders/1XXa9frakEL_QT7oMJfO0aDO2mqGzbGHm?usp=drive_link)


## Display Options
- Light Mode and Dark Mode are set using your iOS device Settings > Display & Brightness > APPEARANCE
- Night Mode (red-tinted) is enabled and disabled in Settings
- Map Style (hybrid, standard, satellite, imagery)  

## Safety Settings
- **Depth Alerts** — Draft + safety margin warnings  
- **Audio Countdown** — Spoken start sequence  
- **MOB (Man Overboard)** — Emergency position mark & tracking

---

## Troubleshooting

### Connection Issues
- Red indicators → Verify IP & port  
- No data → Confirm Expedition is broadcasting  
- Intermittent → Check WiFi strength/stability  

### Display Problems
- Data not updating → Restart connection or Expedition  
- Watch not syncing → Check iPhone–Watch link & permissions  

### Performance Issues
- Slow → Shorten chart time windows/restart app  
- Battery drain → Use Night Mode + lower brightness  

---

## Support & Updates

SailWatchPro is actively developed, with new features driven by user feedback and racing experience.  

For best results, keep both iPhone and Watch apps on the same version.  

**Support & Feature Requests**:  
https://github.com/jbistis/SailWatchPro-Public/issues

Happy sailing! ⛵
**SailWatchPro Team**

