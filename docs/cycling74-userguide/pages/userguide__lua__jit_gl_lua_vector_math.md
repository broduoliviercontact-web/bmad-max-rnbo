---
title: "jit.gl.lua Vector Math"
source: https://docs.cycling74.com/userguide/lua/jit_gl_lua_vector_math/
source_path: /userguide/lua/jit_gl_lua_vector_math/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# jit.gl.lua Vector Math

Source: https://docs.cycling74.com/userguide/lua/jit_gl_lua_vector_math/

## Extracted Text

# jit.gl.lua Vector Math
The vector math functions in jit.gl.lua are located in the`vec`module and are organized into six categories. These categories are:- vec.vec2
-
vec.vec3
-
vec.vec4
-
vec.quat
-
vec.mat3
-
vec.mat4 The arguments to all of the vector math functions are tables containing the appropriate number of values for the data type. For example a vec2 is a table with two elements, {1, 2}, while a mat3 has nine elements {1, 2, 3, 4, 5, 6, 7, 8, 9}. The matrices are specified in column-major order so for a mat3, the first three elements are the first column, the second three the second column and so on.
## vec2
`-- res is a 1 or 0 depending on equality res = vec2.equal(v1, v2)-- res is a 1 or 0 depending on equality res = vec2.not_equal(v1, v2)res = vec2.dot(v1, v2)res = vec2.normalize(v)res = vec2.mult(v1, v2)res = vec2.scale(v, s)res = vec2.div(v1, v2)res = vec2.sub(v1, v2)res = vec2.add(v1, v2)res = vec2.mag_sqr(v)res = vec2.mag(v)res = vec2.negate(v)res = vec2.max(v1, v2)res = vec2.lerp(v1, v2, t)`
## vec3
`-- res is a 1 or 0 depending on equality res = vec3.equal(v1, v2)-- res is a 1 or 0 depending on equality res = vec3.not_equal(v1, v2)res = vec3.mult(v1, v2)res = vec3.scale(v, s)res = vec3.div(v1, v2)res = vec3.sub(v1, v2)res = vec3.add(v1, v2)res = vec3.mag_sqr(v)res = vec3.mag(v)res = vec3.negate(v)res = vec3.cross(v1, v2)res = vec3.dot(v1, v2)res = vec3.reflect(v1, v2)-- calculate the normal to a triangle defined by three points res = vec3.normal(p1, p2, p3)res = vec3.normalize(v)res = vec3.max(v1, v2)res = vec3.min(v1, v2)res = vec3.lerp(v1, v2, t)res = vec3.intersect_line_sphere(linepos1, linepos2, sphere_center, sphere_radius)res = vec3.axisx_from_quat(quat)res = vec3.axisy_from_quat(quat)res = vec3.axisz_from_quat(quat)res = vec3.transform_axisangle(axis, angle, v)res = vec3.mult_mat3(v, mat3)res = vec3.centroid3(v1, v2, v3)res = vec3.centroid4(v1, v2, v3, v4)`
## vec4
`-- res is a 1 or 0 depending on equality res = vec4.equal(v1, v2)-- res is a 1 or 0 depending on equality res = vec4.not_equal(v1, v2)res = vec4.mult(v1, v2)res = vec4.scale(v, s)res = vec4.div(v1, v2)res = vec4.sub(v1, v2)res = vec4.add(v1, v2)res = vec4.mag_sqr(v)res = vec4.mag(v)res = vec4.negate(v)res = vec4.dot(v1, v2)res = vec4.normalize(v)res = vec4.max(v1, v2)res = vec4.min(v1, v2)res = vec4.lerp(v1, v2, t)res = vec4.mult_mat4(v, mat4)`
## quat
`-- res is a 1 or 0 depending on equality res = quat.equal(q1, q2)-- res is a 1 or 0 depending on equality res = quat.not_equal(q1, q2)res = quat.mult(q1, q2)res = quat.scale(q, s)res = quat.div(q1, q2)res = quat.add(q1, q2)res = quat.mag_sqr(q)res = quat.mag(q)res = quat.negate(q)res = quat.dot(q1, q2)res = quat.normalize(q)res = quat.max(q1, q2)res = quat.min(q1, q2)res = quat.slerp(q1, q2, t)res = quat.from_mat3(mat3)res = quat.from_mat4(mat4)res = quat.from_axis_angle(axis, angle)res = quat.conj(q)res = quat.from_euler(euler_angles)`
## mat3
`res = mat3.add(m1, m2)res = mat3.mult(m1, m2)res = mat3.transpose(m)res = mat3.mult_vec3(m, v)res = mat3.from_axisangle(axis, angle)res = mat3.from_uv(v1, v2)res = mat3.determinant(m)res = mat3.negate(m)res = mat3.from_mat4(mat4)res = mat3.from_quat(q)`
## mat4
`res = mat4.add(m1, m2)res = mat4.mult(m1, m2)res = mat4.transpose(m)res = mat4.mult_vec4(m, v)res = mat4.from_axisangle(axis, angle)res = mat4.from_uv(v1, v2)res = mat4.determinant(m)res = mat4.negate(m)res = mat4.from_quat(q)res = mat4.look_at(eye, center, up)res = mat4.frustum(left, right, bottom, top, near, far)res = mat4.perspective(fovy, aspect, near, far)res = mat4.ortho(left, right, bottom, top, near, far)`
