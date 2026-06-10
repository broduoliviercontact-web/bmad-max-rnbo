---
title: "Subpatchers"
source: https://docs.cycling74.com/userguide/subpatchers/
source_path: /userguide/subpatchers/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Subpatchers

Source: https://docs.cycling74.com/userguide/subpatchers/

## Extracted Text

# Subpatchers and Encapsulation
Subpatchers let you collapse a group of objects down to a single object. You can treat the subpatcher as if it were like any other Max object, but you can also double-click on the subpatcher object to see its contents at any time. Subpatchers can be extremely useful for managing the complexity of large patchers, and for grouping together objects that perform a single function.
Create an empty subpatcher object by making a patcher object, which can also be abbreviated to`p`, or create a subpatcher from an existing group of objects using encapsulation .
An empty subpatcher, using the abbreviated object name 'p'. The title of the subpatcher window is the first argument of the subpatcher object.
## Inlets and Outlets
Subpatchers and abstractions handle inlets and outlets in the same way. A subpatcher will have as many inlets or outlets as it has inlet or outlet objects. If you create a new inlet or outlet object in your subpatcher, the parent patcher will update to include the new inlet or outlet. The order of the inlets in the parent patcher corresponds to the order of inlets in the subpatcher. So, if you swap the position of two inlet objects in the subpatcher, those objects will map to different inlets in the parent subpatcher object.
The subpatcher has two inlet objects and one outlet object, so the parent subpatcher object has two inlets and one outlet.
Just like a regular Max object, a subpatcher can add Comments to its inlets and outlets. If you set the`@comment`attribute on an inlet or outlet object, then when you mouse over the inlet or outlet you will see that text displayed.
## Abstractions vs Subpatchers
As mentioned in the article on abstractions , subpatchers are embedded within their parent, while abstractions reference a saved`.maxpat`file. Changes that you make to a subpatcher only affect that subpatcher, whereas changes to an abstraction will modify the original file, and hence all copies of that abstraction. Abstractions can also take advantage of arguments and unique identifiers , while subpatchers cannot.
## Encapsulating and De-encapsulating
With a group of objects selected, press ⌘ shift e (macOS) or CTRL shift e (Windows) , or select Encapsulate from the Edit menu to move those objects to a new subpatcher. If those objects were connected to other objects that weren't part of the encapsulation, Max will create inlet and outlet objects automatically, and connect the new subpatcher object in the correct way. The logic of your patcher will always be preserved after encapsulation.
A group of objects that express the Pythagorean theorem, computing the length of the hypotenuse of a right triangle. After encapsulation, the objects are contained in a subpatcher that implements the same logic.
It's also possible to de-encapsulate a subpatcher, copying all of the contained objects into the parent patcher and removing the subpatcher object. Select any subpatcher and press ⌘ shift d (macOS) or CTRL shift d (Windows) , or select`De-encapsulate`from the Edit menu to perform a de-encapsulation.
### Re-initializing
It's worth mentioning that encapsulation (as well as de-encapsulation) copies the selected objects into a new subpatcher and then deletes the original objects. The objects in the subpatcher are new objects, meaning their internal state will be reset to its initial value. This is a common source of confusion when starting out with Max.
