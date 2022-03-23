class Point:
    MAX_COORD = 100
    MIN_COORD = 0


A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})
pt = A()


class B1:
    pass


class B2:
    pass


A = type('Point', (B1, B2), {'MAX_COORD': 100, 'MIN_COORD': 0})
print(A.__mro__)


def method_1(self):
    print(self.__dict__)


A = type('Point', (B1, B2), {'MAX_COORD': 100, 'method_1': method_1})

pt = A()