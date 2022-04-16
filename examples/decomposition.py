def numerics(n):
    return list(map(int, list(str(n))[::-1]))


num = 2543
print(numerics(num))
