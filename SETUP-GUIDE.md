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

**Exp Tx filter** (select these channels):

**Exp Tx filter** (select these channels):



AWA, AWS, Barometer, BSP, Cog, Course, Current Drift, Current Set, Depth, Heading, Heading - Cog, Heading to steer, Heading to steer polar, Heel (roll), Latitude, Layline bearing, Layline bearing on port, Layline bearing on strb, Layline distance on port, Layline distance on starb, Layline Distance, Layline time, Layline time on port, Layline time on starb, Longitude, Magnetic variation, Mark bearing, Mark bearing - Cog, Mark latitude, Mark longitude, Mark range, Mark time, Mark twa, Opposite track, Next mark awa, Next mark aws, Next mark bearing, Next mark latitude, Next mark longitude, Next mark polar time, Next mark range, Next mark time on port, Next mark time on starb, Next mark tws, Opposite track, Polar bsp, Polar bsp %, Sail mark, Sail next mark, Sog, Start bias length, Start distance below line, Start layline on port, Start layline on strbd, Start line square wind, Start port latitude, Start port longitude, Start stbd latitude, Start stbd longitude, Start time to burn, Start time to gun, Start time to layline P, Start time to layline S, Start time to line, Start time to port, Start time to strb, Target bsp, Target twa, Target bsp %, Target twa, Trim (pitch) rate, TWA, TWS, VMC, VMC %

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

- AWA
- AWS
- Barometer
- BSP
- Cog
- Course
- Current Drift
- Current Set
- Depth
- Heading
- Heading - Cog
- Heading to steer
- Heading to steer polar
- Heel (roll)
- Latitude
- Layline bearing
- Layline bearing on port
- Layline bearing on strb
- Layline distance on port
- Layline distance on starb
- Layline Distance
- Layline time
- Layline time on port
- Layline time on starb
- Longitude
- Magnetic variation
- Mark bearing
- Mark bearing - Cog
- Mark latitude
- Mark longitude
- Mark range
- Mark time
- Mark twa
- Opposite track
- Next mark awa
- Next mark aws
- Next mark bearing
- Next mark latitude
- Next mark longitude
- Next mark polar time
- Next mark range
- Next mark time on port
- Next mark time on starb
- Next mark tws
- Polar bsp
- Polar bsp %
- Sail mark
- Sail next mark
- Sog
- Start bias length
- Start distance below line
- Start layline on port
- Start layline on strbd
- Start line square wind
- Start port latitude
- Start port longitude
- Start stbd latitude
- Start stbd longitude
- Start time to burn
- Start time to gun
- Start time to layline P
- Start time to layline S
- Start time to line
- Start time to port
- Start time to strb
- Target bsp
- Target twa
- Target bsp %
- Target twa
- Trim (pitch) rate
- TWA
- TWS
- VMC
- VMC %

- 
| AWA     | AWS      | WTA |
| AWA     | AWS      | WTA |
| AWA     | AWS      | WTA |
| AWA     | AWS      | WTA |


|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [adaptor](https://github.com/gofiber/fiber/tree/main/middleware/adaptor)             | Converter for net/http handlers to/from Fiber request handlers.                                                                                                         |
| [basicauth](https://github.com/gofiber/fiber/tree/main/middleware/basicauth)         | Provides HTTP basic authentication. It calls the next handler for valid credentials and 401 Unauthorized for missing or invalid credentials.                            |
| [cache](https://github.com/gofiber/fiber/tree/main/middleware/cache)                 | Intercept and cache HTTP responses.                                                                                                                                     |
| [compress](https://github.com/gofiber/fiber/tree/main/middleware/compress)           | Compression middleware for Fiber, with support for `deflate`, `gzip`, `brotli` and `zstd`.                                                                             |
| [cors](https://github.com/gofiber/fiber/tree/main/middleware/cors)                   | Enable cross-origin resource sharing (CORS) with various options.                                                                                                       |
| [csrf](https://github.com/gofiber/fiber/tree/main/middleware/csrf)                   | Protect from CSRF exploits.                                                                                                                                             |
| [earlydata](https://github.com/gofiber/fiber/tree/main/middleware/earlydata)         | Adds support for TLS 1.3's early data ("0-RTT") feature.                                                                                                                |
| [encryptcookie](https://github.com/gofiber/fiber/tree/main/middleware/encryptcookie) | Encrypt middleware which encrypts cookie values.                                                                                                                        |
| [envvar](https://github.com/gofiber/fiber/tree/main/middleware/envvar)               | Expose environment variables with providing an optional config.                                                                                                         |
| [etag](https://github.com/gofiber/fiber/tree/main/middleware/etag)                   | Allows for caches to be more efficient and save bandwidth, as a web server does not need to resend a full response if the content has not changed.                      |
| [expvar](https://github.com/gofiber/fiber/tree/main/middleware/expvar)               | Serves via its HTTP server runtime exposed variables in the JSON format.                                                                                                 |
| [favicon](https://github.com/gofiber/fiber/tree/main/middleware/favicon)             | Ignore favicon from logs or serve from memory if a file path is provided.                                                                                               |
| [healthcheck](https://github.com/gofiber/fiber/tree/main/middleware/healthcheck)     | Liveness and Readiness probes for Fiber.                                                                                                                                |
| [helmet](https://github.com/gofiber/fiber/tree/main/middleware/helmet)               | Helps secure your apps by setting various HTTP headers.                                                                                                                 |
| [idempotency](https://github.com/gofiber/fiber/tree/main/middleware/idempotency)     | Allows for fault-tolerant APIs where duplicate requests do not erroneously cause the same action performed multiple times on the server-side.                           |
| [keyauth](https://github.com/gofiber/fiber/tree/main/middleware/keyauth)             | Adds support for key based authentication.                                                                                                                              |
| [limiter](https://github.com/gofiber/fiber/tree/main/middleware/limiter)             | Adds Rate-limiting support to Fiber. Use to limit repeated requests to public APIs and/or endpoints such as password reset.                                             |
| [logger](https://github.com/gofiber/fiber/tree/main/middleware/logger)               | HTTP request/response logger.                                                                                                                                           |
| [pprof](https://github.com/gofiber/fiber/tree/main/middleware/pprof)                 | Serves runtime profiling data in pprof format.                                                                                                                          |
| [proxy](https://github.com/gofiber/fiber/tree/main/middleware/proxy)                 | Allows you to proxy requests to multiple servers.                                                                                                                       |
| [recover](https://github.com/gofiber/fiber/tree/main/middleware/recover)             | Recovers from panics anywhere in the stack chain and handles the control to the centralized ErrorHandler.                                                               |
| [redirect](https://github.com/gofiber/fiber/tree/main/middleware/redirect)           | Redirect middleware.                                                                                                                                                    |
| [requestid](https://github.com/gofiber/fiber/tree/main/middleware/requestid)         | Adds a request ID to every request.                                                                                                                                     |
| [responsetime](https://github.com/gofiber/fiber/tree/main/middleware/responsetime)   | Measures request handling duration and writes it to a configurable response header.                          |
| [rewrite](https://github.com/gofiber/fiber/tree/main/middleware/rewrite)             | Rewrites the URL path based on provided rules. It can be helpful for backward compatibility or just creating cleaner and more descriptive links.                        |
| [session](https://github.com/gofiber/fiber/tree/main/middleware/session)             | Session middleware. NOTE: This middleware uses our Storage package.                                                                                                     |
| [skip](https://github.com/gofiber/fiber/tree/main/middleware/skip)                   | Skip middleware that skips a wrapped handler if a predicate is true.                                                                                                    |
| [static](https://github.com/gofiber/fiber/tree/main/middleware/static)               | Static middleware for Fiber that serves static files such as **images**, **CSS**, and **JavaScript**.                                                                    |
| [timeout](https://github.com/gofiber/fiber/tree/main/middleware/timeout)             | Adds a max time for a request and forwards to ErrorHandler if it is exceeded.                                                                                           |



