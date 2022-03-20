class Geom:
    pass


class Line(Geom):
    pass


class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))


g = Geom()
l = Line()

print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
print(isinstance(l, Geom))
print(isinstance(Geom, object))
print(issubclass(int, object))
print(issubclass(list, object))


v = Vector([1, 2, 3])

print(v)