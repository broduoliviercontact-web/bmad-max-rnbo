---
title: "Multichannel Delay Systems"
source: https://docs.cycling74.com/userguide/mc/mc_audio_delays/
source_path: /userguide/mc/mc_audio_delays/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Multichannel Delay Systems

Source: https://docs.cycling74.com/userguide/mc/mc_audio_delays/

## Extracted Text

# Multichannel Delay Systems
The mc.tapin~ and mc.tapout~ objects let you build networks of multichannel delay lines. The mc.tapin~ object auto-adapts to the number of channels in the multichannel patch cord connected to its input, creating individual delay memories for each input channel. Connected mc.tapout~ objects create one or more multichannel taps of this multichannel delay line.
## Multichannel Delay Time Control
Using multichannel signals fed to the input(s) of mc.tapout~ that represent delay times, you can control the individual delay times of each of the channels in each multichannel tap.
Here is an example where we use a four-channel delay line with two output taps. Each tap has a four-channel multichannel signal controlling its delay times. The result is eight outputs, each with its own unique delay time.
## Multichannel Feedback Control
You can feed the signals from mc.tapout~ back into the input of mc.tapin~ to create multichannel feedback delays. By multiplying the output gains with mc.multigain~ you can control the feedback levels of each channel individually.
Note that the multichannel inputs to mc.tapin~ are automatically added to the audio input coming from the mc.cycle~ .
