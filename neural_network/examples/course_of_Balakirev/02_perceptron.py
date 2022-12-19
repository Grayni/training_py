import numpy as np
import matplotlib.pyplot as plt

N = 5
b = 3

x1 = np.random.random(N)  # [0.0, 1.0)
deviation = np.random.randint(10, size=N) / 10

x2 = x1 + deviation + b
C1 = [x1, x2]

x1 = np.random.random(N)
deviation = np.random.randint(10, size=N) / 10

x2 = x1 - deviation - 0.1 + b
C2 = [x1, x2]

w = np.array([-0.3, 0.3])

for i in range(N):
    x = np.array([C2[0][i], C2[1][i]])
    y = np.dot(w, x)

    if y >= 0:
        print('Class C1')
    else:
        print('Class C2')

plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')

line = [0+b, 1+b]  # line coordinates per x, default y -> [0, 1, 2, ...]
plt.plot(line, '--')
plt.grid(True)
plt.show()

