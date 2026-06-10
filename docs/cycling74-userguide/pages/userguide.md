---
title: "Overview"
source: https://docs.cycling74.com/userguide/
source_path: /userguide/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Overview

Source: https://docs.cycling74.com/userguide/

## Extracted Text

# User Guide
Welcome to the Max user guide. This guide covers everything to do with how Max works, including the fundamentals of objects, messages, and patchers; the different parts of the Max interface; and how to do things like process sound and work with graphics.
If you're new to Max, you might find it useful to read how to use this documentation
This documentation is also available in PDF format , for viewing offine.
## New in Max 9
If you're a long-time Max user and you want to see what's new in Max 9, check out this overview .
## Demos
If you want to see some of what you can do with Max, check out these demos:
Name Description
JavaScript Codebox Mix textual and visual programming with inline codebox supporting modern JavaScript
Jitter Geometry Half-edge structures for shapes that you can morph and distort
Ableton DSP Use Ableton DSP algorithms for synthesis, modulation, and effects
## Tutorials
These tutorials can guide you through working with Max step-by-step.
- Working with Max - The basics of working with Max, including setting up timers and events, building a user interface, handling input from the webcam, and generating sound.
- Signal Processing - How to generate and manipulate audio signals, extacting automation from real-time audio signals, and working with samples.
- Video Processing - Setting up a graphics environment, making dynamic visualizations, and generating audio-reactive effects.
- Jitter Geometry - Using the jit.geom objects, introduced in Max 9, to manipulate dynamic geometry using the half-edge structure.
If you want to get inspired with even more Max examples, check out our Examples Gallery
## API Reference
Max exposes several APIs—Application Programming Interfaces—that let you use code to control various systems in Max. You can write short scripts to automate simple tasks, or large programs that completely change the way Max behaves. Some of the APIs that Max offers:
- JavaScript API : Use the v8 , v8ui and v8.codebox to embed JavaScript in a Max patch. Define custom objects, programmatically create objects and patch cords, and operate the Max application.
- Live Object Model : Use Max objects like live.object and live.path to read and modify the state of Ableton Live from within a Max for Live device. Also accessible from the JavaScript API.
- Node for Max : Use the node.script and node.debug objects to launch custom Node.js scripts from Max. Send Max messages to a running Node process and fetch a result.
