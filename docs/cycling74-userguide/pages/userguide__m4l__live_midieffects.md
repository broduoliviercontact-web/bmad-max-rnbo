---
title: "Creating MIDI Effects"
source: https://docs.cycling74.com/userguide/m4l/live_midieffects/
source_path: /userguide/m4l/live_midieffects/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Creating MIDI Effects

Source: https://docs.cycling74.com/userguide/m4l/live_midieffects/

## Extracted Text

# Creating MIDI Effects
A great way to start making any kind of device is to check out the Building Max Devices pack. We highly recommend this as a tool for learning how to make specifically devices , both Audio and MIDI.
Max for Live lets you create MIDI effects devices which receive MIDI information from the Live application, perform some operation on that data (e.g. mapping incoming notes to a user-definied musical scale), and then pass MIDI data downstream to another MIDI effect or to a MIDI Instrument - the last device in a MIDI effects chain (although the audio output of the instrument may be further processed by any number of Audio effects devices). By convention, Max for Live gets all its MIDI data from the Live application using the midiin object, and all of that data must all be passed downstream to other MIDI devices by means of the midiout object. Max for Live provides a means to redirect portions of an incoming MIDI data stream for processing while leaving the rest of the stream unchanged, as described below.
Also by convention, all Max for Live MIDI devices receive audio on MIDI channel 1. You can receive receive MIDI data in your Max for Live MIDI Effects device on a channel number other than 1 by routing the MIDI input as described here. Max for Live provides several tutorials and example MIDI effects devices you can try, study, and modify:
## Capturing a portion of the MIDI data stream in Max for Live
Max for Live requires that all MIDI data coming into a MIDI Effects device be passed downstream. There are situations in which you may want to use only a portion of the incoming MIDI data stream - to select only MIDI notes in a given range, or input from specific MIDI continuous controllers for use in your device. The Max midiselect object lets you specify portions of an incoming MIDI data stream to filter out for further processing in your device, and passes any other MIDI data out unchanged.
## Redirecting a part of a MIDI data stream
-
In your unlocked patch, add a midiselect object and connect its inlet to the outlet of the midiin object in your MIDI Effect or MIDI Instrument template file.
-
Following the name of the midiselect object enter the attributes corresponding to the MIDI data you want to filter out of the data stream, followed by any arguments that specify additional data (MIDI channel numbers, MIDI controller numbers, etc.). Attributes names begin with an at-sign (@), and there is no space following it and the type of data you want to filter out. The data types are:
-
ch: MIDI channel (only used when routing MIDI data from a non-channel 1 source, as described below)
-
note: MIDI note data
-
ctl: MIDI controller data
-
bend: pitchbend data
-
pgm: MIDI program change messages
-
touch: Aftertouch data
-
poly: Polyphonic aftertouch data
-
Connect the input of the midiout object in your MIDI Effect or MIDI Instrument template file to the right outlet of the midiselect object. Any data you do not specify when you instantiate the object or data you select by sending messages to the midiselect object will be passed downstream without being edited.
