class Geom:
    def get_pr(self):
        raise NotImplementedError('No method get_pr() in child class')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_pr_(self):
        return self.x + self.y + self.z


geom = [
    Rectangle(1, 2), Rectangle(3, 4),
    Square(10), Square(20),
    Triangle(4, 5, 6), Triangle(1, 2, 3)
]

for s in geom:
    print(s.get_pr())

