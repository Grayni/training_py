def luka(L0, L1, n):
    for i in range(0, n):
        L0, L1 = L1, L0 + L1
    return L0


print(luka(42, 13, 1))
