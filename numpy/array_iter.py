import numpy as np

# V = range(10)

V = map(np.sin, range(10))
Z = np.array(list(V), dtype=float)
print(Z)
