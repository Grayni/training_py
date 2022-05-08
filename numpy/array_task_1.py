import numpy as np


def division(x, y):
    set_1 = np.array(list(map(float, x.split(', '))))
    set_2 = np.array(list(map(float, y.split(', '))))
    return np.array([val/set_2[-2] for val in set_1 if val % set_2[-2] == 0])


print(division('1, 2, 3, 4, 5, 6', '1, 2, 3, 4'))


# variant 2

V1 = np.fromstring(input(), sep=',')
V2 = np.fromstring(input(), sep=',')

V = V1[V1 % V2[-2] == 0] / V2[-2]