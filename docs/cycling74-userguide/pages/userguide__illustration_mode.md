---
title: "Illustration Mode"
source: https://docs.cycling74.com/userguide/illustration_mode/
source_path: /userguide/illustration_mode/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Illustration Mode

Source: https://docs.cycling74.com/userguide/illustration_mode/

## Extracted Text

# Illustration Mode
Observe your patcher running in slow motion to understand and/or debug its operation.
## Enabling Illustration Mode
Choose Illustration Mode from the Debug menu. You can also click the Debug icon in the bottom patcher toolbar to show the debug menu.
Illustration Mode is generally a global setting for all patcher windows.
### A Simple Example
Whlie it might seem as if everything in Max happens all at once, there's a predictable order of operations that becomes visible once you slow things down. The animation below demonstrates the right-to-left sorting of patch cords from a single outlet.
Illustration Mode in Action
## Illustration Mode and Debugging
Most Max debugging features work in Illustration Mode. Your patcher will run in slow motion and messages wil "travel" down patch cords, unlike traditional Max debugging where the patcher runs at regular speed until you stop execution at a Break watchpoint. If a Break watchpoint is encountered in Illustration Mode, excecution will pause. You can then choose Continue from the Debug menu to resume Illustration Mode execution, Abort to cancel execution entirely, or Step to advance to the next outlet and pause again. Choosing Pause from the Debug menu will also pause execution.
When paused, unchecking Illustration Mode in the Debug menu will continue normal execution.
## Debug Event Queue
When using either Illustration Mode or debugging, Max is not completely frozen and other events could occur. Examples include changing UI objects or incoming MIDI messages. Events that occur while debugging or in Illustration Mode are placed into event queues before they are sent out an outlet and illustrated. When the current computation sequence completes, the next event will be removed from the event queue and processed.
In the example below, events are queued when you move a slider, then output one by one once the processing chain of objects connected to the button completes. The pending event queue for each outlet is represented by an orange bubble showing the count of events remaining to process.
Debug Event Queue
To empty the event queue for an outlet, cancelling all pending events, click the close button on the orange bubble. To cancel pending events at all outlets, click the Debug icon in the bottom toolbar and choose Cancel Pending Events.
You can set the maximum size of the Illustration Mode Event Queue in the Preferences window. (The size defaults to 0 which is unlimited.)
As an example, if you set the maximum queue size to 15, up to 15 events will be stored in the queue at each outlet. Once the queue is full, new events will begin overwriting the oldest events.
