---
title: "Using mc.gen with the MC Wrapper"
source: https://docs.cycling74.com/userguide/mc/mc_gen_event_wrapper/
source_path: /userguide/mc/mc_gen_event_wrapper/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Using mc.gen with the MC Wrapper

Source: https://docs.cycling74.com/userguide/mc/mc_gen_event_wrapper/

## Extracted Text

# Using mc.gen with the MC Wrapper
The MC Wrapper contains a set of messages that offer high-level algorithmic control over a set of individual objects. For example, using the`deviate`message with changing values for ranges you can generate and apply a set of random values for signal object parameters such as oscillator frequency.
For more possibilities than those offered by the basic wrapper messages, the mc.gen~ object offers a way to create algorithms for controlling objects in the wrapper. As an example, we will show an example using the`@expr`mode of Gen to create a simple range.
(Note: This feature is already available as the`spread`message to the wrapper but it illustrates a basic pattern you can customize.)
## mc.gen Connections
The mc.gen object is not an audio object; it accepts and produces only Max messages. However, mc.gen uses the MC Wrapper; it contains multiple gen objects. Specify the number inputs using the @chans attribute.
Since mc.gen uses the MC Wrapper, you can connect an audio signal to one of its inputs and it will auto-adapt its channel count. (We will use this trick in our complete example below.)
The mc.gen object contains an extra rightmost outlet that outputs a voice number immediately before any values come out its other outlets. This permits identification of the gen instance that is sending output. The mc.target , mc.route , and mc.makelist objects make it simple to use voice outlet for further isolation of mc.gen output.
## Using MC Operators
To generate a range of control values, one for each wrapper instance, we will need to use the MC-specific mc_channel and mc_channelcount operators in our Gen expression. A formula for generating the range is:
`out_channel = min + (max - min) * (channel / number_of_channels)`
This will scale a range evenly over a space defined by min and max. We will use`in1`as our range minimum and`in2`as our range maximum. As a Gen expression, this would be:
`out1 = in1 + (in2 - in1) \* (mc_channel / mc_channelcount)`
## Target Connections
Now we want to use the rightmost voice outlet of mc.gen in conjunction with mc.target to control an object in the MC Wrapper. In this example, we will control the frequencies of a bank of sawtooth oscillators in mc.saw~ .
By connecting the rightmost outlet of mc.gen to mc.target , the per-voice range value is properly routed to the correct saw~ instance inside mc.saw~ .
