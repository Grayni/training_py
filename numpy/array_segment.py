import numpy as np
start = int('0')
stop = int('1')
n = int('10')
Z = np.round(np.linspace(start, stop, n+2)[1:-1], 3)
print(Z)
