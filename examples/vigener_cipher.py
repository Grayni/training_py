from math import ceil


def jarriquez_encryption(text, key, a='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    letters = ''.join(filter(lambda x: x in a, text.upper()))
    key_str = (f'{key}' * ceil(len(text) / len(str(key))))[:len(text)]

    new_str = ''
    for i, key in enumerate(letters):
        new_str += a[(a.index(key) + (-1)**reverse * int(key_str[i])) % len(a)]

    return new_str


print(jarriquez_encryption('Some encripted text for this assignment', 26101986, a='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False))