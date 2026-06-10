---
title: "MC Mixing and Panning"
source: https://docs.cycling74.com/userguide/mc/mc_mixing_panning/
source_path: /userguide/mc/mc_mixing_panning/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Mixing and Panning

Source: https://docs.cycling74.com/userguide/mc/mc_mixing_panning/

## Extracted Text

# MC Mixing and Panning
## Mixing Multichannel Signals
The primary tool for mixing multichannel audio signals is the mc.mixdown~ object. This object mixes inputs in a multi-channel signal connected to its left inlet to an output multi=channel signal, optionally panning the inputs across the space of the outputs.
### Static Pan Positions
There are two ways to specify a series of unchanging pan positions for inputs to mc.mixdown~ . The most efficient way is by supplying a list of pan values to the`@pans`attribute, which can be a typed-in argument. Alternatively, you can use mc.list] or {mc.range to generate a multi-channel signal containing the pan values, then connect that multi-channel signal to the right inlet of mc.mixdown~ .
### Dynamic Panning
For dynamic panning, you can use any multi-channel signal for the pan input of the mc.mixdown~ object. For example, we can use an mc.sig~ object with the`deviate`message to create a set of random values for channel panning.
Using oscillators for the panning position allows you to create evolving results with only a few objects.
## Panning Modes
There are four panning modes available when using the mc.mixdown~ object: Mode 0 (Circular Panning), Mode 1 (Line Panning, ranged 0-1), Mode 2 (Line Panning, ranged 1-N) and Mode 3 (Circular Panning, ranged 0-N). Each uses a different method of determining where the outputs are located in relation to the number range available for panning.
### Mode 0: Normalized Circular Panning (0-1)
The pan position is a value between 0.0 and 1.0, and represents an even-power pan within a circular configuration of channels spread evenly across that range. For example, a two channel configuration has the two outputs at pan position 0.25 and 0.75.
Why not 0.0 and 1.0? Because 0.5 should represent a value evenly placed between the two channels, and 0.0 should also be halfway between the two channels - as if they were in a circle.
As you can see from the following diagram, if there are three outputs, they will be located at .167, .5 and .833.
0.5 0.75 0.875 0.0 0.25 0.375 0.625 A B C 0.125
Likewise, if there are four outputs, they will be located at 0.125, 0.375, 0.625 and 0.875.
0.5 0.75 0.875 0.0 0.25 0.375 0.625 A B D C 0.125
To determine the pan position of any single channel in a mc.mixdown~ scenario, divide 1.0 by the number of channels times 2, then use the odd-numbered values produced. For example, if you have 5 output channels, the pan positions for the outputs will be:
Calculate 1.0 / (5 channels * 2) = 0.1
The five output channels are 0.1, 0.3, 0.5, 0.7 and 0.9
### Mode 1: Normalized Line Panning (0-1)
In this mode, the pan position is a value between 0.0 and 1.0, and represents an even-power pan across a linear configuration of channels spread evenly across that range, but with the first and last locations at positions 0.0 and 1.0.
This mode can be somewhat more easily understood, but the values are also clamped to the range of 0.0 to 1.0. If we have three outputs, their locations are at 0.0, 0.5 and 1.0:
0.5 0.75 0.875 0.0 1.0 0.25 0.375 0.625 0.125 A B C
A four-output configuration would have the output locations at 0.0, 0.33, 0.66 and 1.0:
0.5 0.75 0.875 0.0 1.0 0.25 0.375 0.625 0.125 A B C D
### Mode 2: Channel-Based Line Panning (1-N)
Panning mode 2 is similar to mode 1, in that the values are placed on across a linear path with the values at the extreme ends. However, in this mode, each output is placed at its integer value, with the lowest output at 1.0, and the highest output located at its value. For example, a three-output configuration would have outputs at 1.0, 2.0 and 3.0:
2.0 2.5 2.75 1.0 3.0 1.5 1.75 2.25 1.25 A B C
And a four-output object would have output locations at 1.0, 2.0, 3.0 and 4.0:
3.0 4.0 1.0 2.0 2.5 3.5 1.5 A B C D
Like mode 1, the values are clamped at the top and the bottom of the range, so values under 1.0, or over the integer value of the highest output, will not produce expected results.
### Mode 3: Channel-Based Circular Panning (0-N)
Mode 3 is similar to mode 0, in that the panning exists in a circular layout. But like mode 2, the outputs are located at their integer value locations. A four-channel configuration would have the outputs as follows:
2.0 3.0 3.5 0.0 4.0 1.0 1.5 2.5 A B D C 0.5
Note that location 0.0 is the same as the location of the last output, and the first output occupies location 1.0. This allows you to 'rotate' a sound around the outputs, but makes direct access to each output easier to manage.
## Auto-Adding Multichannel Signals
As with standard signal patchcords, combining two multichannel patchcords at an object inlet will mix the contents of prior to processing. When the two patchcords contain the same number of channels, the channels will be mixed together individually.
If one multichannel patchcord contains more channels than the other, the result will be the largest channel count of either of the patchcords.
In many cases, you can also mix multichannel and standard audio signals, with the standard signal treated as the equivalent of a 1-channel MC signal.
## User Interface Objects for Multichannel Mixing
To set all levels of a multichannel signal, use the mc.gain~ object. By default, mc.gain~ auto-adapts to the number of channels in its input and produces the same number of channels, with the incoming signals scaled by the value of the gain slider.
To set levels of a multichannel signal individually, use the mc.live.gain~ or mc.multigain~ objects. mc.live.gain~ is a version of live.gain~ with a single multi-channel input and a single multi-channel output. Like mc.gain~ it auto-adapts to its input channel count by default. If the`@channels`attribute mc.live.gain~ is set to a non-zero value it outputs a fixed number of channels regardless of the input channel count.
The mc.multigain~ object is a version of mc.gain~ offering individual sliders for each input channel.
The mc.multigain~ object provides a way to set all sliders with modifier key gestures.
-
To set a slider individually, click in the slider and drag to increase or decrease the level. You will not be able to change a different slider until you end the drag.
-
To draw across all sliders setting them to the position of the cursor, hold down the option while dragging.
-
To change the level of all sliders proportionally, hold down the shift key while dragging one slider.
