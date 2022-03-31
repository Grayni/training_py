def counter_func(arr):
    if arr == []:
        return 0
    else:
        arr.pop(0)
        return 1 + counter_func(arr)


print(counter_func([1, 2, 3, 4, 5, 3, 3]))

