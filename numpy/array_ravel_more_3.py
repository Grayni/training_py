import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 9]])
x = np.ravel(x)
x = [val for val in x if val > 3]

print(x)
