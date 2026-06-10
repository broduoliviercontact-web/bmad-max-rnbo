---
title: "Max for Live Limitations"
source: https://docs.cycling74.com/userguide/m4l/live_limitations/
source_path: /userguide/m4l/live_limitations/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Max for Live Limitations

Source: https://docs.cycling74.com/userguide/m4l/live_limitations/

## Extracted Text

# Max for Live Limitations
Max and Max for Live are two separate products. The version of Max that comes bundled with Live is optimized for use with Live, but it is not the full Max 9 application, and is not intended to be used outside the context of Live. If you only have a Max for Live license, and not a full Max license, then the Max application will have certain limitations.
Limitation Description
Save patches using Gen , MC , and Jitter Geometry You will still be able to load and run Max for Live devices using these advanced Max features, but you will not be able to author your own Max patches using these faetures.
Gen code export You will not be able to export C code from any of the Gen objects, like gen~ and jit.gl.pix .
Integrated OSC Support Objects like udpreceive and udpsend will still work, but integrated OSC support will not be functional.
Direct Audio Driver Access (Multichannel Audio) Audio input/output will be limited to the particular Max for Live device. See Audio Limitations for more details.
Unlimited MIDI Hardware Messages (sysex, program changes, etc.) MIDI input and output will be limited to those messages that Live will recognize and pass between devices.
Direct MIDI Driver Access MIDI input and output will be limited to those MIDI messages sent directly between Live devices. You will not have direct access to your system's MIDI Drivers. See MIDI Driver Limitations for more details.
Standalone Operation (Run Max without Live) You will only be able to use Max inside of Live, and will not be able to run Max on its own.
## Audio Limitations
When authorized only via Live, the Max application will not use its own audio drivers. Its audio input is the input to the Max for Live device you are editing, and its audio output is the output from that Max for Live device. Audio I/O works when using preview mode . If you turn preview mode off, all audio I/O for the Max application will stop.
If Max and MSP are authorized when editing a Live device, Max Consoles that are not a part of the Live device will use the regular Max audio drivers.
The use of the send~ and receive~ objects to pass audio between Max for Live devices is not supported.
## MC Limitations
User initiated connections for MC patches are prohibited with only a Max for Live authorization. Runtime behavior and scripted connections will work, but in order to add new connections, a standalone Max authorization is required.
## MIDI Driver Limitations
When authorized only via Live, the Max application will not use its own MIDI drivers. MIDI input arrives from Live and MIDI output is sent to Live. MIDI I/O works only when using preview mode . If you turn preview mode off, all MIDI I/O for the Max application will stop.
When you open a Max patcher file such as a help file containing Max MIDI objects, the MIDI output will be sent to the MIDI output of the device you are currently editing. If you open a file containing MIDI objects when you are not editing a device, there will be no MIDI I/O.
If Max is authorized when editing a Live device, Max Consoles that are not a part of the Live device will use the regular Max MIDI drivers for MIDI objects.
## pattr and Max for Live Parameters
Although the pattr objects can be used in the context of Max for Live, there are some differences compared to normal Max use.
The autopattr object cannot be used to batch-register objects with the Parameter system. You need to use individual pattr objects for this purpose.
The pattr object functions mostly identically under Max and Max for Live. However, some users might expect the value of a pattr object in a Max for Live device to be automatically maintained by the Live Set upon save and close, and to be correctly restored when the Set is re-opened. This is not the case. This behavior is available, but only if the pattr object's Parameter Mode Enable attribute is enabled in the object's Inspector and the Parameter Visibility attribute is set to '`Automated and Stored`or`Stored Only'`.
The pattrstorage object also functions mostly identically under Max for Live, but there are a few important distinctions to keep in mind, if the object is in Parameter Mode . First, the value of the pattrstorage object in Parameter Mode is its entire storage state (what is ordinarily saved to an external file), rather than the currently recalled slot. This means that devices using pattrstorage in Parameter Mode need not require an external file to recall the storage state of the object (it can be saved in presets, set as an initial value or stored in the Set). Use of an external file can be disabled using by setting the object's savemode attribute to 0. If the pattrstorage object has an Initial Value, the savemode and autorestore attributes are ignored and file-less use of the object is assumed. Finally, the pattrstorage object has an additional attribute when in Parameter Mode: Auto-update Parameter Initial Value. When this is enabled and Initial Enable is turned on, all changes to the object's storage state will cause the Initial Value to auto-update to the new state.
## Other Limitations
The grab object cannot be used to communicate from a send to a receive between devices.
When authorized only via Live, Max cannot build standalones or collectives . Frozen devices , which Max for Live creates, are very similar to collectives.
