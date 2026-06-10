---
title: "Ableton DSP"
source: https://docs.cycling74.com/userguide/abl/
source_path: /userguide/abl/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Ableton DSP

Source: https://docs.cycling74.com/userguide/abl/

## Extracted Text

# Ableton DSP
The Ableton DSP package is a collection of objects that bring Ableton Live devices and high-level DSP components into Max. From oscillators to modulators and filters to reverbs, these objects provide building blocks that speed up patch creation.
## abl.device vs. abl.dsp
The prefixes "abl.device" and "abl.dsp" are used to distinguish between objects that wrap entire Live devices and objects that wrap DSP components. For instance, abl.device.utility~ has the same functionality as the Live Utility device, whereas abl.dsp.ramp~ wraps one of the modulators in Live's Meld instrument and abl.dsp.shimmer~ wraps one of Live's Hybrid Reverb audio effects.
## Inlets and attributes
In most Ableton DSP objects, there are a select number of parameters that can be changed as either attributes or signals. For example, the`@ratio`attribute of abl.dsp.harmonicfm~ can be controlled via the third inlet. When a signal is connected to the inlet, the attribute will become disabled while the signal takes over control. If the signal is disconnected, the attribute will re-enable.
## Internal smoothing
Unlike most Max objects, Ableton DSP objects offer internal parameter smoothing. Whenever a float-type attribute is changed at event-rate (from an attrui or float inlet, for example), a short ramp is applied instead of immediately stepping to the new value. This mitigates "zipper noise" as attributes are changed at event-rate. However, if you control a parameter at signal rate by attaching a signal to an inlet, no extra smoothing is applied.
