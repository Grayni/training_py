REFLECTORS = {
    0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
    3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
    4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
}


text = 'SOME ENCRYPTED TEXT FOR EXAMPLE'
disk = 1

# Reflected: FMOQQKUBAIZQHZQJZSMBQJYOIGQ


def reflector(symbol, n):
    if symbol in REFLECTORS[0]:
        return REFLECTORS[n][REFLECTORS[0].index(symbol)]
    return ''


string = ''

for i in text:
    string += reflector(i, disk)

print(string)
