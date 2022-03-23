class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt1 = Point(1, 2)

pt1.z = 3
print(pt1.z)  # no error


class Point_2d:
    __slots__ = ('x', 'y')  # confines

    def __init__(self, x, y):
        self.x = x
        self.y = y


pt2 = Point_2d(10, 20)

print(pt1.__sizeof__() + pt1.__dict__.__sizeof__())
print(pt2.__sizeof__())

