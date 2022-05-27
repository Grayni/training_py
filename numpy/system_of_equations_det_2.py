import numpy as np

input_1 = '3 2 -1 4'
input_2 = '2 -1 5 23'
input_3 = '1 7 -1 5'

d = {}

for i, string in enumerate([input_1, input_2, input_3], 1):
    d[f'arr_{i}'] = [int(x) for x in string.split()]

det = np.linalg.det([d['arr_1'][:3], d['arr_2'][:3], d['arr_3'][:3]])

if not(det):
    print('Матрица системы вырожденная')
else:
    print(*np.linalg.solve([d['arr_1'][:3], d['arr_2'][:3], d['arr_3'][:3]], [d['arr_1'][-1], d['arr_2'][-1], d['arr_3'][-1]]))


# variant 2

m=np.array([input().split() for i in range(3)], dtype=float)

if np.linalg.det(m[:,:-1]):
    print(*np.linalg.solve(m[:,:-1], m[:,-1]))
else:
    print('Система не имеет решений')
