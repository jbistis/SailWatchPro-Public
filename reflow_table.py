#!/usr/bin/env python3
"""
reflow_table.py
Maintains the Expedition Marine channel list as a simple sorted list,
then outputs a 3-column markdown table. Add items to the list below
and run the script — the table will always be correct.
"""

channels = [
    "Air temperature",
    "AWA",
    "AWS",
    "Barometer",
    "BSP",
    "Cog",
    "Course",
    "Current drift",
    "Current drift predicted",
    "Current set",
    "Current set predicted",
    "Dew point",
    "Depth",
    "Heading - Cog",
    "Heading to steer",
    "Heading to steer polar",
    "Heel (roll)",
    "J1",
    "Latitude",
    "Layline bearing",
    "Layline bearing on port",
    "Layline bearing on strb",
    "Layline dist on port",
    "Layline dist on starb",
    "Layline distance",
    "Layline time",
    "Layline time on port",
    "Layline time on starb",
    "Longitude",
    "Magnetic variation",
    "Mark bearing",
    "Mark bearing - Cog",
    "Mark latitude",
    "Mark longitude",
    "Mark range",
    "Mark time",
    "Mark twa",
    "Next mark awa",
    "Next mark aws",
    "Next mark bearing",
    "Next mark latitude",
    "Next mark longitude",
    "Next mark polar time",
    "Next mark range",
    "Next mark time on port",
    "Next mark time on starb",
    "Next mark twa",
    "Opposite track",
    "Polar bsp",
    "Polar bsp %",
    "Predicted twd",
    "Predicted tws",
    "Predicted Drift",
    "Relative humidity",
    "Sail",
    "Sail event",
    "Sail mark",
    "Sail next mark",
    "Sea temperature",
    "Sog",
    "Start bias angle",
    "Start bias length",
    "Start distance below line",
    "Start layline on port",
    "Start layline on strdb",
    "Start line square wind",
    "Start port latitude",
    "Start port longitude",
    "Start stdb latitude",
    "Start stdb longitude",
    "Start time to burn",
    "Start time to gun",
    "Start time to layline P",
    "Start time to layline S",
    "Start time to line",
    "Start time to port",
    "Start time to port burn",
    "Start time to strb",
    "Start time to strb burn",
    "Target bsp",
    "Target bsp %",
    "Target twa",
    "Trim (pitch)",
    "TWA",
    "TWD",
    "TWD predicted",
    "TWS",
    "TWS predicted",
    "VMC",
    "VMC %",
    "VMC optimum",
    "VMG",
    "VMG %",
]

# Sort case-insensitively
channels_sorted = sorted(channels, key=lambda x: x.lower())

# Reflow into 3-column markdown table
cols = 3
rows = []
for i in range(0, len(channels_sorted), cols):
    row = channels_sorted[i:i+cols]
    while len(row) < cols:
        row.append("")
    rows.append(row)

print("| | | |")
print("|:-|:-:|:-:|")
for row in rows:
    print(f"| {row[0]} | {row[1]} | {row[2]} |")

print(f"\n<!-- {len(channels_sorted)} channels total -->")
