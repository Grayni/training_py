# convert number system


def cns(num, k=2):
    if num//k == 0:
        return num
    return f'{cns(int((num-num%k)/k), k)}' + f'{num%k}'


print(cns(8, 3))  # 22
