---
title: "MC Signal Manipulation Objects"
source: https://docs.cycling74.com/userguide/mc/mc_signals_newobjects/
source_path: /userguide/mc/mc_signals_newobjects/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Signal Manipulation Objects

Source: https://docs.cycling74.com/userguide/mc/mc_signals_newobjects/

## Extracted Text

# MC Signal Manipulation Objects
MC includes a number of objects that are useful for combining, separating, and transforming multichannel signals. These objects do not use the MC Wrapper but are useful in conjunction with wrapper-based objects.
## Creating Multi-Channel Signals
mc.pack~ accepts numbers, single-channel signals, or multichannel signals and produces a multichannel signal with a designated number of outputs. This can be used to group separate single-channel sources into a single multichannel patch cord.
If you want to create a multichannel signal from numbers, you can also use the wrapper-based object mc.sig~ or the even simpler mc.list~ .
## Separating Multi-Channel Signals into Single Channels
To separate a multichannel signal into one or more individual signal outputs, use mc.unpack~ . The argument to mc.unpack~ determines the number of individual signal outlets.
If the multi-channel input to mc.unpack~ contains fewer channels than the number of outlets, the extra outlets will produce a zero signal. If the multichannel input contains more channels than the number of outlets, the additional input channels are ignored.
## Combining and Separating Multi-Channel Signals
If you have several multi-channel signals you would like to group into a single multichannel signal, use the mc.combine~ object. mc.combine~ produces an output multichannel signal containing the total number of input channels in the inputs. The argument to mc.combine~ specifies the number of inputs.
To separate a multichannel signal into two or more multichannel signals, use mc.separate~ . Arguments to mc.separate~ specify the channel counts in its output signals.
## Adding and Removing Channels
To make a multi-channel signal that copies a single-channel input, use mc.dup~ . The argument specifies the number of copies produced.
To force a multichannel output to have a set number of channels, use mc.separate~ with one argument specifying that number of channels. Additional channels are split off to the right outlet, but you don't need to connect that outlet to anything. If there are fewer channels in the input than you specify in the argument, the output will be padded with zero signals.
To mix all channels of a multichannel signal to fewer channels, use mc.mixdown~ . mc.stereo~ is a stereo-specific version of the mc.mixdown~ object. A single mixed channel can be obtained by using mc.op~ with the`@op`attribute set to`sum`.
## Transforming Signals
MC includes several objects that you can use to change how channels within multi-channel patch cords are organized, including mc.interleave~ , mc.deinterleave~ , and mc.transpose~ . Some applications of these objects are described in MC Channel Topology .
