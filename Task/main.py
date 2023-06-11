import numpy as np
import matplotlib.pyplot as plt

from Cube import Cube
from Vertice import Vertice

from math_algorithms import get_GaussianElimination
from math_algorithms import get_determinant

from Functions import DFIABG
from Functions import DFIXYZ
from Functions import DPSITE
from Functions import DPSIXYZ
from Functions import to_global
from Functions import fixate_side

from numpy import linalg

from visualisation import get_all_outer_cubes
from visualisation import get_cubes_side_vertices

from generators import generate27GaussianNodes
from generators import getJacobian
from generators import generate_c_consts
from generators import generate_c_consts_9
from generators import generate9GaussinaNodes

from mge_related import *

from f_vector import create_f_vector
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fill_container(length, width, height, parts_len, parts_width, parts_height, dictionary):
    res = []

    vertices = []

    start_coords = [0, 0, 0]
    outer_number_counter = 1

    step_x = length / parts_len
    step_y = width / parts_width
    step_z = height / parts_height

    check_middle_len = False
    check_middle_width = False
    check_middle_height = False

    z = 0.0
    y = 0.0
    x = 0.0

    while z <= height:
        y = 0.0
        check_middle_width = False
        while y <= width:
            x = 0.0
            check_middle_len = False
            while x <= length:
                if (check_middle_width == True and check_middle_len == True):
                    x += step_x / 2
                    check_middle_len = False
                    continue
                if (check_middle_height == True and check_middle_len == True):
                    x += step_x / 2
                    check_middle_len = False
                    continue
                if (check_middle_width == True and check_middle_height == True):
                    x += step_x / 2
                    continue
                vertices.append(Vertice(outer_number=outer_number_counter, coords=[x, y, z]))
                dictionary[(x, y, z)] = outer_number_counter
                outer_number_counter += 1
                x += step_x / 2

                if not check_middle_len:
                    check_middle_len = True
                else:
                    check_middle_len = False

            if not check_middle_width:
                check_middle_width = True
            else:
                check_middle_width = False

            y += step_y / 2

        if not check_middle_height:
            check_middle_height = True
        else:
            check_middle_height = False
        z += step_z / 2

    return vertices


def generate_vertices_for_cube(vertices, starting_point, step_x, step_y, step_z, counters, dictionary):
    current_x_part = counters[0]
    current_y_part = counters[1]

    index = vertices[vertices.index(starting_point)].coords
    indexindex = vertices.index(starting_point)

    # skip_lower_plate = (x_len - current_x_part) * 2 + x_len + 1
    # skip_entire_lower_plate = (x_len + 1 + 1 + x_len * 2)
    # skip_entire_middle_plate = x_len + 1
    #
    # lower_edge_coeficient = skip_lower_plate + 1 + (current_x_part + 1) * 2
    # lower_center_right = (x_len - current_x_part) * 2 + current_x_part + 2
    # lower_center_back = (x_len - current_x_part) * 2 + x_len + 1 + (current_x_part + 1) * 2
    #
    # high_edge_coeficient = (x_len - current_x_part) * 2 + skip_entire_lower_plate * (y_len - current_y_part) + x_len + 1 + skip_entire_middle_plate * y_len + 1 + current_x_part * 2 + current_y_part * (x_len * 2 + 1 + x_len + 1)
    #
    # central_edge_coeficient_front = (x_len - current_x_part) * 2 + skip_entire_lower_plate * (y_len - current_y_part) + 1 + current_x_part + current_y_part * (x_len + 1)
    # central_edge_coeficient_back = central_edge_coeficient_front + x_len - current_x_part + 1 + current_x_part
    #
    # to_higher = indexindex + high_edge_coeficient
    #
    # LE = [indexindex, indexindex + 2, indexindex + lower_edge_coeficient, indexindex + lower_edge_coeficient - 2]
    # HE = [indexindex + high_edge_coeficient, indexindex + high_edge_coeficient + 2, indexindex + high_edge_coeficient + lower_edge_coeficient, indexindex + high_edge_coeficient + lower_edge_coeficient - 2]
    # LC = [indexindex + 1, indexindex + lower_center_right, indexindex + lower_center_back, indexindex + lower_center_right - 1]
    # MC = [indexindex + central_edge_coeficient_front, indexindex + central_edge_coeficient_front + 1, indexindex + central_edge_coeficient_back + 1, indexindex + central_edge_coeficient_back]
    # HC = [to_higher + 1, to_higher + lower_center_right, to_higher + lower_center_back, to_higher + lower_center_right - 1]

    vertice_1 = indexindex
    vertice_2 = dictionary[(index[0] + step_x, index[1], index[2])]
    vertice_3 = dictionary[(index[0] + step_x, index[1] + step_y, index[2])]
    vertice_4 = dictionary[(index[0], index[1] + step_y, index[2])]

    vertice_5 = dictionary[(index[0], index[1], index[2] + step_z)]
    vertice_6 = dictionary[(index[0] + step_x, index[1], index[2] + step_z)]
    vertice_7 = dictionary[(index[0] + step_x, index[1] + step_y, index[2] + step_z)]
    vertice_8 = dictionary[(index[0], index[1] + step_y, index[2] + step_z)]

    vertice_9 = dictionary[(index[0] + step_x/2, index[1], index[2])]
    vertice_10 = dictionary[(index[0] + step_x, index[1] + step_y/2, index[2])]
    vertice_11 = dictionary[(index[0] + step_x/2, index[1] + step_y, index[2])]
    vertice_12 = dictionary[(index[0], index[1] + step_y/2, index[2])]

    vertice_13 = dictionary[(index[0], index[1], index[2] + step_z/2)]
    vertice_14 = dictionary[(index[0] + step_x, index[1], index[2] + step_z/2)]
    vertice_15 = dictionary[(index[0] + step_x, index[1] + step_y, index[2] + step_z/2)]
    vertice_16 = dictionary[(index[0], index[1] + step_y, index[2] + step_z/2)]

    vertice_17 = dictionary[(index[0] + step_x / 2, index[1], index[2] + step_z)]
    vertice_18 = dictionary[(index[0] + step_x, index[1] + step_y / 2, index[2] + step_z)]
    vertice_19 = dictionary[(index[0] + step_x / 2, index[1] + step_y, index[2] + step_z)]
    vertice_20 = dictionary[(index[0], index[1] + step_y / 2, index[2] + step_z)]

    LE = [indexindex, vertice_2 - 1, vertice_3 - 1, vertice_4 - 1]
    HE = [vertice_5 - 1, vertice_6 - 1, vertice_7 - 1, vertice_8 - 1]
    LC = [vertice_9 - 1, vertice_10 - 1, vertice_11 - 1, vertice_12 - 1]
    MC = [vertice_13 - 1, vertice_14 - 1, vertice_15 - 1, vertice_16 - 1]
    HC = [vertice_17 - 1, vertice_18 - 1, vertice_19 - 1, vertice_20 - 1]

    result = []

    counter = 1

    for i in range(len(LE)):
        vertices[int(LE[i])].inner_number = counter
        result.append(vertices[int(LE[i])])
        counter += 1

    for i in range(len(HE)):
        vertices[int(HE[i])].inner_number = counter
        result.append(vertices[int(HE[i])])
        counter += 1

    for i in range(len(LC)):
        vertices[int(LC[i])].inner_number = counter
        result.append(vertices[int(LC[i])])
        counter += 1

    for i in range(len(MC)):
        vertices[int(MC[i])].inner_number = counter
        result.append(vertices[int(MC[i])])
        counter += 1

    for i in range(len(HC)):
        vertices[int(HC[i])].inner_number = counter
        result.append(vertices[int(HC[i])])
        counter += 1

    return result


def create_cubes(x_len, y_len, z_len, parts_len, parts_width, parts_height, vertices, dictionary):
    number_of_cubes = x_len * y_len * z_len

    start_cube_pos = 0

    cubes_starting_points = []
    number_of_rows_columns = []

    x_len_start = 0
    y_len_start = 0
    z_len_start = 0

    step_x = x_len / parts_len
    step_y = y_len / parts_width
    step_z = z_len / parts_height

    while z_len_start < z_len:
        y_len_start = 0.0
        counter_row_y = 0
        while y_len_start < y_len:
            x_len_start = 0
            counter_row_x = 0
            while x_len_start < x_len:
                cubes_starting_points.append([x_len_start, y_len_start, z_len_start])
                number_of_rows_columns.append([counter_row_x, counter_row_y])
                x_len_start += step_x
                counter_row_x += 1
            y_len_start += step_y
            counter_row_y += 1
        z_len_start += step_z

    cubes = []

    for i in range(len(cubes_starting_points)):
        cube_vertices = generate_vertices_for_cube(vertices, Vertice(outer_number=1, coords=cubes_starting_points[i]), step_x, step_y, step_z, number_of_rows_columns[i], dictionary)
        cubes.append(Cube(cube_number=i + 1, vertices=cube_vertices))

    return cubes


def tranform_into_arrays(vertices):
    array_len = []
    array_wid = []
    array_hei = []

    for i in range(len(vertices)):
        array_len.append(vertices[i].coords[0])
        array_wid.append(vertices[i].coords[1])
        array_hei.append(vertices[i].coords[2])

    return [array_len, array_wid, array_hei]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    c_consts = generate_c_consts()
    c_consts_9 = generate_c_consts_9()

    gauss_nodes_9 = generate9GaussinaNodes()

    vertice_dictionary = {}

    result = fill_container(2, 1, 2, 2, 1, 2, vertice_dictionary)

    ZP = [[2, 6, -30], [3, 6, -30]]

    ZU = []

    # for i in range(4 * 4):
    #     ZU.append([i, 5])

    ZU = [[0, 5], [1, 5]]

    cubes = create_cubes(2, 1, 2, 2, 1, 2, result, vertice_dictionary)

    outer_sides = get_all_outer_cubes(cubes, 0, 2, 0, 1, 0, 2)

    dfiabg = DFIABG()

    ng = 3 * (cubes[0].vertices[6].outer_number - cubes[0].vertices[0].outer_number + 1)

    DJ_all = []

    for cube in cubes:
        DJ_all.append(getJacobian(dfiabg, cube))

    dfixyz_all = []

    for elem in range(len(cubes)):
        dfixyz_all.append(DFIXYZ(DJ_all[elem], dfiabg))

    all_determinants = [[0 for _ in range(27)] for _ in range(len(cubes))]

    for matrix in range(len(cubes)):
        for gauss_node in range(27):
            all_determinants[matrix][gauss_node] = get_determinant(DJ_all[matrix][gauss_node])


    a11_all = []
    a12_all = []
    a13_all = []
    a22_all = []
    a23_all = []
    a33_all = []

    for cube in range(len(cubes)):
        a11_all.append(create_a11(c_consts, [], dfixyz_all, all_determinants, cube))
        a12_all.append(create_a12(c_consts, [], dfixyz_all, all_determinants, cube))
        a13_all.append(create_a13(c_consts, [], dfixyz_all, all_determinants, cube))
        a22_all.append(create_a22(c_consts, [], dfixyz_all, all_determinants, cube))
        a23_all.append(create_a23(c_consts, [], dfixyz_all, all_determinants, cube))
        a33_all.append(create_a33(c_consts, [], dfixyz_all, all_determinants, cube))


    mge_all = []

    for cube in range(len(cubes)):
        mge_all.append(create_mge(a11_all[cube], a12_all[cube], a13_all[cube], a22_all[cube], a23_all[cube], a33_all[cube]))

    dpsite = DPSITE()

    fe_all = []

    for i in range(len(ZP)):
        dpsixyz = DPSIXYZ(dpsite, cubes[ZP[i][0]], ZP[i][1])
        fe_all.append(create_f_vector(dpsixyz, c_consts_9, ZP[i][2], ZP[i][1], gauss_nodes_9))

    for q in range(len(mge_all)):
        for i in range(len(mge_all[0])):
            for j in range(i, len(mge_all[0][0])):
                mge_all[q][j][i] = mge_all[q][i][j]

    global_matrix_mg = [[0 for _ in range(len(result) * 3)] for _ in range(len(result) * 3)]

    global_vector_f = [0 for _ in range(len(result) * 3)]

    to_global(global_matrix_mg, global_vector_f, mge_all, fe_all, ZP, cubes)

    print(global_vector_f[114])

    fixate_side(global_matrix_mg, ZU, cubes)

    # coef = 30

    print(len(global_matrix_mg))
    print(len(global_vector_f))

    # final = gauss_elimination(global_matrix_mg, global_vector_f)

    final = get_GaussianElimination(global_matrix_mg, global_vector_f)

    for i in range(len(result)):
        result[i].coords[0] += final[i * 3]
        result[i].coords[1] += final[i * 3 + 1]
        result[i].coords[2] += final[i * 3 + 2]


    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    cube_vertices = []

    for side in range(6):
        get_cubes_side_vertices(outer_sides[side], side + 1, cube_vertices)

    result_arr = tranform_into_arrays(result)

    ax = plt.figure().add_subplot(projection='3d')

    # ax.scatter(result_arr[0], result_arr[1], result_arr[2])
    for cube_lines in cube_vertices:
        x = [point[0] for point in cube_lines]
        y = [point[1] for point in cube_lines]
        z = [point[2] for point in cube_lines]
        ax.plot(x, y, z, color='black')

    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
