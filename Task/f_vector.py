from Functions import get_side_vertices

from dpsid_something import *


def fv_1(dpsixyz, c_consts_9, power, gauss_nodes_9, local_vertices):
    f_vector_1 = [0 for _ in range(8)]

    for elem in range(8):
        for c_const in range(len(c_consts_9)):
            rest = dpsixyz[c_const][0][1] * dpsixyz[c_const][1][2] - dpsixyz[c_const][0][2] * dpsixyz[c_const][1][1]
            if elem < 4:
                f_vector_1[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_edge(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])
            elif elem == 4 or elem == 6:
                f_vector_1[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_5_7(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])
            elif elem == 5 or elem == 7:
                f_vector_1[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_6_8(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])

    return f_vector_1


def fv_2(dpsixyz, c_consts_9, power, gauss_nodes_9, local_vertices):
    f_vector_2 = [0 for _ in range(8)]

    for elem in range(8):
        for c_const in range(len(c_consts_9)):
            rest = dpsixyz[c_const][0][2] * dpsixyz[c_const][1][0] - dpsixyz[c_const][0][0] * dpsixyz[c_const][1][2]
            if elem < 4:
                f_vector_2[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_edge(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])
            elif elem == 4 or elem == 6:
                f_vector_2[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_5_7(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])
            elif elem == 5 or elem == 7:
                f_vector_2[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_6_8(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])

    return f_vector_2


def fv_3(dpsixyz, c_consts_9, power, gauss_nodes_9, local_vertices):
    f_vector_3 = [0 for _ in range(8)]

    for elem in range(8):
        for c_const in range(len(c_consts_9)):
            rest = dpsixyz[c_const][0][0] * dpsixyz[c_const][1][1] - dpsixyz[c_const][0][1] * dpsixyz[c_const][1][0]
            if elem < 4:
                f_vector_3[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_edge(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])
            elif elem == 4 or elem == 6:
                f_vector_3[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_5_7(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])
            elif elem == 5 or elem == 7:
                f_vector_3[elem] += c_consts_9[c_const][0] * c_consts_9[c_const][1] * power * rest * psi_6_8(gauss_nodes_9[c_const][0], gauss_nodes_9[c_const][1], local_vertices[elem])

    return f_vector_3


def create_f_vector(dpsixyz, c_consts_9, power, side, gauss_nodes_9):
    local_vertices = [
        [-1, -1],
        [1, -1],
        [1, 1],
        [-1, 1],

        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0]
    ]

    f_vector_1 = fv_1(dpsixyz, c_consts_9, power, gauss_nodes_9, local_vertices)
    f_vector_2 = fv_2(dpsixyz, c_consts_9, power, gauss_nodes_9, local_vertices)
    f_vector_3 = fv_3(dpsixyz, c_consts_9, power, gauss_nodes_9, local_vertices)

    side_vertices = get_side_vertices(side)

    f_vector = [0 for _ in range(60)]

    for local_elem in range(8):
        f_vector[side_vertices[local_elem]] = f_vector_1[local_elem]
        f_vector[side_vertices[local_elem] + 20] = f_vector_2[local_elem]
        f_vector[side_vertices[local_elem] + 40] = f_vector_3[local_elem]

    return f_vector
