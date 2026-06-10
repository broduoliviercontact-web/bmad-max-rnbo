---
title: "MC vs MCS Objects"
source: https://docs.cycling74.com/userguide/mc/mc_mcvsmcs/
source_path: /userguide/mc/mc_mcvsmcs/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC vs MCS Objects

Source: https://docs.cycling74.com/userguide/mc/mc_mcvsmcs/

## Extracted Text

# MC vs MCS Objects
As you work with MC you'll encounter a few objects beginning with mcs .
The "s" stands for single , meaning that an MCS object is a single instance with a single multi-channel input and a single multi-channel output. An example is mcs.gen~ : If you make a Gen patcher containing in 1 , in 2 , and in 3 operators, a normal gen~ object would show three inlets:
The mcs.gen~ version of this patch would have only one multi-channel inlet. You can connect a multi-channel patch cord to this inlet and it will distribute the first three channels to the corresponding in operators. Likewise, multiple outlets are provided as a single multi-channel outlet.
By contrast, if you made an mc.gen~ with this same Gen patcher, you would see an object with three inlets and two outlets. Each of these inlets corresponds to the in operator within the Gen patcher, but with mc.gen~ there are multiple instances of the Gen patcher running inside the MC wrapper, so multichannel signals connected to these inlets are distributed to each Gen instance.
Another group of MCS objects deal with multichannel buffer~ data. If you create a buffer~ object with four channels of audio data, the mcs.play~ object will combine all four output channels of this audio data into one multichannel output. By contrast, mc.play~ lets you create multiple "players" of the same data in the MC Wrapper.
In deciding whether you want the MC or MCS version of play~ , ask yourself whether you want to play one copy of a sound with multiple channels, or several copies of the same sound you can control independently.
