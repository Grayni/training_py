import numpy as np

m, n = map(int, '5 4'.split())
k = int('-5')

X = np.arange(k, k+m)

print(X)
Z = np.transpose(np.zeros((n, m)) + X)
print(Z)