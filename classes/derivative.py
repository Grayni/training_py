import math


class Derivative:
    def __init__(self, func):
        self.__func = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__func(x + dx) - self.__func(x)) / dx


@Derivative
def sin_func(value):
    return math.sin(value)
# alternative option
# sin_func = Derivative(sin_func)


df_sin_func = sin_func(math.pi/4)

print(df_sin_func)
