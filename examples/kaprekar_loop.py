import decomposition
import kaprekar_step as ks


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
    while n != 6174:
        print(n)
        n = decomposition.numerics(n)
        n = ks.kaprekar_step(n)
    print(n)


num = 8654

print(kaprekar_loop(num))


