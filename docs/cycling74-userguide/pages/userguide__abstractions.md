---
title: "Abstractions"
source: https://docs.cycling74.com/userguide/abstractions/
source_path: /userguide/abstractions/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Abstractions

Source: https://docs.cycling74.com/userguide/abstractions/

## Extracted Text

# Abstractions
Any saved Max patcher can be loaded into another patcher as an Abstraction . When you create a new Max object , if that object has the same name as a Max patcher, Max will load that patcher into the new object. This lets you create patches that you can reuse over and over again, helping you patcher faster and more effectively.
## Creating an Abstraction
When you create a new Max object, Max will look through the search path for an external or abstraction with that same name. If Max finds a`.maxpat`Max patcher file, it will load that file as if it were a Max subpatcher. Just like a subpatcher , you can view the patcher contained in an abstraction by double-clicking on it in a locked patcher view.
The object named `my_abstraction` loads the file `my_abstraction.maxpat` as an abstraction
Your Max patcher can only load another patcher by name if it appears in the current search path. That means it's very common to see abstractions either saved in the same folder as the parent patcher, or else included as part of a Project . Of course, you can load abstractions from anywhere in the Max search path, but managing abstraction dependencies is a common use case for projects too.
## Editing an Abstraction
If you open an abstraction from a parent patcher, it may open in read-only mode. In this mode, you must click the Modify read-only icon to unlock it for editing. See Modify read-only for more information.
## Inlets and Outlets
An abstraction will have as many inlets or outlets as it has inlet or outlet objects. If you create a new inlet and save your abstraction, the parent patcher (the patcher containing the loaded abstraction) will update to include the new inlet. The order of the inlets in the parent patcher corresponds to the order of inlets in the abstraction. So, if you swap the position of two inlet objects in the abstraction, those objects will map to different inlets in the loaded abstraction.
The abstraction has two inlet objects and one outlet object, so the loaded abstraction object has two inlets and one outlet.
Just like a regular Max object, an abstraction can add Comments to its inlets and outlets. If you set the`@comment`attribute on an inlet or outlet object, then when you mouse over the inlet or outlet you will see that text displayed.
## Abstractions vs Subpatchers
Abstractions and subpatchers are very similar, but they have a few key differences. For a start, abstractions reference a saved`.maxpat`file, while subbpatchers are embedded in their parent patcher. That means that you can't edit an abstraction without changing the original file. If you open an abstraction patcher, you will see that the normal Unlock icon in the patcher toolbar has been replaced with a pencil icon. Hovering over the icon, you will see the text "Modify read only". If you click this icon to enable editing, then any changes you make to the abstraction will change the original file. Consequently, changes you make here will affect all instances of the abstraction. This is different from embedded subpatchers, where each subpatcher has its own data, and changing one does not affect the others.
### Transformations
It's possible to convert a subpatcher into an abstraction using the action menu , with the Abstraction to Embedded Subpatcher command. This command will copy the contents of the abstraction file to a new subpatcher, which can be really useful if you want to modify an abstraction, but you don't want to change the original file.
## Arguments and Attributes
Abstractions can have arguments and attributes, just like a regular Max object. You can handle arguments in one of two ways, either using the patcherargs object, or using the special`#`-sign syntax for abstractions, Max for Live devices, and poly~ patches.
The`#`-sign syntax lets you quickly define "insertion points" where the text of any argument will replace the`#`-sign text. For example, if you have an object inside an abstraction with the text`buffer~ #1`, then the text`#1`will be replaced by the first argument passed to the abstraction object. If you lock and unlock the abstraction, you can alternate between viewing the text before and after replacement.
The #1 symbol in an abstraction will be replaced by the first argument in the parent object.
If you put a patcherargs object into your abstraction, then any arguments that you give to the abstraction object will come out of the left outlet of patcherargs when the abstraction is loaded. The patcherargs object can also process attribute-style arguments. These will come out of the right outlet of patcherargs , one at a time, followed by the`done`messages. In some sense, patcherargs works a lot like a loadbang or loadmess object.
A patcherargs object outputs the argumetns of the parent object when the abstraction is loaded.
## Unique Identifiers
Sometimes it's useful to create unique identifiers inside of an abstraction. Suppose you have a send / receive object pair inside your abstraction. If you create two instances of the abstraction, any messages sent to the send object in one will be received in the receive objects in both instances. If this isn't the behavior you want, you can use the special`#0`prefix to create a unique number. This`#0`prefix will be replaced by a number unique to each patcher instance, so different instances of the same abstraction will get a different unique number. In this way, you can use send and receive in an abstraction, without sharing messages among all instances of that abstraction.
The`#0`prefix will only be replaced with a unique number if it appears at the beginning of the word. In a message box containing the text`#0-text`, the`#0`will be replaced. However, if the same message box contained the text`text-#0`, then the`#0`would not be replaced.
The special #0 prefix will be replaced by a number unique to the specific patcher instance. Different instances of the same abstraction will get a different unique number.
## Description, Tags, and Browsing
The Patcher Inspector has several attributes under the header`Description`, all of which let you describe your patcher in one way or another. Max will parse these attributes into its internal database, meaning you can search for patcher by their description using the File Browser . Tags can be especially useful, since you can search for tags using advanced search , with a search pattern like`tag:<your-tag>`.
## Help Patches
Abstractions can have Help Patches , just like regular Max objects. To create a help file for your abstraction, all you have to do is save a Max patcher with the`.maxhelp`extension, where the name of the patcher file is the same as the name of your abstraction. So, if your abstraction is called`my_abstraction.maxpat`, the help file should be named`my_abstraction.maxhelp`. If the help file is in Max's search path, then when you look up the help file for your abstraction, your custom help file should open.
