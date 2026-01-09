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
- [Data Imports](#data-imports)
- [Troubleshooting](#troubleshooting)
- [Connection Issues](#connection-issues)
- [Display Problems](#display-problems)
- [Performance Issues](#performance-issues)
- [Support & Updates](#support--updates)

---

## Getting Started

**Latest Version**  
It is strongly recommended that all iOS devices (iPhone & Watch) run the **latest version** of the app since some data is shared between users.

### First Launch Setup

**Start Expedition Marine Network**  
   - Download the App
   - Start the App on your iPhone or iPad
   - On the iPad navigate to Settings and enter the following:

**Connection Information**  
<ol>
  <li>Epedition Marine IP Address</li>
  <li>Epedition Marine Port</li>
  <li>NMEA 2000 Server IP Address</li>
  <li>NMEA 2000 Server Port</li>
</ol>



   - From the ☰ Hamburger Menu → drag down → hover over Instruments → click *Number of network connections*  
   - Enter one greater than the displayed number to add a new network → OK  
   - Go back to Instruments → select the new network and configure:  
     - Alias: **SailWatchPro**  
     - Instruments: **Expedition**  
     - Address: **192.168.XXX.YYY** (your Expedition Marine PC's IP)  
     - Port: Choose an unused port  
   - Click *Expedition Settings*  
   - In **Exp Rx filter**: check **Receive marks**  
   - In **Exp Tx filter**: enable the channels listed in [Expedition Marine Requirements](#expedition-marine-requirements) below  

2. **Connect to Expedition Marine**  
   - Install SailWatchPro on your iOS device via TestFlight  
   - Open **Settings** in the app  
   - Enter the same **IP address** and **UDP port** you configured in Expedition Marine  
   - (If using) Enter NMEA 2000 Ethernet Gateway IP/port  
   - Restart connection → look for **green** status indicators  

3. **Configure Your Boat**  
   - Boat Name  
   - MMSI number (if applicable)  
   - Boat Length (used for boat-length distance calculations)  
   - Draft (used for depth safety alerts)  
   - TWA Reaching Threshold (sailing mode detection sensitivity)  

4. **Choose Display Mode**  
   - Light Mode  
   - Dark Mode  
   - Night Mode (red-tinted for night vision)  
   - Test Mode (simulated data for training/demos)  

### Expedition Marine Requirements

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

