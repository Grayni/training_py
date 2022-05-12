import numpy as np

np.random.seed(42)
n = 2
m = 6

Z = np.array(np.random.rand(n*m)).reshape(n, m)

print(np.min(Z))
print(np.max(Z))
