---
title: "Polyphony"
source: https://docs.cycling74.com/userguide/polyphony/
source_path: /userguide/polyphony/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Polyphony

Source: https://docs.cycling74.com/userguide/polyphony/

## Extracted Text

# Polyphony
Max provides a number of systems for managing polyphony . If you've every played an electric piano before, the concept of polyphony should be intuitive. When you press multiple keys at the same time, each key sounds independently, with each note lasting until it fades out, or until each key is released. However it's accomplished, handling polyphony always involves the same basic tasks:
- Routing an input to a specific voice
- Managing the independent state of each voice
- Deciding whether a particular voice is busy
- Muting a voice when it's not in use
## ddg.mono
The simplest way to handle polyphony is not to handle polyphony. The ddg.mono object implements a controller for a monophonic synthesizer with polyphonic input. If you were using a keyboard input, when pressing a second key, ddg.mono would shift the pitch to the new key, no longer tracking the first key.
## Using poly
The poly object is a polyphonic voice controller for MIDI note-on and note-off events. When it receives a note-on event, it assigns that event to the first available voice. When it gets a note-off event with the same pitch, it marks that voice as no longer in use.
The poly is a voice controller only. That means that it doesn't manage the voices themselves—it won't help you turn one oscillator into several. If you want to have multiple voices sounding at the same time, you should use mutiple patchers, the MC system, or the poly~ object.
## Using poly~
Copy
Maybe the "simplest possible" poly~ abstraction patch
The poly~ object combines the voice controller of the poly object with a system for managing multiple voices. When you load an abstraction into poly~ , it will create one copy of that abstraction for each voice. Then, poly~ gives you the tools to route incoming messages to a specific voice, while also managing the individual state of each voice.
### Viewing voices
Just like other abstractions , you can double-click on a poly~ object to view the patch that it's loaded as an abstraction. However, since poly~ loads one copy of the abstraction for each voice, you'll also see a number next to the name of the patch, indicating which voice you're currently looking at.
The number (1) next to ez-synth tells you that you're looking at the first voice.
You can send poly~ the messge`open`to view the loaded abstraction for a particular voice. The messages`open 1`will show the first voice,`open 2`will show the second voice, and so on.
### Event inputs
When poly~ receives a message, it uses one of several systems to determine which voice will receive that message.
The simplest system uses the`@target`attribute. When you set the`@target`attribute to a particular voice number, all subsequent messages will be routed to that voice. If you set`@target 1`, then all messages will be routed to the first voice. Set`@target 0`to make all voices the target, in which case each messages will be copied and sent to each voice.
Messages starting with the symbol`note`will be automatically routed to the first available voice. You can tell poly~ when a voice is busy by using the thispoly~ object—see busy state for more details.
The poly~ object can also handle MIDI note-on and note-off events using the`midinote`message. When you send poly~ a message like`midinote 60 127`, it will get a free voice and send that note-on event to that voice. When you send poly~ a note-off event like`midinote 60 0`, it will find the voice associated with the pitch`60`and send the note off event to that voice. The poly~ object can also receive messages with the symbol`midievent`, like those coming from the rightmost outlet of the midiparse object. In this case, the system for assigning note-on and note-off events to voices is the same.
Finally, poly~ is also an MPE-compatible object. Use mpeparse and mpeformat to generate`mpeevent`messages, which poly~ will then route to the appropriate voice. The really cool thing about this approach is that it can manage not only note-on and note-off events, but also polyphonic aftertouch, pitch bend, and other MPE events.
When using any of the MIDI-based systems for voice control, you can use the`notemessage`message to route events to the voice that has been assigned a particular MIDI pitch. This is different from using`target`, which always addresses the voice at a particular index.
### Busy state
In order for poly~ to route`note`and`midinote`messages to the right place, it needs to know when a note is busy . From within a particular poly~ abstraction, use the thispoly~ object to manage busy state. Send thispoly~ the message`1`to mark the note as busy, and the message`0`to indicate that the voice is free, and ready to recieve new`note`or note-on messages.
You can also send thispoly~ a signal, such as the output from adsr~ , to mark the voice as busy/free.
It's extremely common to see an adsr~ connected like this, where it's used both to modulate the signal and to control the busy state of the poly~ abstraction.
### Muting
When a poly~ voice is muted , Max will skip signal processing for any signal-rate objects in that particular voice. Objects can still pass messages to each other, but no signals will flow between objects. Muting makes poly~ more efficient, since it won't waste processing power computing silent signals for unused voices. This can be especially important when you're working with multiple poly~ objects, or in the context of a custom Max for Live synthesizer.
Since the adsr~ object will also automatically send mute/unmute messages, you'll often see it connected to a thispoly~
### Inlets and outlets
Unlike regular abstractions, poly~ uses the special objects in and out in order to declare inlets and outlets, and the objects in~ and out~ to declare signal inlets and outlets.
This patcher will have one message inlet and one audio outlet.
Unlike the inlet and outlet objects, these objects take an argument to specify their index. This has some upside; for example, you can reference the same inlet/outlet in multiple places, and you can place the inlet/outlet objects in any left-to-right order that you like.
Two in objects share the index 1, and any messages sent to the first inlet will be received by both these objects. Also, the [in 2] object will receive messages sent to the second inlet, even though it appears to the left of the [in 1] object.
There's also a special object polymidiin , specific to poly~ . This object receives any messages sent to poly~ with the`midievent`symbol, like the ones that come from the rightmost outlet of mpeparse and midiformat .
Copy
The polymidiin object (not shown but in the simplepolymidi abstraction) works with midiivent messages, like from mpeparse and midiformat.
### Parameters
The poly~ object supports the use of the param object, which lets you define custom attributes on your poly~ object. You can control these with an attrui object, just like a regular object attribute. You can set a`@min`and`@max`value on your param too, constraining it to a given range. See the param help file for more information.
The param defines a custom attribute mod-depth" that can be controlled with an attrui object.
### mc.poly~ and mcs.poly~
The poly~ object has two wrappers, mc.poly~ and mcs.poly~ . These objects help to bridge the gap between the mc system and the poly~ object. The mc.poly~ object is maybe the simplest to understand: it turns each signal input to poly~ into a multichannel input, where the number of channels is the same as the number of polyphonic voices. Unlike regular poly~ , the mc.poly~ object does not add together the signal output from each voice, but keeps each channel separate.
The number of channels depends on the number of polyphonic voices of the mc.poly~ object.
The mcs.poly~ object collapses all of the signal inputs and outputs of a poly~ object down to a single multichannel input and output. The number of input channels and the number of output channels depends on the number of in~ and out~ objects with different indices in the poly~ abstraction. Each audio input and output will be copied and sent to each polyphonic voice.
With mcs.poly~, the number of input and output channels depends on the in~ and out~ objects.
## Using MC Objects
The MC wrapper can manage polyphony without the use of the poly~ object. The mc.noteallocator~ object works of of MIDI note-on and note-off events, similar to how poly~ responds to`midinote`and`midievent`messages. There's also the mc.voiceallocator~ object, which works more like poly~ in response to the`note`message. For more information, see the guide on MC Wrapper Polyphony .
