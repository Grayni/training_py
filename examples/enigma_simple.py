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


def enigma(text, ref, rot1, rot2, rot3):
    text = filter(lambda x: x in ROTORS[0], text.upper())
    rotors = [rot3, rot2, rot1]

    val = ''
    for t in text:
        for rot in rotors:
            t = ROTORS[rot][ROTORS[0].index(t)]
            print(t)
        val += t

    text = val
    val = ''

    for t in text:
        t = REFLECTORS[ref][REFLECTORS[0].index(t)]
        val += t
    print(val)

    text = val
    val = ''
    rotors = [rot1, rot2, rot3]

    for t in text:
        for rot in rotors:
            t = ROTORS[0][ROTORS[rot].index(t)]
            print(t)
        val += t

    return val


print(enigma('Some encripted text', 1, 1, 2, 3))  # LDRBBKJMWGFBOFBYF