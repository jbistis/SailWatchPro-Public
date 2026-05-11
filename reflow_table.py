#!/usr/bin/env python3
"""
reflow_table.py
Regenerates the channel tables in EXPEDITION-CHANNELS.md.

How it works:
  - The iOS channel set is keyed by Expedition Tx channel ID and mirrors the
    field mapping in ExpeditionDataManager.swift (the merged() function) plus
    the four sail-name channels handled by handleSailUpdate().
  - The web portal extras list (Tack/gybe loss time/metres) is iOS-irrelevant
    but required for the portal's race-log parser.
  - Labels come from the embedded ID -> label dict at the bottom, which mirrors
    ExpeditionChannelNames.lookup in ChannelHealthMonitor.swift. That lookup
    was extracted from Expedition.exe; refresh it with the procedure in
    SailWatchPro/ExpeditionChannelExtraction.md when EM ships a new build.

To add a channel to the iOS list:
  1. Add the field to ExpeditionDataManager.swift's merged() function.
  2. Add the channel ID to IOS_NUMERIC_IDS (or IOS_SAIL_PACKET_IDS) below.
  3. If the ID isn't already in LABELS below, add it there too.
  4. Run this script and copy the resulting tables into EXPEDITION-CHANNELS.md.

Usage:
  python3 reflow_table.py            # prints both tables to stdout
"""

# Channel IDs the iOS app reads from numeric Expedition packets, taken from
# every `updates["N"]` lookup in ExpeditionDataManager.swift's merged().
IOS_NUMERIC_IDS = [
    1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 20,
    31, 33, 34, 35, 36, 37, 38,
    48, 49, 50, 51, 55, 57, 58,
    66, 81, 82, 83, 88, 92, 93, 96, 97, 98, 99,
    101, 105, 106, 108, 109, 110, 112, 113,
    127, 128, 129, 130, 131, 132, 133,
    154, 157, 158, 163, 164, 165, 166, 168,
    204, 205, 206, 207, 237, 238, 261, 262, 263, 276,
    309, 312, 313, 349, 350, 358, 370,
]

# Channel IDs broadcast as #S,A,/M,/N,/E, packets and parsed by
# ExpeditionDataManager.handleSailUpdate(). They still need to be ticked in
# Expedition's Tx filter for the boat to broadcast them.
IOS_SAIL_PACKET_IDS = [
    269,   # Sail
    270,   # Sail mark
    271,   # Sail next mark
    404,   # Sail event
]

# Web portal log analysis. iOS app does not consume these; Channel Health on
# iOS therefore won't warn if they're absent from the broadcast.
PORTAL_ONLY_IDS = [
    273,   # Tack/gybe loss time
    274,   # Tack/gybe loss metres
]

# ID -> Tx-filter label. Mirrors ExpeditionChannelNames.lookup in
# ChannelHealthMonitor.swift. Only entries we actually reference need to be
# in this dict; missing IDs render as "Channel <id>" so the gap is visible.
LABELS = {
    1: "BSP", 2: "AWA", 3: "AWS", 4: "TWA", 5: "TWS", 6: "TWD",
    11: "Current set", 12: "Current drift", 13: "Heading",
    14: "Air temperature", 15: "Sea temperature", 16: "Barometer",
    17: "Depth", 18: "Heel (roll)", 20: "Rudder",
    31: "VMG", 33: "Layline dist on starb", 34: "Layline time on starb",
    35: "Layline bearing on port", 36: "Layline dist on port",
    37: "Layline time on port", 38: "Layline bearing on strb",
    48: "Latitude", 49: "Longitude", 50: "Cog", 51: "Sog",
    55: "Target vmg", 57: "Polar bsp", 58: "Polar bsp %",
    66: "VMG %", 81: "Start time to port", 82: "Start time to strb",
    83: "Start line square wind", 88: "Mark time", 92: "VMC",
    93: "Magnetic variation", 96: "Layline distance",
    97: "Layline time", 98: "Layline bearing", 99: "VMC %",
    101: "VMC optimum", 105: "Mark range", 106: "Mark bearing",
    108: "Mark twa", 109: "Current set predicted",
    110: "Current drift predicted", 112: "Next mark bearing",
    113: "Next mark twa", 127: "Next mark polar time",
    128: "Start bias angle", 129: "Start bias length",
    130: "Start layline on port", 131: "Start layline on strbd",
    132: "Next mark awa", 133: "Next mark aws",
    154: "Target awa", 157: "Start time to layline P",
    158: "Start time to layline S",
    163: "Start port latitude", 164: "Start port longitude",
    165: "Start stbd latitude", 166: "Start stbd longitude",
    168: "Relative humidity",
    204: "Start time to gun", 205: "Start time to line",
    206: "Start time to burn", 207: "Start distance below line",
    237: "Target twa", 238: "Target bsp",
    261: "Target bsp %", 262: "Heading to steer",
    263: "Heading to steer polar", 269: "Sail",
    270: "Sail mark", 271: "Sail next mark",
    273: "Tack/gybe loss time", 274: "Tack/gybe loss metres",
    276: "Mark bearing - Cog", 309: "Opposite track Cog",
    312: "TWD predicted", 313: "TWS predicted",
    349: "Start time to port burn", 350: "Start time to strb burn",
    358: "Layline time GPS", 370: "Dew point",
    404: "Sail event",
}


def label_for(id_: int) -> str:
    return LABELS.get(id_, f"Channel {id_}")


def render_table(labels, cols=3) -> str:
    labels = sorted(set(labels), key=lambda s: s.lower())
    head = "|" + " |" * cols
    sep = "|:-|" + "|".join([":-:"] * (cols - 1)) + "|"
    lines = [head, sep]
    for i in range(0, len(labels), cols):
        row = labels[i:i + cols]
        while len(row) < cols:
            row.append("")
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines), len(labels)


if __name__ == "__main__":
    ios_labels = [label_for(i) for i in (IOS_NUMERIC_IDS + IOS_SAIL_PACKET_IDS)]
    portal_labels = [label_for(i) for i in PORTAL_ONLY_IDS]

    table, n = render_table(ios_labels, cols=3)
    print("=== Required for SailWatchPro iOS (paste into EXPEDITION-CHANNELS.md) ===\n")
    print(table)
    print(f"\n<!-- {n} channels total -->\n")

    table, n = render_table(portal_labels, cols=2)
    print("=== Additionally required for web portal log analysis ===\n")
    print(table)
    print(f"\n<!-- {n} channels total -->")
