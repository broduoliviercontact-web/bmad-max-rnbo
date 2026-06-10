---
title: "Polyphony Using mc.poly~"
source: https://docs.cycling74.com/userguide/mc/mc_poly_newfeatures/
source_path: /userguide/mc/mc_poly_newfeatures/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Polyphony Using mc.poly~

Source: https://docs.cycling74.com/userguide/mc/mc_poly_newfeatures/

## Extracted Text

# Polyphony Using mc.poly~
The poly~ object manages polyphony for multiple instances of a patcher. The poly~ object always copies audio inputs to each patcher instance, and mixes the output of each patcher instance together at the object's outlets.
The mc.poly~ object uses multichannel signals to operate in a more flexible way. A multichannel input to mc.poly~ assigns the audio for each channel to its corresponding patcher instance ( poly~ voice). The first audio input channel in the signal is passed to an in~ object within the first patcher instance, the second audio input channel in the signal is passed to an in~ object in the second patcher instance, and so on.
Similarly, the output fed to out~ objects in a patcher inside mc.poly~ is not mixed with the other patchers, it comes directly out to the corresponding channel of a multichannel signal.
Here is a patcher that simply passes audio input arriving at an in~ directly an out~ :
Here is a comparison of poly~ and mc.poly~ using simple numbers as input to four instances of this patcher loaded in each object. For the poly~ case, we feed a single-channel signal of 1 to the object and it produces a single-channel output:
Note that the output is 4, representing the sum of all the patchers mixing their inputs together.
For the mc.poly~ case, we will feed in a four-channel multichannel signal consisting of 1 in the first channel and 0 in the other three channels.
In this case, the output multichannel signal is equal to the input multichannel signal.
One use of mc.poly~ would be to load a simple patcher to use as an audio effect operating in parallel on each channel of a multichannel signal. If you want to mix the output of all the effects, you can do that later with mc.mixdown~ or mc.op~ .
