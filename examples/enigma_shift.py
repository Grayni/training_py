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


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    text = filter(lambda x: x in ROTORS[0], text.upper())
    rotors = [rot3, rot2, rot1]

    shiftes = [shift3, shift2, shift1]
    val = ''

    for t in text:
        for i, rot in enumerate(rotors):
            t = alphabet[(alphabet.index(t) + shiftes[i]) % len(alphabet)]
            t = ROTORS[rot][ROTORS[0].index(t)]
            t = alphabet[(alphabet.index(t) - shiftes[i]) % len(alphabet)]
        val += t

    text = val
    val = ''

    for t in text:
        t = REFLECTORS[ref][REFLECTORS[0].index(t)]
        val += t

    text = val
    val = ''
    rotors = [rot1, rot2, rot3]
    shiftes = [shift1, shift2, shift3]

    for t in text:
        for i, rot in enumerate(rotors):
            t = alphabet[(alphabet.index(t) + shiftes[i]) % len(alphabet)]
            t = ROTORS[0][ROTORS[rot].index(t)]
            t = alphabet[(alphabet.index(t) - shiftes[i]) % len(alphabet)]
        val += t

    return val


print(enigma('A', 1, 0, 0, 0, 0, 3, 2))
