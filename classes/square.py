class Square:
    def __init__(self, side):
        self.__side = side
        self.__perimeter = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        print('remove out cache', self.__perimeter)
        self.__perimeter = None
        self.__side = value

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = self.side * 4
            print('add in cache', self.__perimeter)
        return self.__perimeter


d = Square(4)

print(d.perimeter)
print(d.perimeter)
print(d.perimeter)
d.side = 20
print(d.perimeter)
print(d.perimeter)
