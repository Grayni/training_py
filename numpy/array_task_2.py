import numpy as np

M1 = np.array((
    (1., 2., 3., 0.),
    (4., 5., 6., 0.),
    (0., 1., 1., 6.),
    (7., 8., 9., 0.)
))

for i, x in enumerate(M1[-2]):
    M1[-2][i] = np.sin(x * np.pi / 6)

for i, x in enumerate(M1[:, -2]):
    M1[:, -2][i] = np.exp(x)

M2 = M1

print(M2)