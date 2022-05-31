import numpy as np
inp = '3'
inp_arr = ['-2 0', '2 0', '0 -4']
M = np.array([])
v = np.array([])
arr = np.array([list(map(int, inp_arr[i].split())) for i in range(int(inp))])

M1 = np.array([[1, 1], [1, -1]])
v = np.array(list(map(int, input().split())))

matrix = np.linalg.solve(M1, v)

if (matrix % 1).sum() or matrix[matrix > 0].shape[0] != 2:
    print('Такой класс не существует')
else:
    print(*matrix.astype(int))

print(arr)