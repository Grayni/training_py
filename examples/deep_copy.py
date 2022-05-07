def deep_copy(L):
    arr = []
    for val in L:
        if type(val) is list:
            arr.append(deep_copy(val))
        else:
            arr.append(val)
    return arr


L1 = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]
L2 = deep_copy(L1)

print(L1)
print(L2)
print(id(L1), id(L2))
