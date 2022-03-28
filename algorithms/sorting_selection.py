lst = [6, 2, 1, 6, 9, 5, 33, 3, 0, 44]


def find_least_index(arr):
    least = arr[0]
    least_index = 0

    for i in range(1, len(arr)):
        if arr[i] < least:
            least_index = i
            least = arr[i]
    else:
        return least_index


def sort_arr(arr):
    lst_buffer = []
    for i in range(len(arr)):
        min_value_index = find_least_index(arr)
        lst_buffer.append(arr.pop(min_value_index))

    return lst_buffer


print(sort_arr(lst))
