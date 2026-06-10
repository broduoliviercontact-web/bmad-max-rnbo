---
title: "Integers and Floats"
source: https://docs.cycling74.com/userguide/integers_vs_floats/
source_path: /userguide/integers_vs_floats/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Integers and Floats

Source: https://docs.cycling74.com/userguide/integers_vs_floats/

## Extracted Text

# Integers and Floats
Max is fairly strict about how it deals with integer and floating point numbers. At a low level, integers and floats are two of the fundamental data types that objects can pass between each other, and many objects will handle the two data types differently.
## Integers and Floats in Max
Integers are whole numbers, while floats can represent values with a decimal component. In Max, many objects operate in either a "floating point mode" or an "integer mode". This is a common source of bugs, since integer-mode objects will convert from float to int before processing, discarding any values after the decimal point.
In this classic example, the result of the division`5 / 4`is computed as`1.25`, but displays as`1`in an integer numbox. This is the expected behavior, but sometimes it can be subtle when an object is in integer-mode.
The object containing a`/`, defining a division operation, can operate either in "integer mode" or "floating-point mode" depending on whether the argument has a decimal or not. As you can see, the integer-mode object will truncate any decimal component.
The scale object behaves similarly—so long as all of the arguments are integers, the object will be in "integer mode", and the output will be truncated to an integer value. The scale object on the left demonstrates this behavior. However, if any of the arguments to scale contains a decimal, then the object will be in "floating point mode", and the output will be a float, even if the input is an integer.
Some objects, like pack , pak , and trigger , can be configured to cast their inputs to floats or integers. A trigger object with the arguments`f`and`i`, as pictured, will cast its input to a float for the leftmost outlet, and to an integer for the rightmost. As you can see, the floating point box on the right displays the truncated value.
Lastly, it's worth mentioning the typeroute object, which can route messages by their type, separating out integers from floats.
A handful of other objects, in particular objects to do with simple math operations, will exhibit special behavior for integers and floats. When in doubt, check the help files and object reference documentation for more information.
## Technical Details
In Max, integers are whole numbers. All integers are 64-bit, so the smallest integer that can pass between objects is -9,223,372,036,854,775,808, and the largest is 9,223,372,036,854,775,807. Floating point numbers in Max are also 64-bit (double precision). Messages can contain positive or negative numbers with a magnitude as large as 1 0 308 10^{308} 1 0 308 , or as small as 1 0 − 308 10^{-308} 1 0 − 308 . Unlike integers, floating point numbers are not evenly spaced. There are as many floating point numbers between 0 and 1 as there are between 1 and 1 0 308 10^{308} 1 0 308 . This may or may not be spiritually significant.
## Gen + RNBO
Unlike Max, Gen and RNBO do not use integers for any internal computation. If you really want Max-style integer math, for example truncating the result of a division operation, then you're best off using the trunc object for Gen, and the trunc object for RNBO.
