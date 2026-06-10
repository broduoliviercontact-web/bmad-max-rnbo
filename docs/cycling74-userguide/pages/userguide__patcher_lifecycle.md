---
title: "Patcher Lifecycle"
source: https://docs.cycling74.com/userguide/patcher_lifecycle/
source_path: /userguide/patcher_lifecycle/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Patcher Lifecycle

Source: https://docs.cycling74.com/userguide/patcher_lifecycle/

## Extracted Text

# Patcher Lifecycle
## Opening a Patcher
In general, it's best practice not to make any assumptions about the order in which things will happen when Max opens up a saved patcher. If there's a way to use an object like trigger to make the order of messages explicit, it's usually a good idea to do so. However, when Max loads a new patcher it does initialize the patcher in specific phases.
Max patcher stages of initialization
- Object Initialization
- Patchcord Connection
- Parameter Initialization
- pattr Restoration
- loadbang and loadmess
- live.thisdevice
- Window Activity
- Patcher Arguments
- dspstate~ and Signal Processing
### Subpatchers
Within a given phase, Max subpatchers are initialized before their parents. If a Max patcher contains a loadbang object, and its subpatcher also contains a loadbang object, the loadbang in the subpatcher will always output a`bang`message before the parent. However, a buffer~ object in a parent patcher will initialize before any loadbang objects output a`bang`, even if the loadbang objects are in a child patcher, because Object Initialization comes before loadbang and loadmess .
### Object initialization
Max creates all objects in the current patcher. For some objects, this may have synchronous behavior, where the behavior might otherwise be asynchronous. For example, when a buffer~ object is initialized, if a file argument is provided, that file is loaded synchronously. After the patcher has loaded, sending a`replace`message to a buffer~ object triggers an asynchronous operation.
### Patchcord connection
After all of the objects in the patcher have been initialized, Max will rebuild all of the patchcord connections between objects. Importantly, since this happens after object initialization, Max messages sent between objects during the object initialization step might not be routed between objects as expected.
### Parameter initialization
Next, Max checks all objects for which Parameter Mode is enabled. For any such objects, if they have an initial value set, those objects will set their internal parameter value to that initial value, and then output their value.
Select Reinitialize from the Edit menu to set all parameters in the current patcher to their initial value.
### pattr Restoration
If there are any pattr objects with`@autorestore`enabled, Max will restore the last set value of each pattr object, and then each pattr object will output a value.
### loadbang and loadmess
Now that all objects have been initialized, loadmess and loadbang objects will generate their output.
### live.thisdevice
The live.thisdevice object functions similarly to loadbang in the context of a Max for Live device. In a regular Max patcher, live.thisdevice is functionally the same as a loadbang except live.thisdevice objects will trigger after loadbang objects.
### Window activity
After all objects have been initialized, and any loadbang or loadmess objects have sent their output, Max will create the window and bring it into focus. Any active objects will now send an output.
### Patcher Arguments
Patcher arguments (arguments and attributes on a patcher object) are parsed by patcherargs objects at the same time as loadbang and loadmess objects send their respective messages. However, the initial output of a patcherargs object is deferred, and will be sent after the window is ready.
### dspstate~ and signal processing
Finally, Max is ready to construct the signal processing graph and start audio processing for the patcher. This is the stage when all dspstate~ objects will send their outputs, reporting the current sample rate, DSP on/off status, etc.
## Closing a Patcher
Similar to the way Max builds up a patcher in stages when opening a new patcher, closing a patcher also breaks the patcher down in a standard order. Similar to opening a patcher, subpatches close before parent patches So, a freebang in a subpatcher will send its bang before a freebang in a parent patcher.
- closebang
- Freeing Objects
### closebang
First, the closing the Max patcher window causes any closebang objects to send a`bang`message. One interesting thing is that if you close a parent patcher window, with an open subpatcher containing a closebang object, that object will not send a`bang`message at this time. However, if you close the subpatcher window manually first, closebang will send a`bang`.
### Freeing objects
Max goes through all of the objects in the patcher and frees them. This frees any memory or other resources that each object might have been holding on to. It also causes any freebang objects to send a`bang`message.
