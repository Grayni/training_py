import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [11.5],
    [12.5],
    [13.5]
])

try:
    Z = np.dot(A, B)
    print(Z)
except ValueError:
    print('Упс! Что-то пошло не так...')

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [11.5, 12.5, 13.5]
])

try:
    Z = np.dot(A, B)
    print(Z)
except ValueError:
    print('Упс! Что-то пошло не так...')
