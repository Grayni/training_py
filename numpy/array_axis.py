import numpy as np

arr = np.random.randint(0, 24, 24).reshape(4, 6)
arr_c = np.random.randint(0, 24, 24).reshape(4, 6)
print(arr)

arr1 = arr.max(axis=0)
print(arr1)

arr2 = arr.max(axis=1)
print(arr2)

arr3 = arr.mean(axis=0)  # middle value in row/str
print(arr3, '\n----\n')
print(arr, '\n----\n')
print(arr_c, '\n----\n')

arr4 = np.concatenate((arr, arr_c), axis=1)
print(arr4, '\n----\n')

arr5 = np.hstack((arr, arr_c))
print(arr5, '\n----\n')

arr6 = np.vstack((arr, arr_c))
print(arr6, '\n----\n')

arr7 = np.split(arr6, 2) # split matrix
print(arr7, '\n----\n')