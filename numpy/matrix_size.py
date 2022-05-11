import numpy as np

n = 6
m = 2
k = 3

Z = np.zeros(shape=(m, k), dtype='int')
x = 0

for i, t in enumerate(Z):
    for j, l in enumerate(Z[i]):
        Z[i][j] = int(x)
        x += 1

print(Z)
print('\n')
# variant 2
Z = np.arange(n).reshape((m, k))
print(Z)
