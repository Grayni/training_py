obj = {'e': '8', 't': ';', 'h': '4', 'o': '‡', 's': ')', 'n': '*', 'a': '5', 'i': '6', 'r': '(', 'f': '1', 'd': '†', 'l': '0', 'm': '9', 'b': '2', 'y': ':', 'g': '3', 'u': '?', 'v': '¶', 'c': '-', 'p': '.'}

value = 'ethosnairfdlmbyguvcp'


def kidds_encryption(text, reverse=False):
    text = text.lower()
    word = ''

    if reverse:
        for letter in text:
            for key, value in obj.items():
                if letter == value:
                    word += key
                    break
    else:
        for letter in text:
            if letter in obj:
                word += obj[letter]

    return word


print(kidds_encryption('te st'))