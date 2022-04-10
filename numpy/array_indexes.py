import numpy as np

arr = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

print(arr, '\n----\n')
# arr[1][2] == arr[1, 2]
print(arr[1][2], arr[1, 2], '\n----\n')
# get every 1 element
print(arr[:, 1], '\n----\n')
# get range row, col
print(arr[1:3, 1:3])
