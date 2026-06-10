---
title: "Syntax Coloring"
source: https://docs.cycling74.com/userguide/syntax_coloring/
source_path: /userguide/syntax_coloring/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Syntax Coloring

Source: https://docs.cycling74.com/userguide/syntax_coloring/

## Extracted Text

# Syntax Coloring
Syntax Coloring uses different colors for a word or number based on the type of token it is in a programming or data description language. Most modern text editors used for programming feature syntax coloring and Max is no exception. The standard text window will adjust text colors based on the theme and file type. Here are some examples:
JavaScript in the **default** theme
Dictionary Editor in the midlight-ash theme
## Enabling Object Box Syntax Coloring
To apply syntax coloring to the text in object boxes in a patcher, enable Syntax Coloring in the Color and Theme tab of the Preferences window.
This applies the current theme's syntax colors to object box text.
In the above example, four colors are used to color the text of object boxes.
- the first word in the object box is the object name
- words starting with @ are attribute names
- words or numbers after the object name but before the typed-in attributes are object arguments
- words or numbers after the object name but before the typed-in attributes are attribute arguments
## Customizing Object Box Syntax Colors
You can override object box syntax colors set by themes in two ways:
- Select a Syntax Color Theme other than Theme Default in the Color and Theme tab of the Preferences window.
The various themes in the menu will not be equally legible with all themes, but they may work better for you than the default theme colors. Here's the olivia Syntax Color Theme used with the default Color Theme.
Note that Syntax Color Themes typically change only the four object box text colors, not the text editing window colors.
- On a per-patcher basis, you can edit the four object box syntax colors in the Format Palette for the patcher. With no objects in the patcher selected, show the Format Palette and click the P icon at the far left.
The Format Palette shows the default object, background, and text colors for the patcher. You'll want to locate the four A icons to the edit the syntax colors, Syntax Attribute Argument Color, Syntax Attribute Name Color, Syntax Object Argument Color, and Syntax Object Name Color.
It's helpful to edit these colors with object boxes showing the various syntax elements in the patcher visible.
Once changed, the customized colors will apply to all object boxes in a patcher (but not its subpatchers). To apply your customized colors more easily to new patchers, you can save the patcher as a template .
To apply the syntax colors to existing patchers, define a patcher-level style . Choose Define New Style from the Style menu in the Format Palette when editing the patcher fonts and colors.
