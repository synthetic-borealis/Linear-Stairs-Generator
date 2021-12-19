def create(count=5, width=2.0, depth=0.3, height=0.15):
    UV_GAP = 0.02

    vertices = []
    faces = []
    uvs = []

    width /= 2

    f = 0

    uvy_offset1 = 0  # front/top island

    # bottom/back island
    uvx_offset1 = (width * 2) + UV_GAP
    uvy_offset2 = 0

    uvx_offset2 = uvx_offset1 + (width * 2) + UV_GAP  # right island
    uvx_offset3 = uvx_offset2 + depth + UV_GAP  # left island
    uvy_offset3 = 0  # both side island

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
        uvs.append(((0, uvy_offset1), (width * 2, uvy_offset1),
                   (width * 2, uvy_offset1 + height), (0, uvy_offset1 + height)))
        uvy_offset1 += height

        faces.append((f + 7, f + 6, f + 4, f + 5))  # top
        uvs.append(((width * 2, uvy_offset1 + depth), (0, uvy_offset1 + depth),
                   (0, uvy_offset1), (width * 2, uvy_offset1)))
        uvy_offset1 += (depth + UV_GAP)

        faces.append((f + 2, f + 3, f + 1, f))  # bottom
        uvs.append(((width * 2 + uvx_offset1, uvy_offset2 + depth), (uvx_offset1, uvy_offset2 + depth),
                   (uvx_offset1, uvy_offset2), (width * 2 + uvx_offset1, uvy_offset2)))
        uvy_offset2 += depth

        faces.append((f + 3, f + 2, f + 6, f + 7))  # back
        uvs.append(((uvx_offset1, uvy_offset2), (width * 2 + uvx_offset1, uvy_offset2),
                    (width * 2 + uvx_offset1, uvy_offset2 + height), (uvx_offset1, uvy_offset2 + height)))
        uvy_offset2 += (height + UV_GAP)

        faces.append((f + 1, f + 3, f + 7, f + 5))  # right
        uvs.append(((uvx_offset2, uvy_offset3), (uvx_offset2 + depth, uvy_offset3),
                    (uvx_offset2 + depth, uvy_offset3 + height), (uvx_offset2, uvy_offset3 + height)))

        faces.append((f + 4, f + 6, f + 2, f))  # left
        uvs.append(((uvx_offset3 + depth, uvy_offset3 + height), (uvx_offset3, uvy_offset3 + height),
                    (uvx_offset3, uvy_offset3), (uvx_offset3 + depth, uvy_offset3)))

        uvy_offset3 += height + UV_GAP

        f += 6

    return vertices, faces, uvs
