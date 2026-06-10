---
title: "Polyphony with Multiple Patchers"
source: https://docs.cycling74.com/userguide/mc/mc_poly_multiple_patchers/
source_path: /userguide/mc/mc_poly_multiple_patchers/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Polyphony with Multiple Patchers

Source: https://docs.cycling74.com/userguide/mc/mc_poly_multiple_patchers/

## Extracted Text

# Polyphony with Multiple Patchers
Both the poly~ and mc.poly~ objects can contain different patchers for each voice. The names of the voice patches are set using the`@patchernames`attribute.
You can use mc.poly~ to load a bank of patchers to use as audio effects operating in parallel on each channel of a multichannel signal. If you want to mix the output of all the effects, you can do that later with mc.mixdown~ or mc.op~ .
