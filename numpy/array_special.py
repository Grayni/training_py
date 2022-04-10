import numpy as np

arr = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)], dtype=np.int64)

arr1 = arr.T  # transposition
print(arr, '\n----\n')
print(arr1, '\n----\n')

arr2 = arr.flatten()  # convert in one-dimensional array
print(arr2, '\n----\n')

arr3 = np.trace(arr)
print(arr3)

print(np.info(np.sin))  # description of function
