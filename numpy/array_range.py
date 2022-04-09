import numpy as np

arr1 = np.arange(0, 10, 1.5)  # fractional step
print(*arr1)  # 0.0 1.5 3.0 4.5 6.0 7.5 9.0

arr2 = np.linspace(0, 4, 5)  # range of numbers
print(*arr2)  # 0.0 1.0 2.0 3.0 4.0

arr_random1 = np.random.random((5,))
arr_random2 = np.random.random_sample((5,))
# random.random alias random.random_sample
print(arr_random1)
print(arr_random2)
