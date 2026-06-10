---
title: "Common Operators"
source: https://docs.cycling74.com/userguide/gen/gen_common_operators/
source_path: /userguide/gen/gen_common_operators/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Common Operators

Source: https://docs.cycling74.com/userguide/gen/gen_common_operators/

## Extracted Text

# Gen Common Operators
The following Gen operators are common to all of Max's Gen family of objects. They can be used as operators in the gen , gen~ , jit.gen , jit.pix , and jit.gl.pix objects.
## Comparison
-
!=p , neqp : Returns in1 if it does not equal in2, else returns zero. Equivalent to in1 * (in1 != in2)
-
> , gt : Returns 1 if in1 is greater than in2, else returns zero.
-
== , eq : Returns 1 if in1 equals in2, else returns zero.
-
==p , eqp : Returns in1 if it equals in2, else returns zero. Equivalent to in1 * (in1 == in2).
-
>= , gte : Returns 1 if in1 is equal to or greater than in2, else returns zero.
-
>=p , gtep : Returns in1 if in1 is equal to or greater than in2, else returns zero. Equivalent to in1 * (in1 >= in2).
-
>p , gtp : Returns in1 if in1 is greater than in2, else returns zero. Equivalent to in1 * (in1 > in2).
-
< , lt : Returns 1 if in1 is less than than in2, else returns zero.
-
<= , lte : Returns 1 if in1 is equal to or less than in2, else returns zero.
-
<=p , ltep : Returns in1 if in1 is equal to or less than in2, else returns zero. Equivalent to in1 * (in1 <= in2).
-
<p , ltp : Returns in1 if in1 is less than in2, else returns zero. Equivalent to in1 * (in1 < in2).
-
max , maximum : The maximum of the inputs
-
min , minimum : The minimum of the inputs
-
!= , neq : Returns 1 if in1 does not equal in2, else returns zero.
-
step : Akin to the GLSL step operator: 0 is returned if in1 < in2, and 1 is returned otherwise.
## Constant
-
constant : A constant value
-
degtorad , DEGTORAD : Multiplicative constant to convert degrees to radians
-
e , E : Base of the natural logarithm
-
f , float : Either outputs a constant float or converts its input value to a float
-
halfpi , HALFPI : One half of the constant pi
-
i , int : Either outputs a constant integer or converts its input value to an integer.
-
invpi , INVPI : One over pi
-
ln10 , LN10 : The natural log of 10
-
ln2 , LN2 : The natural log of 2
-
log10e , LOG10E : Log base 10 of the constant e
-
log2e , LOG2E : Log base 2 of the constant e
-
PHI , phi : 1 + s q r t ( 5 ) 2 \frac{1 + sqrt(5)}{2} 2 1 + s q r t ( 5 ) ​ , the "golden" ratio
-
pi , PI : The constant pi, the ratio of a circle's circumference to its diameter
-
radtodeg , RADTODEG : Multiplicative constant to convert radians to degrees
-
sqrt1_2 , SQRT1_2 : One over the square root of 2
-
sqrt2 , SQRT2 : The square root of 2
-
twopi , TWOPI : Two times pi
## Declare
- param , Param : Named parameters can be modified from outside the gen patcher. The first argument specifies the name of the parameter, the second argument the initial value.
## Expression
- expr : Evaluates GenExpr code. Standard mathematical operators (+, -, *, / etc.) and gen patcher operators can be used. See the GenExpr documentation for more detail.
## Ignore
- pass : Passes the value through unchanged.
## Input-output
-
in : Defines an input for a gen patcher.
-
out : Send output from a gen patcher
## Logic
-
! , not : An input value of zero returns 1, any other value returns zero.
-
&& , and : Returns 1 if both in1 and in2 are nonzero.
-
bool : Converts any nonzero value to 1 while zero passes through.
-
or , || : Returns 1 if either in1 or in2 are nonzero.
-
^^ , xor : Returns 1 if one of in1 and in2 are nonzero, but not both.
## Math
-
!% , rmod : Reverse modulo (remainder of second input / first input)
-
!- , rsub : Reverse subtraction (subtract first input from second)
-
% , mod : Modulo inputs (remainder of first input / second input)
-
+ , add : Add inputs
-
- , sub : Subtract inputs
-
/ , div : Divide inputs
-
absdiff : Compute the absolute difference between two inputs using the equation a b s ( i n 1 − i n 2 ) abs(in1-in2) ab s ( in 1 − in 2 ) .
-
cartopol : Convert Cartesian values to polar format. Angles are in radians.
-
* , mul : Multiply inputs
-
neg : Negate input
-
poltocar : Convert polar values to Cartesian format. Angles are in radians.
-
!/ , rdiv : Reverse division (divide second input by first)
## Numeric
-
abs : Negative values will be converted to positive counterparts.
-
ceil : Round the value up to the next higher integer
-
floor , trunc : Round the value down to the next lower integer (toward negative infinity)
-
fract : Return only the fractional component
-
sign : Positive input returns 1, negative input returns -1, zero returns itself.
-
trunc : Round the value down to the next smaller integer (toward zero)
## Powers
-
exp : Raise the mathematical value e to a power
-
exp2 : Raise 2 to a power
-
fastexp : Approximated e to a power
-
fastpow : Approximated in1 to the power of in2
-
ln , log : The natural logarithm
-
log10 : The logarithm base 10 of the input
-
log2 : The logarithm base 2 of the input
-
pow : Raise in1 to the power of in2
-
sqrt : The square root of the input
## Range
-
clamp , clip : Clamps the input value between specified min and max. Ranges are inclusive (both min and max values may be output)
-
fold : Low and high values can be specified by arguments or by inlets. The default range is 0..1.
-
scale : Similar to the Max scale and MSP scale~ objects. Inputs are: 1) value to scale, 2) input lower bound, 3), input upper bound, 4) output lower bound, 5) output upper bound, 6) exponential curve. Default lower and upper bounds are zero and one; default exponential curve is 1 (linear). No bound clamping is performed. The high and low values can be reversed for inverted mapping.
-
wrap : Low and high values can be specified by arguments or by inlets. The default range is 0..1.
## Route
-
? , switch : Selects between the second and third inputs according to the boolean value of the first. If the first argument is true, the second argument will be output. Otherwise, the third argument will be output.
-
gate : Similar to the MSP gate~ object. It takes an argument for number of outputs (one is the default) and lets you choose which the incoming signal (at the right inlet) is sent to according to the (integer) value in the left inlet. A value of zero or less to the left inlet will choose no output; a value greater than the number of outlets will select the last outlet. Like gate~, un-selected outlets will send zero.
-
mix : Mixes (interpolates) between inputs a and b according to the value of the third input t, using linear interpolation. The factor (t) should vary between 0 (for a) and 1 (for b). If one argument is given, it specifies the mix (interpolation) factor.
-
r , receive : Receive values from a named send. The send/receive pairs are only visible to each other within the same gen patcher. They will not send across gen patchers or sub-patchers.
-
s , send : Send values to a named receive. The send/receive pairs are only visible to each other within the same gen patcher. They will not send across gen patchers or sub-patchers.
-
selector : Similar to the MSP selector~ object. In a Gen patcher it takes an argument for number of choices (one is the default). In GenExpr, the number of choices is determined by the number of arguments. The first input lets you choose which of the remaining inputs is sent to the output. A value of zero or less to the first input will result in a zero signal at the output; a value greater than the number of choices will select the last input.
-
smoothstep : Smoothstep is a scalar interpolation function commonly used in computer graphics. The function interpolates smoothly between two input values based on a third one that should be between the first two. The returned value is clamped between 0 and 1. The slope (i.e. derivative) of the smoothstep function starts at 0 and ends at 0.
## Subpatcher
-
gen : Gen subpatcher or abstraction
-
setparam : Set a param in a subpatcher from a parent patcher
## Trigonometry
-
acos : The arc cosine of the input (returns radians)
-
acosh : The inverse hyperbolic cosine of the input
-
asin : The arc sine of the input (returns radians)
-
asinh : The inverse hyperbolic sine of the input
-
atan : The arc tangent of the input (returns radians)
-
atan2 : Returns the angle to the coordinate (x,y) in radians.
-
atanh : The inverse hyperbolic tangent of the input
-
cos : The cosine of the input (in radians)
-
cosh : The hyperbolic cosine of the input
-
degrees : convert radians to degrees
-
fastcos : The approximated cosine of the input (in radians)
-
fastsin : The approximated sine of the input (in radians)
-
fasttan : The approximated tangent of the input (in radians)
-
hypot : Returns the length of the vector to (in1, in2).
-
radians : convert degrees to radians
-
sin : The sine of the input (in radians)
-
sinh : The hyperbolic sine of the input
-
tan : The tangent of the input (in radians)
-
tanh : The hyperbolic tangent of the input
## Waveform
- noise : A random number generator
