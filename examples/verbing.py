def verbing(s):
    if len(s) > 2 and 'ing' in s:
        return s + 'ly'
    elif len(s) > 2:
        return s + 'ing'
    return s


print(verbing('hail'))  # hailing
print(verbing('swiming'))  # swimingly
print(verbing('do'))  # do
