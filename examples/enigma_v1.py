from collections import Counter
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ROTORS = {
    0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
    2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
    3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
    4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
    5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
    6: 'JPGVOUMFYQBENHZRDKASXLICTW',
    7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
    8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
    'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
    'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
}

REFLECTORS = {
    0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
    3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
    4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
}

steps = {
    1: 17,
    2: 5,
    3: 22,
    4: 10,
    5: 0
}


def change_pairs(symbol, p):
    if symbol in p:
        if p.index(symbol) % 2:
            symbol = p[p.index(symbol) - 1]
        else:
            symbol = p[p.index(symbol) + 1]
    return symbol


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    text = filter(lambda x: x in ROTORS[0], text.upper())
    val = ''

    rotors = [rot1, rot2, rot3]
    shiftes = [shift1, shift2, shift3]

    pairs = ''.join(pairs.split(' ')).upper()
    c = Counter(pairs)
    print(pairs)

    for t in text:

        if c[t] > 1:
            return "Извините, невозможно произвести коммутацию"

        t = change_pairs(t, pairs)

        rotors = rotors[::-1]
        shiftes = shiftes[::-1]

        shiftes[0] += 1
        if shiftes[1] + 1 % len(alphabet) == steps[rotors[1]]:
            shiftes[1] += 1
            if shiftes[1] % len(alphabet) == steps[rotors[1]]:
                shiftes[2] += 1

        if shiftes[0] % 26 == steps[rotors[0]]:
            shiftes[1] += 1

        print(shiftes[0], shiftes[1], shiftes[2])

        for i, rot in enumerate(rotors):
            t = alphabet[(alphabet.index(t) + shiftes[i]) % len(alphabet)]
            t = ROTORS[rot][ROTORS[0].index(t)]
            t = alphabet[(alphabet.index(t) - shiftes[i]) % len(alphabet)]

        t = REFLECTORS[ref][REFLECTORS[0].index(t)]

        rotors = rotors[::-1]
        shiftes = shiftes[::-1]
        for i, rot in enumerate(rotors):
            t = alphabet[(alphabet.index(t) + shiftes[i]) % len(alphabet)]
            t = ROTORS[0][ROTORS[rot].index(t)]
            t = alphabet[(alphabet.index(t) - shiftes[i]) % len(alphabet)]

        t = change_pairs(t, pairs)
        val += t

    return val


print(enigma('A', 1, 1, 0, 2, 0, 3, 0, ''))
