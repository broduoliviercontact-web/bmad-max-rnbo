---
title: "Documentation Window"
source: https://docs.cycling74.com/userguide/documentation_window/
source_path: /userguide/documentation_window/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Documentation Window

Source: https://docs.cycling74.com/userguide/documentation_window/

## Extracted Text

# Documentation Window
The documentation window gives you combined access to core parts of Max's documentation.
- User Guide : Full-page explanation of Max, its systems, and how to work with them.
- Object Reference : Detailed descriptions of individual objects, including all the messages and attributes that each object understands
- Package Documentation : Guides specific to a particular package, written by the package author
In addition to this, each object also has its own help file , which demonstrates the object's functionality in the context of a working patcher. And there is even more documentation online. The JavaScript API is one example of API documentation, listing all of the functions and classes you can use to extend Max with JavaScript. Finally, you can find examples and tutorials online as well, which introduce concepts gradually and show some of what's possible with Max.
## Using the Documentation Window
Open the documentation window by selecting User Guide from the Help menu. This will open the documentation window, focusing on the User Guide.
As mentioned earlier, the in-app documentation is divided into three main sections: the User Guide, Object Reference, and Package Documentation. You can navigate through the different parts of the documentation window using the icons at the top of the window.
- Back : Navigates to the previously visited page
- Forward : After navigating back, returns to the original page
- Documentation Home : Go to the documentation home page
- History : Click to display a list of recently visited pages
- User Guide : Show the User Guide
- Object Reference : List and search the available Max objects
- Package Documentation : Show documentation for installed packages
- Search : Open the search view
- Open Online Version : Open the documentation online
The left side of the documentation window shows the navigation for the current documentation area. In the User Guide, this lists user guide pages organized by topic. You can click the Hide Navigation icon to toggle the navigation display.
The Navigation icon lets you hide and show the navigation.
The navigation lets you jump from page to page, but you can also quickly jump through the contents of a particular page by using the in-page navigation. If you make the documentation window wider, the On this Page navigation will appear.
The page navigation appears when the documentation window is wide enough
## Using the Object Reference
Click the Reference icon to display the object reference list.
On the left side of the page, you'll see the object reference navigation, which groups objects by built-in section for native objects, and by package name for objects from third-party package . Click on any entry in the navigation to list objects from that section.
On the right side of the page, above the object listing, you can use the drop down menu to further refine the list of objects by category. For example, in the Gen section, you can select the buffer category from the drop down to see only Gen objects that deal with buffer objects.
Click on an object to view the reference documentation for a specific object. Use the Open Help button at the top of the object reference page to open the help patcher for that object. Under that button, you'll see extensive reference for the object, including the arguments, attributes, and messages that the object understands.
The reference documentation for the pattr object
Next to the entry for every attribute, argument, and message, you'll see the expected type for that entry. For arguments, you'll also see the keyword optional appear if the value is optional, as well as any default value the argument may have.
If you make the documentation window wide enough, you'll see On this Page navigation, including a disclosure triangle to list arguments, attributes, and messages.
On this Page navigation for the pattr object
## Using the Package Documentation
Click the Packages icon to display the package documentation.
On the left side of the page, you'll see a list of installed packages. If the package authors have written any Guides, Topics, or Tutorials, you'll see those appear in the center of the documentation window. Once you click on a particular entry, you'll see that entry appear.
At the top of a package documentation page, you'll see breadcrumbs showing you the path to the current page. You can click Package Docs to return to the package documentation home page, or on the name of the page to see just the documentation for that package.
## Searching the Documentation
Click the Search icon in the top-right of the window to display the search view.
When you search, you'll see results from the User Guide, Object Reference, and Package Docs, but you'll also see results from online as well, including API Reference and RNBO results. If there are more than a few results in a given category, click More Results to view a page of results from just that category.
Documentation search results with the search term 'matrix'
