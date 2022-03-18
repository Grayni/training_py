class Vector:
    def __init__(self, *args):
        self.values = sorted([d for d in args if type(d) == int])
        self.z = []

    def __str__(self):
        if len(self.values):
            return f'Вектор{tuple(self.values)}'
        else:
            return 'Пустой вектор'

    def __add__(self, other):
        if not isinstance(other, (int, Vector)):
            print(f"Вектор нельзя сложить с {other}")
            return Vector()

        if isinstance(other, int):
            self.z = list(map(lambda m: m + other, self.values))
        elif isinstance(other.values, list):
            if len(other.values) != len(self.values):
                print(f"Сложение векторов разной длины недопустимо")
                return Vector()
            self.z = [m + other.values[i] for i, m in enumerate(self.values)]
        return Vector(*self.z)

    def __mul__(self, other):
        if not isinstance(other, (int, Vector)):
            print(f'Вектор нельзя умножать с {other}')
            return Vector()

        if isinstance(other, int):
            self.values = list(map(lambda m: m * other, self.values))
        elif isinstance(other, Vector):
            if len(other.values) != len(self.values):
                print(f'Вектор нельзя умножать с {other}')
                return Vector()

            self.values = [m * self.values[i] for i, m in enumerate(other.values)]

        return Vector(*self.values)



v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"

v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
