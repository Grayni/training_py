import random
import math

random.seed(42)
n = 6
clear_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
step = 4

discs = []
for i in range(n):
    arr = list(clear_alphabet)
    random.shuffle(arr)
    discs.append(''.join(arr))

print(discs)

text = 'Some encripted text'


def jefferson_encryption(text, discs, step, reverse=False):

    new_str = ''.join(filter(lambda x: x in clear_alphabet, list(text.upper())))
    value_blocks = math.ceil(len(new_str) / n)

    ind = 1
    en_str = ''

    if reverse:
        ind = -1

    for i in range(value_blocks):
        part_str = new_str[n*i:n*i+n]
        for j in range(len(part_str)):
            en_str += discs[j][(discs[j].index(part_str[j]) + ind * step) % len(discs[0])]
    return en_str


print(jefferson_encryption(text, discs, step, reverse=False))
