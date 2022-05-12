import numpy as np
n, m = 3, 3
Z = np.arange(n*m).reshape(n, m)
Z = np.pad(Z, (1, 1), 'constant', constant_values=(0, 0))
print(Z)

print('')
# Variant 2
Z = np.arange(n*m).reshape(n, m)
Z = np.pad(Z, 1, 'constant')
print(Z)
