# find index of max int


def convert(L):
    return [int(v) for v in L]


def max_id(ls):
    lstc = convert(ls)
    return lstc.index(max(lstc))


lst = [1, 2, '42', '3', '4', '5', 6, 13]
convert_lst = convert(lst)
print(convert_lst)  # [1, 2, 42, 3, 4, 5, 6, 13]

print(max_id(convert_lst))
