---
title: "MC Recording and Playback"
source: https://docs.cycling74.com/userguide/mc/mc_multichannel_sources/
source_path: /userguide/mc/mc_multichannel_sources/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Recording and Playback

Source: https://docs.cycling74.com/userguide/mc/mc_multichannel_sources/

## Extracted Text

# MC Recording and Playback
## Buffer Playback with mc.* Objects
The mc.* versions of the objects create multiple parallel versions of the audio playback objects. By changing parameters to each of the devices, you can create complex results with relatively little patching. For example, you can use mc.groove~ modified by the`deviate`wrapper message to create a swarming effect.
## Buffer Playback with mcs.* Objects
Using the mcs.* objects for buffer playback makes it easier to integrate audio streams with other MC objects. The mcs.* objects implement multichannel inlets and outlets that can be further manipulated with MC objects or routed to multi-speaker audio systems.
For example, we can use the multichannel output of the mcs.groove~ object as source material for a dual-channel fade-in patch. Since the multichannel audio is directly manipulated by the mc.*~ object, a multichannel signal will control the output levels of our file player.
## Recording
Use the mc.sfrecord~ object to record a multi-channel signal directly to disk.
You can also record into a multichannel buffer~ object using the mc.record~ object.
