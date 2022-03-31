def counter_func(arr):
    if arr == []:
        return 0
    else:
        return 1 + counter_func(arr[1:])


print(counter_func([1, 2, 3, 4, 5, 3, 3]))

