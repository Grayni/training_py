def dot(a, b):
    if len(a) != len(b[0]):
        raise Exception('Bad sizes of arrays')

    result = []

    for num_a in range(len(a)):
        arr = []
        for i in range(len(b[0])):
            value = 0
            for j in range(len(b)):
                value += a[num_a][j] * b[j][i]
            arr.append(value)
        result.append(arr)

    return result


print(dot([[1, 2], [2, 2], [5, 3]], [[1, 1, 4], [2, 2, 7]]))


import numpy as np

print(np.dot([[1, 2], [2, 2], [5, 3]], [[1, 1, 4], [2, 2, 7]]))
