---
title: "Presets and Interpolation"
source: https://docs.cycling74.com/userguide/presets_and_interpolation/
source_path: /userguide/presets_and_interpolation/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Presets and Interpolation

Source: https://docs.cycling74.com/userguide/presets_and_interpolation/

## Extracted Text

# Presets and Interpolation
A preset is a set of values of one or more objects in your patcher you have stored for later recall. Max has two objects, preset and pattrstorage , whose primary purpose is storing and recalling these sets of values. You can use other objects for this purpose, including table , coll , and dict , but preset and pattrstorage have two principal advantages:
-
they can store and recall the state of objects without patch cord connections
-
they offer the ability to interpolate between two or more preset states
## Storing and Recalling Values
### The preset Object
The preset object is an easy-to-use way to capture the state of user interface objects. The preset object is itself a user interface object. Each square in its grid represents a different preset.
In the example below, shift-clicking on any square in the preset will capture the current state of all the user interface objects in the patcher -- the dial, slider, and number box. Clicking on the square (without holding down the shift key) will recall the stored state asociated with the sequare (and draw that square to indicate it's current).
Any preset data you store will be saved in the patcher file containing the preset object.
### The pattrstorage Object
The pattrstorage object has many features and operating modes that go far beyond what preset is capable of doing. In this brief introduction, we'll discuss how to use pattrstorage in a manner roughly similar to preset .
The name pattrstorage comes from its role in storing the values of pattr objects. "Pattr" is short for patcher attributes and is an object that creates a single named storage location. While preset stores the values of user interface objects directly, pattrstorage needs a pattr object before it will store anything. Conveniently, it's not necessary to make pattr objects explicitly to store the values of user interface objects. Instead, two things are required:
-
ensure each object whose value you want to store has a scripting name -- this will be true for objects such as live.dial that default to parameter mode on but not for toggle , dial or other UI objects that do not enable parameter mode by default. (Parameter mode itself is not required to use pattrstorage , just the scripting name.)
-
add an autopattr object to your patcher.
The autopattr will ensure every user interface object with a scripting name has a hidden pattr to go with it.
If you double-click on the pattrstorage object, you'll see all of the pattr slots and their current values.
To store a preset with the current values managed by pattrstorage , send the message store followed by a slot number starting at 1.
Send that same number back to recall to pattrstorage to recall the preset. (The preset object accepts the same messages.)
To see the contents of all your presets, you can open the storage window by sending the message`storagewindow`to pattrstorage .
Saving pattrstorage data in a file offers more options than preset . The default option is to prompt you to save any newly stored data in a separate file when you close the parent patcher. You can read this data file back into pattrstorage using the`read`message.
## Interpolating Between Two Presets
Both preset and pattrstorage offer the ability to interpolate between two adjacent presets. Interpolation is an operation that produces a value in between two values. In both objects, you use a float value between two storage slots to specify where in the distance between the slots you want the resulting values.
Here's a simple example with a single object. Suppose the value of a slider for preset 1 is 0 and 1 for preset 2. An float value 1.5 sent to preset or pattrstorage will produce an output value halfway between the two presets, resulting in a value of 0.5 (which is half way between 0 and 1). A float value of 1.9 will produce a value closer to preset 2 than preset 1 -- in this case the slider will be set to 0.9.
When you interpolate between two presets with the preset object , the display of the active slot will show the relative contribution of each of the two slots. The display can help you keep in mind that a value of 1.7 does not mean preset 1 contributes 70% to the value; in fact, just the opposite. The interpolation calculation is based on the distance between the value and the whole number. The farther away the float value is from the whole number, the less that preset slot will contribute to the final interpolated outcome. And the closer the float value is to a whole number, the more that preset slot will contribute. Thus 1.99 will be 99% preset 2 and 1% preset 1.
While preset is limited to linear interpolation, pattrstorage offers several other interpolation curves and behaviors via its`interp`message.
## Multi-Preset Interpolation
Both preset and pattstorage offer the ability to interpolate using the data in several preset slots with the`recallmulti`message. Multi-preset interpolation is based on a list of weights, where the integer part of the value is the preset slot number and the decimal part is the relative weight of the preset contributing to the outcome. Weights are normalized so they don't have to add up to 1. Here's an example using the preset object below where we want to use preset slots 1, 4, and 7.
`recallmulti 1.5 4.5 7.5`will weigh each preset slot equally. So will`recallmulti 1.2 4.2 7.2`.`recallmulti 1.8 4.0 7.2`will be 80% preset 1 and 20% 7, with nothiing from preset 4.
As with two-preset interpolation, the preset object will display the weights for the most recent`recallmulti`message.
## Non-Interpolating User Interfaces
### preset As a Front End for pattrstorage
You can use a preset as a front-end for storage and recall of presets in pattrstorage . Give pattrstorage a name with its first argument, then set the`pattrstorage`attribute of preset to this name. After doing this, shift-clicking on a slot in preset actually stores a preset at the same slot in pattstorage , and clicking on a slot in preset recalls the corresponding slot in pattrstorage .
### umenu and chooser As a Front End for preset
To display presets in a list format rather than the grid of the preset object, connect a umenu or chooser to the left inlet of preset . The contents of the umenu and chooser will be kept in sync with the storage state and most-recently recalled slot of preset . You can also display names for each preset slot by appending an optional name to the`store`message.`store 2 Cyclical`will name the new preset`Cyclical`. You can see the name when moving the cursor over the stored slot in preset or, if you have a connected umenu or chooser it will show up in the item text.
## Interpolation User Interfaces
The nodes object is ideal for multi-preset interpolation with either preset or pattrstorage . Connecting nodes to the inlet of preset creates a visual "node" for each stored preset up to a maximum set by the Max Dynamic Nodes (`maxdynamicnodes`) attribute, which defaults to 8. Dragging the mouse over nodes performs multi-preset interpolation.
Using nodes with pattrstorage requires more work including manually creating the set of nodes that will correspond to the preset slots you want to interpolate and some patching logic to translate the values coming out of nodes to the correct values for the`recallmulti`message. An example is found in the pattrstorage tab of the nodes object help file .
## See Also
- Snapshots
