import numpy as np
data = '2 3 bool'.split(' ')
dt = np.float64

if not data[-1].isdigit():
    dt = data[-1]
    sp = tuple(map(int, data[:-1]))
else:
    sp = tuple(map(int, data))

Z = np.zeros(shape=sp,  dtype=dt)

print(Z)

