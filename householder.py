import numpy as np
from numpy import linalg as LA


def euklid_norm(vec):
    return LA.norm(vec)


# unser d
def get_new_diag_elem(A, i):
    return -np.copysign(1, A[i][i]) * euklid_norm(A[:, i])


# unser v_1
def get_vec_entry(A, i):
    tmp = A[i][i] - get_new_diag_elem(A, i)
    return tmp


# unser ||v||_2^2
def konsch(A, i):
    tmp = -2 * get_vec_entry(A, i) * get_new_diag_elem(A, i)
    return tmp


def calc_v(A, i, dim):
    tmp = np.array(A[i:, i])

    ident = np.zeros(dim - i, dtype=float)
    ident[0] = 1.

    tmp += euklid_norm(tmp) * ident

    return tmp


# hilfsfunktion um einen vektor zu transponieren
def trans(vec, dim):
    tmp = np.zeros((dim, 1))
    for i in range(0, dim):
        tmp[i][0] = vec[i]

    return tmp


def get_q(A, i, dim, v):
    I = np.identity(dim - i)

    tmp = I - (2 / konsch(A, i)) * (v * trans(v, dim - i))

    if i > 0:

        result = np.zeros((dim, dim), dtype=float)

        result[i-1][i-1] = 1

        result[i:, i:] = tmp[:, :]

        print "result: ", result

        return result

    return tmp


def householder(A):
    dim = A[0].size

    tmp = get_q(A, 0, dim, calc_v(A, 0, dim))

    result = A.copy()

    result = tmp.dot(result)

    for i in range(1, dim - 1):
        tmp_q = get_q(A, i, dim, calc_v(A, i, dim))
        result = tmp_q.dot(result)

    return result


a_test = np.array([
    [20, 18, 44],
    [0, 40, 45],
    [-15, 24, -108]
], dtype=float)

v_test = calc_v(a_test, 0, 3)

print householder(a_test)
