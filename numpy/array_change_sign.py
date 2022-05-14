import numpy as np
# range (3, 9)
P = np.arange(11)
Z = np.array([y * -1 if y in range(4, 9) else y for y in P])

print(Z)

# variant 2

P[np.logical_and(P > 3, P < 9)] *= -1

print(P)
