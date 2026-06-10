---
title: "MC Visualization and Probing"
source: https://docs.cycling74.com/userguide/mc/mc_visualization/
source_path: /userguide/mc/mc_visualization/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Visualization and Probing

Source: https://docs.cycling74.com/userguide/mc/mc_visualization/

## Extracted Text

# MC Visualization and Probing
Multichannel signals can be visualized using the following objects:
-
meter~ - standard LED-like metering
-
levelmeter~ - VU metering
-
number~ - displays the numerical value a signal
-
scope~ - oscilliscope-like signal display
-
spectroscope~ - displays the spectral content of a signal
## Selecting a Display Channel
The number~ , levelmeter~ , scope~ and spectroscope~ objects will adapt to show all multichannel signals, but will only display or foreground one channel at a time. Use the channel display selector to bring one of the channels into focus.
- Click on one of the channel display selector indicators to switch to the chosen channel.
The scope~ and levelmeter~ objects have an inactivealpha attribute that controls the relative brightness of unselected channels.
## Signal Probing
The Signal Probe works with MC signals.
-
Enable Signal Probe in the Debug menu
-
Move the cursor over a multi-channel patch cord to view the signals it contains:
- Press the down-arrow key to switch to one of the alternative displays:
