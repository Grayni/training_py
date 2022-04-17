def kaprekar_step(L):
    min_num = int(''.join(map(str, sorted(L))))
    max_num = int(''.join(map(str, sorted(L)[::-1])))
    return max_num - min_num


# l = [4, 5, 6, 8]
#
# print(kaprekar_step(l))