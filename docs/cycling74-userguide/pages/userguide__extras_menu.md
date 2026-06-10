---
title: "Extras Menu"
source: https://docs.cycling74.com/userguide/extras_menu/
source_path: /userguide/extras_menu/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Extras Menu

Source: https://docs.cycling74.com/userguide/extras_menu/

## Extracted Text

# Extras Menu
The Extras menu provides quick access to frequently used patchers. Max comes with a set of utility patchers for everyday functions like testing MIDI input and opening the Global Transport , and you can also add your own patchers to the Extras menu.
## Included Extras
Extra Description
Audiotester Measures input and output levels for your audio setup, and can be used to test your audio hardware and sound system.
DSP CPU Monitor Shows the current approximate audio CPU utilization.
ExamplesOverview Browse and launch examples included with Max.
GlobalTransport Start, stop, and display the passage of time for objects that use Max Time formats .
Human Interface Driver Tester Set up and test any object that support the hi object.
JitterTester Tests video input devices.
KeyMidi Use your computer keyboard as a MIDI keyboard.
Meterin and Meterout Provide 24 channels of meters for audio input and output.
MIDI Tester Display all MIDI input and output devices and lets you test your connections.
Mousemeter Tracks the mouse.
ObjectHelpLauncher Fast way to open a help file.
Quickrecord Quickly record the audio output, up to 8 channels.
UDP Tester lets you test the sending of Max messages over a network using UDP.
You can add your own patchers to the Extras menu by creating a Package with an`extras`folder.
## Package Extras
Packages that you add to Max (from the Package Manager or by adding folders to the`Packages`directory) will add patchers to the Extras menu as well. Most packages include a "launcher" patcher that acts as an overview for the package, and some packages will have an extras folder that adds even more patchers.
### Adding extras
If you want to add your own patchers to the Extras menu, you can create a custom package and add your patchers to the`extras`subfolder. See Packages for more information.
