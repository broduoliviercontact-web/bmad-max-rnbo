---
title: "Using Plug-ins with MC"
source: https://docs.cycling74.com/userguide/mc/mc_plugins/
source_path: /userguide/mc/mc_plugins/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Using Plug-ins with MC

Source: https://docs.cycling74.com/userguide/mc/mc_plugins/

## Extracted Text

# Using Plug-ins with MC
In MC, you can work with multiple copies of a plug-in to produce multiple channels of audio, or use multi-channel inputs and output with a single copy of the plug-in.
## Single Plug-in, Multi-Channel Signals
The mcs.vst~ object allows you to work with a single instance of a plug-in, but have multi-channel inputs and outputs. In the most basic case, you can create an mcs.vst~ with a favorite stereo VST effect, and have a 2-channel MC signal routed into and out of the effect.
If the plug-in is capable of more than two input or output channels, you can define the input and output channel counts with the first two arguments to mcs.vst~ .
## Multiple Copies of a Plug-in
The mc.vst~ object works like other MC Wrapper objects: it contains multiple instances of a plug-in within a single Max object. The number of instances will auto-adapt to the number of inputs.
The number of inputs and outputs to the plug-in are defined by the channel argument(s) to mc.vst~ , and each of the inlets and outlets will be a multichannel signal.
For example, a mc.vst~ defined to have two I/O channels and four instances will produce two four-channel signals containing the "left" and "right" inputs to the four plug-in instances.
When using a VST instrument plug-in, you will need to define the number of MC output channels to be used, preferably as a typed-in`@chans`argument, since you won't be sending the plug-in any audio inputs.
## Accessing Parameters of Individual Plug-in Instances
When using mc.vst~ to host multiple copies of the same plug-in, you may want to change the parameters of each copy to different settings. This can be done using the`mcisolate`attribute of the mc.vst~ object, as well as the mc.target and mc.targetlist objects to route messages to a single instance of the plug-in.
To alter individual instances of a plug-in's parameters:
-
Enable the`mcisolate`attribute of mc.vst~ using a typed-in argument, message box, or attrui .
-
Using mc.target or mc.targetlist , send a`setvalue`message followed by the instance number and desired parameter name to mc.vst~ . This will change the parameter for the targeted instance only.
-
To target all instances of the mc.vst~ object, you can target using voice number 0 (zero), or disable the`mcisolate`attribute to distribute the change to all instances of the plug-in.
When`mcisolate`is off, any parameter change for any voice - or any change to the user interface of the plug-in - will result in that parameter being changed in all of the instances of the plug-in.
## Working with Max for Live Devices
Max for Live devices are hosted similarly to VST plug-ins, using the mcs.amxd~ object for a single instance, and mc.amxd~ for multiple-instance applications.
If you are showing the device's interface in your patcher (by toggling on the Show View In Patcher attribute), you can choose the instance of the device that is displayed by using the`displaychan`attribute.
