---
title: "OSC"
source: https://docs.cycling74.com/userguide/OSC/
source_path: /userguide/OSC/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# OSC

Source: https://docs.cycling74.com/userguide/OSC/

## Extracted Text

# OpenSoundControl
With OpenSoundControl (OSC) support, Max can be controlled by any OSC-compatible device or application, and can also send OSC messages to control other OSC-enabled systems.
OSC can be enabled in Max in two ways:
- Through the built-in UDP server, which you can activate for the whole application in Max's preferences , or for a specific patcher using the patcher inspector .
- By using the param.osc object.
Once enabled, parameters are automatically given OSC addresses , which have the following structure:
`/<patcher name>/param/<parameter name>/<attribute name>`
The different components that make up the address are configurable globally and locally in each patcher. Using these addresses, you can get and set the values of the following parameter attributes:
Parameter attribute OSC address Description
Raw Value`/raw`The raw (scaled) value of the parameter. This address container is optional if the raw value is the only value present in the OSC bundle. See the OSC Value Mode attribute.
Normalized Value`/normalized`The normalized (`[0,1]`) value of the parameter. This address container is optional if the raw value is the only value present in the OSC bundle. See the OSC Value Mode attribute.
## osc.codebox
osc.codebox can be used to display the contents of an OSC packet using JSON syntax. It's worth mentioning that OSC is a binary format--it has no human-readable form. The use of JSON syntax to represent OSC should be considered an approximation of the underlying binary data.
## OSCQuery
OSCQuery is a method of describing the capabilities of an OSC server. An http server can be configured to serve OSCQuery requests in Max by enabling OSCQuery in the general preferences.
Once enabled, an OSCQuery request can be generated with a URL like`http://localhost:30339`. All patchers with parameters exposed as OSC will be present in the OSCQuery response. Individual patchers can be excluded from the OSCQuery response using the option in the patcher inspector.
## The`FullPacket`Message
Objects that accept and produce OSC do so using a message called`FullPacket`. This message is passed with two arguments, and should be considered opaque, i.e. these arguments are not to be manipulated as normal max values.
An important property of the FullPacket message is that it is transient and must not be stored in objects like the message box, zl.reg, etc.
