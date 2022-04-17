from decomposition import numerics
from kaprekar_step import kaprekar_step


# monolith
# def kaprekar_loop(n):
#
#     while n != 6174:
#         L = list(map(int, str(n)))
#         min_num = int(''.join(map(str, sorted(L))))
#         max_num = int(''.join(map(str, sorted(L)[::-1])))
#         n = max_num - min_num
#         print(n)
#     return ''


def kaprekar_loop(n):
    if n == 1000:
        print('Ошибка! На вход подано число 1000')
    elif len(set(map(int, str(n)))) == 1:
        print(f'Ошибка! На вход подано число {n} - все цифры одинаковые')
    else:
        while n != 6174:
            print(n)
            n = numerics(n)
            n = kaprekar_step(n)
        print(n)


num = 1111

print(kaprekar_loop(num))


