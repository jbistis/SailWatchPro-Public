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
- [Tx Channels](#tx-channels)

---

## Getting Started

**Latest Version**  
It is strongly recommended that all iOS devices (iPhone & Watch) run the **same version** of the app since data is shared between users.

### First Launch Setup

1. **Configure the Expedition Marine Network**  
   - Start Expedition Marine on the boat PC.  
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

**Exp Rx filter**  
- Enable **Receive marks**

**Exp Tx filter** (select these channels):
>    |Tx Channels|||
>    |:-|-:|-:|
>    |AWS|AWA|Barometer|
>    |BSP|Cog|Course|
>    |Current drift|Current drift|Current drift predicted|
>    |Current set|Current set predicted|Depth|
>    |Heading - Cog|Heading to steer|Heading to steer polar|
>    |Heel (roll)|J1|Lattitude|
>    |Layline bearing|Layline bearing on port|Layline bearing on strb|
>    |Layline dist on port|Layline dist on starb|Layline distance|
>    |Layline time|Layline time on port|Layline time on starb|
>    |Longitude|Magnetic variation|Mark bearing|
>    |Mark bearing - Cog|Mark lattitude|Mark longitude|
>    |Mark range|Mark time|Mark twa|
>    |Next mark awa|Next mark aws|Next mark bearing|
>    |Next mark lattitude|Next mark longitude|Next mark polar time|
>    |Next mark range|Next mark time on port|Next mark time on starb|
>    |Next mark twa|Opposite track|Polar bsp|
>    |Polar bsp %|Sail|Sail event|
>    |Sail mark|Sail next mark|Sea temperature|
>    |Sog|Start bias angle|Start bias length|
>    |Start distance below line|Start layline on port|Start layline on strdb|
>    |Start line square wind|Start port lattitude|Start port longitude|
>    |Start stdb lattitude|Start stdb longitude|Start time to burn|
>    |Start time to gun|Start time to layline P|Start time to layline S|
>    |Start time to line|Start time to port|Start time to port burn|
>    |Start time to strb|Start time to strb burn|Target bsp|
>    |Target bsp %|Target twa|Trim (pitch)|
>    |TWA|TWD|TWD predicted|
>    |TWS|TWS predicted|VMC|
>    |VMC %|VMC optimum|VMG|
>    |VMG %|||






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

## Tx Channels

>    |Tx Channels|||
>    |:-|-:|-:|
>    |AWS|AWA|Barometer|
>    |BSP|Cog|Course|
>    |Current drift|Current drift|Current drift predicted|
>    |Current set|Current set predicted|Depth|
>    |Heading - Cog|Heading to steer|Heading to steer polar|
>    |Heel (roll)|J1|Lattitude|
>    |Layline bearing|Layline bearing on port|Layline bearing on strb|
>    |Layline dist on port|Layline dist on starb|Layline distance|
>    |Layline time|Layline time on port|Layline time on starb|
>    |Longitude|Magnetic variation|Mark bearing|
>    |Mark bearing - Cog|Mark lattitude|Mark longitude|
>    |Mark range|Mark time|Mark twa|
>    |Next mark awa|Next mark aws|Next mark bearing|
>    |Next mark lattitude|Next mark longitude|Next mark polar time|
>    |Next mark range|Next mark time on port|Next mark time on starb|
>    |Next mark twa|Opposite track|Polar bsp|
>    |Polar bsp %|Sail|Sail event|
>    |Sail mark|Sail next mark|Sea temperature|
>    |Sog|Start bias angle|Start bias length|
>    |Start distance below line|Start layline on port|Start layline on strdb|
>    |Start line square wind|Start port lattitude|Start port longitude|
>    |Start stdb lattitude|Start stdb longitude|Start time to burn|
>    |Start time to gun|Start time to layline P|Start time to layline S|
>    |Start time to line|Start time to port|Start time to port burn|
>    |Start time to strb|Start time to strb burn|Target bsp|
>    |Target bsp %|Target twa|Trim (pitch)|
>    |TWA|TWD|TWD predicted|
>    |TWS|TWS predicted|VMC|
>    |VMC %|VMC optimum|VMG|
>    |VMG %|||












