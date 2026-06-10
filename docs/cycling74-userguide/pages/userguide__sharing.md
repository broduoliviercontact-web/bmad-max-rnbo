---
title: "Sharing Overview"
source: https://docs.cycling74.com/userguide/sharing/
source_path: /userguide/sharing/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Sharing Overview

Source: https://docs.cycling74.com/userguide/sharing/

## Extracted Text

# Sharing Patchers
There are several ways to share patchers, depending on whether you want to share a large project with multiple dependencies, or a just a small number of Max objects.
## Copy Compressed
To share a small selection of objects, select the object and select Copy Compressed from the Edit menu. This copies the objects into compressed text that can be easily shared.
In compressed form, this group of objects looks like this:
`<pre><code> ----------begin_max5_patcher---------- 438.3ocuUsraiCCC7r8WgfN6sPV4Uy9qTTTv3HjnBaJCI4zTTz7suRT1nY2l GtHA6EKvwLb3Xpg4i7L9Jydkiy9M6IVV1G4YYDTDHqONi2.6qpAGkFGUuYV8 JuH8JuZumfWCUGXkL4vKZAe0VMt4Eqpxmp+iKePTvjylDOlMiBjOHXO2+Szq oJEp9ujSGpC10nwZkmHW9EnoyOfJhfelmGeTbapvpbFjzgTbckHdLdrX4EUx jSpjomTIk8nIH+6spDebmdCB0b1y2Oo5Ab6gqpwx4SiGStrFkmTik++z3FPi iPLSDz.aAEr3Lh4nAuEZTdk8EEBqpo9TLdgNbYsoq1qq1BHpp2AVMf9iqz49 NTv3204sCd6vntVurL9bt3RS7x4+.+4OZhSrwq03+tUh52H9eKcmoyVMTvAC G6qldsx40H30F73jB6WBt7gjL10J64Wkb+oV7cpKuMpkig59961XRLFlj2Al hWxtNShuwT5JDz1tSYc8YSjD7IuZnO1KKnPMlBIuXX4+N8P9IDvFrH9f+nyR MFe+7zeLwaLgwF1o6mbA4Enj7fXXmgqERJgrp4el+GfYabKx -----------end_max5_patcher----------- </code></pre>`
If you copy this text and paste it into a patcher, Max will re-create the original objects.
You can also create a new patcher from a block of compressed text. Select New From Clipboard from the File menu to create a new patcher using the existing contents of the clipboard. This is especially useful for large patchers that have been shared in compressed form.
## Screenshots and Image Export
Max can export patches in PNG and PDF format, although PDF export is currently available only on macOS. To export a patch as an image, select Export Image... from the File menu. In the dialog box that appears, you'll be able to choose between PNG and PDF export.
With the save dialog open, select the PDF format to export a PDF.
PDF image export saves Max patches in a vector format, with means the image can render at any scale without losing resolution.
PDF image export will render without loss of resolution, even at extreme zoom levels.
## Screen Recording
You can lock the aspect ratio of your patcher window by selecting Aspect Ratio from the Window menu. This can be useful when you want to record your patch for sharing on a platform that expects a certain aspect ratio.
You can lock the aspect ratio of your patcher window to one of several common options.
## Projects
For sharing large patchers with lots of dependencies, you might want to use a Max Project . For each patcher in a project. Max keeps track of the resources (audio samples, text documents, video files, etc.) that the patcher depends on. You can use the consolidate option to bring those resources into the project folder. You can then use the Archive command to create a`.maxzip`project archive, which can be opened by anyone with Max.
A Max project window, showing the implicit dependencies of a patcher that loads audio samples.
## Tools and Abstractions
You may find yourself building a library of Max tools, perhaps in the form of abstractions . You might for example compile a library of audio effects or JavaScript utilities. In order to share these, you can simply share a folder of the`.maxpat`files and other resources. For anyone who wants to use these resources, than can install them anywhere on their computer, provided the installation path is in Max's search path .
## Packages
Over time, your library of tools, abstractions, and other resources may reach the point where you want to share it with a large number of users. You might want to use the library as part of a class or workshop, or you might want to distribute it widely to the whole Max community. A Max package provides a wrapper for libraries like this, making it easier to organize, present, distribute, and update them. See the user guide page on Max Packages and the Package Manager for more information.
