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


text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
disk = 1


def rotor(symbol, n, reverse=False):
    if reverse:
        return ROTORS[0][ROTORS[n].index(symbol)]
    else:
        if symbol in ROTORS[n]:
            return ROTORS[n][ROTORS[0].index(symbol)]
        return ''


string = ''

for symbol in text:
    string += rotor(symbol, disk)

print(string)