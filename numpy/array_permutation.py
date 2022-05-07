import numpy as np

string = '1, 2, 3, 4, 5.0, 6, 7, 8, 9, 10'

V1 = np.array(list(map(lambda x: float(x), string.split(', '))))
V2 = np.array(V1[-2:-1])
V3 = np.array(V1[::-1])
V4 = np.array(V1[::3])
V5 = np.array(range(len(V1)))

print(string.split(', '))  # ['1', '2', '3', '4', '5.0', '6', '7', '8', '9', '10']
print(V1)  # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
print(V2)  # [9.]
print(V3)  # [10.  9.  8.  7.  6.  5.  4.  3.  2.  1.]
print(V4)  # [ 1.  4.  7. 10.]
print(V5)  # [0 1 2 3 4 5 6 7 8 9]
