lst = [4, 2, 54, 1, 6, 7, 9, 33, 22, 12, 5, 32]


def binary_search(arr, value):
    """
    binary algorithm
    :param arr: int values
    :param value: need to find this value
    :return: index of value in sort arr
    """

    arr.sort()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid

        if arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(lst, 6))

