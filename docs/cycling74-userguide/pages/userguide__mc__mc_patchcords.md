---
title: "MC Patchcords"
source: https://docs.cycling74.com/userguide/mc/mc_patchcords/
source_path: /userguide/mc/mc_patchcords/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Patchcords

Source: https://docs.cycling74.com/userguide/mc/mc_patchcords/

## Extracted Text

# MC Patch Cords
MC patch cords carry multiple channels of audio simultaneously. This makes it easier to work with audio spatialization, complex synthesis voicings and explicitly polyphonic signals.
A patch cord will be multi-channel if it is connected to a multi-channel outlet of an MC object.
These patch cords have a distinctive appearance: they are blue and black (as opposed yellow and black single-channel patch cords). MC patch cords are also slightly thicker. You can quickly see how many channels are being used by hovering over the patch cord when the patcher is unlocked.
## Auto-Adding Multi-Channel Signals
With single-channel patch cords, connecting two signals into a single object inlet will add the two signals before they are received by the object.
With multi-channel patch cords, this auto-adding also occurs, but it is more complex when the incoming multi-channel patchcords contain different numbers of channels.
When multi-channel signal patchcords are connected to a single inlet, the resulting signal will contain the number of channels from the patch cord with the greatest number of signals.
