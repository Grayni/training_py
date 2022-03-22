class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'Initializer of class {self.__class__}')
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):

    def draw(self):
        print('Draw line')


class Rect(Geom):

    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, x2, y1, y2)
        print('Initializer of Rect')
        self.fill = fill

    def draw(self):
        print('Draw Rect')


line = Line(0, 0, 10, 20)
rect = Rect(1, 2, 3, 4, 'red')
print(line.__dict__)
print(rect.__dict__)
