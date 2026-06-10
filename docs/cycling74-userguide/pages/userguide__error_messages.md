---
title: "Error Messages"
source: https://docs.cycling74.com/userguide/error_messages/
source_path: /userguide/error_messages/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Error Messages

Source: https://docs.cycling74.com/userguide/error_messages/

## Extracted Text

# Error Messages
When Max encounters an error, it will print a message to the Max Console . This message is often specific to the object that generated it, and the message will usually contain whatever information you need to figure out what went wrong. However, there are some common errors that you may encounter often when working with Max
## Common Error Messages
### Files
#### `<objectname>: error opening file`
The object was able to locate the file with the name, but there was a problem reading or opening the file.
#### `<objectname> : <filename> : can't open`
The object was not able to open the file. This could be because the file contained data that the object was not able to understand, or because the file is missing, or because Max doesn't have permission to read the file. It may be that the file is not in Max's Search Path , so make sure that Max can locate the file.
#### `<filename> : bad magic number`
The Max file you tried to open is corrupted or is not a properly formatted Max document. Restore the file from a backup copy if available.
#### `<filename> : corrupt binary format file`
The Max file you tried to open is corrupted or is not a properly formatted Max document. Restore the file from a backup copy if available.
#### `<filename> : error creating file`
There was an error writing a file; the disk may be write-protected or full.
#### `<filename> : out of memory writing file`
There is insufficient memory to write the file you're trying to save. If possible, close other files and windows that don't relate to the file you're saving.
### Objects and Patching
#### `<objectname> : bad argument creating object`
The object was given an argument that it doesn't understand. This can happen when an object expects a symbol as an argument, but gets a number instead.
#### `<objectname> : bad arguments for message <message>`
The object received a message that it understood, but with a bad argument. For example, trying to set the name of a buffer~ object to be a number will display this error message, because the name of a buffer~ cannot be a number.
#### `<objectname> : doesn't understand <message-selector>`
The object received a message, but it doesn't understand that message. This often occurs when sending a symbol to a number box, when meaning to send an interger or float.
#### `<objectname> : message too long <message>`
A message was sent that contained more elements than the object can handle.
#### `<objectname> : extra arguments for message <message-selector>`
The object received a message that it understands, with valid arguments, but it received more arguments than it expected. This will display as a warning, not an error, since the extra arguments are simply ignored.
#### `<objectname> : missing arguments for message <message>`
The object received a message that it understands, but missing some arguments to that message. When a buffer~ receives the`set`message, without any arguments, it will display this message, because buffer~ expects an argument to the message`set`.
#### `<objectname> : No such object`
Max cannot find an object with the given name. Whether you're trying to load an Abstraction or an External , make sure that the relevant file is in Max's Search Path . If you're opening a patch and you see this error, the author may have forgotten to include an abstraction or external that the patch depends on. It may also be that you need to install a Package from the Package Manager that includes the missing dependencies.
#### `can't connect <objectname> to <objectname>`
Advisory message produced when you try to connect an outlet to an inlet that doesn't understand the message sent by the outlet. Typically you'll only see this message when opening a saved patcher, if for some reason an object doesn't load as expected.
#### `No help available for <objectname>`
A help file could not be located for the given object. Make sure that the help file (with the format`<objectname>.maxhelp`) is in the Search Path .
#### `patcher connect: inlet <number> out of range`
Occurs when editing the name or arguments of an object that has already been created in a patcher, and patch cords that used to be connected to the object can no longer be connected. Very often this occurs when changing the number of inlets or outlets of an object like gate or route , while that object is created.
### Audio
#### `ad_mme: <message>`
(Windows only) Please check that you have the latest driver update for your audio device. Please exit all other audio applications, reboot if necessary, and try again. Also, please check your settings in the Audio Status window to insure appropriate choices are selected for Input Device, Output Device, Sampling Rate, IO Vector Size, and Signal Vector Size. If the problem persists, contact Cycling '74 support.
#### `ad_directsound: <message>`
(Windows only) Please check that you have the latest driver update for your audio device. Please exit all other audio applications, reboot if necessary, and try again. Also, please check your settings in the Audio Status window to insure appropriate choices are selected for Input Device, Output Device, Sampling Rate, IO Vector Size, and Signal Vector Size. If the problem persists, contact Cycling '74 support.
#### `ASIOCreateBuffers error`
(Windows only) A problem was encountered initializing the ASIO device. Please check that you have the latest driver update from your audio device manufacturer. Please also try different settings for the device buffer sizes and latency in the control panel for your audio device provided by your device manufacturer. Check that another audio application is not using the audio device. Also check that the audio device is not the default audio device for Windows System Sounds.
#### `midi_mme: <message>`
(Windows only) Max was unable to open the MIDI input or output device. Please exit from all other MIDI applications and try again.
#### `MSP/ASIO: <message>`
(Windows only) A problem was encountered initializing the ASIO device. Please check that you have the latest driver update from your audio device manufacturer. Please also try different settings for the device buffer sizes and latency in the control panel for your audio device provided by your device manufacturer. Check that another audio application is not using the audio device. Also check that the audio device is not the default audio device for Windows System Sounds
