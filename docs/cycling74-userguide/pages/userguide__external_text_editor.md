---
title: "External Text Editor"
source: https://docs.cycling74.com/userguide/external_text_editor/
source_path: /userguide/external_text_editor/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# External Text Editor

Source: https://docs.cycling74.com/userguide/external_text_editor/

## Extracted Text

# External Text Editor
Objects like coll , js , jsui , and node.script have an internal state that references a body of text. For editing the state of these objects, Max has a built-in text editor. However, you can also use an external text editor if you prefer.
## Editing an Object's Text
For any objects that have some internal text, you can open the text editor for that object by double-clicking on the object. There's also a menu command to open the text editor. For example, with a coll object selected, choose Edit coll Object's Contents from the File menu to open the text editor. By default, this will use Max's internal text editor.
## Using an External Editor
To use an external editor, open Max's preferences and enable Always use External Text Editor .
With this option enabled, Max will use whatever text editor application is the system default when opening a given file. If you set a value for "External Text Editor", them Max will always use that application when opening a text file.
## Required File on Disk
If you've enabled Always use External Text Editor , you may see a dialog appear when you try to open up a text-based object for editing.
When using Max's internal text editor, Max can display the contents of an object as text without creating an actual file on disk. However, when using an external text editor, Max must save an actual file before it can open the object contents with an external editor. Choose "Yes" to save a file on disk. After creating the file, Max will open the file in your chosen external text editor.
