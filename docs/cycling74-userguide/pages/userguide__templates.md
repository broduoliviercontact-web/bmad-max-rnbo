---
title: "Templates"
source: https://docs.cycling74.com/userguide/templates/
source_path: /userguide/templates/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Templates

Source: https://docs.cycling74.com/userguide/templates/

## Extracted Text

# Templates
Templates are a starting point for a Max patcher. You can save any patcher as a template, and then rather than starting from a blank patcher, you can use your saved patcher as a starting point. Templates maintain patcher-level formatting including fonts and colors, so if you create a template with a patcher style , the style will be included in your template.
## Using Templates
Select New From Template from the File menu to see a list of saved templates, including built-in templates. Choose a template from the list and it will open in a new patcher window.
## Creating Templates
To create a template from a Max patcher, choose Create Template... from the File menu. A dialog box will appear that contains the name of a Max template file (the default filename will be based on the filename of the currently open Max patch).
The modal dialog asks for a name for the new template.
## Default Template
You can choose a template to be the default template for the whole Max application. Once you do, any new patcher that you create will be based on that template, rather than the typical empty patcher.
### Setting a new default template
When you save a new template, you can check the`Default for New Patchers`checkbox to make the saved template the new default.
If you want to make an existing template the default, set the Default Patcher Template preference in the Preferences window. See the Default Patcher Template section in the Preferences reference for details.
## Templates in Packages
If you're authoring a Package , whether for your own use, to share with your colleagues, or to publish to the Package Manager , you can include templates in that package as well. This can be really useful, for example as a way to demonstrate the functionality of your package.
To add a template to your package, create a folder called`templates`in your package folder. Any`.maxpat`files that you put in this folder will be available as templates. Once someone installs your package, they should see your custom templates listed in the dropdown whenever they choose`File > New From Template`.
