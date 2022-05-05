from math import sin, pi


def limit_sin(x):
    return sin(pi*x/2) / x


print(round(limit_sin(1e300), 3))
