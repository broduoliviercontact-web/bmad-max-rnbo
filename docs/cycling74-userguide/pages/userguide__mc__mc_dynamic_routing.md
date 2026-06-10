---
title: "MC Dynamic Routing"
source: https://docs.cycling74.com/userguide/mc/mc_dynamic_routing/
source_path: /userguide/mc/mc_dynamic_routing/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC Dynamic Routing

Source: https://docs.cycling74.com/userguide/mc/mc_dynamic_routing/

## Extracted Text

# MC Dynamic Routing
There are two basic methods of dynamic routing for multi-channel signals:
-
Use mc.send~ and mc.receive~ to send multiple channels of audio between patchers
-
Use mc.matrix~ , mcs.matrix~ , mc.selector~ , and mc.gate~ to control routing of multichannel signals using Max messages
## Sending Multi-Channel Audio Between Patchers
mc.send~ and mc.receive~ are multi-channel versions of send~ and receive~ . An important limitation when using these multichannel versions is that you must expicitly define the number of channels you will be communicating between the objects via a typed-in argument that follows the receive name. The mc.receive~ cannot change its number of channels dynamically.
Any mc.send~ objects with a matching name can send up to the defined number of channels in the mc.receive~ . Extra channels in a multi-channel signal connected to mc.send~ are ignored. If you supply too few channels to mc.send~ , mc.receive~ will output these channels as zero signals. In other words, mc.receive~ always produces a multi-channel signal with a set number of channels regardless of what you send it via mc.send~ .
## Dynamic Routing Using mc.send~ and mc.receive~
Like send~ and receive~ , the mc.send~ and mc.receive~ objects accept the`set`message to change the source or destination name they use to communicate. However, the fixed channel limitation of mc.receive~ is tied to the object instance, not the symbol used for the destination name. Here is an example using the`set`message to mc.receive~ . To start, the mc.receive~ uses the name`foo`and is communicating with the four-channel mc.send~ with name`foo`.
If we send`set bar`to the mc.receive~ , the output is still four channels despite the fact that mc.send~ with name`bar`is only sending two channels.
## Dynamic Multi-Channel Routing Using Max Messages
The mc.gate~ and mc.selector~ use the MC Wrapper and work similarly to their single-channel counterparts. The number or signal at the left inlet switches all channels of the multi-channel signal in the other inlets ( mc.selector~ ) or outlets ( mc.gate~ ).
The behavior of the two multichannel variants of the matrix~ warrants a more detailed explanation. The mc.matrix~ consists of multiple matrix~ objects in the MC Wrapper. However, because each matrix~ can be individually targeted, channels within a multichannel input can be routed to different multichannel outputs. In this example, there is an mc.matrix~ with one multichannel input and two multichannel outputs. By sending the message`0 0 1`(which goes to all matrix~ instances in the wrapper), we assign the inputs to the left outlet. The right outlet produces a multi-channel signal with zero in all channels.
Using the wrapper's`setvalue`message to mc.matrix~ , we can assign only the third channel of the input multi-channel signal to the right outlet using the message`setvalue 3 0 1 1`.
The matrix~ object numbers its channels starting at 0 whereas mc.target and the MC Wrapper`setvalue`message start channel numbering at 1. The special wrapper`setvalue`target of 0 before a message will address all instances inside a wrapped object, which is the same thing as sending the message without using`setvalue`.
The mcs.matrix~ object is a single matrix~ object where all the signal inputs are combined into one multichannel input and all the signal outputs are combined into one multichannel output. To duplicate the above example with mc.matrix~ in mcs.matrix~ , first observe that there are four total inputs and eight total outputs, despite the arguments`1 2`to mc.matrix~ . To match this, we need an mcs.matrix~ with arguments`4 8`:
Since mcs.matrix~ provides only one multichannel output, we need to use an mc.separate to split its eight-channel multichannel signal into two four-channel multichannel signals. To route the third channel of the input in the same way, we send the message`2 6 1`(remember matrix~ channels are zero-relative):
Generally, you'll prefer mc.matrix when you want to route multichannel signals as a whole to different patch cords. This can be achived in one message with the mc.matrix example:
By contrast, mcs.matrix~ is an effective way to manipulate channels within a multichannel signal. For example, sending the messages`0 7 1, 1 6 1, 2 5 1, 3 4 1, 4 3 1, 5 2 1, 6 1 1, 7 0 1`in this mcs.matrix~ reverses the order of the eight input channels.
