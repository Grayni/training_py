# sort list alphabetically and words with first letter - 'x' => first in list

arr = ['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']


def front_x(words):
    lst = []
    for n in sorted(words):
        if n:
            lst.insert(0, n) if n[0] == 'x' else lst.append(n)
        else:
            lst.append(n)

    return lst


print(front_x(arr))  # ['xyz', 'xapple', 'x-files', '', 'apple', 'extra', 'mix']
