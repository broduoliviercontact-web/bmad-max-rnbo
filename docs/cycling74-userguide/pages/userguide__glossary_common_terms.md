---
title: "Glossary of Common Terms"
source: https://docs.cycling74.com/userguide/glossary_common_terms/
source_path: /userguide/glossary_common_terms/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Glossary of Common Terms

Source: https://docs.cycling74.com/userguide/glossary_common_terms/

## Extracted Text

# Glossary of Common Terminology
There are many terms used throughout the Max documentation that are unique to the application. Understanding what these terms refer to will help when learning the software. Below is a list of the most commonly used terms in Max, along with their respective definitions.
## #
-
# : The pound sign (#) is a special character that indicates a changeable argument specifically within an abstraction. Message boxes, object boxes, and some object attributes within an abstraction can be given a changeable argument by typing in a pound sign and a number (e.g. #1) as an argument. When the abstraction is used inside another patcher, an argument typed into the object box in the patcher replaces the # argument inside the abstraction. Using a zero with the pound sign (#0) at the beginning of a symbol argument (e.g., #0_value), transforms that argument into an identifier that is unique to each instance of an abstraction (and its subpatchers) when it is loaded.
-
$ : The dollar sign ($) is a special character that indicates a changeable argument in a message box or an object. If used in a message box, $ should be followed by a number in the range 1-9 (such as $2). That argument will then be replaced by the corresponding argument in the incoming message. If used in an expr , if , sxformat , or vexpr object, $ must be followed immediately by the letter i, f, or s, which indicates whether the argument is to be replaced by an int, a float, or a symbol.
-
--- : The three dash (---) identifier is used for coll , dict , and in the context of Max for Live. It serves as a way to create unique names for objects. In the context of Max for Live, if you want a named object to be unique to a device, use three dashes (---) to start the name of your buffer or send/receive destination.
## A
-
Abstraction : Any patch you have created and saved can be used as an object in another patch just by typing the filename of your patch into an object box as if it were an object name. Patches used in this way are called abstractions.
-
Argument : Many objects have arguments which set the initial state of an object. Arguments are typed into the object box after the object's name. All possible arguments for an object are listed in their respective Object Reference Pages .
-
Attribute : Many objects have attributes . An attribute is a setting or property that tells the object how to do its job. These can be set in a variety of ways which are outlined.
-
Attrui : An attrui is an object which displays attribute values of the object it is connected to. If you connect an attrui to another object via a patch cord, it will intelligently display all attributes for that object via a dropdown menu and show their corresponding values when selected.
## B
-
Bang : Bang is a type of message that tells the receiving object to do whatever it is designed to do. It basically tells an object to "Go!". More information on bang messages can be found here .
-
BEAP : The BEAP package is a collection of audio-processing modules that are automatically included with Max. Each module has a help file that explains its function.
## C
-
Changeable Argument : There are two special characters in Max that indicate changeable arguments:`#`and`$`. Please refer to their respective definitions for more information.
-
Collection : A collection is a kind of virtual file folder where you can store patchers, media, saved searches, and any other kind of Max resources you would like to group together for convenience.
-
Console : A window (Window > Max Console ) that displays status information, error messages, and warnings related to your patch.
-
Contextual Menu : A menu that appears when control-clicking (Mac) or right-clicking on the patcher background, an object, or a patch cord in an unlocked patch. This menu provides various options that are relevant to the overall patcher, the object selected, or the patch cord selected.
## D
-
Device : A device is a type of patch that is specifically designed to work within Ableton Live as an audio effect, MIDI effect, or instrument. Devices can also be used within Max. However, they are not compatible with other DAWs.
-
Dictionary : A dictionary is a collection of key-value pairs that can be passed between objects. Each key in the dictionary is a unique symbol. Each value may be a number, symbol, list, array, or another dictionary.
## E
-
Event : An event is the passing of a non-signal message between two objects.
-
External : A binary file that contains one or more Max objects.
## F
- Float : A floating-point number , a.k.a. a number with a decimal point.
## G
- Gen : Gen is an extension of the Max patching environment that converts what you build visually into efficient, compiled code as you go. Gen code can be used outside of Max with Code Export. Gen includes the gen~ and mc.gen~ objects for audio, and the jit.pix and jit.gen objects for matrix and texture processing.
## H
- Help File : Every object in Max has a help file . Help Files are interactive patches that demonstrate how an object works. To access an object's help file you can either right-click (ctrl+click) on the object in an unlocked patch and select "Open Help", or click the "Open Help" button from the object's reference page.
## I
-
Inlet : A "port" at the top of an object where information is sent via a patch cord. Information is passed from the outlet of one object to the inlet of another object. Each inlet can receive a certain type of information. Hover over an inlet with your mouse in an unlocked patch to see what type of information it can receive.
-
Inspector : There is both an Object Inspector and a Patcher Inspector. The Object Inspector is used to edit the attributes of Max objects. The Patcher Inspector is used to edit settings for a patcher window.
-
Integer : A whole number , a.k.a. a number without a decimal point.
## J
- Jitter : Jitter is the visual processing side of Max. All Jitter objects begin with "jit." For help getting started with Jitter, see this group of tutorials .
## L
-
List : A message with several numbers and/or symbols is called a list ; the list is a mechanism for keeping data together into a single message that can be sent via patchcords to other objects. There is no inherent structure to a list; lists are organized simply as one item after the other.
-
Live Object Model (LOM) : The LOM is used in conjunction with Ableton Live. It is essentially a roadmap to each of Live's parameters that are accessible via Max for Live. Using the LOM you can control everything in Live's API that is accessible to Max for Live.
-
Lock/Unlock : A patch can either be locked or unlocked . You unlock a patch to edit it and you lock a patch to perform with it and adjust UI objects.
## M
-
Matrix : A matrix is a grid with each location in the grid containing some information. This term is specifically used in the context of Jitter, the visual processing side of Max. In Jitter, a matrix can have any number of dimensions from 1 to 32.
-
Max : Max is the name of the application, but the word also stands for the data processing side of the software. For help getting started with Max-specific patching, see this list of tutorials .
-
Max for Live : Max for Live is a separate application that is specifically designed to be integrated into Ableton Live. Max for Live allows you to use the Max development environment to create your own Live content. For more information on Max for Live see this page .
-
MC : MC refers to a set of multichannel objects in Max. These objects allow for multiple channels of audio processing and pass multichannel audio signals using a single patchcord. MC objects typically have an mc. or mcs. prefix.
-
Message : Max patches function by passing messages between objects. Messages tell objects what to do. For a list of what messages an object can receive, see the object's reference page .
-
Message Box : A message box is a clickable object for storing, displaying, and passing messages between objects.
-
Method : Another name for a message. See the "Message" entry above for further details.
-
MSP : MSP is the audio processing side of Max. All MSP objects end with a "~". For help getting started with MSP, see this list of tutorials .
## N
-
Node for Max : Node for Max is a package, automatically included in Max. that lets you write custom applications using the Node JavaScript framework then control and communicate with those applications from Max. For Node for Max documentation, open the Documentation Window in Max and look for the Node for Max package documentation.
-
Number : Numbers refer to both floats and integers .
## O
-
Object : Objects are the building blocks of a patch – they perform specific tasks, and operate like miniature programs within the larger environment.
-
Object Action Menu : The object action menu , accessible from the left side of every object, provides a quick way to access the help file, reference page, and object inspector for that object. It also provides sub-menus to discover messages and attributes associated with the object, and serves as an aid to Max patching.
-
Object Reference Page : Every object in Max has its own reference page . This page serves as a manual for the object, explaining what the object does and how to control it with arguments, attributes, and messages.
-
Operate While Unlocked : A mode that allows you to adjust user interface objects while patching. Sliders, dials, and other controls are all active in this mode which means you don't have to lock the patcher to operate them. To activate the Operate While Unlocked mode, click the "Enable Operate While Unlocked" button on the bottom patcher window toolbar.
-
Operator : An operator is a Gen object.
-
Outlet : A "port" at the bottom of an object where information is sent out. Information is passed from the outlet of one object to the inlet of another object via a patch cord. Each outlet sends a certain type of information. Hover over an outlet with your mouse in an unlocked patch to see what type of information is sent out.
## P
-
Package : Packages are a convenient way to bundle objects, media, patchers, and resources for distribution. A package is simply a folder adhering to a prescribed structure and placed in the 'packages' folder. Once placed in the correct location, the package contents are seamlessly integrated into Max.
-
Package Manager : The Package Manager , which is accessed by selecting “Show Package Manager” from the File menu, provides access to a regularly updated, curated selection of Max add-on content. Some packages listed are created in-house, while others are created by third-party developers. Typically, installing one of these packages will give you access to new objects, patchers, and other Max related content.
-
Parameter : Parameters are a simple representation of the current state of that object, compatible with presets, pattr, and snapshots
-
Patch Cord : Patch cords are used to connect objects together in Max. Information is passed from one object to another using a patch cord. There are four different types of patch cords — those used for Max objects, audio patch cords used for MSP objects, MC patch cords used specifically for multichannel objects, and Jitter patch cords. Each type of patch cord has a unique look.
-
Patcher : A Max patcher is the graphical canvas that you move objects around on. A Max patch is the file or program that you create in Max. You create Max patches and you patch in Max.
-
Presentation Mode : A different patcher view that allows you to arrange and resize user interface objects in your patch independently of their functional position and size in patching mode. Presentation Mode is typically used to design a user-friendly interface for a patch. When a patcher is in Presentation Mode, the Presentation Mode button in the bottom patcher window toolbar will turn green/yellow and the word (presentation) will appear in the title bar of the patcher window.
-
Probe : Probing allows you to view data that is passed through patch cords. This can be very helpful when debugging a patch. There are three types of probes: matrix, signal, and event. The matrix probe allows you to monitor data flowing through a Jitter patch cord. The signal probe allows you to monitor data flowing through an MSP (audio) patch cord. The event probe displays event data that is passed through a Max patch cord. All three types can be activated via the Debug menu.
-
Project : A Project is a collection of dependencies that are used in a patch. These dependencies may include patches, abstractions, JavaScript files, media files, data files, third-party externals, etc. Projects are an easy way to keep related files in the same place, and allow for Project-specific search path management outside of the standard Max Search Paths.
## Q
- Quickref Menu : The Quickref Menu displays a list of all messages and attributes that the selected Max object accepts. To access this menu, control-click (Mac) or right-click on any inlet to a Max object. Selecting a menu item will automatically create a message box or attrui that is connected to the object via a patch cord.
## R
- RNBO : A library and toolchain that can take Max-like patches and export them as portable code. RNBO can directly compile that code to targets like a VST, a Max External, or a Raspberry Pi. The online documentation for RNBO can be found here .
## S
-
Scheduler : The internal timing mechanism used to determine when and in what order events in Max are processed. Scheduler settings can be adjusted in the Preferences window.
-
Shader : A shader is a program that performs a calculation to determine how a 3D object is rendered in a 2D frame. Determining factors include the object’s color and position, lighting, texture coordinates, and material characteristics such as how shiny or matte the object should appear.
-
Signal : This refers to audio data in Max. When audio data is passed between objects, the patch cord is yellow and grey striped.
-
Snapshot : Snapshots let you save the state of parameters in your patcher. They are closely related to VST and Audio Unit presets. You can define presets for patchers, vst~, amxd~, and rnbo~ objects.
-
Snippet : A snippet is a patcher file that typically contains a sequence of objects you use often and don't want to have to constantly re-create as you work. Dragging and dropping a snippet from the left-hand toolbar into your patcher will automatically add the contents of that snippet to your patch.
-
Standalone : A standalone is basically an application built from a Max patch. Any patch can be turned into a standalone, which looks and acts like a standard Macintosh or Windows application. You do not need Max installed on your computer to run a standalone. Every standalone includes a runtime version of Max.
-
Style : Styles allow you to standardize the look of objects by changing their colors and font settings. You can apply a style to a specific Max patch, create your own personal library of styles to be applied as you patch, or make use of "factory styles" that come with Max. To learn more about Styles, see this guide .
-
Subpatcher : A subpatcher is a patch within a patch. Subpatches are often used to organize your work.
-
Symbol : A symbol is essentially a word in Max. A message box with the word "hello" would be considered a symbol. However, numbers and lists can also be considered symbols if they are in quotation marks or converted using the tosymbol object. See this guide for information on how to include special characters in symbols.
## T
-
Template : A template is a preconfigured Max patch that is intended to be a starting point for creating certain patches. Templates can include objects that you often use as well as specific patcher attributes for setting the look of your patching environment. Max comes with a selection of premade templates, or you can create your own.
-
Texture : A texture is essentially an image that is overlaid upon geometry. Textures are used in the context of Jitter. Just like other images in Jitter, textures have an alpha, red, green, and blue component.
-
Theme : As of Max 8, you have the ability to select from a number of color themes using the Color Theme preference in the Preference Window. Themes change the application-wide colors of patcher toolbars, the sidebar, and other interface elements (as well as default patcher colors).
-
Time Values : Time Values refer to any measurement of time used in Max. There are two types of time values: fixed time values and tempo-relative time values. Fixed time values express an amount of time that doesn't change. These include milliseconds, hours/minutes/seconds, samples, and frequency. Tempo-relative time values vary according to the current tempo set in a transport object. These include ticks, note values, and bars/beats/units.
-
Toolbar : Toolbars provide quick access to commonly used tools in Max, as well as audio and video samples, images, and plugins. There are two types of toolbars: patcher toolbars and toolbar mini browsers. For further information on each toolbar, see the Patcher Window documentation.
-
Transport : A tempo-based timing mechanism that can be used to keep time and/or control the behavior of certain objects. There is both a transport object and a Global Transport found under the Extras menu.
