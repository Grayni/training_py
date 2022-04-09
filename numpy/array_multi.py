import numpy as np

arr = np.array([(1, 2, 3), (1, 2, 3)])
print(arr, '\n')

arr = arr.reshape(3, 2)  # matrix transposition
print(arr, '\n')

arr = np.random.random((4, 4))
print(arr, '\n')

arr.resize(2, 2)
print(arr, '\n')

new_arr = np.arange(0, 12).reshape(3, 4)  # [] => [[], [], []]
print(new_arr)
