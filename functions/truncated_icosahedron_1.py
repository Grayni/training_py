import numpy as np
import math
# create two functions: return flat shape
# S(x) S flat shape
# S_ceil(x) S flat shape round up


def S_hexagon(x):
    return 3 * 3 ** (1 / 2) * x ** 2 / 2


def S_pentagon(x):
    return 5/4 * x**2 * 1/np.tan(np.pi/5)


def S(x):
    return 20 * S_hexagon(x) + 12 * S_pentagon(x)


def S_ceil(x):
    return math.ceil(S(x))

print(S(7))
print(S_ceil(7))
