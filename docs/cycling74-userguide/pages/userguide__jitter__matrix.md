---
title: "Matrices"
source: https://docs.cycling74.com/userguide/jitter/matrix/
source_path: /userguide/jitter/matrix/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Matrices

Source: https://docs.cycling74.com/userguide/jitter/matrix/

## Extracted Text

# Jitter Matrix
A Matrix holds multidimensional, numeric data. Each matrix has one or more dimensions, in addition to one or more planes. You can think of a matrix as a grid, where each cell of the grid holds a list of numbers. The length of the list in each cell is the number of planes.
A three-by-three matrix. You can see that, since this is a three-plane matrix, each cell contains three values as well.
When a matrix holds an image or a frame of video data, it's equivalent to a two-dimensional array, where each cell represents one pixel. The dimension of the matrix would correspond to the resolution of the image or frame, and there would be one plane for each channel of color data (typically red, green and blue), possibly with one additional channel for alpha. Every cell of a matrix must have the same data type, with the possible types being`char`,`long`,`float32`, and`float64`.
## Quick Reference
Operation Objects
Create a matrix jit.matrix
Display a matrix jit.window , jit.pwindow
Getting and setting values jit.fill , jit.spill , jit.iter
Viewing matrix data jit.cellblock , jit.print
Getting matrix descriptors jit.matrixinfo , jit.fpsgui , getattr
Splitting and combining matrices jit.pack , jit.unpack , jit.submatrix , jit.concat , jit.dimmap
Re-interpreting matrix data jit.coerce
## Matrix processing
Matrix processing will always happen on the CPU, which has advantages and disadvantages. In general, graphics processing can happen on the CPU (Central Processing Unit) or the GPU (Graphics Processing Unit). CPU processing is sequential and generally slower, but can support certain operations that GPU processing cannot. GPU processing is highly parallel and often much faster, but can be more restricted. For video and graphics programming, Max has objects and data structures supporting both kinds of processing. For GPU-based processing, use the`jit.gl.*`and`jit.fx.*`families of objects, which make use of textures instead of matrices.
## Creating a Matrix
Create an empty matrix by creating a jit.matrix object. The object arguments determine its plane count, data type, and dimension size.
### Named matrices
Like other named storage types , each matrix has a unique name. Objects that send matrices to each other send messages like`jit_matrix u12345678`, where`u12345678`is the name of the matrix. Since you can refer to matrices by name, It's possible to define a matrix in one part of your patcher and use it in another.
The matrix named my_matrix is defined in one part of the patcher, but is referred to by name and used in another part of the patcher.
### Loading from a video or image
You can fill a matrix with the contents of a video or image file with the`importmovie`message. If you're loading a video file, you can supply a time offset to load a particular frame. The jit.matrix object can only load a single image frame this way. To work with videos, use jit.movie , jit.playlist , or jit.matrixset .
### Patcher cords
Objects that send out a Jitter matrix will style their outgoing patch cord with black and green stripes. This is only cosmetic, as these just carry regular Max messages of the form`jit_matrix u12345678`. However, the special styling helps to distinguish matrix patch cords from other patch cords.
Even though they have special styling, patch cords carrying Jitter matrices are just carrying regular Max lists. You can work with them in the same way as any other Max message.
## Coordinates
Jitter matrixes index from the top left, meaning the origin`<0, 0>`is in the top left corner. If the matrix is 101 cells wide, then`<50, 50>`is in the center,`<100, 0>`is the top right, and`<0, 100>`is the bottom left.
## Frames, Colors, ARGB
Matrices can hold arbitrary data, but Jitter objects that operate on image frames will interpret each plane as corresponding to a particular color. Most Jitter objects work in ARGB format, expecting the first plane of a matrix to represent alpha, the second the red color value, the third green, and the final plane blue. If the type of the matrix is`char`or`long`, then the maximum value of a cell, when interpreted as a color, is 255. For`float32`or`float64`types, the maximum value for a particular color chanel is 1.0.
Value Type Color
255 255 255 char White
1.0 1.0 1.0 float32 White
255 0 0 char Red
1.0 0 0 float32 Red
128 128 128 char Medium gray
0.5 0.5 0.5 float32 Medium gray
When viewing a three plane matrix in a jit.window or a jit.pwindow , Jitter will assume RGB format instead. You can change the color display mode of a jit.pwindow or a jit.window by setting the`@colormode`attribute
## Data Types
Jitter matrices support four data types:
Type Description
char unsigned 8-bit integer (0 to 255)
long signed 32-bit integer
float32 32-bit floating point number
float64 64-bit floating point number
There aren't very many use cases for a`long`matrix. One of the few is when working with jit.repos , which would let you specify more than 255 pixel offsets.
## Getting and Setting Values
Fetch values from a matrix with the`getcell`message. For example, the message`getcell 9 19`would retrieve the value in the 10th column (since we're indexing from zero) and the 20th row. The jit.matrix object will send the contents of the cell as a list out of its right outlet. The length of the list will be the plane count of the matrix.
For setting the values of a matrix, the most common ways are with the`setcell`,`setall`, and`exprfill`messages. The`setcell`message simply sets the value of one cell to a given value. The message`setcell 1 2 val 255 255 0 255`would set the cell at coordinates`<1, 2>`to the value`255 255 0 255`. The`setall`message fills the whole matrix with a particular value, so the message`setall 0 255 0 255`would set every cell of the matrix to the value`0 255 0 255`. Finally, the`exprfill`message lets you fill a matrix parametrically, according to a function that will be evaluated for each cell of the matrix. For more on the expression language used here, see Jitter expr .
### Helpful objects for getting and setting values
A handful of jitter objects support setting and retrieving values from a matrix using lists. The jit.fill object lets you "fill" a matrix using a list. Note that jit.fill references a matrix by name, and doesn't output a matrix itself.
Going in the other direction, jit.spill can output a matrix as a list. The attributes`@plane`and`@offset`determine the plane and offset into the matrix. The`@listlength`attribute lets you set the length of the output list.
One more object that serves a similar function is the object jit.iter . This object will output each each cell of the input matrix one at a time, along with the coordinates of each cell.
## Adapting and Interpolating
If a jit.matrix object receives a matrix as input that does not match the dimensions of the internal matrix, the object can adapt to or interpolate the incoming data. Interpolating means creating in-between values to fill in gaps where needed. If a 100 by 100 cell jit.matrix object receives a 10 by 10 cell input, it can interpolate to fill in the missing values. Interpolation is off by default. Use the`@interp`attribute to control interpolation.
When enabled, jit.matrix will smoothly interpolate when asked to scale up an input matrix
By default, the arguments to a jit.matrix object determine the plane count, type, and dimensions of the internal matrix. If you enable the`@adapt`attribute, then jit.matrix will change its properties to match the dimensions of the incoming matrix, including plane count, dimensions, and type. An empty jit.matrix object with no arguments will have`@adapt`enabled by default.
If @adapt is enabled, a jit.matrix will update its dimensions to match an input matrix.
## Inspecting Matrices
### Viewing as images
The jit.window and jit.pwindow objects will display whatever matrix they receive as an image. So, jit.pwindow is a great way to monitor a video stream in a running patcher. The jit.window object is often used as a final render destination, where a series of Jitter processes modify a matrix, and then a jit.window presents the final result.
jit.pwindow and jit.window are useful for viewing matrices, and they can also be used to view textures.
### Matrix descriptors
Several objects can get information about the dimension, plane count, type, or other descriptors of a particular matrix. The jit.fpsgui object can be configured to display any of these descriptors, in addition to the frame rate of a stream of matrices.
The jit.fpsgui object shows useful info about a matrix
If you want to retrieve these same matrix descriptors as Max messages, for further downstream processing, use either the jit.matrixinfo object, or use the getattr object to fetch these values as attributes from a matrix. Both methods are equally efficient and idiomatic, the main difference is that jit.matrixinfo processes an incoming matrix, while getattr must attach to a jit.matrix object.
The jit.matrixinfo object reports on the descriptors of an incoming matrix. These same descriptors are available as attributes, so the getattr object can also retrieve them.
### Matrix contents
For viewing the contents of a jit.matrix object as numerical data, use the jit.cellblock object. It can display a one or two dimensional matrix in a "spreadsheet" format. You can choose which plane of the matrix to view by sending the message`plane $1`, where`$1`is the plane of the matrix that you want to display. You can also send the message`plane -1`to view all planes of the matrix simultaneously, with each cell containing a list.
The jit.cellblock object can only display matrices with less than two dimensions. For larger matrices, first split the matrix with jit.submatrix , pass the matrix through jit.dimmap to cut out redundant dimensions, then pass the result through a jit.matrix to copy the matrix reference to a format that jit.cellblock can use. See Splitting by dimension for more details.
Use the jit.cellblock object to view a matrix as numerical cells
Finally, the jit.print object can print the entire contents of any matrix of any number of dimensions and planes.
## Splitting and Recombining Matrices
It's possible to split and recombine matrices across planes or across dimensions. Use jit.unpack and jit.pack to recombine matrices by plane, and use jit.submatrix and jit.concat to recombine by dimension.
### Splitting and remapping planes
By default, the jit.unpack object will split a 4-plane matrix into four single-plane matrices, but you can pass an argument to split into a different number of single planes.
The default configuration of jit.unpack splits a 4-plane ARGB matrix into four single-plane matrices.
If you want to split a multiple-plane matrix into other multiple-plane matrices, use the`@offset`and`@jump`attributes to configure jit.unpack . Arguments following`@offset`indicate, for each outlet, which plane in the input matrix to start reading from. Argments following`@jump`indicate, for each outlet, how many planes to read from the input.
Setting Outlet 1 Outlet 2 Outlet 3
`jit.unpack 2 @offset 0 1 @jump 2 2`two-plane matrix, from planes 0 and 1 of the input matrix two-plane matrix, from planes 1 and 2 of the input matrix none
`jit.unpack 2 @offset 0 3 @jump 3 1`three-plane matrix, from planes 0, 1, and 2 of the input matrix one-plane matrix, from plane 3 of the input matrix none
`jit.unpack 3 @offset 1 2 3 @jump 1 1 1`one-plane matrix from plane 1 one-plane matrix from plane 2 one-plane matrix from plane 3
With @offset and @jump, you can configure jit.unpack to output multiplane matrices.
The jit.pack object combines input matrices into a single multi-plane matrix. Like jit.unpack , it by default expects four input matrices, and the first argument determines the number of inlets.
jit.pack combines mutiple input matrices into a single multi-plane matrix
Using`@offset`and`@jump`, you can combine several multi-plane matrices together. The`@offset`attribute controls the offset into each input matrix (at each inlet), and the`@jump`attribute determines how many planes to pull from each input matrix. The final plane count will the the sum of all the arguments to`@jump`.
Setting Output
`jit.pack 2 @offset 0 0 @jump 2 2`four-plane matrix, with two planes from the first inlet and two planes from the second inlet
`jit.pack 2 @offset 0 0 @jump 1 3`four-plane matrix, with one plane from the first inlet and two planes from the second inlet
`jit.pack 2 @offset 0 2 @jump 2 2`four-plane matrix, with two planes from the first inlet and two from the second inlet. The first two planes of the second input matrix are skipped. This would combine the alpha and red channels of the first input with the green and blue channels of the second.
The jit.matrix object can also remap planes directly, without using any other objects. The`@planemap`attribute controls the mapping between input and output planes.
Setting Result
`jit.matrix 4 @planemap 0 1 2 3`Map the first plane of the input (at index zero) to the first plane of the output, the second plane of the input to the second plane of the output, and so on. In other words, leave the input unchanged.
`jit.matrix 4 @planemap 0 0 0 0`Map the first plane of the input to each of the four output channels. This makes a 4-plane matrix from just the first plane of the input.
`jit.matrix 4 @planemap 1 2 3 0`Shift input planes over by one, effectively converting ARGB format to RGBA format.
### Splitting and remapping dimensions
One way to split an input matrix is with the`@srcdimstart`,`@srcdimend`,`@dstdimstart`, and`@dstdimend`attributes. When a jit.matrix object receives an input matrix, it will look at these attributes to determine how the input is copied into the internal matrix. It's important to note that these attributes will have no effect unless the`@usesrcdim`and`@usedstdim`attributes are enabled.
The source and destination dimensions can control how the input matrix is mapped to the output. This example also shows how if the start and end areas are different in size, the input will grow or shrink as it's mapped to the output.
The jit.submatrix object will let you reference just a portion of the input matrix. The`@dim`attribute determines the size of the portion in each dimension, corresponding to width and height for a two-dimensional matrix. The`@offset`attribute adjusts the offset of the portion, which you could also think of as the x- and y-coordinate of the submatrix.
The @dim attribute determines the size of the submatrix region.
The @offset attribute can shift the submatrix region.
The output of jit.submatrix will have smaller dimensions than the input, but it will never reduce the number of dimensions, even a redundant dimension of size 1. The jit.dimmap object can remove whole dimensions from an input matrix, or insert a redundant dimension. It can also remap and invert dimensions, making it useful for transposing and reversing a matrix.
jit.submatrix will never change the number of dimensions, but jit.dimmap can remove and remap dimensions arbitrarily
Setting Output
`jit.dimmap @map 1 0`Map input dimension 1 to output dimension 0, effectively transposing the input matrix.
`jit.dimmap @map 0 2`Map input dimension 0 to output dimension 0, and input dimension 2 to output dimension 1. This will remove dimension 1 from the input, resulting in a two-dimensional output matrix from a three-dimensional input.
`jit.dimmap @map 0 -1 1`Insert a redundant, size-one dimension between the first and second input dimensions.
`jit.dimmap @map 0 1 @invert 1 0`Leave the input dimensions mapped normally, but flip the first dimension, effectively mirroring an input image from left to right.
To combine or recombine two matrices, use the jit.concat object. The`@concatdim`attribute will determine the dimension along which the two matrices will be concatenated. They do not need to have the same size, although there may be empty space in the resulting concatenated matrix, or some data might be lost if the edges of the two matrices don't line up.
Concatenating two matrices. The @concatdim attribute determines the dimension along with the two matrices are combined.
### More ways to split
There are still other matrix manipulation objects that may be helpful when splitting and recombining matrices:
Object Description
jit.split Split a matrix into two
jit.scissors Cut up a matrix into equal parts
jit.glue Recombine a matrix from multiple parts
jit.multiplex Multiplex (interleave) two matrices into one
jit.demultiplex Demultiplex (deinterleave) one matrix into two
## Coercing
The jit.coerce object can be used to change the interpretation of the contents of a matrix, without copying or changing those contents. For example, you could treat a`long`matrix as if it were a`float32`matrix, or you could treat a 4-plane`char`matrix as a 1-plane`float32`matrix. This is similar to a`cast`operation in many programming languages.
The jit.coerce can change the way the underlying bits of a matrix are interpreted
