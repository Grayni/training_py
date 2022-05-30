import numpy as np

# There are 20 students in the class.
# There are girls and boys among them.
# There are more girls than boys for 4 people.
# How many boys and girls are in this class?
# x + y = 20
# x - 4 = y => x - y = 4

M1 = np.array([[1, 1], [1, -1]])
v = np.array([20, 5])

matrix = np.linalg.solve(M1, v)

if (matrix % 1).sum() or matrix[matrix > 0].shape[0] != 2:
    print('Такой класс не существует')
else:
    print(*matrix.astype(int))
