from math import sqrt
import numpy as np


def getQ_k(matrix, i, j):
    alpha = matrix[j][j] - matrix[i][i]
    c = sqrt(0.5 + 0.5 * sqrt((alpha * alpha) / (1 + (alpha * alpha))))
    s = np.copysign(1, alpha) / (2 * c * sqrt(1 + alpha * alpha))

    matrix_copy = np.zeros((matrix[0].size, matrix[0].size), dtype=float)

    matrix_copy[i][i] = c
    matrix_copy[i][j] = s
    matrix_copy[j][j] = c
    matrix_copy[j][i] = -s

    for l in range(0, matrix_copy[0].size):
        if matrix_copy[l][l] == 0:
            matrix_copy[l][l] = 1

    return matrix_copy


def jac_eigen_vals(matrix, dimen, n):

    matrix_k_it = matrix.copy()

    q_k = np.zeros((dimen, dimen), dtype=float)
    q_k_t = np.zeros((dimen, dimen), dtype=float)
    q_gesamt = np.identity(dimen, dtype=float)
    q_gesamt_t = np.identity(dimen, dtype=float)
    matrix_copy = matrix.copy()

    # for i in range(0, n):

    # l ist der spaltenindex!!
    for l in range(0, dimen - 1):
        # m ist der zeilenindex!!
        for m in range(1, dimen):
            if l != m:
                q_k = getQ_k(matrix_copy, m, l)

                q_k_t = q_k.copy()
                np.transpose(q_k_t)

                q_k.dot(q_gesamt, q_gesamt)

                q_k_t.dot(q_gesamt_t, q_gesamt_t)

                q_gesamt_t.dot(matrix).dot(q_gesamt, matrix_copy)
                print matrix_copy

    return matrix_copy


test = np.array([[1, 1. / 2, 1. / 3], [1. / 2, 1. / 3, 1 / 4], [1. / 3, 1. / 4, 1. / 5]], dtype=float)
print jac_eigen_vals(test, 3, 5)
