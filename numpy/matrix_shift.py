import numpy as np
x = 1
k = 2
Z = np.diagflat(np.arange(1, k+1), x)
print(Z)
