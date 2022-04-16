# fibonacci index
num = 9


def fib(n):
    arr = [0, 1]
    while n != 1:
        arr.append(sum([arr[-2], arr[-1]]))
        n -= 1

    return arr[-1]


print(fib(num))  # 34
