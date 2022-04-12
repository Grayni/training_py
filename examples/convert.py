# convert list with different type in int type


def convert(L):
    return [int(v) for v in L]


lst = [1, 2, '3', '4', '5', 6]

print(convert(lst))  # [1, 2, 3, 4, 5, 6]
