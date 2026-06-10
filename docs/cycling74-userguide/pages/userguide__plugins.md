---
title: "Plugins"
source: https://docs.cycling74.com/userguide/plugins/
source_path: /userguide/plugins/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Plugins

Source: https://docs.cycling74.com/userguide/plugins/

## Extracted Text

# Audio Plugins
Most DAWs (Digital Audio Workstations) support plug-ins, which let third parties extend the audio processing capabilities of the main software. Max supports Audio Unit, VST, and VST3 plug-ins, and can load Max for Live devices (AMXDs) as plug-ins as well.
The Max object wrapping VST and Audio Unit support is called vst~ or mc.vst~ , and the object wrapping Max for Live devices is called amxd~ or mc.amxd~ . The object plugin~ is for authoring Max for Live devices, and does not load plug-ins itself.
macOS includes an Audio Unit called AUHighShelfFilter, which Max can load as a plugin to implement that audio effect.
## Loading a Plugin
If you have a`.component`or`.vst`file, you should be able to drop that file onto an unlocked patcher to load the plug-in. This will automatically create a vst~ object that points to that file.
The left toolbar also provides access to the Plug-in Browser . Clicking on the Plug-ins icon will open the browser, letting you filter for plug-ins and AMXDs by name and kind.
Max builds the list of plug-ins by scanning for them at launch. In the Plug-ins section, you can use the Full Scan button to initiate a scan manually, which can be useful if you're adding new plug-ins with Max open.
## User Interface
When you drop a plug-in into your patcher, the vst~ or amxd~ object will enable the`@viewvisibility`attribute and show you a user interface for the plug-in. For an Audio Unit or VST plug-in, you'll see the generic interface. This lists all of the parameters in the plug-in, and lets you set their values.
The generic plug-in interface
With Max for Live devices, you'll see the customized user interface for that device.
The custom user interface for the 'Additive Heaven' Max for Live device
### Configuring parameter visibility
In the generic interface, click the pencil icon in the top toolbar to edit parameter visibility. Disable the Visibility checkbox to hide the parameter from view.
### Viewing the native editor
Most VST and Audio Unit plug-ins provide their own user interface. Click on the wrench icon in the top toolbar to open the native editor.
The native editor for the AUFilter Audio Unit
### Saving and restoring snapshots
You can save the current state of a plug-in as a Snapshot , which will include the current value of all of the plug-in parameters. Click on the camera icon in the top toolbar to save the current parameter set to a snapshot. Click on the snapshot selection button in the top-right to list all saved snapshots.
Viewing saved snapshots for the plug-in
The plug-in object UI does not provide any way to edit or delete snaphots. Select the vst~ object and open the Snapshot Sidebar to edit the names of snapshots, or to delete a snapshot.
With the vst~ object selected, open the snapshot sidebar to edit snapshots.
### Hiding the controls
The`@viewvisibility`attribute on a vst~ or amxd~ object determines whether or not the object will show an editable interface in the patcher. By disabling this attribute, you can get a much more compact representation of the wrapping object.
With @viewvisibility disabled, the object looks like a typical Max signal processing object.
