---
title: "Resolving Conflicts in Frozen Devices"
source: https://docs.cycling74.com/userguide/m4l/live_resolveconflicts/
source_path: /userguide/m4l/live_resolveconflicts/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Resolving Conflicts in Frozen Devices

Source: https://docs.cycling74.com/userguide/m4l/live_resolveconflicts/

## Extracted Text

# Resolving Conflicts in Frozen Devices
The process of freezing adds copies of files in the Max search path to the device file. Consider the example shown below. A Max device called MyEffect contains an abstraction called pumper .
If we freeze this device and save it, a copy of the pumper patcher file will be added to the device. If we now open pumper, modify it, and save the changes, the frozen device is unaffected. However, what happens if we decide we want to work on our MyEffect device some more? At this point, there are two different versions of Pumper, the one in the device, and the one saved on disk. Which one should we use?
## Overview of the Conflict Resolution and Unfreezing Process
Whenever you edit a frozen device, Max compares the files in the device with the versions on disk. If it spots differences, it disables the unfreeze icon and unlock icons in the patcher toolbar and enables the resolve conflicts icon, as shown below.
Before you can unfreeze a device with conflicts, you'll need to resolve them. Once you have decided which file(s) you wish to work with, both the version you want to keep and the version you want to discard will be written into a special folder located in your computer's Desktop folder called Unfrozen Max Device Files. However, only the version you wish to keep will be in the search path. The other version is put into a Discarded folder that is kept out of the search path.
## Resolving Conflicts for a Frozen Device
-
Click the Resolve Conflicts icon in the patcher toolbar. The Resolve Conflicts window will open.
-
Use the Action pop-up menu for each listed file with a conflict to choose which version you wish to use.
-
Once all conflicts have been resolved, the icon in the patcher window toolbar will turn gray, its caption will indicate No Conflicts, and the Unfreeze icon will become enabled.
-
Click the Unfreeze icon in the patcher window toolbar to unfreeze the device.
