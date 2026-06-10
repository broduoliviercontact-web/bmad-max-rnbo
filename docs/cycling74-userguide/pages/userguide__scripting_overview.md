---
title: "Scripting Overview"
source: https://docs.cycling74.com/userguide/scripting_overview/
source_path: /userguide/scripting_overview/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Scripting Overview

Source: https://docs.cycling74.com/userguide/scripting_overview/

## Extracted Text

# Scripting
Max provides several mechanisms for Scripting the behavior of a patcher. Through scripting, you can accomplish many of the same things that you would normally do using the mouse and keyboard, but through an automated or programmatic mechanism. Some examples of things you could do with scripting:
- Create, delete, and connect objects
- Open and close patcher files
- Customize the appearance of UI objects
- Walk up and down the patcher hierarchy
## Identifying Objects with Scripting Name
All Max objects have an attribute called`@varname`, also known as the Scripting Name of the object. This is the name by which the object can be uniquely identified within a patcher, and so no two objects in a patcher can share a scripting name. The scripting name is usually optional, but some objects require a scripting name. For example, any object with Parameter Mode enabled, including all`live.*`UI objects, must have a scripting name.
You can use the thispatcher object to send messages to an object using its scripting name.
Using JavaScript, you can also get a reference to an object using its scripting name.
`function find_object ( name ) { let obj = this . patcher . getnamed (name); if (obj) { post ( `Found an object named ${name} \n`); } else { post ( `No object with name ${name} \n`); } }`
## thispatcher
The thispatcher object is the object-level interface to Max's scripting capabilities. The help file for thispatcher provides an overview of its capabilities.
## JavaScript
The v8 and v8ui objects let you embed JavaScript code directly in your patcher. In addition to all of the functionality of the JavaScript engine itself, you can also call on the Max JavaScript API to interact with the Max application. See JavaScript for more.
## Messages to Max
Finally, you can send messages directly to the Max application itself (or to global resources that the Max application owns, like the audio engine). This uses a special syntax with a semicolon`;`at the beginning of a message. See Controlling Max with Messages for more information, including a list of all available messages.
