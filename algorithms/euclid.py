from math import gcd


def algorithm_euclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


print('euclid`s algorithm:', algorithm_euclid(1680, 640))

# alternative
print('math.gcd:', gcd(1680, 640))
