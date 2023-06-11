import math


def generate27GaussianNodes():
    nodes = []

    possible_values = [-math.sqrt(0.6), 0, math.sqrt(0.6)]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                nodes.append([possible_values[i], possible_values[j], possible_values[k]])

    return nodes


def generate9GaussinaNodes():
    nodes = []

    possible_values = [-math.sqrt(0.6), 0, math.sqrt(0.6)]

    for i in range(3):
        for j in range(3):
            nodes.append([possible_values[i], possible_values[j]])

    return nodes


def generate_c_consts():
    consts = []

    possible_values = [5.0/9, 8.0/9, 5.0/9]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                consts.append([possible_values[i], possible_values[j], possible_values[k]])

    return consts


def generate_c_consts_9():
    consts = []

    possible_values = [5.0/9, 8.0/9, 5.0/9]

    for i in range(3):
        for j in range(3):
            consts.append([possible_values[i], possible_values[j]])

    return consts


def getJacobian(DFIABG, finite_element_aka_cube):
    jacobian = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(27)]

    for gauss_node in range(len(DFIABG)):
        for gaussaxis in range(3):
            for globalaxis in range(3):
                for finite_element_element_index in range(len(finite_element_aka_cube.vertices)):
                    jacobian[gauss_node][gaussaxis][globalaxis] += finite_element_aka_cube.vertices[finite_element_element_index].coords[globalaxis] \
                                                                   * DFIABG[gauss_node][gaussaxis][finite_element_element_index]
                    
    return jacobian
