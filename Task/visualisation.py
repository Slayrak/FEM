def get_all_outer_cubes(cubes, x_start, x_end, y_start, y_end, z_start, z_end):
    side1 = []
    side2 = []
    side3 = []
    side4 = []
    side5 = []
    side6 = []

    for cube in cubes:
        if cube.vertices[0].coords[1] == y_start:
            side1.append(cube)
        if cube.vertices[1].coords[0] == x_end:
            side2.append(cube)
        if cube.vertices[2].coords[1] == y_end:
            side3.append(cube)
        if cube.vertices[0].coords[0] == x_start:
            side4.append(cube)
        if cube.vertices[0].coords[2] == z_start:
            side5.append(cube)
        if cube.vertices[4].coords[2] == z_end:
            side6.append(cube)

    return [side1, side2, side3, side4, side5, side6]


def get_vertice_side_numbers(side_number):
    vertices = []

    if side_number == 1:
        vertices = [0, 8, 1, 13, 5, 4, 12, 0]
    if side_number == 2:
        vertices = [1, 9, 2, 14, 6, 17, 5, 13, 1]
    if side_number == 3:
        vertices = [2, 14, 6, 18, 7, 15, 3, 10, 2]
    if side_number == 4:
        vertices = [0, 12, 4, 19, 7, 15, 3, 11, 0]
    if side_number == 5:
        vertices = [0, 8, 1, 9, 2, 10, 3, 11, 0]
    if side_number == 6:
        vertices = [4, 16, 5, 17, 6, 18, 7, 19, 4]

    return vertices


def get_cubes_side_vertices(side1, side_number, cubes_vertices):
    vertices_numbers = get_vertice_side_numbers(side_number)

    for cube in side1:
        vertices = []
        for vertice_number in vertices_numbers:
            vertices.append([cube.vertices[vertice_number].coords[0], cube.vertices[vertice_number].coords[1], cube.vertices[vertice_number].coords[2]])
        cubes_vertices.append(vertices)




