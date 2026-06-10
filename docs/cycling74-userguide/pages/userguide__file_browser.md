---
title: "File Browser"
source: https://docs.cycling74.com/userguide/file_browser/
source_path: /userguide/file_browser/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# File Browser

Source: https://docs.cycling74.com/userguide/file_browser/

## Extracted Text

# File Browser
The File Browser is a graphical interface to Max's Search Path , letting you view, search, and organize all the files that Max can access. It's helpful not only for finding your own files, but also for finding all of the content that comes with Max. You can also create Collections , which are like virtual folders that group together patchers and other media.
You can open the file browser from a Max patcher window by clicking the button in the left toolbar.
You can also select the Show File Browser option from the File menu.
## Browsing
From the navigation bar on the left of the File Browser window, you can view Recently Used items, Recently Added items.
You can also browse content by package, or browse all of the content that comes built-in with Max.
## Adding Files to the Search Path
At the bottom of the File Browser window, there's a button that you can use to add files to the search path and, by extension, the file browser.
Clicking this button will bring up a system dialog box that you can use to browse for files or folders to add to Max's search path. If you select a file, that file will be visible and searchable in the file browser. To remove that file from the search path, right-click on the file and select Remove from Search Path.
From the same dialog box you can also add a whole folder to Max's search path. Once you do, you can select File Preferences from the Options menu to view the path that you added. By default this will add that folder and all subfolders to the Max search path. You can remove the folder by selecting the folder and clicking the Remove Path button at the bottom of the File Preferences window.
## Advanced Search
When you open the File Browser for the first time, or when you click on the Question Mark button in the top-right of the window, you'll see a description of the advanced search syntax for the file browser. This lets you build search queries to narrow in on just the content you're looking for. For example, the search
`package:BLOCKS kind:audio`
will search only for audio files in the package BLOCKS . When you click on buttons in the left sidebar, you may notice that these change the contents of the search box. In fact, these buttons are just shortcuts to using the advanced search terms. Clicking on the Recently Used button is exactly the same as starting a search with`recent:true`. Clicking on a button in the left sidebar and then adding additional search terms is a convenient way to build up a complex search term.
## Bookmarks
If you want to save a search query for later, you can click on the Bookmark Search button in the top-right of the File Browser window, next to the search bar. This button creates a new Saved Search or Bookmark so you can easily find it again later. And once you've created a Saved Search, you can find it using the Saved Search button in the left sidebar.
## Collections
Collections group together patchers, media, and saved searches. In addition to helping you stay organized, anything that you add to a Collection will also be added to the Max search path. You can also access a Collection from the sidebar in any Max patcher, making them convenient for accessing files that you use frequently.
### Creating a Collection
Create a new Collection by clicking the Create New Collection button in the bottom-left of the File Browser window.
It's also possible to right-click on any file in the File Browser and select Add to Collection or Create Collection with selected file .
### Removing a Collection
To remove a collection, first open the collection in the File Browser. Then, click the Garbage Can icon in the top-right of the collection viewer.
