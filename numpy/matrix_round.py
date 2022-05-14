import numpy as np

A = np.array([-3.1, -5.9, 0, 2.2, 9.8])
Z = np.copysign(np.ceil(np.absolute(A)), A)

print(Z)
