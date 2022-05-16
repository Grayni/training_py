import numpy as np

start = int('1')
stop = int('1000')
n = int('4')

Z = np.geomspace(start, stop, n).round(3)

print(Z)
