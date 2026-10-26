# Memo: Google open-display ad tech (DV360, DFP, AdX)

**Purpose:** Interview / cover-letter background for Keystone London (Economist 2027).  
**One case to know:** UK advertisers’ claim that Google steered open-web display ads through its own exchange (AdX). Keystone (Andrea Coscelli’s team) is the economic expert for the proposed class side.

---

## The three layers in one load of a webpage

When a reader opens a site, an ad slot is sold in a few hundred milliseconds. Three Google products often sit in that path:

| Short | Full name | Side | Role in one sentence |
| --- | --- | --- | --- |
| **DV360** | **Display & Video 360** | **Buy-side** (advertisers / agencies) | Decides whether to bid, how much, and which creative to show |
| **DFP** | **DoubleClick for Publishers** (now largely **Google Ad Manager**; cases still say DFP) | **Sell-side** (publishers) | Manages slots on the site, floors, and which demand source fills the slot |
| **AdX** | **Google Ad Exchange** (buyers often access it via **Authorized Buyers**) | **Exchange / SSP** (marketplace; sell-side of the stack) | Runs the auction that matches bids to publisher inventory |

**Google Ads** is Google’s other main buy-side product (broader / smaller-advertiser facing). **DV360** is the large buy-side platform used heavily by agencies and brands for display and video.

---

## Who is buyer vs seller?

- **Only DV360 (and Google Ads) are buy-side.**
- **DFP is sell-side** (publisher’s traffic controller).
- **AdX is not a buyer tool.** It is the auction house that **sells** publisher inventory to whoever is bidding (including Google’s own buy-side tools and rival buyers).

So: **DV360 places bids; AdX runs the auction; DFP places the winning ad on the page.**

---

## A short story that connects them

1. A reader opens a newspaper sports page. An empty banner must be filled.
2. **DFP** (newspaper) packages the impression (slot, context, floor) and asks for demand.
3. The request goes to **AdX**, which auctions the impression to many buyers at once.
4. **DV360** (shoe brand / agency) applies campaign rules, bids into AdX if the impression looks valuable.
5. AdX picks a winner and tells DFP; DFP serves the creative. The reader sees the ad.

One page load: **DV360 buys → AdX auctions → DFP places.**

---

## What the UK claim alleges (why it matters for competition)

The claim says Google is strong in **buy-side tools** (Google Ads, DV360) and in the **publisher ad server** (DFP), and used that position to **steer** open-web display transactions through its own exchange **AdX** (self-preferencing)—for example by favouring AdX on the buy side and by sell-side practices such as “Last Look”—so rival exchanges competed on worse terms and advertisers paid more for less effective ads.

That is a **multi-sided platform / self-preferencing** story: own the tools on both sides of the market, and allegedly tilt the middle marketplace toward yourself.

---

## Difference to remember in one line

**DV360 = shopper with a wallet. AdX = auction house. DFP = store manager who hangs the winning poster.**

---

## Sources (for further reading)

- UK CAT summary of the AGC collective proceedings claim form (case 1773/7/7/26)
- KP Law note on the UK display-advertiser claim (Keystone / Coscelli as economic expert)
- Industry descriptions of programmatic stack: DSP (buy-side), publisher ad server, exchange/SSP
