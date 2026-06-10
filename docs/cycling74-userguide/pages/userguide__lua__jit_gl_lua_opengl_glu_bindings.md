---
title: "jit.gl.lua OpenGL GLU Bindings"
source: https://docs.cycling74.com/userguide/lua/jit_gl_lua_opengl_glu_bindings/
source_path: /userguide/lua/jit_gl_lua_opengl_glu_bindings/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# jit.gl.lua OpenGL GLU Bindings

Source: https://docs.cycling74.com/userguide/lua/jit_gl_lua_opengl_glu_bindings/

## Extracted Text

# jit.gl.lua OpenGL GLU Bindings
The GLU (openGL Utility) bindings are located in the`opengl.glu`module. It is a sub-module of`opengl`module. To access them, use Lua's built-in`require`function as follows:
`local glu = require( "opengl.glu" )`
For the standard OpenGL bindings, see the jit.gl.lua OpenGL Bindings .
`LookAt (eye, center, up)`
Define a viewing transformationOpenGL Documentation: gluLookAt If LookAt has nine arguments, it expects unpacked vectors. Otherwise, it will look for 3 vectors as arguments.
-
`eye`Specifies the position of the eye point.
-
`center`Specifies the position of the reference point.
-
`up`Specifies the direction of the up vector.
`Ortho2D (left, right, bottom, up)`
Define a 2D orthographic projection matrixOpenGL Documentation: gluOrtho2D
-
`left`Specify the coordinates for the left vertical clipping planes.
-
`right`Specify the coordinates for the right vertical clipping planes.
-
`bottom`Specify the coordinates for the bottom horizontal clipping planes.
-
`up`Specify the coordinates for the up horizontal clipping planes.
`Perspective (fovy, aspect, near, far)`
Set up a perspective projection matrixOpenGL Documentation: gluPerspective
-
`fovy`Specifies the field of view angle, in degrees, in the y direction.
-
`aspect`Specifies the aspect ratio that determines the field of view in the x direction. The aspect ratio is the ratio of x (width) to y (height).
-
`near`Specifies the distance from the viewer to the near clipping plane (always positive).
-
`far`Specifies the distance from the viewer to the far clipping plane (always positive).
`Project (...)`
Map object coordinates to window coordinatesOpenGL Documentation: gluProject
- `...`Specify the object coordinates as either a table or unpacked values.
`UnProject (...)`
Map window coordinates to object coordinatesOpenGL Documentation: gluUnProject
- `...`Specify the window coordinates as either a table or unpacked values.
