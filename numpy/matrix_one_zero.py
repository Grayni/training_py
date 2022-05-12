import numpy as np

n, m = 10, 10 #map(int, input().split())

Z = np.zeros(shape=(n, m))

Z[0] = Z[0] + 1
for i in range(1, len(Z)-1):
    Z[i][0] = 1
    Z[i][-1] = 1

Z[-1] = Z[-1] + 1

print(Z)
print('\n')

# variant 2
Z = np.ones(shape=(n, m))
Z[1:-1, 1:-1] = 0

print(Z)

