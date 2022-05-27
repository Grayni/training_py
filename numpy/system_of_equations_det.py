import numpy as np

input_1 = '1 1 1'
input_2 = '2 2 5'

d = {}

for i, string in enumerate([input_1, input_2], 1):
    d[f'arr_{i}'] = [int(x) for x in string.split()]

det = np.linalg.det([d['arr_1'][:2], d['arr_2'][:2]])

if not(det):
    print('Матрица системы вырожденная')
else:
    print(*np.linalg.solve([d['arr_1'][:2], d['arr_2'][:2]], [d['arr_1'][-1], d['arr_2'][-1]]))
