---
title: "Creating Audio Effect Devices"
source: https://docs.cycling74.com/userguide/m4l/live_audiodevices/
source_path: /userguide/m4l/live_audiodevices/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Creating Audio Effect Devices

Source: https://docs.cycling74.com/userguide/m4l/live_audiodevices/

## Extracted Text

# Creating Audio Effect Devices
A great way to start making any kind of device is to check out the Building Max Devices pack. We highly recommend this as a tool for learning how to make specifically devices , both Audio and MIDI.
Max for Live lets you create audio effects devices which receive audio input from the Live application process it in some manner, and pass its audio output either back to the Live application, or to other downstream audio effects devices in the same audio track where the device resides. By convention, a Max for Live device gets all its audio from the Live application using the plugin~ object and sends its audio output using the plugout~ object. Audio input and output is limited to two channels.
Sending audio to another Max for Live Audio Effect, Instrument, or MIDI Effect device using the Max send , receive , send~ , or receive~ , objects is not supported. While creating a Max for Live audio device can begin by using the Max for Live device templates, you can use some of the Max for Live Audio devices, MIDI effects, and Instruments that come with Max for Live as your starting point. Read more about Max for Live limitations .
## Defining Latency For A Device
When Live sends audio or when MIDI triggers audio through an effect created using Max for Live, the events should all be time-aligned (e.g., if a MIDI note falls on the downbeat, the MIDI Instrument's audio should also end up in the mix on the downbeat). A device can provide latency information to the Live host application so that the host can use latency compensation to adjust the relative timing of different audio tracks.
When you use Max for Live, there are situations where it is useful to set latency to counteract timing differences introduced in your signal processing. If your signal processing patch requires you perform some kind of analysis on a block of samples before any output is produced, you can enable latency to make sure that the output from your effect will be correctly aligned in the mix (whereas if you are creating a device in which signal delay is what you intend, there's no problem and you don't need to set any latency).
### Setting Device Latency
-
With a device window as the topmost window, choose Patcher Inspector from the View menu to show the Inspector .
-
Double-click in the Value column for the Defined Latency attribute to show a cursor and text box. Type in a value for the latency value in samples , followed by a carriage return.
