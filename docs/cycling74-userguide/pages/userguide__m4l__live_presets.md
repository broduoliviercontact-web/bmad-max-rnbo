---
title: "Presets"
source: https://docs.cycling74.com/userguide/m4l/live_presets/
source_path: /userguide/m4l/live_presets/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Presets

Source: https://docs.cycling74.com/userguide/m4l/live_presets/

## Extracted Text

# Presets
Presets are a feature of Live that permit you to store the current state of a device. Since it is Live, not Max, that does the saving, the state must be known to Live, which means a preset captures the state of all the parameters you have defined. This means that the value of a number box not connected to a parameter will not be saved -- Live presets are different from the Max preset object in this way.
## Storing a Preset
- Click the Save Preset icon in the title bar of the Max device. (The Save Preset icon is the one at the far right that resembles a floppy disk , for those of you who know what a floppy disk looks like.)
- In the File Browser, a new preset will be created and its name will be selected, ready for you to edit. Type in a name for the preset.
## Presets for a Devices in the Library
When you store a preset for a Max device in the Library, it appears beneath the device hierarchically. In the example shown below, NicePreset is a preset that has been saved for the Max device MyEffect .
## Presets for a Devices Outside the Library
When you store a preset for a Max device that is not located in the Library, the preset will have a special preset-plus-device icon and also show the device name in square brackets before the preset name. In the example below, we stored a preset called GiantPreset for an effect originally outside the Library called MyGiantEffect .
## Saving a Max Device in the Library
If you want to save a device into the Live library, it's better to use the Save As... command within Max instead of moving the device file using your operating system. Using Save As... permits Live to keep track of your device and manage its presets.
-
Insert the device you want to move. Click the edit button to launch Max to edit the device.
-
In Max, choose Save As... from the File menu. Navigate the standard save file dialog to show the current Live Library folder. Save the device inside the Presets folder inside the Library folder, or a subfolder of the Presets folder.
-
Return to Live and you will see the newly saved device. In the example below, we saved our device as MyEffect .
