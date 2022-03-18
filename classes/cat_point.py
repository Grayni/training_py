class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}'


cat = Cat('Tom')

print('str: ', cat)


class Point:

    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return tuple(abs(x) for x in self.__coords)


p = Point(-1, 2, -3)

print('len: ', len(p))
print('abs: ', abs(p))
