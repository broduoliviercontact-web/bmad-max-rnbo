---
title: "Inspector"
source: https://docs.cycling74.com/userguide/inspector/
source_path: /userguide/inspector/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Inspector

Source: https://docs.cycling74.com/userguide/inspector/

## Extracted Text

# Inspector
View and modify the internal state of any Max object using the inspector.
## Opening the Inspector
Open the inspector by clicking the Inspector icon in the right toolbar.
Opening the Inspector .
You can also select Inspector from the Object menu as another way to open or close the inspector. If you'd prefer to see the inspector in a separate window, select Inspector Window from the View menu instead.
## Inspector contents
The contents of the inspector are determined by the current selection. With a single object selected, the inspector will show all attributes for that object.
Inspecting an object
With multiple object selected, the inspector will show all attributes that are shared by the selected objects. Changing the value of a single attribute will update that attribute's value for all selected objects.
### Inspector Toolbar
The toolbar at the bottom of the inspector exposes several handy functions.
The inspector toolbar
Icon Name Function
Modify Selected Item Copy or change the value of an attribute.
Show Attribute Names Show the programmatic ID of an attribute.
Show Column Header Show the column headers for sorting.
Freeze Attribute Freeze or unfreeze an attribute.
Make Attribute in Patcher Create an attrui object in the patcher to modify the selected attribute.
Show in Reference Open the reference documentation for the selected object attribute.
Show Object Highlight and focus the selected object in the patcher view.
### Finding your attribute
Some objects can have a lot of attributes. At the very top of the inspector window, a text input lets you display only those attributes whose text matches the contents of your filter. The match includes the attribute name, not just its display name, and so the filter text "var" will match the attribute`varname`with the display name "Scripting Name", even if Show Attribute Name is not enabled.
Filtering the inspector
The tabs underneath the filter input select for attributes matching a given category. Attributes in the Basic tab are the most common attributes for the selected object. Attributes under Layout handle the positioning and appearance of the object. Recent shows attributes most recently modified for the object, and the All tab shows all attributes. Click and hold the All tab to show the subcategories of all attributes, and pick one to open just the disclosure tab for that subcategory.
Show subcategories under All
### Sorting attributes
It's possible to sort attributes by name or by value. In the bottom toolbar, click on the Show Column Header icon in the bottom toolbar to reveal the headers of the inspector table.
With the headers revealed, click on any header to sort all attributes based on the value of that column. Click on the header again to switch between ascending and descending sort.
### Dragging attributes
You can drag rows from the inspector into your Max patch. When you do so, Max will create a new attrui object, configured to display the selected attribute. In this way you can quickly build an interface for controlling a particular set of attributes.
Drag and drop attributes from the inspector to create attrui objects
If you drag the attribute on top of an existing object, Max will automatically connect the attrui object to the target object. Finally, you can hold down the option key while dragging to display a popup menu with more options, including an option to create a message box containing the current value of the attribute.
## Attribute Names
Attributes can be identified by their Display Name , a brief, human-readable description, or by their Scripting Name , a unique identifier used to fetch the attribute programatically. By default, the inspector hides the scripting name and shows only the display name. The Show Attribute Name button in the inspector toolbar lets you toggle the visibility of the scripting name of each attribute.
Enable 'Show Attribute Names' to display the scripting name of each attribute.
## The Patcher Inspector
The Patcher itself is, behind the scenes, just a Max object like any other. Many properties of the patcher, like the patcher background color, can be controlled by modifying the attributes of the patcher. To access the patcher inspector, open up the inspector with no object selected. An icon will appear at the top of the empty inspector view, which you can click to access the Patcher Inspector .
An empty inspector, revealing the 'Show Patcher Inspector' icon at the top of the inspector view.
## Freezing Attributes
Most attributes, like font size or scripting name, are saved with the patcher and will be restored when you reopen the patcher later. However, some attributes are not stored by default, and will appear italicized in the object inspector.
Unsaved attributes are shown in italics
If you want to save the value of an attribute, you can use the snowflake icon in the inspector toolbar to freeze the attribute. Frozen attributes will embed their current value with the patcher, so that this value can be restored when the patcher is next opened. Once the attribute is frozen, the display name will show the frozen value of the attribute. It is also possible to freeze attributes that are normally saved with the patcher. Once an attribute is frozen in its way, the frozen value is the value that will be restored when the patcher is closed and reopened. It might be useful to freeze an attribute like this to "anchor" it to the frozen value, rather than its current value.
The frequency attribute, after it's been frozen.
## Modifying and Resetting Attributes
The Modify icon in the bottom toolbar lets you copy, revert, and reset the value of a given attribute.
The gear icon in the left of the bottom toolbar
Select an attribute, then click on this icon to access several options related to the value of the attribute.
The expanded 'Modify Selected Item' menu.
Menu Item Description
Copy Attribute Copy the value of the attribute to the clipboard. Once the value is copied, you can paste the value to another attribute using the Paste command from the Edit menu.
Revert Value If the value of the attribute has been modified since the last time the inspector was opened, this option lets you set the attribute back to its original value.
Set to Default Value Reset the value of the attribute to its default. Not all attributes have a default value, so this option might not be enabled for all attributes.
Set to Frozen Value If you've frozen the attribute, establishing a new saved value for the attribute, you can use this option to set the attribute to the frozen value.
