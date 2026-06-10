---
title: "Object Reference"
source: https://docs.cycling74.com/userguide/object_reference/
source_path: /userguide/object_reference/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Object Reference

Source: https://docs.cycling74.com/userguide/object_reference/

## Extracted Text

# Object Reference
Every object in Max not only has a dedicated help file , but also a reference page. This page completely describes the object's behavior, inlcuding:
- A short and long description of the object's functionality
- The Arguments and attributes that can configure the object
- The symbols that the object understands
- Other related object and documentation
## Sidebar
You can view an abbreviated form of the full reference for an object by clicking on the Reference icon in the right sidebar.
The reference sidebar view will display reference documentation for whichever object is currently selected in the patcher.
With the buffer~ object selected, the sidebar view displays reference documentation for that object.
### Filtering the sidebar
The top of the sidebar view shows a short description of the object. Using the text field above the description, you can filter the contents of the sidebar view to find the entry that you're looking for.
### Arguments
The first section of the reference list view is for arguments. In this section, you can see all of the arguments that the object expects. Next to the name of the argument, you will see a short description of what the argument does. Click on an argument to select it, and a detailed description of that argument will appear at the bottom of the view.
### Messages
Under the arguments section, the messages section lists all of the messages that the object can understand. Click on a message to see a detailed description of that message at the bottom of the view.
You can drag and drop a row from the Messages section into an unlocked patcher. When you do, a message box will appear in the patcher.
### Attributes
The attributes section lists all of the selected object's attributes. As in the other sections, click on the attribute to see a detailed description of the attribute in the detail view at the bottom of the sidebar reference.
You can also drag and drop a row from the Attributes section into an unlocked patcher. When you do, an attrui object will appear in the patcher, pre-configured to select for the named attribute.
### See also
The last section of the sidebar reference is the See Also section. This section lists related objects and documentation. You can double-click on any object in this section to open the help file for that object, and you can double-click on any piece of documentation in this section to open it.
### Navigation
Use the buttons in the Navigation Bar at the bottom of the view to quickly jump to related pages.
- Show Previous Object — Jump to the sidebar reference for the last selected object.
- Show Next Object — After pressing Show Previous Object , navigate forwards again.
- Open Full Reference - Show the Full Reference for the selected object.
- Open Help File — Open the help file for the selected object.
## Full Reference
### Accessing the full reference
You can access the full reference for a selected object in a variety of ways.
Right-click on the object and select Open Reference from the contextual menu.
From the object action menu , select Reference .
With the object selected, click on the object name in the clue bar, and select Reference from the menu.
Select the object, then select Open Reference from the Help menu.
Finally, you can open the reference sidebar, and then click the Open Full Reference button in the bottom navigation bar.
### Using the full reference
The full reference for an object is an extended version of the abbreviated reference available in the sidebar view. At the top of the reference document, you'll see the name of the object, a short and long description, a longer discussion about the object, and a button to open the help file. At the very top, you'll see breadcrumbs that show the path to the reference file in Max's documentation.
The left side of the page shows the location of this reference document in Max's overall documentation. The primary Max documentation categories are listed here, in addition to a section Package Documentation that lists all the documentation for installed packages .
On the right side of the page, you'll see a navigation menu similar to the section categories from the sidebar reference view. From here you can jump to any section on the page, including the documentation for each argument, attribute, and message that the object supports. Additionally, the Output section describes what messages or signals the object will send out.
In the Arguments section, you'll see a detailed description of each argument. In addition to a description, you'll see the text`OPTIONAL`if the argument is optional, and you'll see the expected type of the argument as well. If the type is`[number]`, it means that the argument can be an int or a float.
The Attributes section lists attributes in a similar way. Note that for some attributes, you may see a special label indicating the version of Max in which this attribute was introduced.
The Messages section lists all of the messages to which the object responds. A message will have the special symbol`(mouse)`to indicate how the object will respond to mouse clicks. The symbol`signal`indicates how the object will handle signal inputs.
Finally, the Output section will describe what kinds of messages and signals the object generates. This optional section is most common for signal objects.
### Object parent classes
The full reference for an object documents every message and attribute for that object. Some objects have many, many messages and attributes, especially objects that have a parent class .
Max objects don't have a strict notion of inheritance like you might find in object-oriented programming languages like C++. However, certain Max object do have a parent class from which the inherit many common messages and attributes. For example, the jit.gl.gridshape object inherits from the Common object class and the OB3D object class.
- Common - The class that all objects with an object box inherit from. Adjust things like the font, background color, and the annotation.
- OB3D - The parent class for all objects that manage an object in a 3D computer graphics scene. Attributes let you control things like the matrix transform and the color.
In the reference page for an object like this, you'll see a list of object parent classes with a disclosure triangle next to each.
Click on the disclosure triangle to see the attributes or messages that the current object inherited from the given parent class.
Some of the messages that all objects from the OB3D object class will respond to
