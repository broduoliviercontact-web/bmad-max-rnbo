---
title: "New in Max"
source: https://docs.cycling74.com/userguide/new_in_max9/
source_path: /userguide/new_in_max9/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# New in Max

Source: https://docs.cycling74.com/userguide/new_in_max9/

## Extracted Text

# What's New in Max 9
## Jitter
-
Jitter Geometry — A specialized group of Jitter objects designed to work with Half-edge Geometry Structures . This makes geometry manipulations like redistributing and adding vertices much more efficient.
-
jit.fx - Tons of Jitter effects packaged as`jit.fx`objects, giving you access to effects, compositing, transitions, and analysis shaders. Each one has a help file and reference page.
- jit.ui — New Jitter UI objects for building interfaces and "heads-up displays".
## Audio
-
ABL Objects — These objects offer a patchable interface to the internal workings of some of Ableton Live Suite's most popular devices.
-
loudness~ — Reports the loudness of a signal according to the EBU R 128 standard
-
jweb~ — Load a web browser inside a patcher, capture its audio, and route the audio output into Max.
-
Global Record — Record the output of a patcher with a single click, from the patcher toolbar.
## JavaScript and Coding
-
JavaScript V8 — Modern JavaScript engine, supporting JavaScript classes, the spread operator, destructuring assignment, typed arrays, and much more.
-
Codebox — top-level codebox objects like v8.codebox for JavaScript and node.codebox for node.script .
-
REPL — Read-evaluate-print-loop interface for controlling Max using text entry
## Patching Enhancements
-
Patcher List View — See all the objects in your patch in a hierarchical list.
-
Illustration Mode — Understand how your patcher works by running it in slow motion.
-
New Preferences Window — Updated, tabbed UI for Max preferences
-
Syntax Coloring — Increased readability for object boxes with colored text for object names, arguments, attributes, and attribute arguments.
-
New Documentation — Documentation rewritten and modernized.
## User Interaction and Interface Tools
-
Integrated OSC — Controll Max with any OSC-compatible device or application, and send OSC messages to control other OSC-enabled systems.
-
hid — Modern human interface device input object
-
Param Connect — Connect parameter-enabled UI objects to supported objects without patch cords
-
poly~ param Object — Named parameters in poly~ subpatchers
-
Preset Interpolation — Blend between presets floats or the nodes object
