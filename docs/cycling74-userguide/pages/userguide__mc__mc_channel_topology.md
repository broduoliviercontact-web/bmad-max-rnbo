---
title: "MC Channel Topology"
source: https://docs.cycling74.com/userguide/mc/mc_channel_topology/
source_path: /userguide/mc/mc_channel_topology/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Channel Topology

Source: https://docs.cycling74.com/userguide/mc/mc_channel_topology/

## Extracted Text

# MC Channel Topology
Multichannel patch cords are useful as a way to organize audio signals. MC includes several objects that you can use to change how signals are organized.
For example, if you are using mc.vst~ with a stereo synth plug-in that has 10 instances, that object will have two multichannel outputs with 10 channels each. The multichannel patch cord on the left has the "left" outputs for all 10 synths and the multichannel patch cord on the right has the "right" outputs for all 10 synths.
If want to mix all the synths to stereo, you will need to produce a two-channel signal routed to mc.dac~ . To mix the signals as expected, use mc.interleave~ to produce a 20-channel signal that alternates the left and right channels.
You can feed this 20-channel signal to mc.stereo~ , which (by default) will add the odd-numbered channels (1, 3, 5...) to its first (or "left" output) and even-numbered channels (2, 4, 6...) to its second (or "right" output). The resulting signal can be connected directly to mc.dac~ .
Use mc.deinterleave~ to transform an interleaved signal back to two non-interleaved signals. This is useful for separating signals for the inputs to mc.vst~ , mc.poly~ , or mc.gen~ .
The mc.transpose~ object provides a more general way to reorganize multichannel signals. If you have four instances of groove~ in an mc.groove~ object playing back stereo samples, it provides you with two four-channel patch cords separating left and right channels. It may be more useful to have four two-channel patch cords, each of which has the left and right channels for the four instances. This can be accomplished with mc.transpose~ :
Now you can add individual effects on a per-MC-instance basis, using mcs.vst~ as shown here:
