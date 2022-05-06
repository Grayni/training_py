import math


def derivative(f, x0=0):
    dx = 0.0001
    return round((f(x0+dx) - f(x0)) / dx, 3)


print(derivative(math.sin))  # 1.0
print(derivative(math.cos))  # -0.0
print(derivative(math.atan, 1000000))  # 0.0
print(derivative(math.exp, 1))  # 2.718
