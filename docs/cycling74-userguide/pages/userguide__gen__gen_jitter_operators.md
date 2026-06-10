---
title: "Jitter Operators"
source: https://docs.cycling74.com/userguide/gen/gen_jitter_operators/
source_path: /userguide/gen/gen_jitter_operators/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Jitter Operators

Source: https://docs.cycling74.com/userguide/gen/gen_jitter_operators/

## Extracted Text

# Jitter Operators
The following Gen operators are unique to the jit.gen , jit.pix , and jit.gl.pix objects - unlike the Common Gen Operators , they are only used in the matrix/texture domain.
## Color
-
hsl2rgb : Convert HSL to RGB, preserving alpha
-
rgb2hsl : Convert RGB to HSL, preserving alpha
## Coordinate
-
cell : Cell coordinates of input matrix [0, dim-1]
-
dim : Dimensions of input matrix
-
norm : Normalized coordinates of input matrix [0, 1]
-
snorm : Signed normalized coordinates of input matrix [-1, 1]
## Quaternion
-
qconj : Get the conjugate of a quaternion.
-
qmul : Multiply quaternion inputs
-
qrot : Rotate a vector by a quaternion. The equation of the rotation is q ∗ v ∗ q − 1 q*v*q^{-1} q ∗ v ∗ q − 1 .
## Sampling
-
nearest : Nearest neighbor sample a matrix at a given coordinate (normalized). Nearest has a boundmode attribute that can be set to wrap, mirror or clamp.
-
nearestpix : Nearest neighbor sample a matrix at a given coordinate (in pixels). Nearest has a boundmode attribute that can be set to wrap, mirror or clamp.
-
sample : Sample a matrix at a given coordinate (normalized) with linear interpolation. Sample has a boundmode attribute that can be set to wrap, mirror or clamp.
-
samplepix : Sample a matrix at a given coordinate (in pixels) with linear interpolation. Pixel centers are located at PIXEL+0.5. For example, the center of the upper-left pixel is (0.5, 0.5). Samplepix has a boundmode attribute that can be set to wrap, mirror or clamp.
## Surface
-
circle : Equation of a circle taking input coordinates ranging from [0, 1]
-
cone : Equation of a cone taking input coordinates ranging from [0, 1]
-
cylinder : Equation of a cylinder taking input coordinates ranging from [0, 1]
-
plane : Equation of a plane taking input coordinates ranging from [0, 1]
-
sphere : Equation of a sphere taking input coordinates ranging from [0, 1]
-
torus : Equation of a torus taking input coordinates ranging from [0, 1]
## Vector
-
concat : Concatenate vector values into a larger vector
-
cross : Take the cross product of two vectors
-
dot : Take the dot product of two vectors
-
faceforward : Return a vector pointing in the same direction as another
-
length : Returns the length of a vector
-
normalize : Normalize a vector to unit length
-
reflect : Reflect a vector off a surface defined by a normal
-
refract : Refract a vector through a surface defined by a normal and a refraction index
-
rotor : Return a quaternion that can rotate the first input into the second.
-
swiz : Unpack and remap vector components
-
vec : Pack scalar values into a vector
