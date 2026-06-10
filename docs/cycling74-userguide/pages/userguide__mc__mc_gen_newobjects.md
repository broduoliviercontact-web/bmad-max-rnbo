---
title: "MC Gen Operators"
source: https://docs.cycling74.com/userguide/mc/mc_gen_newobjects/
source_path: /userguide/mc/mc_gen_newobjects/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Gen Operators

Source: https://docs.cycling74.com/userguide/mc/mc_gen_newobjects/

## Extracted Text

# MC Gen Operators
Two Gen operators are useful with mc.gen~ and mc.gen :
-
mc_channel reports the current channel of the Gen patcher within mc.gen~ or mc.gen (starting at 1).
-
mc_channelcount reports the total number of channels (Gen instances) within mc.gen~ or mc.gen .
These Gen operators make it possible to do voice-specific calculations. You can also connect them to the Gen out operator to provide voice-specific identification signals or events outside the Gen context.
When used in a patcher inside gen~ , mcs.gen~ , or gen (in other words, outside the context of the MC Wrapper), both operators output 1.
