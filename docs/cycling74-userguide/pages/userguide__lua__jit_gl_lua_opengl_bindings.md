---
title: "jit.gl.lua OpenGL Bindings"
source: https://docs.cycling74.com/userguide/lua/jit_gl_lua_opengl_bindings/
source_path: /userguide/lua/jit_gl_lua_opengl_bindings/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# jit.gl.lua OpenGL Bindings

Source: https://docs.cycling74.com/userguide/lua/jit_gl_lua_opengl_bindings/

## Extracted Text

# jit.gl.lua OpenGL Bindings
The OpenGL bindings for jit.gl.lua are found in the`opengl`module, which is built-in to the object. To access the bindings, simpply use the built-in Lua function,`require`, to load the module as follows:
`-- load in the module and set some aliases local gl = require( "opengl" ) local GL = gl`
The idiom above allows us to write code that more closely resembles C-style OpenGL code. For the OpenGL Utility (GLU) functions see the For the standard OpenGL bindings, see the jit.gl.lua OpenGL GLU Bindings .
`Accum (op, value)`
Operate on the accumulation bufferOpenGL Documentation: glAccum
-
`op`Specifies the accumulation buffer operation. Symbolic constants GL_ACCUM, GL_LOAD, GL_ADD, GL_MULT, and GL_RETURN are accepted.
-
`value`Specifies a floating-point value used in the accumulation buffer operation. op determines how value is used.
`AlphaFunc (func, ref)`
Specify the alpha test functionOpenGL Documentation: glAlphaFunc
-
`func`Specifies the alpha comparison function. Symbolic constants GL_NEVER, GL_LESS, GL_EQUAL, GL_LEQUAL, GL_GREATER, GL_NOTEQUAL, GL_GEQUAL, and GL_ALWAYS are accepted. The initial value is GL_ALWAYS
-
`ref`Specifies the reference value that incoming alpha values are compared to. This value is clamped to the range 0 1 , where 0 represents the lowest possible alpha value and 1 the highest possible value. The initial reference value is 0
`Begin (mode)`
Delimit the vertices of a primitive or a group of like primitivesOpenGL Documentation: glBegin
- `mode`Specifies the primitive or primitives that will be created from vertices presented between glBegin and the subsequent glEnd. Ten symbolic constants are accepted: GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP, GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP, and GL_POLYGON.
`BlendFunc (sfactor, dfactor)`
Specify pixel arithmeticOpenGL Documentation: glBlendFunc
-
`sfactor`Specifies how the red, green, blue, and alpha source blending factors are computed. The following symbolic constants are accepted: GL_ZERO, GL_ONE, GL_SRC_COLOR, GL_ONE_MINUS_SRC_COLOR, GL_DST_COLOR, GL_ONE_MINUS_DST_COLOR, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_DST_ALPHA, GL_ONE_MINUS_DST_ALPHA, GL_CONSTANT_COLOR, GL_ONE_MINUS_CONSTANT_COLOR, GL_CONSTANT_ALPHA, GL_ONE_MINUS_CONSTANT_ALPHA, and GL_SRC_ALPHA_SATURATE. The initial value is GL_ONE.
-
`dfactor`Specifies how the red, green, blue, and alpha destination blending factors are computed. The same constants are accepted as for sfactor.
`CallList ( list )`
Execute a display listOpenGL Documentation: glCallList
- `list`Specifies the integer name of the display list to be executed.
`Clear (mask)`
Clear buffers to preset valuesOpenGL Documentation: glClear
- `mask`Bitwise OR of masks that indicate the buffers to be cleared. The four masks are GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_ACCUM_BUFFER_BIT, and GL_STENCIL_BUFFER_BIT.
`ClearAccum (...)`
Specify clear values for the accumulation bufferOpenGL Documentation: glClearAccum
- `...`Either a 4 numbers or a table specifying the red, green, blue, and alpha values used when the accumulation buffer is cleared. The initial values are all 0.
`ClearColor (...)`
Specify clear values for the color buffersOpenGL Documentation: glClearColor
- `...`Either a 4 numbers or a table specifying the red, green, blue, and alpha values used when the color buffers are cleared. The initial values are all 0.
`ClearDepth (depth)`
Specify the clear value for the depth bufferOpenGL Documentation: glClearDepth
- `depth`Specifies the depth value used when the depth buffer is cleared. The initial value is 1.
`ClearIndex (c)`
Specify the clear value for the color index buffersOpenGL Documentation: glClearIndex
- `c`Specifies the index used when the color index buffers are cleared. The initial value is 0.
`ClearStencil (c)`
Specify the clear value for the stencil bufferOpenGL Documentation: glClearStencil
- `c`Specifies the index used when the stencil buffer is cleared. The initial value is 0.
`ClipPlane (plane, equation)`
Specify a plane against which all geometry is clippedOpenGL Documentation: glClipPlane
-
`plane`Specifies which clipping plane is being positioned. Symbolic names of the form GL_CLIP_PLANEi, where i is an integer between 0 and GL_MAX_CLIP_PLANES -1 , are accepted.
-
`equation`Specifies the address of an array of four double-precision floating-point values. These values are interpreted as a plane equation.
`Color (...)`
Set the current colorOpenGL Documentation: glColor
- `...`Specify either 3 or 4 numbers or a table for new red, green, blue and [alpha] values for the current color. The default value is (0, 0, 0, 1).
`ColorMask (...)`
Enable and disable writing of frame buffer color componentsOpenGL Documentation: glColorMask
- `...`Either 4 numbers or a table specifying whether red, green, blue, and alpha can or cannot be written into the frame buffer. The initial values are all GL_TRUE, indicating that the color components can be written.
`ColorMaterial (face, mode)`
Cause a material color to track the current colorOpenGL Documentation: glColorMaterial
-
`face`Specifies whether front, back, or both front and back material parameters should track the current color. Accepted values are GL_FRONT, GL_BACK, and GL_FRONT_AND_BACK. The initial value is GL_FRONT_AND_BACK.
-
`mode`Specifies which of several material parameters track the current color. Accepted values are GL_EMISSION, GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, and GL_AMBIENT_AND_DIFFUSE. The initial value is GL_AMBIENT_AND_DIFFUSE.
`CopyPixels (x, y, width, height, type)`
Copy pixels in the frame bufferOpenGL Documentation: glCopyPixels
-
`x`Specify the x window coordinate of the lower left corner of the rectangular region of pixels to be copied.
-
`y`Specify the y window coordinate of the lower left corner of the rectangular region of pixels to be copied.
-
`width`Specify the horizontal dimensions of the rectangular region of pixels to be copied. Both must be nonnegative.
-
`height`Specify the vertical dimensions of the rectangular region of pixels to be copied. Both must be nonnegative.
-
`type`Specifies whether color values, depth values, or stencil values are to be copied. Symbolic constants GL_COLOR, GL_DEPTH, and GL_STENCIL are accepted.
`CopyTexImage (target, level, internalformat, x, y, width, [height], border)`
Copy pixels into a 1D or 2D texture imageIf no height argument is given, glCopyTexImage1D will be used, otherwise, glCopyTexImage2D be used. Example usage: 1D case: gl.CopyTexImage(GL.TEXTURE_1D, 0, GL.RGBA, 0, 0, 128, 0) 2D case: gl.CopyTexImage(GL.TEXTURE_2D, 0, GL.RGBA, 0, 0, 128, 128, 0) OpenGL Documentation: glCopyTexImage1D , glCopyTexImage2D
-
`target`Only relevant in the 2D case. Specifies the target texture. Must be GL_TEXTURE_2D, GL_TEXTURE_CUBE_MAP_POSITIVE_X, GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, GL_TEXTURE_CUBE_MAP_POSITIVE_Z, or GL_TEXTURE_CUBE_MAP_NEGATIVE_Z.
-
`level`Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image.
-
`internalformat`Specifies the internal format of the texture. See OpenGL documentation for accepted values.
-
`x`Specify the x window coordinate of the left corner of the row of pixels to be copied.
-
`y`Specify the y window coordinate of the left corner of the row of pixels to be copied.
-
`width`Specifies the width of the texture image. Must be 0 or 2 n + 2 border for some integer n.
-
`[height]`Specifies the height of the texture image. Must be 0 or 2 m + 2 border for some integer m. The height of the texture image in the 1D case is 1.
-
`border`Specifies the width of the border. Must be either 0 or 1.
`CopyTexSubImage (target, level, xoffset, [yoffset], x, y, width, [height])`
Copy a 1D or 2D texture subimageIf no yoffset or height argument is given, glCopyTexSubImage1D will be used, otherwise, glCopyTexSubImage2D be used. Example usage: 1D case: gl.glCopyTexSubImage(GL.TEXTURE_1D, 0, 32, 0, 0, 64) 2D case: gl.glCopyTexSubImage(GL.TEXTURE_2D, 0, 16, 24, 0, 0, 128, 128) OpenGL Documentation: glCopyTexSubImage1D , glCopyTexSubImage2D
-
`target`Only relevant in the 2D case. Specifies the target texture. Must be GL_TEXTURE_2D, GL_TEXTURE_CUBE_MAP_POSITIVE_X, GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, GL_TEXTURE_CUBE_MAP_POSITIVE_Z, or GL_TEXTURE_CUBE_MAP_NEGATIVE_Z.
-
`level`Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image.
-
`xoffset`Specifies a texel offset in the x direction within the texture array..
-
`[yoffset]`Specifies a texel offset in the y direction within the texture array..
-
`x`Specify the x window coordinate of the left corner of the row of pixels to be copied.
-
`y`Specify the y window coordinate of the left corner of the row of pixels to be copied.
-
`width`Specifies the width of the texture subimage.
-
`[height]`Specifies the height of the texture subimage.
`CullFace (mode)`
Specify whether front- or back-facing facets can be culledOpenGL Documentation: glCullFace
- `mode`Specifies whether front- or back-facing facets are candidates for culling. Symbolic constants GL_FRONT, GL_BACK, and GL_FRONT_AND_BACK are accepted. The initial value is GL_BACK.
`DeleteLists ( list , range)`
Delete a contiguous group of display listsOpenGL Documentation: glDeleteLists
-
`list`Specifies the integer name of the first display list to delete.
-
`range`Specifies the number of display lists to delete.
`DepthFunc (func)`
Specify the value used for depth buffer comparisonsOpenGL Documentation: glDepthFunc
- `func`Specifies the depth comparison function. Symbolic constants GL_NEVER, GL_LESS, GL_EQUAL, GL_LEQUAL, GL_GREATER, GL_NOTEQUAL, GL_GEQUAL, and GL_ALWAYS are accepted. The initial value is GL_LESS.
`DepthMask (flag)`
Enable or disable writing into the depth bufferOpenGL Documentation: glDepthMask
- `flag`Specifies whether the depth buffer is enabled for writing. If flag is GL_FALSE, depth buffer writing is disabled. Otherwise, it is enabled. Initially, depth buffer writing is enabled.
`DepthRange (near, far)`
Specify mapping of depth values from normalized device coordinates to window coordinatesOpenGL Documentation: glDepthRange
-
`near`Specifies the mapping of the near clipping plane to window coordinates. The initial value is 0.
-
`far`Specifies the mapping of the far clipping plane to window coordinates. The initial value is 1.
`Disable (cap)`
Disable server-side GL capabilitiesOpenGL Documentation: glDisable
- `cap`Specifies a symbolic constant indicating a GL capability.
`DrawBuffer (mode)`
Specify which color buffers are to be drawn intoOpenGL Documentation: glDrawBuffer
- `mode`Specifies up to four color buffers to be drawn into. Symbolic constants GL_NONE, GL_FRONT_LEFT, GL_FRONT_RIGHT, GL_BACK_LEFT, GL_BACK_RIGHT, GL_FRONT, GL_BACK, GL_LEFT, GL_RIGHT, GL_FRONT_AND_BACK, and GL_AUXi, where i is between 0 and the value of GL_AUX_BUFFERS minus 1, are accepted. (GL_AUX_BUFFERS is not the upper limit; use glGet to query the number of available aux buffers.) The initial value is GL_FRONT for single-buffered contexts, and GL_BACK for double-buffered contexts
`EdgeFlag (flag)`
Flag edges as either boundary or nonboundaryOpenGL Documentation: glEdgeFlag
- `flag`Specifies the current edge flag value, either GL_TRUE or GL_FALSE. The initial value is GL_TRUE.
`Enable (cap)`
Enable server-side GL capabilitiesOpenGL Documentation: glEnable
- `cap`Specifies a symbolic constant indicating a GL capability.
`End ()`
Delimit the vertices of a primitive or a group of like primitivesOpenGL Documentation: glEnd
`EndList ()`
End the creation or replacement of a display listOpenGL Documentation: glEndList
`Finish ()`
Block until all GL execution is completeOpenGL Documentation: glFinish
`Flush ()`
Force execution of GL commands in finite timeOpenGL Documentation: glFlush
`Fog (pname, ...)`
Specify fog parametersOpenGL Documentation: glFog
-
`pname`Specifies a single-valued fog parameter. GL_FOG_MODE, GL_FOG_DENSITY, GL_FOG_START, GL_FOG_END, GL_FOG_INDEX, and GL_FOG_COORD_SRC are accepted.
-
`...`Specifies the value that pname will be set to.
`FrontFace (mode)`
Define front- and back-facing polygonsOpenGL Documentation: glFrontFace
- `mode`Specifies the orientation of front-facing polygons. GL_CW and GL_CCW are accepted. The initial value is GL_CCW.
`Frustum (left, right, bottom, top, near, far)`
Multiply the current matrix by a perspective matrixOpenGL Documentation: glFrustum
-
`left`Specify the coordinates for the left vertical clipping plane.
-
`right`Specify the coordinates for the right vertical clipping plane.
-
`bottom`Specify the coordinates for the top horizontal clipping plane.
-
`top`Specify the coordinates for the bottom horizontal clipping plane.
-
`near`Specify the distance to the near depth clipping plane. Must be positive.
-
`far`Specify the distance to the far depth clipping plane. Must be positive.
`GenLists (range)`
Generate a contiguous set of empty display listsOpenGL Documentation: glGenLists
- `range`Specifies the number of contiguous empty display lists to be generated.
`Get (pname)`
Return the value or values of a selected parameterOpenGL Documentation: glGet
- `pname`Specifies the parameter value to be returned. See documentation for the list of accepted values.
`GetClipPlane (plane)`
Return the coefficients of the specified clipping planeOpenGL Documentation: glGetClipPlane
- `plane`Specifies a clipping plane. The number of clipping planes depends on the implementation, but at least six clipping planes are supported. They are identified by symbolic names of the form GL_CLIP_PLANE i where i ranges from 0 to the value of GL_MAX_CLIP_PLANES - 1.
`GetError ()`
Return error informationOpenGL Documentation: glGetError
`GetLight (light, pname)`
Return light source parameter valuesOpenGL Documentation: glGetLight
-
`light`Specifies a light source. The number of possible lights depends on the implementation, but at least eight lights are supported. They are identified by symbolic names of the form GL_LIGHTi where i ranges from 0 to the value of GL_MAX_LIGHTS - 1.
-
`pname`Specifies a light source parameter for light. Accepted symbolic names are GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_POSITION, GL_SPOT_DIRECTION, GL_SPOT_EXPONENT, GL_SPOT_CUTOFF, GL_CONSTANT_ATTENUATION, GL_LINEAR_ATTENUATION, and GL_QUADRATIC_ATTENUATION.
`GetMaterial (target, pname)`
Return material parametersOpenGL Documentation: glGetMaterial
-
`target`Specifies which of the two materials is being queried. GL_FRONT or GL_BACK are accepted, representing the front and back materials, respectively.
-
`pname`Specifies the material parameter to return. GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_EMISSION, GL_SHININESS, and GL_COLOR_INDEXES are accepted.
`GetString (name)`
Return a string describing the current GL connectionOpenGL Documentation: glGetString
- `name`Specifies a symbolic constant, one of GL_VENDOR, GL_RENDERER, GL_VERSION, GL_SHADING_LANGUAGE_VERSION, or GL_EXTENSIONS.
`GetTexEnv (target, pname)`
Return texture environment parametersOpenGL Documentation: glGetTexEnv
-
`target`Specifies a texture environment. May be GL_TEXTURE_ENV, GL_TEXTURE_FILTER_CONTROL, or GL_POINT_SPRITE.
-
`pname`Specifies the symbolic name of a texture environment parameter. Accepted values are GL_TEXTURE_ENV_MODE, GL_TEXTURE_ENV_COLOR, GL_TEXTURE_LOD_BIAS, GL_COMBINE_RGB, GL_COMBINE_ALPHA, GL_SRC0_RGB, GL_SRC1_RGB, GL_SRC2_RGB, GL_SRC0_ALPHA, GL_SRC1_ALPHA, GL_SRC2_ALPHA, GL_OPERAND0_RGB, GL_OPERAND1_RGB, GL_OPERAND2_RGB, GL_OPERAND0_ALPHA, GL_OPERAND1_ALPHA, GL_OPERAND2_ALPHA, GL_RGB_SCALE, GL_ALPHA_SCALE, or GL_COORD_REPLACE.
`GetTexGen (coord, pname)`
Return texture coordinate generation parametersOpenGL Documentation: glGetTexGen
-
`coord`Specifies a texture coordinate. Must be GL_S, GL_T, GL_R, or GL_Q.
-
`pname`Specifies the symbolic name of the value(s) to be returned. Must be either GL_TEXTURE_GEN_MODE or the name of one of the texture generation plane equations: GL_OBJECT_PLANE or GL_EYE_PLANE.
`GetTexLevelParameter (target, level, pname)`
Return texture parameter values for a specific level of detailOpenGL Documentation: glGetTexLevelParameter
-
`target`Specifies the symbolic name of the target texture, either GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, GL_PROXY_TEXTURE_1D, GL_PROXY_TEXTURE_2D, GL_PROXY_TEXTURE_3D, GL_TEXTURE_CUBE_MAP_POSITIVE_X, GL_TEXTURE_CUBE_MAP_NEGATIVE_X, GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, GL_TEXTURE_CUBE_MAP_POSITIVE_Z, GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, or GL_PROXY_TEXTURE_CUBE_MAP.
-
`level`Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n is the nth mipmap reduction image.
-
`pname`Specifies the symbolic name of a texture parameter. GL_TEXTURE_WIDTH, GL_TEXTURE_HEIGHT, GL_TEXTURE_DEPTH, GL_TEXTURE_INTERNAL_FORMAT, GL_TEXTURE_BORDER, GL_TEXTURE_RED_SIZE, GL_TEXTURE_GREEN_SIZE, GL_TEXTURE_BLUE_SIZE, GL_TEXTURE_ALPHA_SIZE, GL_TEXTURE_LUMINANCE_SIZE, GL_TEXTURE_INTENSITY_SIZE, GL_TEXTURE_DEPTH_SIZE, GL_TEXTURE_COMPRESSED, and GL_TEXTURE_COMPRESSED_IMAGE_SIZE are accepted.
`GetTexParameter (target, pname)`
Return texture parameter valuesOpenGL Documentation: glGetTexParameter
-
`target`Specifies the symbolic name of the target texture. GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, and GL_TEXTURE_CUBE_MAP are accepted.
-
`pname`Specifies the symbolic name of a texture parameter. GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_PRIORITY, GL_TEXTURE_RESIDENT, GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_DEPTH_TEXTURE_MODE, and GL_GENERATE_MIPMAP are accepted.
`Hint (target, mode)`
Specify implementation-specific hintsOpenGL Documentation: glHint
-
`target`Specifies a symbolic constant indicating the behavior to be controlled. GL_FOG_HINT, GL_GENERATE_MIPMAP_HINT, GL_LINE_SMOOTH_HINT, GL_PERSPECTIVE_CORRECTION_HINT, GL_POINT_SMOOTH_HINT, GL_POLYGON_SMOOTH_HINT, GL_TEXTURE_COMPRESSION_HINT, and GL_FRAGMENT_SHADER_DERIVATIVE_HINT are accepted.
-
`mode`Specifies a symbolic constant indicating the desired behavior. GL_FASTEST, GL_NICEST, and GL_DONT_CARE are accepted.
`Index (c)`
Set the current color indexOpenGL Documentation: glIndex
- `c`Specifies the new value for the current color index.
`IndexMask (mask)`
Control the writing of individual bits in the color index buffersOpenGL Documentation: glIndexMask
- `mask`Specifies a bit mask to enable and disable the writing of individual bits in the color index buffers. Initially, the mask is all 1's.
`InitNames ()`
Initialize the name stackOpenGL Documentation: glInitNames
`IsEnabled (cap)`
Test whether a capability is enabledOpenGL Documentation: glIsEnabled
- `cap`Specifies a symbolic constant indicating a GL capability.
`IsList ( list )`
Determine if a name corresponds to a display listOpenGL Documentation: glIsList
- `list`Specifies a symbolic constant indicating a GL capability.
`IsTexture (texture)`
Determine if a name corresponds to a textureOpenGL Documentation: glIsTexture
- `texture`Specifies a value that may be the name of a texture.
`Light (light, pname, params)`
Set light source parametersOpenGL Documentation: glLight
-
`light`Specifies a light. The number of lights depends on the implementation, but at least eight lights are supported. They are identified by symbolic names of the form GL_LIGHTi, where i ranges from 0 to the value of GL_MAX_LIGHTS - 1.
-
`pname`Specifies a light source parameter for light. GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_POSITION, GL_SPOT_CUTOFF, GL_SPOT_DIRECTION, GL_SPOT_EXPONENT, GL_CONSTANT_ATTENUATION, GL_LINEAR_ATTENUATION, and GL_QUADRATIC_ATTENUATION are accepted.
-
`params`Specifies the value that parameter pname of light source light will be set to.
`LightModel (pname, params)`
Set the lighting model parametersOpenGL Documentation: glLightModel
-
`pname`Specifies a single-valued lighting model parameter. GL_LIGHT_MODEL_LOCAL_VIEWER, GL_LIGHT_MODEL_COLOR_CONTROL, and GL_LIGHT_MODEL_TWO_SIDE are accepted.
-
`params`Specifies the value that param will be set to.
`LineStipple (factor, pattern)`
Specify the line stipple patternOpenGL Documentation: glLineStipple
-
`factor`Specifies a multiplier for each bit in the line stipple pattern. If factor is 3, for example, each bit in the pattern is used three times before the next bit in the pattern is used. factor is clamped to the range [1, 256] and defaults to 1.
-
`pattern`Specifies a 16-bit integer whose bit pattern determines which fragments of a line will be drawn when the line is rasterized. Bit zero is used first; the default pattern is all 1's.
`LineWidth (width)`
Specify the width of rasterized linesOpenGL Documentation: glLineWidth
- `width`Specifies the width of rasterized lines. The initial value is 1.
`ListBase (base)`
Set the display-list base for glCallListsOpenGL Documentation: glListBase
- `base`Specifies an integer offset that will be added to glCallLists offsets to generate display-list names. The initial value is 0.
`LoadIdentity ()`
Replace the current matrix with the identity matrixOpenGL Documentation: glLoadIdentity
`LoadMatrix (m)`
Replace the current matrix with the specified matrixOpenGL Documentation: glLoadMatrix
- `m`Specifies 16 consecutive values, which are used as the elements of a 4×4 column-major matrix.
`LoadName (name)`
Load a name onto the name stackOpenGL Documentation: glLoadName
- `name`Specifies a name that will replace the top value on the name stack.
`LogicOp (opcode)`
Specify a logical pixel operation for color index renderingOpenGL Documentation: glLogicOp
- `opcode`Specifies a symbolic constant that selects a logical operation. The following symbols are accepted: GL_CLEAR, GL_SET, GL_COPY, GL_COPY_INVERTED, GL_NOOP, GL_INVERT, GL_AND, GL_NAND, GL_OR, GL_NOR, GL_XOR, GL_EQUIV, GL_AND_REVERSE, GL_AND_INVERTED, GL_OR_REVERSE, and GL_OR_INVERTED. The initial value is GL_COPY.
`Material (face, pname, params)`
Specify material parameters for the lighting modelOpenGL Documentation: glMaterial
-
`face`Specifies which face or faces are being updated. Must be one of GL_FRONT, GL_BACK, or GL_FRONT_AND_BACK.
-
`pname`Specifies the material parameter of the face or faces that is being updated. Must be one of GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_EMISSION, GL_SHININESS, GL_AMBIENT_AND_DIFFUSE, or GL_COLOR_INDEXES.
-
`params`Specifies a pointer to the value or values that pname will be set to.
`MatrixMode (mode)`
Specify which matrix is the current matrixOpenGL Documentation: glMatrixMode
- `mode`Specifies which matrix stack is the target for subsequent matrix operations. Three values are accepted: GL_MODELVIEW, GL_PROJECTION, and GL_TEXTURE. The initial value is GL_MODELVIEW. Additionally, if the ARB_imaging extension is supported, GL_COLOR is also accepted.
`MultMatrix (m)`
Multiply the current matrix with the specified matrixOpenGL Documentation: glMultMatrix
- `m`Specifies 16 consecutive values, which are used as the elements of a 4×4 column-major matrix.
`NewList ( list , mode)`
Create or replace a display listOpenGL Documentation: glNewList
-
`list`Specifies the display-list name.
-
`mode`Specifies the compilation mode, which can be GL_COMPILE or GL_COMPILE_AND_EXECUTE.
`Normal (...)`
Set the current normal vectorOpenGL Documentation: glNormal
- `...`Either a 3 numbers or a table specifying the x, y, and z coordinates of the new current normal. The initial value of the current normal is the unit vector, (0, 0, 1).
`Ortho (left, right, bottom, top, near, far)`
Multiply the current matrix with an orthographic matrixOpenGL Documentation: glOrtho
-
`left`Specify the coordinates for the left vertical clipping plane.
-
`right`Specify the coordinates for the right vertical clipping plane.
-
`bottom`Specify the coordinates for the bottom horizontal clipping plane.
-
`top`Specify the coordinates for the top horizontal clipping plane.
-
`near`Specify the distances to the nearer depth clipping plane. This value is negative if the plane is to be behind the viewer.
-
`far`Specify the distances to the farther depth clipping plane. This value is negative if the plane is to be behind the viewer.
`PassThrough (token)`
Place a marker in the feedback bufferOpenGL Documentation: glPassThrough
- `token`Specifies a marker value to be placed in the feedback buffer following a GL_PASS_THROUGH_TOKEN.
`PixelStore (pname, param)`
Set pixel storage modesOpenGL Documentation: glPixelStore
-
`pname`Specifies the symbolic name of the parameter to be set. Six values affect the packing of pixel data into memory: GL_PACK_SWAP_BYTES, GL_PACK_LSB_FIRST, GL_PACK_ROW_LENGTH, GL_PACK_IMAGE_HEIGHT, GL_PACK_SKIP_PIXELS, GL_PACK_SKIP_ROWS, GL_PACK_SKIP_IMAGES, and GL_PACK_ALIGNMENT. Six more affect the unpacking of pixel data from memory: GL_UNPACK_SWAP_BYTES, GL_UNPACK_LSB_FIRST, GL_UNPACK_ROW_LENGTH, GL_UNPACK_IMAGE_HEIGHT, GL_UNPACK_SKIP_PIXELS, GL_UNPACK_SKIP_ROWS, GL_UNPACK_SKIP_IMAGES, and GL_UNPACK_ALIGNMENT.
-
`param`Specifies the value that pname is set to.
`PixelTransfer (pname, param)`
Set pixel transfer modesOpenGL Documentation: glPixelTransfer
-
`pname`Specifies the symbolic name of the pixel transfer parameter to be set. Must be one of the following: GL_MAP_COLOR, GL_MAP_STENCIL, GL_INDEX_SHIFT, GL_INDEX_OFFSET, GL_RED_SCALE, GL_RED_BIAS, GL_GREEN_SCALE, GL_GREEN_BIAS, GL_BLUE_SCALE, GL_BLUE_BIAS, GL_ALPHA_SCALE, GL_ALPHA_BIAS, GL_DEPTH_SCALE, or GL_DEPTH_BIAS.
-
`param`Specifies the value that pname is set to.
`PixelZoom (xfactor, yfactor)`
Specify the pixel zoom factorsOpenGL Documentation: glPixelZoom
-
`xfactor`Specify the x zoom factor for pixel write operations.
-
`yfactor`Specify the y zoom factor for pixel write operations.
`PointSize (size)`
Specify the diameter of rasterized pointsOpenGL Documentation: glPointSize
- `size`Specifies the diameter of rasterized points. The initial value is 1.
`PolygonMode (face, mode)`
Select a polygon rasterization modeOpenGL Documentation: glPolygonMode
-
`face`Specifies the polygons that mode applies to. Must be GL_FRONT for front-facing polygons, GL_BACK for back-facing polygons, or GL_FRONT_AND_BACK for front- and back-facing polygons.
-
`mode`Specifies how polygons will be rasterized. Accepted values are GL_POINT, GL_LINE, and GL_FILL. The initial value is GL_FILL for both front- and back-facing polygons.
`PolygonOffset (factor, units)`
Set the scale and units used to calculate depth valuesOpenGL Documentation: glPolygonOffset
-
`factor`Specifies a scale factor that is used to create a variable depth offset for each polygon. The initial value is 0.
-
`units`Is multiplied by an implementation-specific value to create a constant depth offset. The initial value is 0.
`PopAttrib ()`
Pop the server attribute stackOpenGL Documentation: glPopAttrib
`PopClientAttrib ()`
Pop the client attribute stackOpenGL Documentation: glPopClientAttrib
`PopMatrix ()`
Pop the current matrix stackOpenGL Documentation: glPopMatrix
`PopName ()`
Pop the name stackOpenGL Documentation: glPopName
`PushAttrib (mask)`
Push the server attribute stackOpenGL Documentation: glPushAttrib
- `mask`Specifies a mask that indicates which attributes to save.
`PushClientAttrib ()`
Push the client attribute stackOpenGL Documentation: glPushClientAttrib
`PushMatrix ()`
Push the current matrix stackOpenGL Documentation: glPushMatrix
`PushName (name)`
Push the name stackOpenGL Documentation: glPushName
- `name`Specifies a name that will be pushed onto the name stack.
`RasterPos (..)`
Specify the raster position for pixel operationsOpenGL Documentation: glRasterPos
- `..`Specifies an array or list of values of two, three, or four elements, specifying x, y, z, and w coordinates, respectively.
`ReadBuffer (mode)`
Select a color buffer source for pixelsOpenGL Documentation: glReadBuffer
- `mode`Specifies a color buffer. Accepted values are GL_FRONT_LEFT, GL_FRONT_RIGHT, GL_BACK_LEFT, GL_BACK_RIGHT, GL_FRONT, GL_BACK, GL_LEFT, GL_RIGHT, and GL_AUXi, where i is between 0 and the value of GL_AUX_BUFFERS minus 1.
`Rect (...)`
Draw a rectangleOpenGL Documentation: glRect
- `...`Specify the vertices of a rectangle as an array or list of 4 values.
`RenderMode (mode)`
Set rasterization modeOpenGL Documentation: glRenderMode
- `mode`Specifies the rasterization mode. Three values are accepted: GL_RENDER, GL_SELECT, and GL_FEEDBACK. The initial value is GL_RENDER.
`Rotate (...)`
Multiply the current matrix by a rotation matrixOpenGL Documentation: glRotate
- `...`Specify an array or list of 4 values with the order being the angle of rotation in degrees and then the the x, y, and z coordinates of a vector, respectively
`Scale (...)`
Multiply the current matrix by a general scaling matrixOpenGL Documentation: glScale
- `...`Specify an array or list of 3 values of scale factors along the x, y, and z axes, respectively
`Scissor (x, y, width, height)`
Define the scissor boxOpenGL Documentation: glScissor
-
`x`Specify the x-coordinate of the lower left corner of the scissor box.
-
`y`Specify the y-coordinate of the lower left corner of the scissor box.
-
`width`Specify the width of the scissor box.
-
`height`Specify the height of the scissor box.
`ShadeModel (mode)`
Select flat or smooth shadingOpenGL Documentation: glShadeModel
- `mode`Specifies a symbolic value representing a shading technique. Accepted values are GL_FLAT and GL_SMOOTH. The initial value is GL_SMOOTH.
`StencilFunc (func, ref, mask)`
Set front and back function and reference value for stencil testingOpenGL Documentation: glStencilFunc
-
`func`Specifies the test function. Eight symbolic constants are valid: GL_NEVER, GL_LESS, GL_LEQUAL, GL_GREATER, GL_GEQUAL, GL_EQUAL, GL_NOTEQUAL, and GL_ALWAYS. The initial value is GL_ALWAYS.
-
`ref`Specifies the reference value for the stencil test. ref is clamped to the range 0 2 n-1 , where n is the number of bitplanes in the stencil buffer. The initial value is 0.
-
`mask`Specifies a mask that is ANDed with both the reference value and the stored stencil value when the test is done. The initial value is all 1's.
`StencilMask (mask)`
Control the front and back writing of individual bits in the stencil planesOpenGL Documentation: glStencilMask
- `mask`Specifies a bit mask to enable and disable writing of individual bits in the stencil planes. Initially, the mask is all 1's.
`StencilOp (sfail, dpfail, dppass)`
Set front and back stencil test actionsOpenGL Documentation: glStencilOp
-
`sfail`Specifies the action to take when the stencil test fails. Eight symbolic constants are accepted: GL_KEEP, GL_ZERO, GL_REPLACE, GL_INCR, GL_INCR_WRAP, GL_DECR, GL_DECR_WRAP, and GL_INVERT. The initial value is GL_KEEP.
-
`dpfail`Specifies the stencil action when the stencil test passes, but the depth test fails. dpfail accepts the same symbolic constants as sfail. The initial value is GL_KEEP.
-
`dppass`Specifies the stencil action when both the stencil test and the depth test pass, or when the stencil test passes and either there is no depth buffer or depth testing is not enabled. dppass accepts the same symbolic constants as sfail. The initial value is GL_KEEP.
`TexCoord (..)`
Set the current texture coordinatesOpenGL Documentation: glTexCoord
- `..`Specifies an array or list of one, two, three, or four elements, which in turn specify the s, t, r, and q texture coordinates.
`TexEnv (target, pname, param)`
Set texture environment parametersOpenGL Documentation: glTexEnv
-
`target`Specifies a texture environment. May be GL_TEXTURE_ENV, GL_TEXTURE_FILTER_CONTROL or GL_POINT_SPRITE.
-
`pname`Specifies the symbolic name of a single-valued texture environment parameter. May be either GL_TEXTURE_ENV_MODE, GL_TEXTURE_LOD_BIAS, GL_COMBINE_RGB, GL_COMBINE_ALPHA, GL_SRC0_RGB, GL_SRC1_RGB, GL_SRC2_RGB, GL_SRC0_ALPHA, GL_SRC1_ALPHA, GL_SRC2_ALPHA, GL_OPERAND0_RGB, GL_OPERAND1_RGB, GL_OPERAND2_RGB, GL_OPERAND0_ALPHA, GL_OPERAND1_ALPHA, GL_OPERAND2_ALPHA, GL_RGB_SCALE, GL_ALPHA_SCALE, or GL_COORD_REPLACE.
-
`param`Specifies a single symbolic constant, one of GL_ADD, GL_ADD_SIGNED, GL_INTERPOLATE, GL_MODULATE, GL_DECAL, GL_BLEND, GL_REPLACE, GL_SUBTRACT, GL_COMBINE, GL_TEXTURE, GL_CONSTANT, GL_PRIMARY_COLOR, GL_PREVIOUS, GL_SRC_COLOR, GL_ONE_MINUS_SRC_COLOR, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, a single boolean value for the point sprite texture coordinate replacement, a single floating-point value for the texture level-of-detail bias, or 1.0, 2.0, or 4.0 when specifying the GL_RGB_SCALE or GL_ALPHA_SCALE.
`TexGen (coord, pname, param)`
Control the generation of texture coordinatesOpenGL Documentation: glTexGen
-
`coord`Specifies a texture coordinate. Must be one of GL_S, GL_T, GL_R, or GL_Q.
-
`pname`Specifies the symbolic name of the texture-coordinate generation function. Must be GL_TEXTURE_GEN_MODE.
-
`param`Specifies a single-valued texture generation parameter, one of GL_OBJECT_LINEAR, GL_EYE_LINEAR, GL_SPHERE_MAP, GL_NORMAL_MAP, or GL_REFLECTION_MAP.
`TexParameter (target, pname, param)`
Set texture parametersOpenGL Documentation: glTexParameter
-
`target`Specifies the target texture, which must be either GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D, or GL_TEXTURE_CUBE_MAP.
-
`pname`Specifies the symbolic name of a single-valued texture parameter. pname can be one of the following: GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R, GL_TEXTURE_PRIORITY, GL_TEXTURE_COMPARE_MODE, GL_TEXTURE_COMPARE_FUNC, GL_DEPTH_TEXTURE_MODE, or GL_GENERATE_MIPMAP.
-
`param`Specifies the value of pname.
`Translate (...)`
Multiply the current matrix by a translation matrixOpenGL Documentation: glTranslate
- `...`Specify an array or list of 3 values of translation vector
`Vertex (..)`
Specify a vertexOpenGL Documentation: glVertex
- `..`Specifies an array or list of two, three, or four elements, which in turn specify the x, y, z, and w vertex coordinates.
`Viewport (x, y, width, height)`
Set the viewportOpenGL Documentation: glViewport
-
`x`Specify the x-coordinate of the lower left corner of the viewport rectangle.
-
`y`Specify the y-coordinate of the lower left corner of the viewport rectangle.
-
`width`Specify the width of the viewport rectangle.
-
`height`Specify the height of the viewport rectangle.
