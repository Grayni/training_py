class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x**2 + self.y**2

    def __bool__(self):
        print('__bool__')
        return self.x == self.y


p = Point(3, 4)
print(bool(p))

if p:
    print('Bool True')
else:
    print('Bool False')

