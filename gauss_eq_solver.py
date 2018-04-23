import numpy as np


# matrix A darf keine 0 auf der diagonalen enthalten
def gauss(matrix, b):
    n = matrix[0].size

    cpmatrix = matrix.copy()

    # untere dreiecksmatrix bilden
    for k in range(1, n):

        # Faktor bestimmen und Zeilen abzaehlen
        for i in range(k, n):
            factor = float(cpmatrix[i][k - 1] / cpmatrix[k - 1][k - 1])

            # Spaltenoperation
            for j in range(0, n):
                cpmatrix[i][j] -= (factor * cpmatrix[k - 1][j])
                b[i] -= (factor * b[k - 1])

    # normieren
    for l in range(0, n):
        factor = cpmatrix[l][l]

        for m in range(0, n):
            cpmatrix[l][m] /= factor

    # rueckwaerts einsetzen
    for i_1 in range(n - 2, -1, -1):            # in der vorletzten (!) zeile beginnen
        for j_1 in range(n - 1, i_1, -1):         # von der letzten spalte zur i-ten spalte gehen
            b[i_1] -= cpmatrix[i_1][j_1] * b[j_1]
            cpmatrix[i_1][j_1] = 0

    # ausgabe
    print (cpmatrix), '\n'
    print 'b = ', b, '\n'

# test aufgabe 1
A1 = np.array(
    [
        [1., 3., 1., 1.],
        [2., 1., 0., 0.],
        [0., 4., 4., 0.],
        [0., 1., 0., 2.]
    ])

b1t = np.array(
    [6., 4., 12., 2.]
)

b2t = np.array(
    [8., 1., 12., 7.]
)

gauss(A1, b1t)
gauss(A1, b2t)

# test aufgabe 2
dim = 5

A2 = np.empty([dim, dim], dtype=float)
b3 = np.empty([dim], dtype=float)

for i in range(0, dim):
    b3[i] = 1. / (i + 1)
    for j in range(0, dim):
        A2[i][j] = 1. / (i + j + 1 + 1 - 1)

print (A2)
gauss(A2, b3)
