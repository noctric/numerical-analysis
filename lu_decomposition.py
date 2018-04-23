import numpy as np


def change(A, i, j):
    A[[i, j]] = A[[j, i]]


def lu_decomp(A):
    # suche betragsmaessig groesstes element und tausche die zeilen
    for i in range(0, A[0].size):

        # diagonalelement
        tmp = abs(A[i][i])
        index = i

        for j in range(i + 1, A[0].size):
            if abs(A[j][i]) > tmp:
                tmp = A[j][i]
                index = j

        # zeilen tauschen
        change(A, i, index)
        print "tausche Zeilen z{} mit z{}".format(i + 1, index + 1)

        for j in range(i + 1, A[0].size):
            if A[i][i] == 0:
                print "div by zero!"
                return

            A[j][i] /= A[i][i]
            factor = A[j][i]
            for k in range(i + 1, A[0].size):
                A[j][k] -= (factor * A[i][k])

    l_mat = np.zeros((A[0].size, A[0].size))
    u_mat = np.zeros((A[0].size, A[0].size))

    for i in range(0, A[0].size):
        l_mat[i][i] = 1
        u_mat[i][i] = A[i][i]
        for j in range(0, i):
            l_mat[i][j] = A[i][j]
        for j in range(i, A[0].size - i):
            u_mat[i][j] = A[i][j]
            
    print "L:"
    print l_mat
    print "U:"
    print u_mat


a_test = np.array([[0, 0, 0, 1], [2, 1, 2, 0], [4, 4, 0, 0], [2, 3, 1, 0]], dtype=float)
lu_decomp(a_test)
print a_test
