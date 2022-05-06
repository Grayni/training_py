def list_pull(L):
    arr = []
    for val in L:
        if type(val) is list:
            arr.extend(list_pull(val))
        else:
            arr.append(val)

    return arr


print(list_pull([['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]))


# variant 2

def list_pull(L):
    ls0=[]
    lscopy=L[:]
    for outer in lscopy:
        if type(outer) is list:
            lscopy.extend(outer)
        else:
            ls0.append(outer)
    return(ls0)


print(list_pull([['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]))