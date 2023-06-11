def create_a11(c_consts, gauss_consts, dfixyz, determinants, finite_elem_number):
    e = 100
    nu = 0.3
    mu = e / (2 * (1 + nu))
    lambda_var = e / ((1 + nu) * (1 - 2 * nu))

    a11 = [[0 for _ in range(20)] for _ in range(20)]

    #оскільки гауса і c-шки однаково генеряться по розмірах то можна просто форік по 27

    for i in range(20):
        for j in range(20):
            for k in range(27):
                a11[i][j] += c_consts[k][0] * c_consts[k][1] * c_consts[k][2] * (lambda_var * (1 - nu) * dfixyz[finite_elem_number][k][i][0] * dfixyz[finite_elem_number][k][j][0]
                            + mu * (dfixyz[finite_elem_number][k][i][1] * dfixyz[finite_elem_number][k][j][1] + dfixyz[finite_elem_number][k][i][2] * dfixyz[finite_elem_number][k][j][2])) \
                            * determinants[finite_elem_number][k]

    return a11


def create_a22(c_consts, gauss_consts, dfixyz, determinants, finite_elem_number):
    e = 100
    nu = 0.3
    mu = e / (2 * (1 + nu))
    lambda_var = e / ((1 + nu) * (1 - 2 * nu))

    a22 = [[0 for _ in range(20)] for _ in range(20)]

    for i in range(20):
        for j in range(20):
            for k in range(27):
                a22[i][j] += c_consts[k][0] * c_consts[k][1] * c_consts[k][2] * (lambda_var * (1 - nu) * dfixyz[finite_elem_number][k][i][1] * dfixyz[finite_elem_number][k][j][1]
                            + mu * (dfixyz[finite_elem_number][k][i][0] * dfixyz[finite_elem_number][k][j][0] + dfixyz[finite_elem_number][k][i][2] * dfixyz[finite_elem_number][k][j][2])) \
                             * determinants[finite_elem_number][k]

    return a22


def create_a33(c_consts, gauss_consts, dfixyz, determinants, finite_elem_number):
    e = 100
    nu = 0.3
    mu = e / (2 * (1 + nu))
    lambda_var = e / ((1 + nu) * (1 - 2 * nu))

    a33 = [[0 for _ in range(20)] for _ in range(20)]

    for i in range(20):
        for j in range(20):
            for k in range(27):
                a33[i][j] += c_consts[k][0] * c_consts[k][1] * c_consts[k][2] * (lambda_var * (1 - nu) * dfixyz[finite_elem_number][k][i][2] * dfixyz[finite_elem_number][k][j][2]
                            + mu * (dfixyz[finite_elem_number][k][i][0] * dfixyz[finite_elem_number][k][j][0] + dfixyz[finite_elem_number][k][i][1] * dfixyz[finite_elem_number][k][j][1])) \
                             * determinants[finite_elem_number][k]

    return a33


def create_a12(c_consts, gauss_consts, dfixyz, determinants, finite_elem_number):
    e = 100
    nu = 0.3
    mu = e / (2 * (1 + nu))
    lambda_var = e / ((1 + nu) * (1 - 2 * nu))

    a12 = [[0 for _ in range(20)] for _ in range(20)]

    for i in range(20):
        for j in range(20):
            for k in range(27):
                a12[i][j] += c_consts[k][0] * c_consts[k][1] * c_consts[k][2] * (lambda_var * nu * dfixyz[finite_elem_number][k][i][0] * dfixyz[finite_elem_number][k][j][1]
                            + mu * dfixyz[finite_elem_number][k][i][1] * dfixyz[finite_elem_number][k][j][0]) \
                            * determinants[finite_elem_number][k]

    return a12


def create_a13(c_consts, gauss_consts, dfixyz, determinants, finite_elem_number):
    e = 100
    nu = 0.3
    mu = e / (2 * (1 + nu))
    lambda_var = e / ((1 + nu) * (1 - 2 * nu))

    a13 = [[0 for _ in range(20)] for _ in range(20)]

    for i in range(20):
        for j in range(20):
            for k in range(27):
                a13[i][j] += c_consts[k][0] * c_consts[k][1] * c_consts[k][2] * (lambda_var * nu * dfixyz[finite_elem_number][k][i][0] * dfixyz[finite_elem_number][k][j][2]
                            + mu * dfixyz[finite_elem_number][k][i][2] * dfixyz[finite_elem_number][k][j][0]) \
                             * determinants[finite_elem_number][k]

    return a13


def create_a23(c_consts, gauss_consts, dfixyz, determinants, finite_elem_number):
    e = 100
    nu = 0.3
    mu = e / (2 * (1 + nu))
    lambda_var = e / ((1 + nu) * (1 - 2 * nu))

    a23 = [[0 for _ in range(20)] for _ in range(20)]

    for i in range(20):
        for j in range(20):
            for k in range(27):
                a23[i][j] += c_consts[k][0] * c_consts[k][1] * c_consts[k][2] * (lambda_var * nu * dfixyz[finite_elem_number][k][i][1] * dfixyz[finite_elem_number][k][j][2]
                            + mu * dfixyz[finite_elem_number][k][i][2] * dfixyz[finite_elem_number][k][j][1]) \
                             * determinants[finite_elem_number][k]

    return a23


def create_all_a(c_consts, gauss_consts, dfixyz, determinants, finite_elem_number):
    e = 100
    nu = 0.3
    mu = e / (2 * (1 + nu))
    lambda_var = e / ((1 + nu) * (1 - 2 * nu))

    all_a = []

    a11 = [[0 for _ in range(20)] for _ in range(20)]
    a22 = [[0 for _ in range(20)] for _ in range(20)]
    a33 = [[0 for _ in range(20)] for _ in range(20)]
    a12 = [[0 for _ in range(20)] for _ in range(20)]
    a13 = [[0 for _ in range(20)] for _ in range(20)]
    a23 = [[0 for _ in range(20)] for _ in range(20)]

    for local_node_number_i in range(20):
        for local_node_number_j in range(20):
            for gauss_node in range(27):
                a11[local_node_number_i][local_node_number_j] += c_consts[gauss_node][0] * c_consts[gauss_node][1] * c_consts[gauss_node][2] * (
                            lambda_var * (1 - nu) * dfixyz[finite_elem_number][gauss_node][local_node_number_i][0] *
                            dfixyz[finite_elem_number][gauss_node][local_node_number_j][0]
                            + mu * (dfixyz[finite_elem_number][gauss_node][local_node_number_i][1] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][1] +
                                    dfixyz[finite_elem_number][gauss_node][local_node_number_i][2] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][2])) \
                             * determinants[finite_elem_number][gauss_node]

                a22[local_node_number_i][local_node_number_j] += c_consts[gauss_node][0] * c_consts[gauss_node][1] * c_consts[gauss_node][2] * (
                            lambda_var * (1 - nu) * dfixyz[finite_elem_number][gauss_node][local_node_number_i][1] *
                            dfixyz[finite_elem_number][gauss_node][local_node_number_j][1]
                            + mu * (dfixyz[finite_elem_number][gauss_node][local_node_number_i][0] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][0] +
                                    dfixyz[finite_elem_number][gauss_node][local_node_number_i][2] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][2])) \
                             * determinants[finite_elem_number][gauss_node]

                a33[local_node_number_i][local_node_number_j] += c_consts[gauss_node][0] * c_consts[gauss_node][1] * c_consts[gauss_node][2] * (
                            lambda_var * (1 - nu) * dfixyz[finite_elem_number][gauss_node][local_node_number_i][2] *
                            dfixyz[finite_elem_number][gauss_node][local_node_number_j][2]
                            + mu * (dfixyz[finite_elem_number][gauss_node][local_node_number_i][0] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][0] +
                                    dfixyz[finite_elem_number][gauss_node][local_node_number_i][1] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][1])) \
                             * determinants[finite_elem_number][gauss_node]

                a12[local_node_number_i][local_node_number_j] += c_consts[gauss_node][0] * c_consts[gauss_node][1] * c_consts[gauss_node][2] * (
                            lambda_var * nu * dfixyz[finite_elem_number][gauss_node][local_node_number_i][0] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][1]
                            + mu * dfixyz[finite_elem_number][gauss_node][local_node_number_i][1] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][0]) \
                             * determinants[finite_elem_number][gauss_node]

                a13[local_node_number_i][local_node_number_j] += c_consts[gauss_node][0] * c_consts[gauss_node][1] * c_consts[gauss_node][2] * (
                            lambda_var * nu * dfixyz[finite_elem_number][gauss_node][local_node_number_i][0] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][2]
                            + mu * dfixyz[finite_elem_number][gauss_node][local_node_number_i][2] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][0]) \
                             * determinants[finite_elem_number][gauss_node]

                a23[local_node_number_i][local_node_number_j] += c_consts[gauss_node][0] * c_consts[gauss_node][1] * c_consts[gauss_node][2] * (
                            lambda_var * nu * dfixyz[finite_elem_number][gauss_node][local_node_number_i][1] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][2]
                            + mu * dfixyz[finite_elem_number][gauss_node][local_node_number_i][2] * dfixyz[finite_elem_number][gauss_node][local_node_number_j][1]) \
                             * determinants[finite_elem_number][gauss_node]

    all_a = [a11, a22, a33, a12, a13, a23]

    return all_a


def create_mge(a11, a12, a13, a22, a23, a33):

    mge = [[0 for _ in range(60)] for _ in range(60)]

    for i in range(20):
        for j in range(20):
            mge[i][j] = a11[i][j]
            mge[i + 20][j + 20] = a22[i][j]
            mge[i + 40][j + 40] = a33[i][j]
            mge[i][j + 20] = a12[i][j]
            mge[i][j + 40] = a13[i][j]
            mge[i + 20][j + 40] = a23[i][j]

    return mge
