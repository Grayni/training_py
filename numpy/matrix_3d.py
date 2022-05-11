import numpy as np
n, m, l = map(int, input('send 3 numbers: ').split())
np.random.seed(42)
Z = np.array(np.random.random(n * m * l)).reshape(n, m, l)

print(Z)

print('')

# Variant 2
Z = np.random.rand(*(n, m, l))
print(Z)
