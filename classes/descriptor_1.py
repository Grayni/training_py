class PositiveNumber:
    @staticmethod
    def verify_coord(coord):
        if type(coord) != int:
            raise ValueError('Введите целое число')
        elif coord < 0:
            raise ValueError('Значение должно быть больше нуля')

    def __get__(self, instance, owner):
        return getattr(instance, self.coord_name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.coord_name, value)

    def __set_name__(self, owner, name):
        self.coord_name = '_' + name


class Coords:
    x = PositiveNumber()
    y = PositiveNumber()
    z = PositiveNumber()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def show_coords(self):
        return self.x, self.y, self.z


coords = Coords(4, 2, 9)
coords.z = 20
result = coords.show_coords()
print(result)
