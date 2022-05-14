import numpy as np

A = np.array([0, 9, 7, 1, 3, 7, 5, 2, 5, 1])
B = np.array([3, 1, 3, 7, 4, 1, 8, 1, 1, 8])

Z = np.intersect1d(A, B)

print(Z)
