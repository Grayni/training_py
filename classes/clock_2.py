class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Должно быть целое число.')
        self.seconds = seconds

    @classmethod
    def verify_data(cls, value):
        if not isinstance(value, (int, Clock)):
            raise TypeError('Значение должно быть int или Clock')

        return value if type(value) == int else value.seconds

    def __eq__(self, other):
        sc = self.verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.verify_data(other)
        return self.seconds <= sc


c1 = Clock(4100)
c2 = Clock(4100)

print(c1 == c2)
print(c1 < c2)
print(c1 >= c2)
# print(c1 == c2)

