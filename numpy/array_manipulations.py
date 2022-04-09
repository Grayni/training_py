import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

arr = np.insert(arr, 4, -12)
print(arr)

arr = np.delete(arr, 0)
print(arr)

arr = np.sort(arr)
print(arr)

arr = np.concatenate((arr, [1, 2, 3]))
print(arr)

arr = np.array_split(arr, 3)
print(arr)

