---
title: "MC and Max for Live"
source: https://docs.cycling74.com/userguide/mc/mc_maxforlive_interface/
source_path: /userguide/mc/mc_maxforlive_interface/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC and Max for Live

Source: https://docs.cycling74.com/userguide/mc/mc_maxforlive_interface/

## Extracted Text

# MC and Max for Live
Max for Live devices receive audio input via plugin~ and send audio to Live via plugout~ . The mc.plugin~ and mc.plugout~ versions of these objects accept multi-channel inputs and outputs to be routed to and from Max for Live.
Devices created with multi-channel inputs and outputs will support multichannel routing within Live, as well as having the appropriate number of inlets and outlets when loaded into Max within the amxd~ object. The current maximum channel count is 64.
