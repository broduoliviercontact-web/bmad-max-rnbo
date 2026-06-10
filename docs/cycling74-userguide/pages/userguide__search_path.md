---
title: "Search Path"
source: https://docs.cycling74.com/userguide/search_path/
source_path: /userguide/search_path/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Search Path

Source: https://docs.cycling74.com/userguide/search_path/

## Extracted Text

# Search Path
The Search Path is a collection of folders that Max looks through whenever it needs to find a file. It lets you reference files based on just their name, rather than their absolute path. To locate a file, Max looks in the following places, in order:
- The folder containing the currently open patch
- The project to which the current patcher belongs, if any
- The Max 9 Folder , including built-in patches and media, installed Projects , and others
- The folders in the current search path, in order
The File Browser lets you search, organize, and filter files in the current search path.
## Editing the Search Path
Edit the search path by selecting File Preferences... from the Options Menu. This will open the File Preferences window.
The paths to the folders for User Library , Global Library , Examples , and Snapshots are managed by Max and cannot be modified. If you want Max to search other folders when looking for files, you can add your own folders using this window.
Select any path and click the Reveal in Finder buttom in the bottom toolbar to open that folder in Finder or File Explorer .
### Adding a file to the search path
Click on the Add Path button in the bottom-left of the window. This will add a new, empty row to the search path list. Click the Choose button to open a dialog box that lets you browse for the folder you'd like to add to the search path. You can also name your path by double-clicking on the Name field. If you'd like to include subfolders as well, check the Subfolders box.
### Removing a file from the search path
Select any path and click the Remove Path button in the bottom toolbar to remove it from the search path.
### Listing all folders in the search path
You can click the List Path button in the bottom toolbar to list all of the folders currently in the search path. This includes subfolders and can include a lot of folders.
## Max 9 Folder
Max adds a folder to the Documents directory called`Max 9`, containing files of different kinds that get added to Max as you work with it. This folder is located at`%HOMEDRIVE%%HOMEPATH%\Documents\Max 9`on Windows and`~/Documents/Max 9`on other operating systems.
The Library and Snapshots folders are automatically added to the search path. Folders in the Paackages folder are also added, as each package is loaded.
- Collections - Collections that you make using the File Browser get stored here
- Library - This folder is for your use. Whatever files you put in this folder will be included in Max's search path.
- Packages - Packages instlaled by the Package Manager get installed here.
- Palettes - Palettes that you create using the Color Picker get stored here.
- Projects - This is the default location to save projects . Max will also unpack amxd s here.
- Prototypes - Any saved Prototypes will be stored here.
- Recordings - The default directory for audio Recordings .
- Snapshots - New Snapshots get saved here.
- Snippets - When you create a Snippet , it gets stored here.
- Styles - New Styles get saved here.
- Templates - Saved Templates go to this directory.
## Path Objects
Several objects facilitate working with Max's search path:
Name Description
absolutepath Convert a file name to an absolute path
conformpath Convert file path styles
filepath Manage and report on the Max search path
relativepath Convert an absolute to a relative path
strippath Separate filename from a full pathname
### Path Prefixes
When resolving a file path, Max can use special path prefixes to locate files relative to a known location. For example, you could use the path`Patcher:/sources/my_patcher.maxpat`to locate a patcher relative to the current patcher, even if the patcher`my_patcher.maxpat`is not in the current search path . This works for all objects that can load files. The absolutepath and conformpath objects can be used to illustrate where Max is resolving these relative paths on disk.
Prefix Description Example
~: path relative to the user's home folder`~:/sources/my_patcher.maxpat`
C74: path relative to the Cycling '74 resources folder (on macOS, this is inside the application bundle`Max.app/Contents/Resources/C74/`, on Windows, this is the resources folder next to the`Max.exe`executable)`C74:/sources/my_patcher.maxpat`
C74_AU Max-specific plugin directory for AudioUnit plugins. Mostly used with the`plug`message to vst~ to disambiguate plugin types. `C74_AU:/MyPluginName
C74_VST Max-specific plugin directory for VST plugins. Mostly used with the`plug`message to vst~ to disambiguate plugin types. `C74_VST:/MyPluginName
C74_VST3 Max-specific plugin directory for VST3 plugins. Mostly used with the`plug`message to vst~ to disambiguate plugin types. `C74_VST3:/MyPluginName
Usermax: path relative to the Max 9 folder in the user's Documents folder`Usermax:/sources/my_patcher.maxpat`
Desktop: path relative to the user's Desktop folder`Desktop:/sources/my_patcher.maxpat`
Tempfolder: path relative to Max's temp folder (this folder will be automatically emptied when Max quits)`Tempfolder:/sources/my_patcher.maxpat`
Package: path relative to the package specified in package-name`Package:/miraweb/misc/app.js`
Project: path relative to the project (if any) containing the file loading object`Project:/sources/my_patcher.maxpat`
Patcher: path relative to the patcher (if any) containing the file loading object`Patcher:/sources/my_patcher.maxpat`
## Projects
Projects collect and organize dependencies. All files in a given project will be able to locate other files in the same project. In addition, projects support Project Search Paths , which are extra search path folders specified by that project. For more details, see the documentation for Projects .
Max for Live devices are just projects, and follow the same rules as projects when locating files using the search path.
## Standalones
Search paths in standalones work more or less the same as in regular Max, with a couple of small differences. Check out the documentation for Standalones for more details.
