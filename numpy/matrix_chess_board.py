import numpy as np
n = 3
m = 5
Z = np.ones(shape=(n, m))
Z[::2, ::2] = 0
Z[1::2, 1::2] = 0
print(Z)