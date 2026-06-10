---
title: "Conversion Cheat Sheet"
source: https://docs.cycling74.com/userguide/conversion/
source_path: /userguide/conversion/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Conversion Cheat Sheet

Source: https://docs.cycling74.com/userguide/conversion/

## Extracted Text

# Conversion Cheat Sheet
## Message to Audio
Copy
Convert a message to a signal without any smoothing Copy
Convert a message to a signal with linear smoothing Copy
Convert a message to a signal with logarithmic smoothing
## Audio to Message
Copy
Convert audio to a stream of messages Copy
Analyze an audio stream for peaks, average, or RMS
## Signal to Event
Copy
Signal to Event
## Unit Conversions
Copy
Samples to Milliseconds Copy
Frequency to MIDI Pitch Copy
Amplitude to Decibel Copy
Note Value to Millisecond
See Time Value Syntax for more details.
Copy
Tempo to Millisecond
This same patch will convert milliseconds to tempo (kinda cool huh?)
Copy
Linear to Quadratic
## Multichannel
Copy
Single channel to multichannel Copy
Multichannel to separate channels Copy
Multichannel to stereo mixdown
## List to buffer~
Copy
Fill using peek~ Copy
Fill using jit.buffer~
## buffer~ to List
Copy
Using peek~ and zl.group Copy
Using jit.buffer~ and jit.spill
## Audio to Matrix
Copy
Filling up a matrix Copy
Reading from a buffer Copy
Writing into a matrix
## Matrix to Audio
Copy
Scanning a matrix Copy
Read a video as an audio signal
## Matrix to Texture
Copy
Convert a matrix to a texture. It really is that simple.
## Texture to Matrix
Copy
Convert a texture to a matrix
## Matrix to Messages
Copy
Get cell values from a matrix as a list Copy
Read a specific cell from a matrix Copy
Get a representative number from a matrix Copy
Output the cells of a matrix one by one
## Message to Matrix
Copy
Fill up a matrix using a list Copy
Set a single cell in a matrix
## Matrix Upsampling/Downsampling
Copy
Downsample a matrix, no interpolation Copy
Upsample a matrix with interpolation
## Matrix Color Conversion
Copy
Red-Green-Blue to Hue-Saturation-Lightness Copy
Red-Green-Blue to Luminance Copy
More color space conversions
## Thread Priority Conversion
Copy
Move a high-priority message to the low priority queue Copy
Move a low-priority message to the high-priority scheduler
Note that this won't make the message get processed "sooner", but if you know what you're doing there may be situations where it's useful.
## Dictionaries
Copy
Convert a dictionary to a coll Copy
Convert a coll to a dictionary Copy
Add an array to a dictionary
## Number Formats
Copy
Decimal to Hex Copy
Hex to Decimal Copy
Decimal to Binary Copy
Binary to Decimal
## String to Array
Copy
String to Array
## Array to String
Copy
Array to String
## buffer~ to Array
Copy
buffer~ to Array
## Array to buffer~
Copy
Array to buffer~ using array.tobuffer
## Array to buffer~ (multiple channels)
Copy
Each nested array is its own channel
