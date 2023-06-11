def gauss_elimination(matrix, b, result_matrix):
    # FORWARD

    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            if matrix[i][i] == 0:
                return
            coef = matrix[j][i] / matrix[i][i]
            for k in range(i, len(matrix[0])):
                matrix[j][k] = matrix[j][k] - matrix[i][k] * coef
            b[j] = b[j] - b[i] * coef

    # ======================================================

    # BACKWARD

    res = list(b)
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(i + 1, len(matrix)):
            res[i] -= matrix[i][j] * res[j]
        if matrix[i][i] == 0:
            return []
        res[i] /= matrix[i][i]
    return res


def get_GaussianElimination(matrix, b):
    matrixRows = len(matrix)
    matrixCols = len(matrix[0])

    for i in range(matrixRows - 1):
        if matrix[i][i] == 0:
            print("Attention: 0")
            return 1
        for j in range(i + 1, matrixRows):
            ratio = matrix[j][i] / matrix[i][i]

            for k in range(i, matrixCols):
                matrix[j][k] = matrix[j][k] - matrix[i][k] * ratio

            b[j] = b[j] - b[i] * ratio

    answer = b.copy()
    for i in range(matrixRows - 1, -1, -1):
        if matrix[i][i] == 0:
            print("Attention: 0")
            return []

        for j in range(i + 1, matrixRows):
            answer[i] -= matrix[i][j] * answer[j]

        answer[i] /= matrix[i][i]

    return answer


def get_determinant(jacobian_martrix):
    first_part = jacobian_martrix[0][0] * jacobian_martrix[1][1] * jacobian_martrix[2][2] \
                 + jacobian_martrix[0][1] * jacobian_martrix[1][2] * jacobian_martrix[2][0] \
                 + jacobian_martrix[1][0] * jacobian_martrix[2][1] * jacobian_martrix[0][2]

    second_part = jacobian_martrix[2][0] * jacobian_martrix[1][1] * jacobian_martrix[0][2] \
                  - jacobian_martrix[1][0] * jacobian_martrix[0][1] * jacobian_martrix[2][2] \
                  - jacobian_martrix[0][0] * jacobian_martrix[2][1] * jacobian_martrix[1][2]

    determinant = first_part - second_part

    return determinant
