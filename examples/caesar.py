from string import ascii_uppercase as au


def caesar(text, key):
    text = ''.join(filter(lambda x: x in au, text.upper()))
    encrypt = ''.join(map(lambda x: au[(au.index(x) + key) % 26], text))

    return encrypt


print(caesar('Ave, Caesar', 3))
