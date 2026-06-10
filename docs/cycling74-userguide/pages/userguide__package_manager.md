---
title: "Package Manager"
source: https://docs.cycling74.com/userguide/package_manager/
source_path: /userguide/package_manager/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Package Manager

Source: https://docs.cycling74.com/userguide/package_manager/

## Extracted Text

# Package Manager
The Package Manager provides instant access to a regularly updated, curated selection of Max add-on content and tools. The Package Manager allows you to manage which Packages are currently installed in Max. From the package manager you can install new packages, enable/disable existing packages, update or downgrade installed packages, and launch the default patcher for a given pacakge.
To access the Package Manager, select Show Package Manager from the File menu.
## Browsing and Installing Packages
By default, the package manager opens in the Browse Remote Packages view. letting you browse through packages that you do not currently have installed. You can instead view the list of currently installed packages by selecting Installed Packages from the drop-down menu at the top of the window.
Click on a package to inspect its details. This will show you information such as system requirements, a description of the package, and a link to the package author’s website.
To install a package, click the blue Install button. Once a package is installed, click the Launch button (if available) to view the Launch Patcher for the package. The Show in Filebrowser button will open the package in the File Browser , letting you see all the files included in the package.
## Managing Installed Packages
At the top of the package manager window, click the drop-down menu and select "Installed Packages". This will list all installed packages, including both those you installed through the package manager, as well as those you might have added by dropping them in the Packages folder.
To disable a package without deleting it entirely, click the Disable button after selecting the package. Max will ignore any files in a disabled package, but the package will remain downloaded and installed.
Many packages, including any packages that contain externals , will require a restart of Max before changes take effect.
You can remove a package entirely by clicking the red Uninstall button.
## Package Install Location
All packages are installed in your User Packages Folder , located at`%HOMEDRIVE%%HOMEPATH%\Documents\Max 9\Packages`on Windows, and at`~/Users/Max 9/Packages`on macOS. You can install packages that aren't available in the package manager, including your own custom packages, by dropping them in this directory.
Note that if you install a package that is itself available on the Package Manager by dropping them in this directory, the Package Manager will warn of a conflict. We recommend installing a package via the Package Manager if available in order to stay informed of updates to that package.
Don't change the folder names for any packages installed using the package manager.
## Package Updates and Versions
The Package Update icon in the bottom-right of the package manager window will highlight if there are updates available for any installed packages.
Click on the Package Update icon to show all packages with an available update.
You can change the installed version of any package by clicking "Show All Available Versions" in the package detail view. If you have a self-installed Package that conflicts with a Package available in our online library, you will have the option to overwrite it with our version or ignore it and leave it unchanged.
The Package Manager itself is automatically updated with each version of Max. Occationally, you may be prompted to update the Package Manager when you open the window if an update is available.
