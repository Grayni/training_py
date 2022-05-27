import numpy as np

input_1 = '2 5 1'
input_2 = '1 -10 3'

arr_1 = list(map(int, input_1.split()))
arr_2 = list(map(int, input_2.split()))

print(*np.linalg.solve([arr_1[:2], arr_2[:2]], [arr_1[-1], arr_2[-1]]))
