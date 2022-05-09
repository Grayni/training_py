import numpy as np

M = np.array([
    [1, -1, 0, 0],
    [1, 0, -1, 0],
    [1, 0, 0, -1],
    [0, 1, -1, 0],
    [0, 1, 0, -1],
    [0, 0, 1, -1],
])

print(np.linalg.matrix_rank(M))