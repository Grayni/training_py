class Clock:
    __DAY = 86400

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __init__(self, seconds):
        if not isinstance(seconds, int):
            raise TypeError('Введите целое число')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.__get_formatted(self.seconds % 60)
        m = self.__get_formatted(self.seconds // 60 % 60)
        h = self.__get_formatted(self.seconds // 3600)
        return f'{h}:{m}:{s}'

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Нужны число или класс Clock')

        if isinstance(other, Clock):
            st = other.seconds
        else:
            st = other

        return Clock(self.seconds + st)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Нужны число или класс Clock')

        if isinstance(other, Clock):
            st = other.seconds
        else:
            st = other

        self.seconds += st

        return self


time1 = Clock(16300)
time2 = Clock(10000)
time = 4 + time1 + time2 + 57 + time1
time += 100
print(time1.get_time(), time2.get_time(), time.get_time())
