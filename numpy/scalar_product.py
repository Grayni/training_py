import numpy as np

A = np.array([1.5, 2.5, 3.5])
B = np.array([4, 5, 6])

print(np.sum(A*B))

# variant 2

Z = A @ B

print(Z)
