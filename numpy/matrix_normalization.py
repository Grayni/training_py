import numpy as np

Y = np.array([[1, 2], [2, 1]])
mean = np.mean(Y)
std = np.std(Y)

Z = np.around((Y - mean)/std, 2)

print(Z)
