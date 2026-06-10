---
title: "Saving and Pattr"
source: https://docs.cycling74.com/userguide/pattr/
source_path: /userguide/pattr/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Saving and Pattr

Source: https://docs.cycling74.com/userguide/pattr/

## Extracted Text

# Saving State with pattr
When you save a patcher to a`.maxpat`document, you save its structure but not the state of objects in that patcher. The pattr object, along with object like autopattr , pattrstorage , pattrforward , and pattrhub , lets you save and recall the state of a patcher, or a subset of objects within the patcher.
## Saving State with pattr
Unlike some applications, Max does not save the state of a patcher along with its structure . When you save a patcher normally, you're saving the names of all the objects, their connections, their arguments, and their frozen attributes. However, the state of the patcher—the value of all your sliders, the contents of your number boxes—is not usually saved. The pattr object family is responsible for helping with saving the state of a patcher.
- We can maintain sets of data from objects throughout a Max patcher hierarchy. For example, with pattr you can control the state of objects inside of patcher and bpatcher objects all from the top level of the patcher.
- We can use pattr objects to remotely set and query the state of objects controlled by the pattr system from anywhere within the patcher.
- The pattr objects store groups of settings as JSON or XML files, allowing us to easily read and edit saved data outside of Max.
- The pattr objects can recall the state of objects in a specific order, avoiding difficulties with, for example, the recalling of a toggle object that starts a process before all the variables are in place for the process to function correctly.
- Not only can we store the states of many objects under a single address, we can also interpolate between these states, allowing for a seamless crossfade between multiple settings.
- The pattr objects feature a high-level interface for viewing and managing the current state of controlled objects and the states that have been saved.
## Quickstart
The simplest way to save the state of your patcher using pattr is to add an autopattr object and a pattrstorage object to your patcher. With autopattr , objects that have a scripting name will be added to pattrstorage automatically. Now store the state of your patcher by sending pattrstorage the message`store 1`. If pattrstorage has the attribute`@savemode 2`, then when you save your patcher, pattrstorage will save the state of your patcher to a JSON file. When you open your patcher, if Max can locate that JSON file, pattrstorage will load it automatically, and you can send pattrstorage the message`recall 1`to reload the state of your patcher.
Copy
Simple setup to save the state of a patch
## Parameters and pattr
Any object whose internal state can be represented as a parameter can be stored in the pattr system. This includes most UI objects ( slider , multislider , nodes ), along with any object with the`@parameter_enable`attribute. Also, dictionaries, strings, and arrays can be included in the pattr system.
An array, string, and dictionary, all stored in pattr
The pattr object itself can either be bound or unbound. When bound to an object, via either its middle outlet or the`@bindto`attribute, pattr simply references the internal state of the bound object. If pattr is unbound, then it instead manages its own, internal state.
The pattr 'var1' is bound to the slider. Changing the state of the slider updates the data stored in 'var1', but the data is stored under the key 'var1'. The data in 'var2' is managed internally by the other pattr object, and is not bound to any object.
Complex internal state can be represented as a parameter, so even objects like live.grid can be included in the pattr system and saved to pattrstorage . However, some objects cannot. For example, the contents of a jit.matrix or buffer~ cannot be stored with pattr.
## Including Objects in pattrstorage
In order to save the state of an object, it must be included in the pattr system.
- All pattr objects are included in the pattr system automatically. Both bound and unbound pattr objects will be addressable via pattrhub and saved with pattrstorage .
- Any object with a scripting name (`@varname`attribute) will be included in the pattr system if it's in a patcher with an autopattr object. If autopattr has the attribute`@autoname 1`, it will automatically give all valid objects a scripting name.
- Any object connected to the left outlet of autopattr .
The autopattr object will also collect the state of plugins included with vst~ or amxd~ . See the autopattr help file for more.
## Binding Objects to pattr
Bind a pattr object to pattr-compatible object either using the`@bindto`attribute, or using the middle outlet of pattr . Only one object may be bound to a given pattr at a time.
The pattr 'var1' is bound to the number box with @varname special. The pattr 'var2' is bound to another number box using its middle outlet. Finally, the pattr 'var3' tried to bind to two object, which caused an error message.
### Automatic Naming
Like many named entities in Max, every pattr object must have a name. If you don't give it a name, Max will assign one automatically. Also, every object that pattr binds to must itself have a name. If you bind a pattr to an object without a name, Max will assign a unique`@varname`automatically.
## Working with preset
The preset object can be used as an interface to the pattrstorage object. Set the`@pattrstorage`attribute of a preset object to turn that object into a visual representation of the pattrstorage object. Each preset slot in the preset object represents a different storage slot in the pattrstorage object. Use preset to create, update, and delete presets normally, and the state of the pattrstorage object will update automatically.
## Paths, Hierarchy and pattrhub
The pattrhub object can forward messages to any object in the pattr system. That includes pattr objects, as well as any object included in the pattr system with autopattr . If a pattr object has the name "var1", send a message like`var1 10`to pattrhub to send a message 10 to the pattr object "var1".
Using pattrhub to send messages to objects in the pattr system, including a pattr object as well as a number box with a scripting name.
### Other patchers and pattrmarker
In typical usage, a pattr system is linked to a single patcher hierarchy. If you have two distinct root patchers, then each will have a completely independent pattr system.
However, you can use the pattrmarker object to give a root patcher a global name that can be referenced from anywhere in pattr. If your root patcher contains a pattrmarker object with the text`pattrmarker earth`, then you can send messages to objects in that patcher by using the path prefix`::earth`. See the pattrmarker help file for details.
## Managing Storage
Similar to the preset object, store the state of pattrstorage by sending it a message like`store 1`to store the current state in slot 1. Recall a given state by sending it a message like`recall 1`to recall the data in slot 1. A floating-point value for recall, like 1.5, will interpolate between two stored slots. The interpolation curve and other parameters can be configured, see the pattrstorage help file for details.
### Saving and loading pattr data
Send pattrstorage the`write`message to save its contents to a JSON file. Later, use the`read`message to load the contents of a saved pattrstorage data file.
When you open a Max patcher containing a pattrstorage object, it will try to automatically load data from it's JSON file. The name of a pattrstorage object is important if you want this automatic loading to work, since Max will look up the data file using the same name as the pattrstorage object.
Because the pattrstorage object is named 'mydata', Max will look for the file 'mydata.json' to initialize pattrstorage when the patcher loads.
Saving pattrstorage data can be automated somewhat. If you set the`@savemode`attribute to something other than 0, Max will prompt you to save the contents of your pattrstorage .
@savemode Description
0 (no autosave or prompt) Never save automatically or ask to save
1 (prompt to save when object is freed) When you delete a pattrstorage object, or when the patcher that contains it gets freed or deleted, prompt the user to save. This keeps you from accidentally losing data held in pattrstorage .
2 (attempt autosave when patcher is saved else prompt) When you save the patcher, pattrstorage will try to save to the same place as it saved last time. If it can't, it will prompt the user to save.
3 (attempt autosave when patcher is closed else prompt) When you close the patcher, pattrstorage will try to save to the same place as it saved last time. If it can't, it will prompt the user to save.
### Multiple pattrstorage objects
Generally you'll only have one pattrstorage object per patcher. However, using the attribute value`@subscribemode 1`, you can explicitly assign objects to pattrstorage with the`subscribe`message.
Copy
Use the subscribe message to assign objects to pattrstorage.
## Usage with Max for Live Devices
Live-specific user interface objects such as live.dial save their state within Live documents and presets. Standard Max objects will not. If you want to use standard Max objects and have Live save their state, you'll have to attach those objects to a pattr object with`@parameter_enable`enabled. The "Parameter Visibility" attribute must also be set to "Automated and Stored" or "Stored Only".
Because this Max dial is bound to a pattr with @parameter_enable 1, its state will be saved with Live and included in Live presets.
There are some other important differences to keep in mind when building a Max for Live device with pattr objects:
- The autopattr object does not work with Max for Live's parameter system. It will not work with Live's parameter system, so objects that are attached to an autopattr will not be seen by Live. If you want a pattr parameter to appear for modulation etc, you will need to add a pattr object for each instance.
- The pattrstorage object mostly works the same in Max for Live, but there are a few important distinctions to keep in mind, if the object is in Parameter Mode .
- The value of the pattrstorage object in Parameter Mode is its entire storage state (what is ordinarily saved to an external file), rather than the currently recalled slot. This means that Live can save the contents of pattrstorage in the Live set itself, eliminating the need for a separate JSON or XML file. Use of an external file can be disabled by setting`@savemode`to 0.
- If the pattrstorage object has an Initial Value (Initial Enable is turned on in the Inspector), the`@savemode`and`@autorestore`attributes are ignored and file-less use of the object is assumed.
- The pattrstorage object has an additional attribute when in Parameter Mode: Auto-update Parameter Initial Value. When this is enabled and Initial Enable is turned on, all changes to the object's storage state will cause the Initial Value to auto-update to the new state.
