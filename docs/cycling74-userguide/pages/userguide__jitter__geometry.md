---
title: "Geometry"
source: https://docs.cycling74.com/userguide/jitter/geometry/
source_path: /userguide/jitter/geometry/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Geometry

Source: https://docs.cycling74.com/userguide/jitter/geometry/

## Extracted Text

# Geometry Objects
The`jit.geom`family of objects, like jit.geom.shape , are a specialized group of Jitter objects designed to work with Half-edge Geometry Structures . This way of representing geometries makes certain kinds of geometry manipulations much easier and more efficient:
- Generating shapes - Use jit.geom.shape to create simple geometries with an arbitrary number of subdivisions.
- Vertex adjustment - The jit.geom.remesh object lets you rearrange the vertices of a geometry, making them more evenly distributed without changing the overall shape. You can add and remove vertices with jit.geom.subdivide and jit.geom.decimate .
- Transformations - Smooth out a geometry with jit.geom.smooth , add roughness or procedural displacement with jit.geom.dimples and jit.geom.displace , or perform more radical transformations with jit.geom.twist , jit.geom.waves , and jit.geom.xform .
- Property generation - Create dynamic, adjustable shapes with lifelike surface properties, using jit.geom.texgen and jit.geom.normgen to generate texture coordinates and surface normals.
## Learning & Examples
Follow the Jitter Geometry tutorial series , or check out some examples of what's possible with these objects:
Example Description
Contours Example of how to make a Jitter geometry look hand-drawn
Fractals Fractal geometries using jit.geom + JavaScript
Point Cloud Generate a point cloud using jit.geom
Thickness Extrude triangles to create volumes
## Half-edge Structure
The Jitter geometry objects represent geometries using a half-edge structure. This structure makes it easy to determine which vertices are adjacent to each other, so that manipulations like extruding, decimating, and remeshing are all possible. The basic idea is that each vertex should maintain a pointer to the next vertex in the shape. This pointer from one vertex to the next is the half-edge that gives the structure its name. Each half-edge also has a twin (sometimes called its opposite) that points from the next vertex back to the original. These two half-edges together make up one edge.
A single triangular face, in a half-edge representation.
One more requirement completes the definition of the half-edge structure, that following the half-edges from one vertex to the next must loop around one face of the 3D shape. You can view the structure of a half-edge geometry as text using jit.geom.todict , which converts the geometry to a structured dictionary .
A half-edge structure as a dictionary
## Creating Geometries
Use the jit.geom.shape object to create a simple geometry, like an icosphere, torus, or cube. You can also use the jit.geom.togeom object to convert a Jitter matrix of triangles into a geometry. Like you see here, it can work with the output of jit.gl.model , but it works just as well with shapes from jit.gl.gridshape , or with any kind of triangular mesh.
Use jit.geom.togeom to convert a Jitter matrix to a geometry
If you're not working with the output of jit.gl.model or jit.gl.gridshape , then you'll need to make sure that the input to jit.geom.togeom follows the standard for 3D surfaces as represented by a Jitter matrix.
## Remeshing, Subdividing, Decimating
You can adjust the shape of a Jitter geometry using various objects.
Object Description
jit.geom.remesh Evenly redistribute vertexes without changing the overall shape
jit.geom.subdivide Subdivide each face into multiple faces, creating new vertices without changing the overall shape
jit.geom.decimate Combine vertices, reducing the number of vertices wihtout changing the overall shape
jit.geom.smooth Smooth out the surface vertices, which will distort the surface of the shape
### Texture coordinates
The jit.geom.remesh algorithm cannot generate texture coordinates. Once a geometry passes through this object, there's no guarantee that the texture coordinates will contain anything useful. You can try to use jit.geom.texgen to generate new texture coordinates, although these won't necessarily correspond to the originals.
Texture coordinates are no longer usable after remesh
## Texture Cooridinates and Surface Normals
Generate new texture coordinates for a Jitter geometry with jit.geom.texgen . The jit.geom.texgen objects has a few different algorithms that it can use to compute new texture coordinates, based on the shape of the geometry. Generate new surface normals with jit.geom.normgen .
## Effect Chains
When chaining multiple Jitter geometry transformation effects together (effects like jit.geom.twist or jit.geom.dimples ), you can use the`@bypass`attribute to route geometries through an object unchanged. This is the right way to work with geometry effects.
Geometry routed through a jit.geom.twist and a jit.geom.waves, using @bypass to skip an effect
Generally, it's not a good idea to treat geometry objects like matrix or texture processing objects, when it comes to using a regular gate object to route geometry computations.
The wrong way to bypass a geometry effect
The`jit.geom`objects are careful to only trigger new computation when necessary. Unlike video effects, where every new frame passes through the whole render chain,`jit.geom`objects only trigger new computation when their internal state changes. When you change the state of the gate object in this example, you're not changing the state of any`jit.geom`object. This won't trigger any new computation, and you won't actually see any change to the geometry.
Of course, you could bang the first object in the`jit.geom`chain to re-trigger computation manually.
## Drawing Geometries
You can draw a Jitter geometry using jit.gl.mesh , after having first converted the geometry to a matrix. The jit.geom.tomesh is slightly more performant, and should be used if you're trying to draw a geometry directly with jit.gl.mesh . If you want to use the geometry for some other purpose, where a Jitter matrix would be more useful, there is alto the jit.geom.tomatrix object to convert a geometry to a full matrix.
If you connect jit.geom.tomesh to a jit.gl.mesh object, it will automatically set the`@drawmode`attribute of jit.gl.mesh to draw the geometry correctly. Otherwise, you should set`@drawmode triangles`on jit.gl.mesh to draw a geometry.
Both of these objects have an attribute`@auto_normals`that will compute surface normals, which may make an explicit jit.geom.normgen unnecessary.
## Asynchrony
By default, the Jitter geometry objects are asynchronous . They process their input on a special thread reserved for geometry calculations. This allows them to handle large, complex inputs, without slowing down video, audio, or other computations. When a Jitter geometry object is actively processing, its appearance will change to show that it's currently working.
When a Jitter geometry object is actively processing, it shows zebra stripes.
Because of this potential asynchrony, when you change a Jitter geometry object's attributes, or when you send it a new geometry, the result may not come out of the object's outlet right away. You can bypass this behavior by setting the`@async`attribute to`0`.
