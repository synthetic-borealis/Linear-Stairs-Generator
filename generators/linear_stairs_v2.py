def create(count=5, width=2.0, depth=0.3, height=0.15):
    UV_GAP = 0.02

    vertices = []
    faces = []
    uvs = []

    width /= 2

    f1 = 0

    uvy_offset = 0

    for i in range(count):
        # Vertices
        if i == 0:
            # bottom, front, left - 0
            vertices.append((-width, 0, 0))
            # bottom, front, right - 1
            vertices.append((width, 0, 0))
        # top, front, left - 2
        vertices.append((-width, i * depth, (i + 1) * height))
        # top, front, left - 3
        vertices.append((width, i * depth, (i + 1) * height))
        # top, back, left - 4
        vertices.append((-width, (i + 1) * depth, (i + 1) * height))
        # top, back, left - 5
        vertices.append((width, (i + 1) * depth, (i + 1) * height))

        # Faces & UVs
        faces.append((f1, f1 + 1, f1 + 3, f1 + 2))  # front
        uvs.append(((0, uvy_offset), (width * 2, uvy_offset),
                    (width * 2, uvy_offset + height), (0, uvy_offset + height)))
        uvy_offset += height

        faces.append((f1 + 5, f1 + 4, f1 + 2, f1 + 3))  # top
        uvs.append(((width * 2, uvy_offset + depth), (0, uvy_offset + depth),
                    (0, uvy_offset), (width * 2, uvy_offset),))
        uvy_offset += depth
        f1 += 4

    # bottom
    top_vert_idx = f1
    uvy_offset = 0
    uvx_offset = width * 2 + UV_GAP
    f1 += 2
    vertices.append((-width, depth, 0))
    vertices.append((width, depth, 0))
    faces.append((f1, f1 + 1, 1, 0))
    uvs.append(((uvx_offset + (width * 2), uvy_offset + depth), (uvx_offset, uvy_offset + depth),
                (uvx_offset, uvy_offset), (uvx_offset + (width * 2), uvy_offset)))
    uvy_offset += depth

    if count > 1:
        vertices.append((-width, depth * count, 0))
        vertices.append((width, depth * count, 0))
        faces.append((f1 + 2, f1 + 3, f1 + 1, f1))
        uvs.append(((uvx_offset + (width * 2), uvy_offset + (depth * (count - 1))), (uvx_offset, uvy_offset + (depth * (count - 1))),
                    (uvx_offset, uvy_offset), (uvx_offset + (width * 2), uvy_offset)))
        uvy_offset += depth * (count - 1)
        f1 += 2

    # back
    for i in range(count):
        if i < count - 1:
            vertices.append((-width, depth * count, height * (i + 1)))
            vertices.append((width, depth * count, height * (i + 1)))
            faces.append((f1 + 2, f1 + 3, f1 + 1, f1))
            uvs.append(((uvx_offset + (width * 2), uvy_offset + height), (uvx_offset, uvy_offset + height),
                        (uvx_offset, uvy_offset), (uvx_offset + (width * 2), uvy_offset)))
            uvy_offset += height
            f1 += 2

    faces.append((top_vert_idx, top_vert_idx + 1, f1 + 1, f1))
    uvs.append(((uvx_offset + (width * 2), uvy_offset + height), (uvx_offset, uvy_offset + height),
                (uvx_offset, uvy_offset), (uvx_offset + (width * 2), uvy_offset)))

    # sides
    uvx_offset_r = uvx_offset + width * 2 + UV_GAP
    uvx_offset_l = uvx_offset_r + depth * count * 2 + UV_GAP
    uvy_offset = 0
    faces_l = []
    uvs_l = []

    # right
    f2 = top_vert_idx + 2
    faces.append((1, f2 + 1, 5, 3))
    uvs.append(((uvx_offset_r, uvy_offset), (uvx_offset_r + depth, uvy_offset),
                (uvx_offset_r + depth, uvy_offset + height), (uvx_offset_r, uvy_offset + height)))

    # left
    faces_l.append((2, 4, f2, 0))
    uvs_l.append(((uvx_offset_l, uvy_offset + height), (uvx_offset_l - depth, uvy_offset + height),
                  (uvx_offset_l - depth, uvy_offset), (uvx_offset_l, uvy_offset)))

    if count > 1:
        uvx_offset_r += depth
        uvx_offset_l -= depth

        # right
        faces.append((f2 + 3, f2 + 5, 5, f2 + 1))
        uvs.append(((uvx_offset_r + depth * (count - 1), uvy_offset), (uvx_offset_r + depth * (count - 1), uvy_offset + height),
                    (uvx_offset_r, uvy_offset + height), (uvx_offset_r, uvy_offset)))

        # left
        faces_l.append((f2, 4, f2 + 4, f2 + 2))
        uvs_l.append(((uvx_offset_l, uvy_offset), (uvx_offset_l, uvy_offset + height),
                      (uvx_offset_l - depth * (count - 1), uvy_offset + height), (uvx_offset_l - depth * (count - 1), uvy_offset)))

        uvy_offset += height

        f2 += 4

        f1 = 4
        for i in range(1, count - 1):
            # right
            faces.append((f1 + 5, f1 + 3, f1 + 1))
            uvs.append(((uvx_offset_r + depth, uvy_offset + height), (uvx_offset_r, uvy_offset + height),
                        (uvx_offset_r, uvy_offset)))
            faces.append((f1 + 1, f2 + 1, f2 + 3, f1 + 5))
            uvs.append(((uvx_offset_r, uvy_offset), (uvx_offset_r + depth * (count - i), uvy_offset),
                        (uvx_offset_r + depth * (count - i), uvy_offset + height), (uvx_offset_r + depth, uvy_offset + height)))

            # left
            faces_l.append((f1, f1 + 2, f1 + 4))
            uvs_l.append(((uvx_offset_l, uvy_offset), (uvx_offset_l, uvy_offset + height),
                          (uvx_offset_l - depth, uvy_offset + height)))
            faces_l.append((f1 + 4, f2 + 2, f2, f1))
            uvs_l.append(((uvx_offset_l - depth, uvy_offset + height), (uvx_offset_l - depth * (count - i), uvy_offset + height),
                          (uvx_offset_l - depth * (count - i), uvy_offset), (uvx_offset_l, uvy_offset)))

            uvy_offset += height
            uvx_offset_r += depth
            uvx_offset_l -= depth

            f1 += 4
            f2 += 2

        # right
        faces.append((f2 + 1, f1 + 5, f1 + 3, f1 + 1))
        uvs.append(((uvx_offset_r + depth, uvy_offset), (uvx_offset_r + depth, uvy_offset + height),
                    (uvx_offset_r, uvy_offset + height), (uvx_offset_r, uvy_offset)))

        # left
        faces_l.append((f1, f1 + 2, f1 + 4, f2))
        uvs_l.append(((uvx_offset_l, uvy_offset), (uvx_offset_l, uvy_offset + height),
                      (uvx_offset_l - depth, uvy_offset + height), (uvx_offset_l - depth, uvy_offset)))

    # append left side faces & UVs
    faces += faces_l
    uvs += uvs_l

    return vertices, faces, uvs
