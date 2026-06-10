---
title: "Prototypes"
source: https://docs.cycling74.com/userguide/prototypes/
source_path: /userguide/prototypes/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Prototypes

Source: https://docs.cycling74.com/userguide/prototypes/

## Extracted Text

# Prototypes
Prototypes are configurations of object attributes that can be saved and recalled later. For example, you might have an object like a slider that you've set up to have a certain size and to look a certain way. You could define a prototype from that slider, and then apply that prototype to make other sliders look the same way.
Prototypes are mostly used with UI objects, but you can use them for generic Max objects as well. For example, you might have a Jitter object with a complex state that you find yourself reusing often.
## Defining a Prototype
With an object selected, open the Object menu and select`Save Prototype...`to define a new prototype. A dialog box will appear, allowing you to give the prototype a name.
Defining a new prototype
## Applying a Prototype
Select the object to which you'd like to apply your prototype. Open the Object menu and choose`Prototype > <name>`, where`<name>`is the name of your saved prototype. The object should change its text and/or appearance to match your saved prototype.
## Deleting a Prototype
Max prototypes are stored in files with the`.maxproto`extension. You can find these files the`Prototypes`folder in the Max 9 Folder , which on macOS is in`~/Documents/Max 9`and on Windows is in`%USERPROFILE%\Documents\Max 9`. If you delete a`.maxproto`file from the`Prototypes`folder, it will no longer appear in the list of prototypes for the specified object.
## Prototypes in Packages
To include a prototype as part of a Package , create a folder in your package directory named`prototypes`, and put any`.maxproto`files that you want to include into that directory. When a user installs your package, those prototypes will be available to them as well. This can be useful if your package has a consistent look and feel that you want to enable other users to reproduce.
