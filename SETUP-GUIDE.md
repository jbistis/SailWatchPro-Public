# SailWatchPro

<p align="center">
  <a href="https://sailwatchpro.io/">
    <img alt="SailWatchPro" title="SailWatchPro" src="images/icon-76x76@2x.png">
  </a>
</p>

<p align="center">
  Setup Guide
</p>


## Apple Watch Integration

Your Apple Watch becomes a powerful racing companion with dedicated views:

<div align="center">
 <img src="images/swp-apple-watch-views.png" width="512"/>
</div>

**Watch Features**
- **Race Timer**: Dedicated start sequence display
- **BSP Split Box**: Speed data with performance indicators
- **Heel Angle**: Real-time heel monitoring
- **VMG Split Box**: Velocity made good analysis
- **TWA/AWA Split Boxes**: Wind angle optimization
- **Depth Split Box**: Safety monitoring with alerts
- **Custom Data Fields**: Personalized data display
- **Automatic Page Switching**: Switches to the depth page on dangerous conditions

**Watch Connectivity**
- Seamless data sync from iPhone app
- Independent operation during races
- Night mode support for all watch faces

---

## Settings & Customization

### Connection Settings
- **IP Address**: Your boat's network broadcast address
- **UDP Port**: Communication port (typically 5098)
- **Test Mode**: Use simulated data for training

### Boat Configuration
- **Boat Name**: Your vessel identification
- **Boat Length**: Used for distance calculations in boat lengths
- **Draft**: Critical for depth safety calculations
- **TWA Reaching Threshold**: Sailing mode detection sensitivity

### Display Options
- **Light Mode**: Uses traditional dark text on a light background
- **Dark Mode**: Inverts the color scheme, displaying light text on a dark background
- **Night Mode**: Red-tinted display for night vision preservation
- **Chart Time Windows**: Customizable data history viewing
- **Map Style**: Choose between hybrid, standard, satellite, or imagery views

### Safety Settings
- **Depth Alerts**: Automatic warnings based on draft + safety margin
- **Audio Countdown**: Spoken start sequence announcements
- **MOB (Man Overboard)**: Emergency position marking and tracking

---

## Troubleshooting

### Connection Issues
- **Red status indicators**: Check IP address and UDP port settings
- **No data reception**: Verify Expedition Marine is broadcasting data
- **Intermittent connection**: Check WiFi signal strength and network stability

### Display Problems
- **Data not updating**: Restart Expedition Marine or the UDP connection in settings
- **Watch not syncing**: Check iPhone-Watch connectivity and app permissions

### Performance Issues
- **Slow response**: Reduce chart time windows or restart the app
- **Battery drain**: Use night mode and reduce display brightness
- **Memory issues**: Clear old event logs and restart periodically

---

## Getting Started
- **Latest Version**: Because this app shares data between users, it is recommended that all iOS devices run the same version of the app.

### First Launch Setup

1. **Configure the Expdition Marine Network**
  - Start Expedition Marine on the boat PC.
  - From the ☰ Hamburger Menu > drag down and hover over Instruments > click on Number of network connections
  - Enter one greater than the number displayed to add one more network > click OK
  - From the ☰ Hamburger Menu > drag down, hover over, and click Instruments
  - Select the Network you just created and enter the following
  - Alias - SailWatchPro
  - Instruments - Expedition
  - Address - 192.168.XXX.YYY, where this is the IP address of your Expedition Marine PC.
  - Port - Select any port that is not used by another Expedition Marine network.
  - Click Expedition Settings
  - Click the Exp Rx filter and select the Receive marks check box.
  - Click the Exp Tx filter and select the channels noted in Appendix A below.

1. **Connect to Expedition Marine**
  - Install the app on your iOS device.
  - In the SailProApp, touch Settings and configure your boat's WiFi network and other details.
  - Set the IP address to match the Expedition Marine network IP address you set in the previous step.
  - Set the UDP port to match the Expedition Marine network port you set in the previous step.
  - Set the IP address for any NMEA 2000 Ethernet Gateway and UDP port
  - Restart to enable the connection and look for green status indicators.

2. **Configure Your Boat**
  - Enter your boat name
  - Enter your boat's MMSI number
  - Set boat length (for distance calculations in boat lengths)
  - Set draft (for depth safety alerts)
  - Adjust TWA reaching threshold for sailing mode detection

3. **Choose Your Display Mode**
  - **Night Mode**: Red-tinted display for night sailing
  - **Test Mode**: Use simulated data for testing and demos

## Expedition Marine Requirements

## Exp Rx filter
Enable Receive marks

## Exp Tx filter
AWA, AWS, Barometer, BSP, Cog, Course, Current Drift, Current Set, Depth,
Heading, Heading - Cog, Heading to steer, Heading to steer polar, Heel (roll), Latitude,
Layline bearing, Layline bearing on port, Layline bearing on strb, Layline distance on port, Layline distance on starb, Layline Distance, Layline time, Layline time on port, Layline time on starb, Longitude,
Magnetic variation, Mark bearing, Mark bearing - Cog, Mark latitude, Mark longitude, Mark range, Mark time, Mark twa, Opposite track,
Next mark awa, Next mark aws, Next mark bearing, Next mark latitude, Next mark longitude,
Next mark polar time, Next mark range, Next mark time on port, Next mark time on starb, Next mark tws,
Opposite track, Polar bsp, Polar bsp %, Sail mark, Sail next mark, Sog,
Start bias length, Start distance below line, Start layline on port, Start layline on strbd, Start line square wind,
Start port latitude, Start port longitude, Start stbd latitude, Start stbd longitude,
Start time to burn, Start time to gun, Start time to layline P, Start time to layline S, Start time to line,
Start time to port, Start time to strb, Target bsp, Target twa, Target bsp %, Target twa, Trim (pitch) rate,
TWA, TWS, TWS, VMC, VMC %

---

## Support & Updates

SailWatchPro is continuously updated with new features and improvements based on user feedback and racing experience. Regular updates include enhanced analytics, new data visualizations, and improved integration with marine electronics.

For the best racing experience, ensure both your iPhone and Apple Watch apps are up to date.

For Support & Enhancement Requests, please contact us at https://github.com/jbistis/SailWatchPro-Public/issues.  We’re eager to hear your suggestions on features that would make the app even more valuable to you.

---

*Happy sailing, and may you always find the favorable wind shift!*

**SailWatchPro Team**
