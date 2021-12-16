import bpy
import bmesh


def create(count=5, width=2.0, depth=0.3, height=0.15):
    vertices = []
    faces = []
    uvs = []

    width /= 2

    f = 0

    # for the front/top island
    uvx_offset1 = width
    uvy_offset1 = 0

    # for the bottom/back islan
    uvx_offset2 = uvx_offset1 + (width * 2) + 0.02
    uvy_offset2 = 0

    for i in range(count):
        # we need to generate the bottom front vertices for the first stair
        if i == 0:
            # bottom, front, left - 0
            vertices.append((-width, i * depth, i * height))
            # bottom, front, right - 1
            vertices.append((width, i * depth, i * height))

        # bottom, back, left - 2
        vertices.append((-width, (i + 1) * depth, i * height))
        # bottom, back, right - 3
        vertices.append((width, (i + 1) * depth, i * height))
        # top, front, left - 4
        vertices.append((-width, i * depth, (i + 1) * height))
        # top, front, right - 5
        vertices.append((width, i * depth, (i + 1) * height))
        # top, back, left - 6
        vertices.append((-width, (i + 1) * depth, (i + 1) * height))
        # top, back, right - 7
        vertices.append((width, (i + 1) * depth, (i + 1) * height))

        faces.append((f, f + 1, f + 5, f + 4))  # front
        #           bottom-front-left      bottom-front-right
        uvs.append(((-width + uvx_offset1, uvy_offset1), (width + uvx_offset1, uvy_offset1),
        #           top-front-right              top-front-left
                   (width + uvx_offset1, uvy_offset1 + height), (-width + uvx_offset1, uvy_offset1 + height)))
        uvy_offset1 += height

        faces.append((f + 7, f + 6, f + 4, f + 5))  # top
        #            top-back-right                top-back-left
        uvs.append(((width + uvx_offset1, uvy_offset1 + depth), (-width + uvx_offset1, uvy_offset1 + depth),
        #           top-front-left         top-front-right
                   (-width + uvx_offset1, uvy_offset1), (width + uvx_offset1, uvy_offset1)))
        uvy_offset1 += (depth + 0.02)

        faces.append((f + 2, f + 3, f + 1, f))  # bottom
        #            bottom-back-right                         bottom-back-left
        uvs.append(((width + uvx_offset2, uvy_offset2 + depth), (-width + uvx_offset2, uvy_offset2 + depth),
        #            bottom-front-left                          bottom-front-right
                   (-width + uvx_offset2, uvy_offset2), (width + uvx_offset2, uvy_offset2)))
        uvy_offset2 += depth

        faces.append((f + 3, f + 2, f + 6, f + 7))  # back
        #           bottom-back-left                    bottom-back-right
        uvs.append(((-width + uvx_offset2, uvy_offset2), (width + uvx_offset2, uvy_offset2),
        #          bottom-top-right                            bottom-top-left
                  (width + uvx_offset2, uvy_offset2 + height), (-width + uvx_offset2, uvy_offset2 + height)))

        uvy_offset2 += (height + 0.02)
        # faces.append((f + 1, f + 3, f + 7, f + 5))  # right
        # faces.append((f + 4, f + 6, f + 2, f))  # left

        f += 6

    return vertices, faces, uvs


vertices, faces, uvs = create(3)

mesh = bpy.data.meshes.new("Stairs")
bm = bmesh.new()

for vert in vertices:
    bm.verts.new(vert)

bm.verts.ensure_lookup_table()
for face in faces:
    bm.faces.new([bm.verts[i] for i in face])

uv_layer = bm.loops.layers.uv.new()
loop = bm.loops.layers.uv[0]
for face, face_uvs in zip(bm.faces, uvs):
    for loop, uv in zip(face.loops, face_uvs):
        loop[uv_layer].uv = uv

bm.to_mesh(mesh)
bm.free()
mesh.update()

print("Create new object with the mesh data")
stairs_obj = bpy.data.objects.new("Stairs", mesh)


view_layer = bpy.context.view_layer
view_layer.active_layer_collection.collection.objects.link(stairs_obj)
