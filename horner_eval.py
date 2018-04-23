import numpy as np


# start region helper
def diff_func(x_0, x_1, y_0, y_1):
    return (x_1 - x_0) / (y_1 - y_0)


def mult_func(a, b, c):
    return a * b * c
# end region helper

data = np.array([[0, 1, 3],
                 [3, 2, 6]])


def get_diff(n, m):
    if n == m:
        return data[1][m]
    elif (n > 0) & (m < 3):
        return diff_func(get_diff(n - 1, m), get_diff(n, m + 1), data[0][n - 1], data[0][n])


pol = np.zeros(data[0].size)


for i in range(0, pol.size):
    pol[i] = get_diff(i, 0)


print pol


def eval_horner(k, x):
    if k == 0:
        return get_diff(data[0].size - 1, 0)
    else:
        return mult_func(pol[k - 1], (x - data[0][data[0].size - k]), eval_horner(k - 1, x))


print eval_horner(data[0].size, 2)
