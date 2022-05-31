import numpy as np
# find coefficients of polynomial
inp = '6'  # value of polynomials

inp_arr = ['0 1', '1 1', '2 25', '-1 1', '-2 -23', '0.5 0.90625']  # [[x y], [x y] ...]
M = np.array([])
v = np.array([])


for i in range(int(inp)):
    empty = np.array([])
    v = np.append(v, float(inp_arr[i].split()[1]))

    for j in range(int(inp)):
        empty = np.append(empty, float(inp_arr[i].split()[0]) ** j)

    if M.shape[0] == 0:
        M = np.array([empty])
    else:
        M = np.concatenate((M, [empty]))


print(M, '\n')
print(v, '\n')
print(np.linalg.solve(M, v))
