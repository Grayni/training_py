import numpy as np
inp = ['1 0 1 0 2', '-1 1 -2 1 -2', '4 0 1 -2 0', '-4 4 0 1 5']
arr = np.array([inp[i].split() for i in range(4)], dtype='float')

if np.linalg.det(arr[:, :-1]):
    print(*np.linalg.solve(arr[:, :-1], arr[:, -1]))
else:
    print('Матрица системы вырожденная')