import numpy as np

data = [1, 2, 3, 4, 5, 2, 3]
arr1 = np.array(data)
arr2 = np.array(data, dtype=np.float64)

print('arrays:', arr1, arr2)
print('shape:', arr1.shape, arr2.shape)  # number of index

print('type:', arr1.dtype, arr2.dtype)  # type
print('dimension:', arr1.ndim, arr2.ndim)  # dimension
print('len:', len(arr1), len(arr2))
print('size:', arr1.size, arr2.size)

arr3 = np.array(data)
arr3 = arr3.astype(np.int64)
print('change type:', arr3.dtype)
