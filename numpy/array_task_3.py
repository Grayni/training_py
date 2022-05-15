import numpy as np

m, n = map(int, '5 4'.split())
k = int('-5')

X = np.arange(k, k+n)

print(X)
Z = np.zeros((m, n)) + X
print(Z)
