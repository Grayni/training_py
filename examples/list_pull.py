def list_pull(L):
    arr = []
    for val in L:
        if type(val) is list:
            arr.extend(list_pull(val))
        else:
            arr.append(val)

    return arr


print(list_pull([['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]))
