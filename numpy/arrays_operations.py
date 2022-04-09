import numpy as np
arr_def1 = [1, 2, 3, 4]
arr_def2 = [1, 2, 3, 4]
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3, 4])

print(arr_def1 + arr_def2)

# in numpy.array: '+' == add
print('\n', 'add')
print(arr1 + arr2)
print(np.add(arr1, arr2))

# in numpy.array: '*' == multiply
print('\n', 'multiply')
print(arr1 * arr2)
print(np.multiply(arr1, arr2))

# in numpy.array: '-' == subtract
print('\n', 'subtract')
print(arr1 - arr2)
print(np.subtract(arr1, arr2))

# in numpy.array: '/' == divide
print('\n', 'divide')
print(arr1 / arr2)
print(np.divide(arr1, arr2))

print()
print(arr1 * 2)
print(arr1**2)
