import numpy as np

input_1 = '3'

inp = ['3 2 -1 4', '2 -1 5 23', '1 7 -1 5']

arr = np.array([inp[i].split() for i in range(int(input_1))], dtype='float')

if np.linalg.det(arr[:, :-1]):
    print(*np.linalg.solve(arr[:, :-1], arr[:, -1]))
else:
    print('Матрица системы вырожденная')
