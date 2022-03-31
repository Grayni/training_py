def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less_pivot = [i for i in arr[1:] if i <= pivot]
        greater_pivot = [i for i in arr[1:] if i > pivot]
        return qsort(less_pivot) + [pivot] + qsort(greater_pivot)


print(qsort([10, 20, 10, 12, 5, 3, 5, 6]))
