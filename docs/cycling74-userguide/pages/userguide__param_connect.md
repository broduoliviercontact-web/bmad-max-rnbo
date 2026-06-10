---
title: "Parameter Connect"
source: https://docs.cycling74.com/userguide/param_connect/
source_path: /userguide/param_connect/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Parameter Connect

Source: https://docs.cycling74.com/userguide/param_connect/

## Extracted Text

# Connecting Parameters
You can include an object called param in Gen and RNBO that declares a parameter . Gen and rnbo~ parameters can be changed as attributes of the object. If you wanted to link a live.dial to control a gen~ parameter you would have to do the following:
- copy the Gen parameter's min, max and default to the live.dial 's`parameter_range`,`parameter_inital`, and`parameter_initial_enable`.
- use getattr to listen to the value of the Gen parameter, then patch the live.dial to gen~ and getattr using a`set`message to avoid creating a feedback loop and another message box to prepend the attribute name to the value of the dial
Note that you have to copy this patching for every parameter you want to control.
The`param_connect`attribute of many Max UI objects (including live.dial ) provides a way to handle all of this with one step, as demonstrated below. In this example, we will connect a live.dial to a parameter inside gen~ called`xyz`.
Once this connection is established, the live.dial will control the`xyz`parameter inside gen~ and if the`xyz`parameter's value changes in Gen, the live.dial will update to reflect the new value. Furthermore, because the Gen parameter is linked to a live.dial , it can be automated in a Max for Live device or used to for state management in pattrstorage or preset .
## Supplier Objects
The list of suppliers —objects that define parameters connectable to UI objects via`param_connect`will continue to expand over time. It currently includes:
- Gen ( gen~ , gen , jit.gen , jit.gl.pix , and jit.pix as well as all the Gen codebox variants such as gen.codebox~ ).
- RNBO ( rnbo~ )
- The ABL objects
- v8 with attributes defined via scripts that call`declareattribute`
- poly~ objects that contain subpatchers with param objects. For more information, refer to Polyphony .
- jit.gl.slab (shader parameters)
Not all supplier objects will support every`param_connect`feature but all provide for bidirectional control.
## UI Objects
To verify if a UI object can be connected to a parameter, look in the Behavior category in the Inspector . If the object is compatible, you'll see a Connect to Parameter attribute:
Generally, any UI object that is parameter-aware —in other words, an object with`parameter_enable`attribute—will be able to connect to a supplier object. While some UI objects such as multislider handle multiple values, only the first value will interact with a parameter of a supplier.
Some non-UI objects— pattr for example—are also parameter-aware but they cannot connect to parameters of supplier objects.
## Establishing Connections
Connections to parameters are always established with the UI object you want to use for control and display. There are three ways to establish a connection:
-
Use the Connect submenu of the Object Action Menu
-
Using the Inspector on the selected UI Object, choose the desired parameter from menu for the Connect to Parameter attribute
-
Send the message`param_connect <path ID>`to the UI object. To determine the path ID, combine the scripting name of the supplier object with the parameter name separated by double colons as follows:`gen~_AB::xyz`
To view the scripting name of an object, select the object and open the Inspector or choose Name... from the Object menu.
Note that while multiple UI objects can be connected to the same parameter, a UI object can only control a single parameter.
To disconnect a UI object from its parameter, choose None from the Connect submenu of the Object Action Menu .
## Visualizing Connections
To see the connected parameter for a UI object, hold down the Option / Alt key while the cursor is over the object. A line will connect the UI object and supplier as shown below:
You can also check the connection via the menu in Object Action Menu or Inspector . The menu shows a check mark next to the connected parameter name.
## Limitations
Connections between UI objects and supplier objects can only occur in the same patcher. If you put the supplier object in a subpatcher (for example, via encapsulation ), the connection will disappear.
Parameter connections are generally single-valued. Multi-valued parameter data and user interface objects are not yet fully supported.
