def double_factorial(value):
    if value in (0, 1):
        return 1

    return value * double_factorial(value - 2)


print(double_factorial(6))
print(double_factorial(5))
