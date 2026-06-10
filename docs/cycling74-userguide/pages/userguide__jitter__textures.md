---
title: "Textures"
source: https://docs.cycling74.com/userguide/jitter/textures/
source_path: /userguide/jitter/textures/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Textures

Source: https://docs.cycling74.com/userguide/jitter/textures/

## Extracted Text

# Textures
A Texture is a collection of data, organized as an array of pixel data and stored in texture memory on the GPU. Textures commonly hold image data—they have the name "texture" because they're often applied to the surface of a 3D model to change its appearance. However, a texture can hold any kind of data that can be expressed as an array of numbers.
An image of chili peppers, mapped as a texture onto the surface of a sphere
Because textures are managed by the GPU, they can be processed much faster than the equivalent matrix , which is managed by the CPU. For tasks like distorting or manipulating an image, it's almost always more efficient to work with a texture than a matrix.
## Creating a Texture
The Max object for managing textures is called jit.gl.texture . Similar to objects like jit.matrix and buffer~ , every Jitter texture has a name, and objects send a message like`jit_gl_matrix u1234567`to other objects to refer to a specific texture. Like matrices, Jitter textures have a dimension and a type . The type of a texture determines the resolution of each pixel. For example, a`char`type can have 256 different values, while a`float32`type can have millions of different values.
If a texture isn't given an explicit name, Max will assign it a unique name automatically.
### Graphics context
All textures are belong to a particular graphics context , usually a window managed by jit.world , or else a view managed by jit.pworld . Use the`@drawto`attribute to explicitly assign a texture to one context or another.
Use @drawto to bind a jit.gl.texture to a particular graphics context.
If you don't assign jit.gl.texture a value for`@drawto`, it will bind to the first graphics context that it can find. If there is more than one graphics context, it's undefined which context it will bind to. It's common to see`@drawto`omitted when there is only one graphics context.
### Loading from a video or image
You can fill a texture with an image by sending it the`read`message. After reading, the texture will store the contents of the image in memory. If you don't give the texture an explicit value for`@dim`, then the dimensions of the texture will adapt to fit the image.
Even though both texture objects loaded the same image, the dimensions are different because one texture does not have an explicit value for @dim.
### Adapt
When a jit.gl.texture receives another texture as input, it copies that input texture. If the`@adapt`attribute is enabled, the jit.gl.texture will also update its dimensions and type to match that of the input. The`@adapt`attribute defaults to active, unless an explicit value for`@dim`is set.
## Texture output
Many Jitter objects have an attribute`@output_texture`that can be enabled in order to configure them for texture output. When streaming video, either from a camera with jit.grab or from a file with jit.movie or jit.playlist , enable`@output_texture`to stream to a texture as opposed to a matrix. Similarly, toggle`@output_texture`on a jit.world object to capture the entire render output as a texture. When using jit.gl.node to render to an offscreen context , use`@capture 1`instead of`@output_texture 1`to get a texture output from jit.gl.node .
Three important objects that can be configured for texture output
## Converting to a Matrix
Remember that Jitter matrices reside on the CPU, while Jitter textures are managed by the GPU. Because of this, converting an texture to a matrix or a matrix to a texture requires copying data from one processor to the other. This can take an undefined amount of time, and so Max provides both a synchronous and an asynchronous method to convert matrices to textures.
### jit.matrix
You can send a Jitter texture directly to a jit.matrix object. Max will read the data from the texture and store it in the matrix. This is the synchronous way of converting a texture to a matrix. It's the fastest way to get the result, but it can block other rendering commands during the data copy. If you're trying to copy a texture to a matrix during a live performance, it's usually better to use jit.gl.asyncread .
### jit.gl.asyncread
This object uses a double-buffering technique to copy data to a matrix without blocking. Because of this, you're safe to use jit.gl.asyncread as much as you want, even during other real-time rendering. However, since the process is asynchronous, you're guaranteed to incur one frame of delay durin the copy. Most of the time this doesn't matter, and it's fine to use jit.gl.asyncread unless you're doing something very specific.
## Procedural Textures
In addition to loading textures from an image file, or copying them from a Jitter matrix, you can also generate texture procedurally.
### jit.gl.pix
The jit.gl.pix object uses the Gen object namespace to define a pixel shader. One way to make a procedural texture is by using the cell , dim , norm , and snorm objects.
A simple procedural shader defined with jit.gl.pix
### jit.gl.slab
The jit.gl.slab object works very similarly to jit.gl.pix , except it load a shader definition from a Jitter XML Shader or JXS description file. Generator shaders like`gn.stripes.jxs`can use texture coordinates to fill a texture procedurally, just like you might do with jit.gl.pix .
## 3D Textures
Most textures have two dimensions, but Jitter supports 3D textures as well. This can be useful when generating your own textures, or when using textures to do simulations or other kinds of computation. To create a 3D texture, simply set the`@dim`attribute of a texture to be a list of three numbers, one for the size of each dimension.
A three-dimensional texture
When working with a 3D texture, you must set the`@rectangle`attribute to zero. This may change with a future version of Max, but it's necessary for now.
You can fill a 3D texture directly by sending it a 3D matrix. As usual when converting from a matrix , Max will simply copy the matrix to the texture. However, you can also use two-dimensional images to fill each slice of the 3D texture one-by-one. If you want to fill a 3D texture using a series of 2D matrices, use the message`subtex_matrix`in conjunction with the`@dstdimstart`and`@dstdimend`attributes. Open the example patcher subtex.3d for a demo.
You can also fill a 3D texture using a series of 2D textures. For this method, set the`@slice`attribute of the 3D texture object before sending it a two-dimensional texture. See the example patcher tex3d.warpy to see how this works in practice.
To pull a 2D texture slice from a 3D texture, you must use a shader program that takes a 3D texture input. The built-in JXS file`td.plane3d.jxs`implements a shader program that can sample a specific slice from a 3D texture using either an`offset`parameter or with a secondary map texture. Use this shader with jit.gl.slab to convert a 3D to a 2D texture.
Copy
Taking a 2D slice from a 3D texture with td.plane3d.jxs and jit.gl.slab
