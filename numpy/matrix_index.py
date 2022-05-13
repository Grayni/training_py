import numpy as np

i = 3
Z = [[0,  1,  2,  3], [4,  5,  6,  7], [8,  9, 10, 11]]

val = np.unravel_index(i, np.shape(Z))

print(val)
