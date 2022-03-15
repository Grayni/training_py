class Vector:
    def __init__(self, *args, **kwargs):
        self.values = [x for x in list(args) if type(x) == int]

    def __str__(self):
        if len(self.values):
            return f"Вектор({', '.join(map(str, sorted(self.values)))})"
        else:
            return "Пустой вектор"

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"