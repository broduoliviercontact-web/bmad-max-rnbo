---
title: "Gen Features for MC"
source: https://docs.cycling74.com/userguide/mc/mc_gen_newfeatures/
source_path: /userguide/mc/mc_gen_newfeatures/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Gen Features for MC

Source: https://docs.cycling74.com/userguide/mc/mc_gen_newfeatures/

## Extracted Text

# Gen Features for MC
New features have been added to Gen to support MC as well as to make integration of Gen easier with the remainder of your Max patching. The changes include:
## Create Simple Gen Patchers with`@expr`
You can use the`@expr`typed-in attribute with a gen , gen~ , mc.gen~ or mcs.gen~ object to specify a single line of Genexpr code.
## Control gen Execution with the`@hot`Attribute
By default, gen triggers processing only when receiving a value in its left inlet. The`@hot`attribute will set any other inlet to be "hot" and trigger processing.
