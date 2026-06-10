---
title: "Using Symbols in Max for Live"
source: https://docs.cycling74.com/userguide/m4l/live_symbols/
source_path: /userguide/m4l/live_symbols/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Using Symbols in Max for Live

Source: https://docs.cycling74.com/userguide/m4l/live_symbols/

## Extracted Text

# Using Symbols in Max for Live
The "name space" in Max is global - when you have objects that have names associated with them such as coll , send , receive , table , or buffer~ , you can share data between Max for Live devices. In these cases, the Max name space is shared, but the "signal processing space" is independent - each Max for Live device processes its audio or data separately.
## Defining a unique symbol name
If you want a named object to be unique to a device, use three dashes ( --- ) to start the name of your buffer~ or send / receive destination (e.g.`s ---filtercutoff`).
When your patch is initialized, it will replace the three dashes with a unique-to-Live number (e.g.`s 024filtercutoff`);
