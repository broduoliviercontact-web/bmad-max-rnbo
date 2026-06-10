---
title: "MC Gen Instances"
source: https://docs.cycling74.com/userguide/mc/mc_gen_instances/
source_path: /userguide/mc/mc_gen_instances/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Gen Instances

Source: https://docs.cycling74.com/userguide/mc/mc_gen_instances/

## Extracted Text

# MC Gen Instances
When you create an mc.gen~ object, you are creating a hosting environment for multiple instances of a Gen DSP patch. There are several ways to manage the contents of the object, based on how the Gen DSP is loaded.
If you create an mc.gen~ object without a patcher name argument, you are working with the default, unnamed Gen DSP patch maintained by Gen. This patch is duplicated across all instances, and any changes to this patch will be propagated across all voices.
## Using One Gen DSP File
When you load a single Gen DSP file into an mc.gen~ object, it is copied to all voices. If the patch is changed, the changes are immediately propogated to all voices as you edit.
## Using Multiple Gen DSP Files
You can load each gen~ instance inside mc.gen~ with a different Gen DSP file. This is done using the`@values`wrapper message as a typed-in attribute. If fewer files are provided than channels are defined, the remaining channels will use the default Gen DSP patch.
In this case, if you make a change to one of the patches, it will not propogate any changes to the other voices - each of the Gen DSP files is isolated from the others.
