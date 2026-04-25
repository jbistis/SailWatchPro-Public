# SailWatchPro

<p align="center">
  <a href="https://sailwatchpro.com/">
    <img alt="SailWatchPro" title="SailWatchPro" src="images/icon-76x76@2x.png">
  </a>
</p>

<p align="center">
  <strong>Subscription & Licensing Guide</strong>
</p>

---

## Table of Contents

- [Overview](#overview)
- [Subscription Tiers](#subscription-tiers)
- [Subscribing to SailWatchPro](#subscribing-to-sailwatchpro)
- [Your License Key](#your-license-key)
- [Activating SailWatchPro on iOS](#activating-sailwatchpro-on-ios)
- [Sharing with Your Crew](#sharing-with-your-crew)
- [Renewals](#renewals)
- [Managing Multiple Boats](#managing-multiple-boats)
- [Managing Your Subscription](#managing-your-subscription)
- [Beta Program](#beta-program)
- [Troubleshooting](#troubleshooting)
- [Privacy](#privacy)
- [Support](#support)

---

## Overview

SailWatchPro is licensed per boat with an annual subscription. One subscription covers your boat and all the crew devices — iPhones, iPads, and Apple Watches — connected to it during a race or training session.

Your subscription includes:
- Full access to the iOS app on iPhone and Apple Watch
- Unlimited devices on your boat (skipper, tactician, navigator, crew)
- Annual updates with new features and improvements
- Full access to the post-race analytics portal
- Email support

A subscription is tied to a specific boat — identified by its **Expedition Marine License ID** and **MMSI**. The license key embeds these identifiers, so it only validates against the boat it was issued for.

---

## Subscription Tiers

SailWatchPro is offered in three tiers:

### Performance — $TBD/year

For competitive sailing on boats under 60 feet LOA. Includes everything most racing programs need: tactical advisories, AI race briefings, MOB safety alerts, polar tracking, sail change logging, and Apple Watch integration.

### Grand Prix — $TBD/year

For high-performance racing programs on boats 60 feet and over. Includes everything in Performance, plus advanced features tailored to professional and semi-professional campaigns. Reach out if your program needs custom support.

### Beta

For approved beta testers. By invitation only — typically active racers willing to provide regular feedback during early development. Beta keys expire each January 31, with continuation reviewed annually based on engagement.

If you're interested in joining the beta program, contact us through the [GitHub Issues page](https://github.com/jbistis/SailWatchPro-Public/issues) or reply to any email from `noreply@sailwatchpro.com`.

---

## Subscribing to SailWatchPro

The subscription portal is at [sailwatchpro.com](https://sailwatchpro.com).

### Step 1 — Sign In

Click **Sign In** on the homepage and enter your email address. You'll receive a magic link from `noreply@sailwatchpro.com` — click it to authenticate. No password needed.

The magic link is valid for one hour. If you don't see the email, check your spam folder. If it doesn't arrive, request another from the sign-in page.

### Step 2 — Add Your Boat

After signing in, you'll land on **My Boats**. Click **+ Add Another Boat** and enter:

| Field | Description |
|-------|-------------|
| **Boat Name** | The name as you want it to appear in your account and emails |
| **Expedition Marine License ID** | Your 8-character EM license ID (e.g., `73f15c54`) — find it in Expedition under Help → About |
| **MMSI** | Your boat's 9-digit MMSI number |
| **Tier** | Performance or Grand Prix |

> **Important:** Both the EM License ID and MMSI become part of your license key signature. Enter them carefully — they cannot be changed after a subscription is created.

### Step 3 — Subscribe

Click into your boat from the My Boats page. On the boat detail page, click **Subscribe to SailWatchPro**.

You'll be redirected to Stripe Checkout to complete payment. Subscription is annual and renews automatically.

After successful payment, you'll receive your license key via email within a few seconds.

---

## Your License Key

Your license key looks something like this:

```
SWPRO-NzNmMTVjNTR8MzM4NDgwNjUxfDIwMjcwNDI1fFBSfDU0MzBlZmIw
```

Each key is unique to your boat and tier. Keys contain:
- Your EM License ID
- Your MMSI
- An expiration date
- Your subscription tier (Performance, Grand Prix, or Beta)
- A cryptographic signature

The signature lets SailWatchPro validate the key offline — no internet connection is required to verify a license. As long as your subscription is active, your key continues working even at sea with no signal.

### Where to Find Your Key Later

Your key is always accessible at any time:

- In the original subscription email
- On your boat's detail page at sailwatchpro.com — click **Load License Key**
- Your key persists as long as your subscription is active. If you lose the email, just sign back in to retrieve it.

---

## Activating SailWatchPro on iOS

### Step 1 — Install the App

Install SailWatchPro via TestFlight (during beta) or the App Store (at launch).

### Step 2 — Connect to Expedition Marine

The app needs to receive data from Expedition Marine to validate your license. Make sure:
- Expedition Marine is running on your nav PC
- Your iOS device is on the same network as Expedition
- Expedition has been configured per the [Setup Guide](SETUP-GUIDE.md)

### Step 3 — Activate

In SailWatchPro, navigate to **Settings → Licenses → SailWatchPro → Activate**.

Paste your license key and tap **Activate**.

The app validates the key against:
- Your boat's MMSI from Expedition Marine
- Your Expedition Marine License ID

If both match, you'll see **Valid License** and the app unlocks all features. If validation fails, see [Troubleshooting](#troubleshooting) below.

---

## Sharing with Your Crew

A single license covers your whole crew. Each crew member just needs to install the app and activate it on their own device using the same key.

### Two Ways to Share

**1. Share the License Key Directly**

Forward the key from your subscription email, or copy it from the boat detail page on sailwatchpro.com. Crew members paste it into Settings → Licenses → SailWatchPro → Activate.

**2. Use the In-App QR Code**

If you're already activated, you can share via QR code:

1. In SailWatchPro: **Settings → Licenses → SailWatchPro → Share via QR**
2. Crew member opens the camera app and scans the code
3. The app activates automatically

The QR code is the fastest option for onboarding crew at the dock.

### Crew Limitations

There's no hard limit on devices per license, but please use common sense — a license is intended for one boat's program. If your fleet operates across multiple boats, each boat needs its own subscription.

---

## Renewals

Subscriptions auto-renew annually on the anniversary of your initial payment. A few things to know:

### Your License Key Rotates on Renewal

When your annual payment processes successfully, the system generates a fresh license key with the new expiration date. The new key is emailed to you, and the old key stops working a week or so after the old expiry date.

You'll need to:
1. Check your email for the new key after renewal
2. Activate the new key on each device (or share the new QR code with the crew)

The 7-day grace period means you have time to update your devices without disruption.

### If Your Card Fails

If the renewal payment fails (expired card, insufficient funds, etc.), Stripe will retry several times over a few days. You'll receive notifications. Your existing license continues working through the grace period.

To prevent gaps, update your payment method via the **Manage Subscription** button on your boat's detail page.

### Canceling

You can cancel anytime via **Manage Subscription**. Your license remains active until the end of the current paid period — no prorated refunds, but you don't lose what you've paid for.

After cancellation, your key expires naturally at the end of the period. To resume, simply re-subscribe.

---

## Managing Multiple Boats

If you sail on multiple boats, you can add each one to your account:

1. Sign in at sailwatchpro.com
2. **My Boats → + Add Another Boat**
3. Each boat gets its own subscription, key, and billing cycle

Each subscription is independent. You can subscribe to Performance for one boat and Grand Prix for another, cancel one without affecting the other, etc.

> **Two Expedition installs on the same boat?** Each Expedition installation has its own License ID. For now, register the primary install (the one used during racing) under your boat. Multi-install support is on the roadmap.

---

## Managing Your Subscription

For each boat, the boat detail page shows:

- **Subscription status** — Active, Past Due, Canceled, or Not Subscribed
- **Renewal date** — When your next payment is due
- **License key** — Click **Load License Key** to view it
- **Manage Subscription** button — Opens Stripe's customer portal where you can:
  - Update your payment method
  - Download invoices
  - Cancel your subscription
  - View payment history

Stripe's billing portal is secure and handles all card data — SailWatchPro never sees or stores your card details.

---

## Beta Program

Beta access is free but invite-only. Beta keys are issued manually by the SailWatchPro team to active racers willing to provide regular feedback.

### Beta Mechanics

- **Tier code:** BT
- **Expiration:** January 31 each year (aligns with off-season for most racing programs)
- **Renewal:** Reviewed each January based on participation and feedback. Active beta testers receive renewed keys for the upcoming season.
- **Cost:** Free during beta phase

### Expectations of Beta Testers

We ask beta testers to:
- Use the app during real racing (not just testing at the dock)
- Report bugs, crashes, and unexpected behavior promptly via [GitHub Issues](https://github.com/jbistis/SailWatchPro-Public/issues)
- Share suggestions for improvements
- Respond to occasional check-in emails

If you're an active racer interested in joining the beta, reach out via GitHub Issues.

---

## Troubleshooting

### License Activation Fails

If you paste your key and see **"Invalid License"**, work through these in order:

**1. Check Expedition Marine connection**

The app validates your key against data Expedition sends over the network. If Expedition isn't running or isn't sending data:

- Verify Expedition is running on your nav PC
- Confirm your iOS device is on the same network as Expedition
- Restart Expedition Marine — sometimes the app needs a restart to send the `#S,LICENCE` packet
- Check **Settings → Expedition** in SWP — you should see recent data and a populated License ID

**2. Check the EM License ID matches**

Open Expedition → **Help → About**. Note the License ID shown there. It must match exactly the License ID you entered when adding the boat in the portal.

If they don't match, you registered the wrong License ID at sailwatchpro.com. Contact support — we can help correct this.

**3. Check the MMSI matches**

The MMSI in your boat configuration in SailWatchPro must match the MMSI you entered in the portal. Both come from your boat's official MMSI registration.

**4. Check the expiration date**

If your subscription expired, the key won't validate. Renew at sailwatchpro.com.

### Email Didn't Arrive

License key emails come from `noreply@sailwatchpro.com`.

- Check your spam/junk folder
- Add `noreply@sailwatchpro.com` to your address book
- If you have an iCloud, Gmail, or corporate filter, check the quarantine
- Sign in to sailwatchpro.com and use **Load License Key** on your boat's page — the key is always available there

### Magic Link Email Didn't Arrive

Same email troubleshooting as above. If still missing:

- Make sure you typed your email address correctly
- Wait 2-3 minutes — sometimes email delivery has slight delays
- Check that you're not behind a corporate firewall blocking magic link emails

### Subscribe Button Doesn't Work

If clicking Subscribe shows an error message instead of loading Stripe:

- Refresh the page and try again
- Sign out and sign back in
- Try a different browser
- If still failing, [report the issue](https://github.com/jbistis/SailWatchPro-Public/issues)

### Key Works on iPhone But Not Apple Watch

Apple Watch reads its license from the paired iPhone. If your phone validates but the watch doesn't:

- Make sure both devices are running the same version of SailWatchPro
- Restart both apps
- If the issue persists, restart both devices

### Multiple Devices, One Stops Working

This usually means Expedition Marine connection was lost on that specific device.

- Verify the device is on the boat's network
- Check Settings → Expedition for connection status
- Restart Expedition Marine if needed

---

## Privacy

SailWatchPro stores the minimum data needed to provide your subscription:

- Your email address
- Your boat's name, License ID, MMSI, and tier
- Subscription status and renewal date
- License key

Payment processing is handled entirely by Stripe. SailWatchPro never sees, stores, or has access to your card details.

For Beta and Performance tiers, no personal data beyond the above is collected. Race data, GPS positions, and tactical information stay on your device — they're never transmitted to SailWatchPro servers.

---

## Support

**Email Support**

For subscription, billing, or account questions, reply to your subscription email — replies route directly to the SailWatchPro team.

**Bug Reports & Feature Requests**

Open an issue at [github.com/jbistis/SailWatchPro-Public/issues](https://github.com/jbistis/SailWatchPro-Public/issues).

**Setup Help**

For setup, configuration, and connection issues, see the [Setup Guide](SETUP-GUIDE.md) and [Troubleshooting Guide](TROUBLESHOOTING.md).

---

Happy sailing! ⛵
**SailWatchPro Team**
