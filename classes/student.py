class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if not isinstance(value, int):
            raise TypeError('Укажите целое число')
        if value > 5 or value < 0:
            raise ValueError('Число должно быть в диапазоне от 0 до 5')

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')

        del self.marks[key]


s1 = Student('Alex', [4, 3, 4, 5])
s1[10] = 5

print(s1.marks)

del s1[2]

print(s1.marks)
