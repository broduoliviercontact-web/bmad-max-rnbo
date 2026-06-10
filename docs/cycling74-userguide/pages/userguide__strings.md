---
title: "Strings"
source: https://docs.cycling74.com/userguide/strings/
source_path: /userguide/strings/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Strings

Source: https://docs.cycling74.com/userguide/strings/

## Extracted Text

# Strings
A String is a container for text (specifically UTF-8 text) that is independent of Max's Symbol Table . You can create and manage Strings using the string object. Like Arrays and Dictionaries , Strings have names and can be passed between objects with`string u12345678`messages. For developers, a String wraps Max's internal`t_string`object.
## When to Use Strings
In addition to the string object, Max has several objects for editing, combining, filtering, and searching through strings. The string.at object searches a string for the position of a substring, and string.slice creates a new string from a character range within an existing string. If your patchers require this sort of text manipulation, it's easier and more efficient to use these purpose-built String objects than it is to use Symbols .
## Working with Strings
Create a new String using the string object. The first argument is the initial value for the string, and you can (optionally) provide a name for the string as well using the`@name`attribute. Strings with the same name will share the same value, so you can create a string in one place and then refer to it somewhere else. When you print a string using the print object, Max will format the output to show the name and contents of the string.
Strings basics
If you use a message object to display a string, you'll see the actual values that pass between Max objects when sending a string in a message. In a message, a string is represented by the symbol`string`followed by the unique identifier for that string. If you don't give your string an explicit name using the`@name`attribute, Max will assign one automatically.
The message object has a`@convertobjs`attribute which will automatically convert received String objects into symbols for display.
If a string object changes the input string somehow, it will output a new string rather than modifying the original. This means that if you want to modify a string recursively, adding your changes back to the original string, you can use the name of the string to replace the original string.
### pattr and pattrstorage
The pattr and pattrstorage objects will store the value of a string. They do not store the string itself, so if you modify the string after storing its value in a pattr object, the updated value will not appear in pattr until you send the string to pattr again.
In this example, changing the value of the string by sending the`new_value`message to the second string object will not update the value stored in pattr .
### Backwards compatibility
If a receiving object does not understand the new`string`type, then Max will automatically convert that string into a symbol to maintain compatibility.
A handful of control objects will always pass strings unmodified, so that they can still be used to route strings between objects. Those objects include:
- append
- prepend
- route
- routepass
- trigger
- match
- router
- universal
- typeroute~
- gate / switch
The trigger object passes the string message through without decomposing it into a symbol. This works even when we use the symbol formatter for trigger.
## JavaScript
Use the`MaxString`class to create a JavaScript reference to a Max String. You can give it an initial value by passing a string value to the constructor. Update the value of the string by calling`.parse`or`.set`.
`var max_str = new MaxString ( "initial_value" ); max_str. parse ( "new_value" ); // update the string contents`
By setting the name property of the`MaxString`, you can refer to a String defined in the parent patcher.
`var max_str = new MaxString (); max_str. name = "fred" ; // Now the MaxString refers to a string named "fred" max_str. set ( "new_value" ); // Updates the string in the containing patcher`
If you want to manipulate the String value, call`.stringify`or`.get`to turn the Max String into a JavaScript string. From there, you can use regular JavaScript string manipulation functions.
`var max_str = new MaxString (); max_str. set ( "the original string value" ); var js_str = max_str. get (); // retrieve the value as a JS string var updated_str = js_str. replace ( "original" , "new" ); max_str. parse (updated_str); post (max_str. stringify ()); // prints "the new string value"`
To send a Max String out of an outlet defined in JavaScript, send the symbol "string" followed by the name of the string.
`function bang ( ) { var str = new MaxString (); str. parse ( "I got a bang" ); outlet ( 0 , "string" , str. name ); }`
## Strings vs Symbols
When working in Max, most of the time, objects pass around text in the form of symbols. When you include text like`bgcolor`or`set`in a list, you're using a symbol. Max doesn't pass the text of a symbol directly, but instead generates a unique identifier for each symbol, passing that identifier between objects instead. This makes certain operations on symbols very efficient, for example comparing the value of two symbols. However, it also means that every time you use a new symbol, it must be assigned to a unique identifier, and that identifier must be added to the Symbol Table . The identifiers added to the Symbol Table are never removed -- the table will grow forever until Max is quit, or runs out of memory.
Strings, on the other hand, do not interact with the Symbol Table. Instead, Max manages Strings in a similar way to Buffers or the contents of a dict object. The text contents of a String are located somewhere in memory, and Max gives that memory a name that can be used to locate the contents of the String. The object interface to a block of audio samples is buffer~ , and the object interface to a Dictionary is the dict object. In a similar way, the string object is the interface to a text String. When a buffer~ or a dict is cleared, the underlying memory is released back to the operating system to be used for new storage. The same applies to Strings, which can be, depending on your requirements, a more efficient way to store text data.
One further difference is that Max symbols are restricted to 32767 characters. Strings have no such limitation, and support the storage of huge blocks of text data.
