def create(count=5, width=2.0, depth=0.3, height=0.15):
    vertices = []
    faces = []

    width /= 2

    f = 0

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

        faces.append((f + 2, f + 3, f + 1, f))  # bottom
        faces.append((f, f + 1, f + 5, f + 4))  # front
        faces.append((f + 7, f + 6, f + 4, f + 5))  # top
        faces.append((f + 3, f + 2, f + 6, f + 7))  # back
        faces.append((f + 1, f + 3, f + 7, f + 5))  # right
        faces.append((f + 4, f + 6, f + 2, f))  # left

        f += 6

    return vertices, faces
