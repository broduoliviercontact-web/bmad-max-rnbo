---
title: "Snippets"
source: https://docs.cycling74.com/userguide/snippets/
source_path: /userguide/snippets/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Snippets

Source: https://docs.cycling74.com/userguide/snippets/

## Extracted Text

# Snippets
A Snippet is a small group of objects, saved in a special format for easy reuse. You can create snippets from parts of a patcher that you find yourself using often, saving you the trouble of having to recreate the objects and connections from scratch.
A snippet for a basic video display patch.
## Creating Snippets
Select the objects you'd like to include in a snippet. Click the Save Snippet button in the bottom toolbar.
## Using Snippets
A dialog will appear, letting you name your snippet. Once you've saved your new snippet, you'll be able to add it to any patcher either using the contextual menu or using the left sidebar .
## Adding Snippets to a Patcher
### Via the contextual menu
Right- or control-click an unlocked patcher where you'd like to paste your snippet. A contextual menu will appear. Select`Paste From > User Snippets`then choose the desired snippet from the submenu.
The`Paste From`menu also lets you quickly add patchers and snippets from installed packages.
### Via the left sidebar
Click on the Snippets tab in the left sidebar to open the Snippets browser.
Click to open the Snippets browser
The Snippets Browser lets you browse snippets my name or by preview image. When viewing snippets by name, use the left column to filter by package . When viewing by preview image, use the pop-up menu to filter by package. To filter snippets by name, use the filter text entry field at the top of the browser.
To add a snippet to your patcher, just drag it from the browser and drop it into an unlocked patcher.
## Snippet Location
Snippets are saved in the Snippets folder inside the Max 9 folder. Snippet files have the`.maxsnip`extension. They are`.maxpat`format files that include a preview image.
You can add regular Max patcher files to the Snippets folder as well. This will add that patcher to the`Paste From`section of the context menu.
## Using Snippets with Packages
Packages can include snippets as well. If you're authoring a package, either for your own use or for distribution through the Package Manager , you can add snippets to your package. Create a folder called`Snippets`inside your package folder, and put whatever`.maxsnip`and`.maxpat`files you like into that folder.
