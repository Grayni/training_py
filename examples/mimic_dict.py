def mimic_dict(string):
    arr = string.split()

    dictionary = {'': [arr[0]]}
    print(arr)
    for i, key in enumerate(arr):
        if key != arr[-1]:
            if key in dictionary:
                dictionary[key].append(arr[i+1])
            else:
                dictionary[key] = [arr[i+1]]
    return dictionary


print('a cat and a dog\na fly')
print(mimic_dict('a cat and a dog \na fly'))


# variant 2

def mimic_dict(string):
    words = string.split()

    d = {}

    prev_word = ""
    for word in words:
        d.setdefault(prev_word, []).append(word)
        prev_word = word

    return d
