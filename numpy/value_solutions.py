import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[12, 2, 1]])

det_A = np.linalg.det(A)
print(det_A) # 0.0

print(A, '\n')
C = np.concatenate((A, B.T), axis=1)
print(C)

rank_A, rank_C = np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001)
print(rank_A, rank_C)
n = A.shape[1]
print(n)

if rank_A < rank_C:
    print("Система не имеет решений")
elif (rank_A == rank_C) and (rank_A == n):
    print("Система имеет единственное решение")
else:
    print("Система имеет бесконечное кол-во решений")

B = np.array([[1, 1, 1]])
C = np.concatenate((A, B.T), axis=1)
print(np.linalg.matrix_rank(C))
print(C)