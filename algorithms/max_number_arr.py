def max_number(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        arr.pop(-1) if arr[0] >= arr[-1] else arr.pop(0)
        return max_number(arr)


print(max_number([1, 8, 2, 5, 6, 2]))
