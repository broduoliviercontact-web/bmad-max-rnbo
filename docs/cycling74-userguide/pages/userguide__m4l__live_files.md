---
title: "Working With Files in Max for Live"
source: https://docs.cycling74.com/userguide/m4l/live_files/
source_path: /userguide/m4l/live_files/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Working With Files in Max for Live

Source: https://docs.cycling74.com/userguide/m4l/live_files/

## Extracted Text

# Working With Files in Max for Live
Historically, Max developers have used the search path for convenient access to files by name, but this is not sufficient for managing files in Live presets or documents.
The live.drop object was designed to be added to Max devices that work with files. When you drag an audio file from either the Live file browser or your operating system's file manager, live.drop will output the complete file path as a single symbol. You can then pass this symbol to a buffer~ or sfplay~ object, as shown in the example below.
The live.drop object also stores the name and location of the most recently dropped file in a way that Live understands. By default, live.drop has its Parameter Mode Enable set to true, so any files dropped onto it will be saved in the current Live document. When the document is re-opened, the name will be sent out live.drop 's outlet. When saving a preset for a device containing a live.drop , Live will copy any referenced audio files to the Live library if they are not already there. When a user opens the preset, the file's path in the Library, not the file's original path, will be sent out live.drop 's outlet.
If you perform a Collect All and Save on your Live Set, any audio files referenced by live.drop objects with Parameter Mode Enable set to true will be copied into a newly created folder. This permits Live users to move documents containing Max devices written with live.drop to different computers without losing the audio files the devices were using.
A Live user can, however, choose to turn off the program's default file-copying behavior.
## Setting Live's Preset and Export File Copying Behavior
-
Open the Live Preferences window.
-
Click the File Folder tab.
-
At the bottom of the File Folder preference pane, you will see an item called Collect Files on Export . Always is the default behavior. You can also choose Never , in which case files are never copied, or Ask , where you will be given the opportunity to decide whether files should be copied in each case that arises.
