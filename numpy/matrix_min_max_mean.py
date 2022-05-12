import numpy as np

np.random.seed(42)
n, m = map(int, input().split())
Z = np.random.random([n, m])


Z = np.transpose(Z)
mean = np.array([])
for i in Z:
    mean = np.append(mean, np.sum(i)/len(i))

print(np.min(mean))
print(np.max(mean))
