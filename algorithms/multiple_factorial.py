def multiple_factorial(value, k=1):
    if value <= 1:
        return 1

    return value * multiple_factorial(value - k, k)


print(multiple_factorial(6, 3))

