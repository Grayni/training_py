import numpy as np

ls1 = list(map(int, '1, 2, 3, 4'.split(', ')))
ls2 = list(map(int, '10, 20, 30, 40'.split(', ')))

V1 = np.array(ls1)
V2 = np.array(ls2)
V3 = np.array(ls1) + np.array(ls2)
V4 = (np.array(ls1) * np.array(ls2[::-1]))[::2]

print(f'{V1}\n{V2}\n{V3}\n{V4}')
