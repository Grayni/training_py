# check value on simple number


def simple_numbers(n):
    if not n % 2 and n > 2:
        return False

    x = 2
    while x < n**0.5:
        x += 1

        if not n % x:
            return False
    return True


num = 11
print(simple_numbers(num))
