import numpy as np

arr = np.array([(1, 2, -1), (2, 5, -6), (3, 8, -10)], dtype=np.int64)
print('matrix:')
print(arr, '\n----\n')
print('inverse matrix:')
print(np.linalg.inv(arr), '\n----\n')  # inverse matrix
arr1 = arr.T  # transposition
print(arr, '\n----\n')
print(arr1, '\n----\n')

arr2 = arr.flatten()  # convert in one-dimensional array
print(arr2, '\n----\n')

arr3 = np.trace(arr)
print(arr3)

print(np.info(np.sin))  # description of function
