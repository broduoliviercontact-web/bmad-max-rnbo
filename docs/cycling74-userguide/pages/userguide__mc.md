---
title: "MC Overview"
source: https://docs.cycling74.com/userguide/mc/
source_path: /userguide/mc/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Overview

Source: https://docs.cycling74.com/userguide/mc/

## Extracted Text

# MC
MC supports multiple channels of audio in a single patchcord. It also allows standard Max audio objects to operate on many channels of audio at the same time.
Signal visualization objects such as meter~ and scope~ will adapt themselves to multichannel input signals.
The MC Wrapper holds multiple instances of Max audio objects in a single object box. Wrapped object names start with mc , for instance mc.cycle~ is the MC-wrapped cycle~ object. The wrapper also offers many powerful features for controlling multiple objects.
In addition to MC wrapper objects, MC-specific objects aid in multichannel signal manipulation.
## Topics
-
Spatialization - Working with multiple channels over multiple speakers or output channels
-
Polyphony - Managing polyphony with MC
-
Gen - MC and Gen
-
Events - Events and MC objects
-
Mixing and Panning - Up- and down-mixing, multi-speaker panning, and signal routing
-
Plug-ins - Hosting plug-ins in MC
-
Dynamic Routing - Sending multi-channel signals to different places
