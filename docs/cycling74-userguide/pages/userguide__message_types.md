---
title: "Message Types"
source: https://docs.cycling74.com/userguide/message_types/
source_path: /userguide/message_types/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Message Types

Source: https://docs.cycling74.com/userguide/message_types/

## Extracted Text

# Message Types
All Max messages are built up of atoms, which can be a bang , a float , an int , or a symbol . These are simple types which hold a small, fixed amount of data. An ordered group of atoms is called a list . These are the fundamental Max data types. For larger, more complex data types, Max messages use atoms to refer to the place where that more complex data is stored.
## Atoms
There are no more fundamental types in Max than bang , float , int , and symbol . An ordered group of these types is called a list , which also acts a lot like a fundamental Max data type. In a message box , Max treats each space-separated element as an atom. You can use the typeroute~ object to separate messagse traveling on a single patch cord by their data type.
Name Description
bang bang means "do it"—most objects respond to a bang by performing their primary function.
int A whole number without a decimal component
float A number with a decimal component
symbol Any combination of characters, including numeric characters
### Floats and Ints
In Max, the difference between an int and a float can be significant. Some objects will have different behavior depending on whether they receive a float or an int, and some might refuse to accept one type of number when they expect the other. For a more in-depth discussion, see Integers and Floats .
### Symbols
Symbols can contain any combination of characters. Max will automatically treat any non-numeric group of characters as a symbol (the one exception is the characters`bang`, which Max will recognize as a bang ). If you want to treat a group of numbers as a symbol, or you want your symbol to contain spaces, use quotation marks.
A symbol is a fixed-length, immutable entity. Adding or removing characters from a symbol will create a new symbol and add that to the Symbol Table . Often this is a technical detail that you can safely ignore. If you want to know more, you can read about symbols and strings .
## Lists
A list is just an ordered group of atoms. Often, if the first element of a list is a symbol, the object receiving the list will interpret the leading symbol as a selector , and the following list elements as arguments .
Building, manipulating, and routing lists is fundamental to working in Max. You can route a list to one part of your patcher or another, based on the first element of the list, using the route object. It's also very common to build lists using dollar-sign replacement in a message box. The`list.*`family of objects, like list.append , list.iter , and list.rot , provide even more ways to work with lists.
Technically, a list must always start with either a float or an integer. If a list starts with a symbol, then the symbol is the selector, and what follows are the arguments for that selector. Usually you can ignore this technicality, but the distinction can be important to remember when working with Max's C or JavaScript APIs. There are also some sneaky situations that expose what's really going on "under the hood". For example, any object that accepts a message like ::message[list 1 2 3] will respond the same way to the message ::message[1 2 3]. So, the "length" of the message ::message[list 1 2 3] is actually 3.
The list selector instructs the object to treat the arguments that follow as a list.
## Named Storage Types
Atoms and lists are primitive in the sense that the name of the data is the same as the data. The number 12 and the atom`12`are the same. However, for larger and more complex data, it's not feasible to put the entire block of data into a message box. When one Max object wants to tell another Max object to process an image that's stored in a matrix , it doesn't send a message containing the data, but rather the name of the matrix that stores the data.
## Matrices
Matrices store multidimensional data, where every cell has the same data type. Matrices are often used to store images, 3D models, and 3D transformations. The object that manages a reference to a matrix is called jit.matrix .
When you view a matrix in a message box, you'll see that matrices are identified by a list with two parts: the symbol`jit_matrix`, followed by the unique name of the matrix. For more info on matrices, see matrix .
Patcher cords that carry matrices also get a special, striped-green style. This is just cosmetic—as you can see it's simply carrying a normal message.
## Textures
Textures are similar to matrices, in that they store multidimensional data of all the same type. However, the big difference between Max matrices and textures is that textures reside on the Graphics Processing Unit, or GPU. Max itself manages the data and the life cycle of matrices, but it asks the graphics API to manage textures on its behalf.
The object that manages a reference to a texture is called jit.gl.texture . When you view a texture in a message box, you'll see that a texture is identified by the symbol`jit_gl_texture`followed by the unique name of the texture. For more info on textures, see textures .
Like matrices, texture patch cords get their own styling.
## Dictionaries
Dictionaries store structured data. That data is organized into keys and values , and you can use the key to look up the value. A value can be a number, a list, a symbol, a string, an array, or even another dictionary.
Dictionaries are managed by the dict object, and you can work with dictionaries using the`dict.*`family of objects. In a message box, you'll see that dictionaries are identified by the symbol`dict`followed by the name of the dictionary. For more info on dictionaries, see dictionaries .
## Strings
Strings store an ordered collection of characters. Unlike a symbol, strings are mutable, which means that a string can be changed without creating a new string.
Strings are managed by the string object and manipulated with the`string.*`family of objects. In a message box, you'll see strings represented as by the symbol`string`followed by the name of the string. For more info on strings, see strings .
## Arrays
Arrays are an ordered collection of arbitrary data. Unlike lists, arrays can store complex data types like dictionaries, strings, and other arrays. Max provides the handy array.map and array.reduce for functional-style programming on arrays.
Arrays are managed by the array object and manipulated with the`array.*`family of objects. In a message box, you'll see arrays represented as by the symbol`array`followed by the name of the array. For more info on arrays, see arrays .
