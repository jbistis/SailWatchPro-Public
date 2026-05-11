# Expedition Marine Channel Requirements

<p align="center">
  <a href="https://sailwatchpro.io/">
    <img alt="SailWatchPro" title="SailWatchPro" src="images/icon-76x76@2x.png">
  </a>
</p>

<p align="center">
  <strong>Tx Filter Channels Required by SailWatchPro</strong>
</p>

---

## Table of Contents

- [Overview](#overview)
- [How to Enable Channels in Expedition](#how-to-enable-channels-in-expedition)
- [Required for SailWatchPro iOS](#required-for-sailwatchpro-ios)
- [Additionally Required for Web Portal Log Analysis](#additionally-required-for-web-portal-log-analysis)
- [Channel Health Monitor](#channel-health-monitor)
- [What to Do If a Channel Goes Silent](#what-to-do-if-a-channel-goes-silent)

---

## Overview

SailWatchPro reads its data from Expedition Marine over UDP. For everything in the iOS app to work — sail crossover, layline guidance, start sequencing, weather, course display — the channels listed below need to be ticked in Expedition's **Exp Tx filter** so they are broadcast on the boat network.

The web portal at [sailwatchpro.com](https://sailwatchpro.com) additionally analyzes uploaded `.csv` log files. Two extra channels need to be enabled in the Tx filter so they are written to those logs; the iOS app does not use them, so they are listed separately below.

---

## How to Enable Channels in Expedition

Step 1 of the [Setup Guide](SETUP-GUIDE.md#step-1--find-ip-addresses) walks through opening the Tx filter dialog. Once you are in **Exp Tx filter**, tick every channel listed in the tables below. The dialog is alphabetical; the tables here are also alphabetical, so you can scan top-to-bottom in both at the same time.

When you are done, click **OK**, and verify in SailWatchPro that the connection indicator turns green.

---

## Required for SailWatchPro iOS

These are the channels the iOS app actively consumes — derived from the field mapping in `ExpeditionDataManager.swift` (`merged()`) plus the four sail-name channels handled by `handleSailUpdate(...)`. If any of these stop arriving, [Channel Health Monitor](#channel-health-monitor) in the app will flag them.

<!-- Channel list maintained in reflow_table.py — add new IDs there and run the script to regenerate this table. The script's iOS list mirrors ExpeditionDataManager.swift; keep them in sync. -->

| | | |
|:-|:-:|:-:|
| Air temperature | AWA | AWS |
| Barometer | BSP | Cog |
| Current drift | Current drift predicted | Current set |
| Current set predicted | Depth | Dew point |
| Heading | Heading to steer | Heading to steer polar |
| Heel (roll) | Latitude | Layline bearing |
| Layline bearing on port | Layline bearing on strb | Layline dist on port |
| Layline dist on starb | Layline distance | Layline time |
| Layline time GPS | Layline time on port | Layline time on starb |
| Longitude | Magnetic variation | Mark bearing |
| Mark bearing - Cog | Mark range | Mark time |
| Mark twa | Next mark awa | Next mark aws |
| Next mark bearing | Next mark polar time | Next mark twa |
| Opposite track Cog | Polar bsp | Polar bsp % |
| Relative humidity | Rudder | Sail |
| Sail event | Sail mark | Sail next mark |
| Sea temperature | Sog | Start bias angle |
| Start bias length | Start distance below line | Start layline on port |
| Start layline on strbd | Start line square wind | Start port latitude |
| Start port longitude | Start stbd latitude | Start stbd longitude |
| Start time to burn | Start time to gun | Start time to layline P |
| Start time to layline S | Start time to line | Start time to port |
| Start time to port burn | Start time to strb | Start time to strb burn |
| Target awa | Target bsp | Target bsp % |
| Target twa | Target vmg | TWA |
| TWD | TWD predicted | TWS |
| TWS predicted | VMC | VMC % |
| VMC optimum | VMG | VMG % |

<!-- 84 channels total -->

---

## Additionally Required for Web Portal Log Analysis

These channels are not used by the iOS app, but the web portal's race-log parser needs them to detect tacks, gybes, and per-maneuver loss. Enable them in the Tx filter so Expedition writes them to the `.csv` log file.

> **Note:** Because the iOS app does not consume these channels, Channel Health Monitor on iOS will **not** warn you if they are missing. Set them once in Expedition's Tx filter and you are done.

| | |
|:-|:-|
| Tack/gybe loss metres | Tack/gybe loss time |

<!-- 2 channels total -->

---

## Channel Health Monitor

Once your boat has been broadcasting for a while, SailWatchPro learns which channels you typically send. From then on, **Settings → Channel Health → Run Check Now** compares the channels arriving right now against that historical set and flags any that have stopped.

Learning is per-boat: switching boats in **Boat Configuration** swaps the monitor to that boat's bucket, so a boat without (for example) a barometer will not be warned about it.

This is a setup and verification tool — useful when:

- Setting up SailWatchPro on a new boat
- Verifying the data feed after restarting Expedition
- Troubleshooting an iOS display that does not look right

---

## What to Do If a Channel Goes Silent

1. Confirm the channel is still ticked in Expedition's **Exp Tx filter**. Channels can get unticked accidentally when reviewing the dialog.
2. Confirm Expedition is still running and connected to the boat's instrument network.
3. If the channel is sourced from a sensor (e.g. depth, barometer, heel), verify the sensor itself is reporting through the NMEA 2000 / instrument network into Expedition.
4. Restart Expedition's network connection (see [Step 1 of the Setup Guide](SETUP-GUIDE.md#step-1--find-ip-addresses)).
5. If the issue persists, see the [Troubleshooting Guide](TROUBLESHOOTING.md).
