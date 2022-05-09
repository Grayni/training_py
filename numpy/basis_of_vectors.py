import numpy as np

MM = np.array([
    [(1, 2, 2),
     (-1, 2, 1),
     (0, 8, 0)],
    [(1, 2, 2),
     (-1, 2, 1),
     (0, 8, 6)]
])

for M in MM:
    if np.linalg.matrix_rank(M) == 3:
        print(M)

