def bruteforce(text, a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    # all variants with step -= 1

    letters = ''.join(filter(lambda l: l in a, text.upper()))

    for i in range(len(a) - 1, 0, -1):
        convert_string = ''.join(map(lambda l: a[(a.index(l) + i) % len(a)], letters))
        print(convert_string)


bruteforce('BQQMF')
