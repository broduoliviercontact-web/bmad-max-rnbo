---
title: "Snapshots"
source: https://docs.cycling74.com/userguide/snapshots/
source_path: /userguide/snapshots/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Snapshots

Source: https://docs.cycling74.com/userguide/snapshots/

## Extracted Text

# Snapshots
Snapshots let you save the state of parameters in your patcher. They are similar to the pattr system , but with some key differences:
- Snapshots can be embedded with a patcher, and do not need to be saved as a separate JSON file.
- There is no built-in mechanism to interpolate between snapshots.
- Snapshots are global, containing all of the parameters in a given patcher, plugin, or device.
- You can give snapshot slots a name
In general, snapshots give you less granular control than working with pattr, but require less configuration to work. Snapshots were designed with a few particular use cases in mind:
- Saving and restoring the state of all parameter-enabled objects in a patch
- Saving and restoring the state of a VST or Audio Unit plugin , or a Max for Live Device
- Saving and restoring the state of a rnbo~ object.
Snapshots use the Parameter system to determine what to save; you will need to set the Parameter mode enable for each UI object whose state you wish to save.
## Patcher Snapshots
A patcher snaphot contains the state of all parameters in a patcher hierarchy. Since snapshots work with the parameter system , an object must have parameter mode enabled in order to be saved in a snapshot.
If you're unable to create new patcher snapshots, it might be because there are no parameter-enabled objects. Snapshots will only be enabled if there is at least one parameter-enabled object in your patcher. You can enable parameter mode on most UI objects from the inspector .
Here at the top of the Snapshots sidebar view, you can see the text "patcher snapshots", indicating that these are snapshots that belong to the patcher itself. With nothing selected, the Snapshots sidebar view will display patcher snapshots. If you select a vst~ , rnbo~ , or amxd~ object, you'll see that the sidebar view updates to display snapshots for that object.
Patcher snapshots are saved and recalled at the top-level of a patcher hierarchy, but will save subpatcher parameters.
Subpatches can't have snapshots separate from the root patcher. If you need this kind of behavior, you can create a Max for Live device and host it in a patcher with the amxd~ object.
## Effects Snapshots
Effects snapshots store the parameter states of plugins, Max for Live devices, or RNBO devices hosted by vst~ , amxd~ , or rnbo~ objects.
When you select one of these objects in your patcher window, the snapshots pane will display any snapshots associated with they selected device.
Unlike patcher snaphsots, which are always saved with the patcher, effects snapshots are not embedded by default. Instead, they are saved in the Max 9 Folder in a folder called Snapshots . This means that when you create a snapshot for a VST, Audio Unit, or Max for Live Device, it's available throughout Max, no matter where it was created. See embedding snapshots for more.
If you want to share a snapshot that you created, you can share the associated snapshot file located in the Max 9 Folder . You can also use Max projects to automatically collect snapshot dependencies, which may make sharing snapshots easier.
The header/title bar for vst~ and amxd~ objects lets you create and recall new snapshots when the patcher window is locked. The camera icon creates snapshots, and the circular icon to the right will recall snapshots.
## Managing Snapshots
To view, create, load, rename, and delete snapshots, open the Snapshots sidebar view by clicking the Show Snapshots icon in the right toolbar.
All of the following snapshot options are also available by right-clicking on any snapshot.
### Creating Snapshots
To create a new snapshot, click on the Add a new Snapshot button in the bottom of the Snapshots sidebar view.
### Recalling Snapshots
Recall a snapshot by either clicking on the triangle next to a snapshot, or by clicking on the Restore Snapshot icon in the bottom toolbar.
### Renaming Snapshots
Rename a snapshot either by double-clicking on the name of a snapshot, or by clicking on the Rename Snapshot icon in the bottom toolbar.
### Modifying Snapshots
You can modify a snapshot by clicking the Take Snapshot button in the bottom toolbar. This will overwrite the currently selected snapshot with the current parameter values of the selected patcher or, device, or plugin.
### Deleting Snapshots
Delete a snapshot by clicking the Delete the selected Snapshot icon in the bottom toolbar.
## Embedding Snapshots
Patcher snapshots are always embedded with the patcher, but snapshots for plugins, amxds, and RNBO devices are not. Click on the circle icon next to any snapshot to embed it with the current patcher.
Whether they are embedded or not, snapshots are always saved in the Snapshots folder in the Max 9 Folder . These snapshot files are named according to the name of the current patcher, so it's good practice to name your patcher file prior to creating snapshots.
### Usage with Projects
When you use a vst~ , amxd~ , or rnbo~ object as part of a Max Project , any snapshots of that object become dependencies of the project. When you consolidate your project, those snapshots will be copied to the project directory. This lets you share your project with others, including any snapshots that the project might depend on.
## Usage with pattr
Snapshots can be easily integrated into your pattr workflow. Using a pattrstorage object along with pattr objects or an autopattr object, the internal state of your VST, AU or AMXD can be recalled.
See the pattr and autopattr help files for example usage (under the "snapshots" tab).
## Snapshot-enabled Messages
All snapshot-enabled objects ( amxd~ , vst~ , rnbo~ , and thispatcher ) understand the messages:
- `snapshot`[userpath (optional)] [index (optional)] [name (optional)]
- `restore`[index (optional)]
- `addsnapshot`[userpath (optional)] [index (optional)] [name - (optional)]
- `deletesnapshot`[index]
- `setsnapshotname`[index] [name]
- `deletesnapshot`[index]
- `setembedsnapshot`[index] [embedstate]
- `movesnapshot`[srcindex] [dstindex]
- `exportsnapshot`[srcindex] [userpath]
- `importsnapshot`[dstindex] [userpath]
## JavaScript Snapshot API
For advanced users and those creating standalone patchers, Snapshots can be accessed via the Snapshots API. See the JavaScript Snapshot API for more information.
