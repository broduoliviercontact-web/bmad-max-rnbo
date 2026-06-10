---
title: "MC Wrapper"
source: https://docs.cycling74.com/userguide/mc/mc_wrapper/
source_path: /userguide/mc/mc_wrapper/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Wrapper

Source: https://docs.cycling74.com/userguide/mc/mc_wrapper/

## Extracted Text

# MC Wrapper
When you type mc.cycle~ into an object box, one or more traditional cycle~ objects are embedded inside the MC Wrapper .
The wrapper holds multiple instances of audio objects such as cycle~ . It permits you to control all of the objects at once with one message or target individual objects. It also manages multi-channel connections to other MC objects. For the most part, this is done transparently and you don't have to think about the wrapper too much. But wrapped objects share some useful messages and attributes not availble in the "unwrapped" versions.
A general rule of thumb is that if there is an MSP object xxx~, mc.xxx~ will be xxx~ in the MC Wrapper. But this is not always the case. Exceptions include:
-
Objects that perform I/O: mc.adc~ , mc.dac~ , mc.ezadc~ , mc.plugin~ , mc.plugout~ , mc.ezdac~ , mc.sfplay~ , and mc.sfrecord~ . In these cases, you don't need multiple copies of objects, you just need multi-channel inputs and outputs to the outside world
-
UI objects including gain sliders ( mc.live.gain~ , mc.gain~ , mc.multigain~ ) and signal visualization objects including scope~ , meter~ , levelmeter~ and spectroscope~ . The mc. is optional and does nothing for these objects, as they auto-adapt to the number of channels of a multichannel input signal.
-
mc.tapin~ , mc.tapout~ , mc.send~ , mc.receive~ : these can be thought of as I/O objects to internal memory buffers
-
Any objects begining with mcs which are single instances of audio objects whose inputs and/or outputs are combined into a single multi-channel inlet and/or outlet
-
MC objects specific to multi-channel signal manipulation
