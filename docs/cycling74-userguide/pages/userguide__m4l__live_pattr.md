---
title: "Using pattr in Live Devices"
source: https://docs.cycling74.com/userguide/m4l/live_pattr/
source_path: /userguide/m4l/live_pattr/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Using pattr in Live Devices

Source: https://docs.cycling74.com/userguide/m4l/live_pattr/

## Extracted Text

# Using pattr in Live Devices
Live-specific user interface objects such as live.dial save their state within Live documents and presets. If you want to use standard Max objects and have them interact with Live, you will have to enable the Parameter Mode Enable attribute in the pattr object. This ensures that the data internal to pattr is also stored (and recalled) using Live's document.
## Enabling Parameter Mode
- Select a pattr object and click the Inspector button in the Patcher toolbar to show the object's
- Click the Parameter tab at the top of the inspector window to show the Parameter attributes.
- Check the Parameter Mode Enable checkbox.
## autopattr Considerations
The autopattr object provides an easy to way manage the state of standard Max objects, but it will not work with the parameter system, so objects that are attached to an autopattr will not be seen by Live. If you want a pattr parameter to appear for modulation etc, you will need to add a pattr object for each instance.
## Differences Between Max and Max for Live
Although the pattr objects can be used in the context of Max for Live, there are some differences when compared to Max. You can read more about various limitations here . To better understand pattr we encourage you to visit the pattr guide .
