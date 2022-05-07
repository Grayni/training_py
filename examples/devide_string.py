import math


def front_back(a, b):
    a = [a[0:int(math.ceil(len(a)/2))], a[int(math.ceil(len(a)/2)):]]
    b = [b[0:int(math.ceil(len(b)/2))], b[int(math.ceil(len(b)/2)):]]
    return a[0] + b[0] + a[1] + b[1]


print(front_back('abdff', 'tewts'))