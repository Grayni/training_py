from decomposition import numerics
from kaprekar_step import kaprekar_step


def kaprekar_check(n):
    if (n in range(101, 1000) or n in range(1001, 10000) or n in range(100001, 1000000)) and len(set(map(int, str(n)))) != 1:
        return True
    return False

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
    if kaprekar_check(n):
        arr = []
        while n not in [495, 6174, 549945, 631764]:
            print(n)
            n = numerics(n)
            n = kaprekar_step(n)
            if n in arr:
                return f"Следующее число - {n}, кажется процесс зациклился..."
            arr.append(n)
        print(n)
    else:
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")


num = 103303

print(kaprekar_loop(num))

