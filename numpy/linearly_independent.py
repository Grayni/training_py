import numpy as np

M = np.array([
    #a, b, c, d, e, f
    [0, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0]
])

for a, b, c, d, e, f in M:
    N = np.array([
        [a, 0, 0],
        [b, d, 0],
        [c, e, f]
    ])

    if np.linalg.matrix_rank(N) == 3:
        print(f'rank: {np.linalg.matrix_rank(N)}')
        print(N)
        print('String:', (a, b, c, d, e, f))
