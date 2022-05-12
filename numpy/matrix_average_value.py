import numpy as np

np.random.seed(42)
n, m = list(map(int, input().split()))
Z = np.random.random([n, m])

print(np.sum(Z)/(n*m))
