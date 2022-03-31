def sum_arr(arr):
    if len(arr) == 0:
        return 0
    return arr.pop(0) + sum_arr(arr)


print(sum_arr([1, 2, 3, 5]))

