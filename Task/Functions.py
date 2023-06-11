from generators import generate27GaussianNodes
from generators import generate9GaussinaNodes

from math import floor

from dfidsomething import *

from dpsid_something import *

from math_algorithms import get_GaussianElimination

def getAKT(axes, number_of_vertex, vertices):
    result = 0.0

    if axes == 1:
        result = vertices[number_of_vertex].coords[0]
    elif axes == 2:
        result = vertices[number_of_vertex].coords[1]
    elif axes == 3:
        result = vertices[number_of_vertex].coords[2]

    return result


def getNT(local_number, finite_element_number_aka_cube):
    vertex = list(filter(lambda x: x.inner_number == local_number, finite_element_number_aka_cube.vertices))[0]

    return vertex


def get_side_vertices(outer_side):
    vertices_indexes = []
    match outer_side:
        case 1:
            vertices_indexes = [0, 1, 5, 4, 8, 13, 16, 12]
        case 2:
            vertices_indexes = [1, 2, 6, 5, 9, 14, 17, 13]
        case 3:
            vertices_indexes = [2, 3, 7, 6, 10, 15, 18, 14]
        case 4:
            vertices_indexes = [3, 0, 4, 7, 11, 12, 19, 15]
        case 5:
            vertices_indexes = [3, 2, 1, 0, 10, 9, 8, 11]
        case 6:
            vertices_indexes = [4, 5, 6, 7, 16, 17, 18, 19]

    return vertices_indexes

def getZP(finite_element_number_aka_cube, outer_side):

    vertices_indexes = get_side_vertices(outer_side)

    vertices = []

    for index in vertices_indexes:
        vertices.append(finite_element_number_aka_cube.vertices[index])

    return vertices


def getZU(finite_element_number_aka_cube, outer_side):
    vertices_indexes = get_side_vertices(outer_side)

    vertices = []

    for index in vertices_indexes:
        vertices.append(finite_element_number_aka_cube.vertices[index])

    return vertices


def DFIABG():

    gaussnodes = generate27GaussianNodes()

    local_vertices = [
        [-1, 1, -1],
        [1, 1, -1],
        [1, -1, -1],
        [-1, -1, -1],

        [-1, 1, 1],
        [1, 1, 1],
        [1, -1, 1],
        [-1, -1, 1],

        [0, 1, -1],
        [1, 0, -1],
        [0, -1, -1],
        [-1, 0, -1],

        [-1, 1, 0],
        [1, 1, 0],
        [1, -1, 0],
        [-1, -1, 0],

        [0, 1, 1],
        [1, 0, 1],
        [0, -1, 1],
        [-1, 0, 1]

    ]



    dfiabg_array = [[[0 for _ in range(len(local_vertices))] for _ in range(3)] for _ in range(len(gaussnodes))]

    counter = 0

    for i in range(len(gaussnodes)):
        for axis in range(3):
            for k in range(len(local_vertices)):
                if counter < 8:
                    if axis == 0:
                        dfiabg_array[i][axis][k] = dfid_alpha_edge(gaussnodes[i][0], gaussnodes[i][1], gaussnodes[i][2], local_vertices[k])
                    elif axis == 1:
                        dfiabg_array[i][axis][k] = dfid_beta_edge(gaussnodes[i][0], gaussnodes[i][1], gaussnodes[i][2], local_vertices[k])
                    elif axis == 2:
                        dfiabg_array[i][axis][k] = dfid_gamma_edge(gaussnodes[i][0], gaussnodes[i][1], gaussnodes[i][2], local_vertices[k])
                elif counter >= 8:
                    if axis == 0:
                        dfiabg_array[i][axis][k] = dfid_alpha_rest(gaussnodes[i][0], gaussnodes[i][1], gaussnodes[i][2], local_vertices[k])
                    elif axis == 1:
                        dfiabg_array[i][axis][k] = dfid_beta_rest(gaussnodes[i][0], gaussnodes[i][1], gaussnodes[i][2], local_vertices[k])
                    elif axis == 2:
                        dfiabg_array[i][axis][k] = dfid_gamma_rest(gaussnodes[i][0], gaussnodes[i][1], gaussnodes[i][2], local_vertices[k])
                counter += 1
                pass
            counter = 0

    return dfiabg_array


def DFIXYZ(DJ_matrix, DFIABG):

    dfixyz = [[0 for _ in range(20)] for _ in range(27)]

    for i in range(27):
        for j in range(20):
            dfixyz[i][j] = get_GaussianElimination(DJ_matrix[i], [DFIABG[i][0][j], DFIABG[i][1][j], DFIABG[i][2][j]])

    return dfixyz


def DPSITE():
    gauss_nodes = generate9GaussinaNodes()

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


    dpsite = [[[0 for _ in range(8)] for _ in range(2)] for _ in range(9)]

    for gauss_node in range(len(gauss_nodes)):
        for axis in range(2):
            for vertice in range(len(local_vertices)):
                if vertice < 4:
                    if axis == 0:
                        dpsite[gauss_node][axis][vertice] = dpsi_d_eta_edge(gauss_nodes[gauss_node][0],
                                                                            gauss_nodes[gauss_node][1],
                                                                            local_vertices[vertice])
                    if axis == 1:
                        dpsite[gauss_node][axis][vertice] = dpsi_d_tau_edge(gauss_nodes[gauss_node][0],
                                                                            gauss_nodes[gauss_node][1],
                                                                            local_vertices[vertice])
                if vertice == 4 or vertice == 6:
                    if axis == 0:
                        dpsite[gauss_node][axis][vertice] = dpsi_d_eta_5_7(gauss_nodes[gauss_node][0],
                                                                            gauss_nodes[gauss_node][1],
                                                                            local_vertices[vertice])
                    if axis == 1:
                        dpsite[gauss_node][axis][vertice] = dpsi_d_tau_5_7(gauss_nodes[gauss_node][0],
                                                                            gauss_nodes[gauss_node][1],
                                                                            local_vertices[vertice])
                if vertice == 5 or vertice == 7:
                    if axis == 0:
                        dpsite[gauss_node][axis][vertice] = dpsi_d_eta_6_8(gauss_nodes[gauss_node][0],
                                                                           gauss_nodes[gauss_node][1],
                                                                           local_vertices[vertice])
                    if axis == 1:
                        dpsite[gauss_node][axis][vertice] = dpsi_d_tau_6_8(gauss_nodes[gauss_node][0],
                                                                           gauss_nodes[gauss_node][1],
                                                                           local_vertices[vertice])

    return dpsite


def DPSIXYZ(dpsite, finite_element, finite_element_side):
    dpsixyz = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(9)]

    side_vertices = getZP(finite_element, finite_element_side)

    for gauss in range(9):
        for local_axis in range(2):
            for global_axis in range(3):
                for elem in range(8):
                    dpsixyz[gauss][local_axis][global_axis] += side_vertices[elem].coords[global_axis] * dpsite[gauss][local_axis][elem]

    return dpsixyz


def to_global(global_matrix_mg, global_vector_f, all_mge, all_fe, ZP, cubes):
    for mge in range(len(all_mge)):
        for mge_for_elem_i in range(len(all_mge[0])):
            for mge_for_elem_j in range((len(all_mge[0]))):
                x_or_y_or_z_i = floor(mge_for_elem_i / 20)
                x_ot_y_or_z_j = floor(mge_for_elem_j / 20)
                index_1 = (cubes[mge].vertices[mge_for_elem_i % 20].outer_number - 1) * 3 + x_or_y_or_z_i
                index_2 = (cubes[mge].vertices[mge_for_elem_j % 20].outer_number - 1) * 3 + x_ot_y_or_z_j
                global_matrix_mg[index_1][index_2] += all_mge[mge][mge_for_elem_i][mge_for_elem_j]

    for i in range(len(ZP)):
        for mge_for_elem_i in range(len(all_fe[0])):
            comp = floor(mge_for_elem_i / 20)
            index = (cubes[ZP[i][0]].vertices[mge_for_elem_i % 20].outer_number - 1) * 3 + comp
            global_vector_f[index] += all_fe[i][mge_for_elem_i]


def fixate_side(global_matrix_mg, ZU, cubes):

    for i in range(len(ZU)):
        side_vertices = getZU(cubes[ZU[i][0]], ZU[i][1])
        for j in range(8):
            index = (side_vertices[j].outer_number - 1) * 3

            global_matrix_mg[index][index] = math.pow(10, 30)
            global_matrix_mg[index + 1][index + 1] = math.pow(10, 30)
            global_matrix_mg[index + 2][index + 2] = math.pow(10, 30)
