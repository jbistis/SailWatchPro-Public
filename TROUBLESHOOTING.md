# SailWatchPro Troubleshooting Guide

<p align="center">
  <a href="https://sailwatchpro.io/">
    <img alt="SailWatchPro" title="SailWatchPro" src="images/icon-76x76@2x.png">
  </a>
</p>

<p align="center">
  <strong>Connection & Performance Troubleshooting</strong>
</p>

---

## Table of Contents

- [Connection Issues](#connection-issues)
  - [Test Network Connectivity](#test-network-connectivity)
  - [Check WiFi Signal Strength](#check-wifi-signal-strength)
  - [Verify Port Settings](#verify-port-settings)
  - [Windows Firewall Configuration](#windows-firewall-configuration)
- [Data Sync Issues](#data-sync-issues)
- [Display Problems](#display-problems)
- [Performance Issues](#performance-issues)
- [Common Error Messages](#common-error-messages)
- [Still Need Help?](#still-need-help)

---

## Connection Issues

### Symptoms
- Red connection indicators in SailWatchPro
- No data appearing from Expedition Marine
- Intermittent connection drops
- Can receive data but cannot send commands

---

### Test Network Connectivity

**Step 1: Find IP Addresses**

**Find your Expedition PC's IP address:**
1. Open Command Prompt in Windows:
   - **Windows PC:** Press **Windows Key + R**
   - **Mac keyboard (VM):** Press **Command (⌘) + R** or click the Windows Start menu
2. Type `cmd` and press Enter
3. Type `ipconfig` and look for **IPv4 Address** under your active network adapter
4. Write down this IP (example: 192.168.1.50)

**Find your iPad's IP address:**
- Settings → Wi-Fi → Tap the (i) icon → IPv4 Address
- Write down this IP (example: 192.168.1.100)

---

**Step 2: Test Connection from iPad to PC**

**From your iPad/iPhone:**
1. Install [Ping - Network Utility](https://apps.apple.com/us/app/ping-network-utility/id576773404)
2. Open the app and ping your Expedition PC's IP address
3. If successful, you'll see replies with response times

---

**Step 3: Test Connection from PC to iPad**

**From your Expedition PC:**
1. Open Command Prompt (already open from Step 1, or press **Windows Key + R**, type `cmd`)
2. Type: `ping` followed by your iPad's IP address
   - Example: `ping 192.168.1.100`
3. Press Enter
4. If successful, you'll see replies with response times

---

**If ping works in both directions, your network is fine.** The issue is likely firewall or port configuration.

**If ping fails:**
- ✅ Verify both devices are on the same Wi-Fi network
- ✅ Check that no VPN is active on either device
- ✅ Restart your router and reconnect devices
- ✅ Check for "AP Isolation" or "Client Isolation" settings on your router (disable if enabled)

---

### Check WiFi Signal Strength

Weak WiFi signals can cause intermittent connections and data loss.

**Check signal strength on your iPad/iPhone:**
1. Install [WiFiman](https://apps.apple.com/us/app/wifiman/id1385561119) (free)
2. Open the app to see real-time signal strength

**Signal strength guide:**
- **-30 to -50 dBm** = Excellent ✅
- **-50 to -60 dBm** = Good ✅
- **-60 to -70 dBm** = Fair ⚠️ (may have issues)
- **-70 dBm or worse** = Poor ❌ (connection problems likely)

**If signal is weak:**
- Move closer to the router
- Reduce obstacles between device and router
- Consider adding a WiFi extender or access point
- Check for interference from other devices

---

### Verify Port Settings

Port configuration must be **opposite** between Expedition and SailWatchPro:

| Application | Rx Port (Receive) | Tx Port (Transmit) |
|-------------|-------------------|-------------------|
| **Expedition Marine** | 5098 | 5099 |
| **SailWatchPro** | 5099 | 5098 |

**Why opposite?** Expedition's Tx port (5099) must match SailWatchPro's Rx port (5099), and vice versa.

**To check in SailWatchPro:**
- Settings → Expedition Marine → Verify Rx and Tx ports

**To check in Expedition Marine:**
- Tools → Settings → Communications → UDP ports

**Common port issues:**
- ❌ Using same port for Rx and Tx on both apps
- ❌ Ports swapped (5098 where 5099 should be)
- ❌ Firewall blocking one or both ports

---

### Windows Firewall Configuration

**Quick Test: Temporarily disable firewall**

Open Command Prompt **as Administrator** and run:
```cmd
netsh advfirewall set allprofiles state off
```

Test your connection. If it works, the firewall was blocking UDP traffic.

**Re-enable firewall:**
```cmd
netsh advfirewall set allprofiles state on
```

---

**Permanent Fix: Add firewall rules for Expedition**

**Method 1: Add Port Rules**

1. Open **Windows Defender Firewall with Advanced Security**
   - Press Windows Key, type "firewall", select "Windows Defender Firewall with Advanced Security"
2. Click **Inbound Rules** → **New Rule**
3. Select **Port** → Click Next
4. Select **UDP** → Enter ports: `5098, 5099` → Click Next
5. Select **Allow the connection** → Click Next
6. Check all profiles (Domain, Private, Public) → Click Next
7. Name: "Expedition Marine UDP Ports" → Click Finish

**Method 2: Add Application Rule**

1. Open **Windows Defender Firewall with Advanced Security**
2. Click **Inbound Rules** → **New Rule**
3. Select **Program** → Click Next
4. Browse to `Expedition.exe` (usually in `C:\Program Files\Expedition`)
5. Select **Allow the connection** → Click Next
6. Check all profiles → Click Next
7. Name: "Expedition Marine" → Click Finish

---

### Still Having Connection Issues?

**Check these additional items:**

✅ **Same Network**
- Both devices must be on the same Wi-Fi network
- Some boats have multiple networks (2.4GHz and 5GHz) - use the same one

✅ **Expedition UDP Output Enabled**
- In Expedition: Tools → Settings → Communications
- Verify UDP output is enabled
- Broadcast IP should be: `255.255.255.255`

✅ **Router AP Isolation**
- Some routers have "AP Isolation" or "Client Isolation" enabled
- This prevents devices from communicating with each other
- Check router settings and disable if present

✅ **No VPN Active**
- VPNs can interfere with local network communication
- Disable VPN on both devices while using SailWatchPro

✅ **Restart Services**
- Restart Expedition Marine
- Force quit and restart SailWatchPro
- Restart router if issues persist

---

## Data Sync Issues

### Sail Changes Not Syncing Between Devices

**Symptoms:**
- Hoist sail on iPad A, doesn't appear on iPad B
- Crew positions not updating across devices
- Race setup changes not syncing

**Troubleshooting:**

1. **Check SW Protocol Status**
   - Settings → SW Protocol → Verify "Allow Coordinator" is enabled on at least one device
   - Check "Connected Devices" count - should show other iPads/devices

2. **Verify SW Port**
   - Default SW port is 5100
   - All devices must use the same SW port
   - Settings → SW Protocol → SW Port

3. **Check Coordinator Election**
   - Only one device should be coordinator (highest uptime)
   - Settings → SW Protocol → Shows coordinator status

4. **Network Issues**
   - Follow [Test Network Connectivity](#test-network-connectivity) steps
   - SW Protocol uses UDP broadcasts like Expedition data

**If only some data syncs:**
- Crew positions work but sails don't = Check sail state timestamps
- Nothing syncs = Network/firewall blocking SW port (5100)

---

## Display Problems

### Data Not Updating

**Symptoms:**
- Wind data frozen
- Speed/heading not changing
- Old timestamps on data

**Solutions:**

1. **Check connection status** (top right indicators)
   - Green = Connected ✅
   - Red = Disconnected ❌

2. **Verify Expedition is running and broadcasting**
   - Check Expedition Marine is open
   - Verify data is updating in Expedition itself

3. **Restart connection**
   - Settings → Expedition Marine → Toggle connection off/on
   - Or force quit and restart SailWatchPro

4. **Check network connection**
   - Settings → Wi-Fi → Verify connected
   - Run ping test (see [Test Network Connectivity](#test-network-connectivity))

---

### Chart Data Not Displaying

**Symptoms:**
- Blank charts
- Missing historical data
- Charts show "No Data"

**Solutions:**

1. **Shorten time window**
   - Very long time ranges can be slow to load
   - Try shorter time window (1 hour instead of 24 hours)

2. **Clear and rebuild**
   - Settings → Advanced → Clear cache (if available)
   - Force quit and restart app

3. **Check data source**
   - Verify Expedition is sending the specific data type
   - Some data may not be available from your instruments

---

### Watch Not Syncing

**Symptoms:**
- Apple Watch shows old data
- Watch app not updating
- Watch shows "Connecting..."

**Solutions:**

1. **Check iPhone-Watch connection**
   - Swipe up on Watch → Check connected icon
   - iPhone → Watch app → My Watch → Verify paired

2. **Verify Watch Complications**
   - Watch face complications may need refresh
   - Force touch watch face → Customize → Re-add complication

3. **Restart both devices**
   - Force quit SailWatchPro on iPhone
   - Restart Watch app
   - If issues persist, unpair and re-pair Watch

4. **Check app versions**
   - iPhone and Watch must run same version of SailWatchPro
   - Update both if needed

---

## Performance Issues

### App Running Slow

**Symptoms:**
- Lag when switching screens
- Delayed button responses
- Choppy chart animations

**Solutions:**

1. **Reduce chart time windows**
   - Shorter time ranges = faster performance
   - Settings → Charts → Adjust default time windows

2. **Close background apps**
   - Double-click home button → Swipe up on unused apps
   - Free up memory for SailWatchPro

3. **Restart app**
   - Force quit SailWatchPro
   - Reopen fresh

4. **Restart device**
   - Power off iPad/iPhone
   - Wait 30 seconds
   - Power back on

---

### Battery Drain

**Symptoms:**
- Battery draining faster than expected
- Device getting hot

**Solutions:**

1. **Enable Night Mode**
   - Settings → Night Mode ON
   - Red-tinted display uses less power

2. **Reduce screen brightness**
   - Swipe down → Adjust brightness slider
   - Use lowest comfortable brightness

3. **Close unused apps**
   - Background apps consume battery
   - Close everything except SailWatchPro

4. **Disable unnecessary features**
   - Turn off features you're not using
   - Settings → Disable unused data displays

5. **Use Low Power Mode** (if critical)
   - Settings → Battery → Low Power Mode
   - Note: May affect performance

---

## Common Error Messages

### "Unable to Connect to Expedition"

**Cause:** Network connection issue or Expedition not broadcasting

**Solution:**
1. Verify Expedition is running
2. Check IP address is correct (Settings → Expedition Marine)
3. Run ping test (see [Test Network Connectivity](#test-network-connectivity))
4. Check Windows Firewall (see [Windows Firewall Configuration](#windows-firewall-configuration))

---

### "Connection Timeout"

**Cause:** Network latency or weak WiFi signal

**Solution:**
1. Check WiFi signal strength (see [Check WiFi Signal Strength](#check-wifi-signal-strength))
2. Move closer to router
3. Restart router
4. Check for network congestion (too many devices)

---

### "Port Already in Use"

**Cause:** Another app is using the same UDP port

**Solution:**
1. Close other navigation/marine apps
2. Change port in Settings → Expedition Marine
3. Update Expedition to match new port
4. Restart SailWatchPro

---

### "Firewall Blocking Connection"

**Cause:** Windows Firewall blocking UDP packets

**Solution:**
- Follow [Windows Firewall Configuration](#windows-firewall-configuration) steps
- Add rules for ports 5098 and 5099
- Add application rule for Expedition.exe

---

## Still Need Help?

If you've tried the above steps and still have issues:

1. **Check for app updates**
   - App Store → Updates → Install latest SailWatchPro version

2. **Review setup guide**
   - [Setup Guide](SETUP-GUIDE.md) - Verify initial configuration

3. **Submit bug report**
   - GitHub Issues: https://github.com/jbistis/SailWatchPro-Public/issues
   - Include:
     - Device model and iOS version
     - SailWatchPro version
     - Expedition version
     - Description of problem
     - Steps to reproduce
     - Screenshots if applicable

4. **Community support**
   - Check existing GitHub issues for similar problems
   - Search for your error message

---

**Happy sailing! ⛵**  
**SailWatchPro Team**