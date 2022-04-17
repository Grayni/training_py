from decimal import *


def fi(L0, L1, n):
    for i in range(0, n-1):
        L0, L1 = L1, L0 + L1
    return Decimal(L1)/Decimal(L0)


print(fi(0, 1, 11))  # 1.618181818181818181818181818
