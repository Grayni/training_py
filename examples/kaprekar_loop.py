def kaprekar_loop(n):

    while n != 6174:
        L = list(map(int, str(n)))
        min_num = int(''.join(map(str, sorted(L))))
        max_num = int(''.join(map(str, sorted(L)[::-1])))
        n = max_num - min_num
        print(n)
    return ''


num = 8654

print(kaprekar_loop(num))


