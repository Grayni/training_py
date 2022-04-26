import random


def disc_generator(alphabet):
    random.seed(42)
    arr = list(alphabet)
    random.shuffle(arr)
    new_alphabet = ''.join(arr)
    return new_alphabet


print(disc_generator('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
