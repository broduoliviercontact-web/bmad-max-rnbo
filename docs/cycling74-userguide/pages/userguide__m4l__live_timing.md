---
title: "Timing"
source: https://docs.cycling74.com/userguide/m4l/live_timing/
source_path: /userguide/m4l/live_timing/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Timing

Source: https://docs.cycling74.com/userguide/m4l/live_timing/

## Extracted Text

# Timing and Synchronization in Max for Live
The Live transport is a clock source for the Max tempo-based time system .
## Implementation Notes
-
By default, all transport objects in Live devices (those without names) synchronize to the Live transport.
-
Named transport objects do not synchronize to Live unless you set the`clocksource`attribute to the name`live`.
-
If two device instances contain transport objects that share the same name, they will run independently.
-
The tempo-based timing system synchronizes to Live even in preview mode . However, there may be disruptions in the continuity of timing when switching into or out of preview mode.
