def caesar(text, key, a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    letters = ''.join([letter for letter in text.upper() if letter in a])
    new_string = ''.join(map(lambda l: a[(a.index(l) + key) % len(a)], letters))

    return new_string


print(caesar('Ave, Caesar', 3))
