a = 3
b = 4


def f(x):
    return (x+a)**2 - b


def g(x):
    return abs(f(x))


print(f(2))
print(g(2))
