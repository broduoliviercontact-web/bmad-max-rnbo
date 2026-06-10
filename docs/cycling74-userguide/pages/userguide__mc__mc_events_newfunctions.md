---
title: "Processing Events from MC Objects"
source: https://docs.cycling74.com/userguide/mc/mc_events_newfunctions/
source_path: /userguide/mc/mc_events_newfunctions/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Processing Events from MC Objects

Source: https://docs.cycling74.com/userguide/mc/mc_events_newfunctions/

## Extracted Text

# Processing Events from MC Objects
## Events and MC Values
It is often useful to obtain values from an audio signal and use them in event-level processing. With standard MSP signals, you can use the snapshot~ object to get an instantaneous value from an audio signal at a regular interval.
In the case of multi-channel signals, things are more complex: at each measurement, you would get a list with a value for each input channel. Instead of producing a list, the mc.snapshot~ object has an additional outlet that provides a voice number .
At each sampling interval, mc.snapshot~ outputs each of the values from each of the incoming samples, but outputs the voice number before the signal value. This combination of values can be used with a routing object (like mc.route ) to send each value to a unique location. Alternatively, if you do want a list of all the snapshot values, mc.makelist can do that for you.
## Voice outputs from poly~ and mc.poly~
Similar to the mc.snapshot~ object, both poly~ and mc.poly~ may have an additional voice output. This is only created when contained in a poly~ contains an event (non-signal) outlet.
You can use the voice output, along with a routing object such as mc.route to use the event output to control other parts of your patch.
## See Also
MC Event-Based Objects
