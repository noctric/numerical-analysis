import math

a = float(9.8606)
c = float(-1.1085 * pow(10, 25))
d = float(0.029)


def f(x):
    return a / (1. - c * math.exp(-d * x))


def f_1(x):
    return -1. * (a * c * d * math.exp(d * x)) / pow(math.exp(d * x) - c, 2)


def newton_f(x):
    return x - (f(x)) / (f_1(x))


def seki_f(x, x_old):
    return x - ((x - x_old)/(f(x) - f(x_old))) * f(x)


def newton(count, x):
    x_k = x
    for i in range(0, count):
        x_k = newton_f(x_k)
        print "x_{} = {}".format(i + 1, x_k)


def seki(count, x_, x):
    x_old = x_
    x_k = x

    for i in range(0, count):
        tmp = x_k

        x_k = seki_f(x_k, x_old)

        x_old = tmp

        print "x_{} = {}".format(i + 1, x_k)


x_0 = 1961.
x_1 = 1961.
x_2 = 2000.

n = 10
print "\nnewton-verfahren:\n"
newton(n, x_0)
print "\nsekanten-verfahren:\n"
seki(n, x_1, x_2)
