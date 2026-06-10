---
title: "Bpatchers"
source: https://docs.cycling74.com/userguide/bpatchers/
source_path: /userguide/bpatchers/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Bpatchers

Source: https://docs.cycling74.com/userguide/bpatchers/

## Extracted Text

# Using bpatchers
A bpatcher embeds the interface of a patcher inside a box in its parent patcher.
The audio processing patcher in the center of this patcher is inside a bpatcher.
## Creating a bpatcher
You can create a bpatcher either by creating one from scratch, or by transforming an abstraction or subpatcher into a bpatcher.
### Starting with an Empty bpatcher
Create a new object (by pressing the n key for example), then type the name`bpatcher`. A bpatcher will replace the object box when you click outside the box.
An empty bpatcher, immediately after creation
An empty bpatcher won't do anything. Setting the bpatcher's`@name`or "Patcher File" attribute will assign a patcher file within the search path to load. After a file is loaded, enable the`@embed`( Embed Patcher in Parent ) attribute to save the contents of the file in the parent patcher.
You can also assign a file to a bpatcher by dragging a patcher file onto the object from the File Browser or one of the left sidebar browsers.
### Starting with a Patcher File
-
To turn a named patcher file into a bpatcher, start by pressing the e key. After the object box appears, type the file's name into the box, then click outside of the box. A bpatcher containing the file will replace the object box. For more details, see Patcher Appearance in bpatchers below.
-
If you hold down the Option key while dragging a patcher file into a empty space in a patcher window, you'll see a contextual menu with several options. The Create a bpatcher option will let you create a bpatcher directly with the contents of the .maxpat file.
-
Finally, you can drag any patcher file onto a bpatcher to replace the file the bpatcher currently uses.
### Converting a Subpatcher or Abstraction
Given any subpatcher or abstraction, you can also open the Action Menu and select Transform > Patcher to Bpatcher to convert to a bpatcher. You can also transform a bpatcher to a subpatcher or abstraction with the same menu.
## Opening the Contained Patcher
Choose Open from the bpatcher's Action Menu to view and edit the bpatcher's contained patcher in a separate window.
### Editing an embedded patcher
If you open an embedded bpatcher from a bpatcher object in the parent patcher, it may open in read-only mode. In this mode, you must click the Modify read-only icon to unlock it for editing. See Modify read-only for more information.
## Presentation View
By default, a bpatcher will display its patcher's patching view. If you want to display the Presentation View instead, enable the`@openinpresentation`( Open in Presentation ) attribute in the patcher file the bpatcher contains ( not the bpatcher itself) using the Patcher Inspector .
## Changing the Patcher's Offset
Often you'll want to set up a bpatcher to have a dynamic display, changing its presentation depending on some value. The best way to achieve this is by changing the`@offset`attribute of the bpatcher object, which will shift the origin of the displayed view by the desired horizontal and vertical amount. Since bpatcher is a slightly unusual object, you have to set this attribute using a thispatcher object in the embedded subpatcher. See the bpatcher help file for more details.
Overview of the offset technique for adjusting the display of a bpatcher
## Embeded vs Referenced Patchers
As mentioned above, a bpatcher can either refer to an existing patcher file or embed its contents in its parent. The differences are similar to subpatchers and abstractions. When you enable the`@embed`attribute on a bpatcher, the contents of the bpatcher will be saved with the parent patcher.
If`@embed`is not enabled, the bpatcher references a patcher file specified in its`name`attribute. As with abstractions, changes to the original file will update every bpatcher that refers to that file. See abstractions for more detailed information on working with bpatchers that reference patcher files.
## Patcher Appearance in bpatchers
As mentioned above, when loading a patcher file, the bpatcher will use the`openinpresentation`attribute of the patcher to determine whether to show it in patching or presentation mode.
In addition, the patcher file can control the bpatcher's initial size and appearance when using the e command to create the object.
-
To assign a default size for the bpatcher, use the`openrect`( Fixed Initial Window Location ). The x and y coordinates of the openrect are ignored, but the width and height will be assigned to the bpatcher's initial width and height.
-
If`openinpresentation`is enabled and`openrect`is not set, the enclosing rectangle for all objects that belong to the presentation will be used as the bpatcher's initial size.
As an example, this patcher contains a function object that has been added to the presentation.
When using the e command and typing this patcher file's name, the resulting bpatcher frames the function object as shown below.
