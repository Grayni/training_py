import numpy as np

A1 = np.array((-1, 1))
A2 = np.array((2, 5))
A3 = np.array((5, -3))


L1 = ((A1[0] - A2[0])**2 + (A1[1] - A2[1])**2)**0.5
L2 = ((A1[0] - A3[0])**2 + (A1[1] - A3[1])**2)**0.5
L3 = ((A2[0] - A3[0])**2 + (A2[1] - A3[1])**2)**0.5
p = (L1 + L2 + L3) / 2

result = (p*(p-L1)*(p-L2)*(p-L3))**0.5

print(result)
