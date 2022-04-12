def factorial(value):
    if value == 0:
        return 1

    return value * factorial(value - 1)


def sf(value):
    if value == 0:
        return 1

    return factorial(value) * sf(value - 1)


print(factorial(4))  # 24
print(sf(4))  # 288


