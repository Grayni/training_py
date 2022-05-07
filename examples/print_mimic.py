import random

def mimic_dict(string):
    arr = string.split()

    dictionary = {'': [arr[0]]}
    for i, key in enumerate(arr):
        if key != arr[-1]:
            if key in dictionary:
                dictionary[key].append(arr[i+1])
            else:
                dictionary[key] = [arr[i+1]]
    return dictionary


def print_mimic(mimic, word=''):
    txt = ''
    count = 0
    while True:
        if word != '':
            txt += word + ' '
            count += 1
        else:
            txt += word

        if word in mimic:
            word = random.choice(mimic[word])
        else:
            word = ''

        if count == 200:
            return txt.rstrip()


mimic = mimic_dict('''We are not what we should be\n
We are not what we need to be\n
But at least we are not what we used to be\n
  -- Football Coach''')

print(print_mimic(mimic))


# variant 2

def print_mimic(mdict, word, n=200):
    res = []
    for _ in range(n):
        res.append(word)
        word = random.choice(mdict.get(word, mdict['']))
    return ' '.join(res)
