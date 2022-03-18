class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    @staticmethod
    def verify_value(my_rating, sign, value):
        if isinstance(value, int):
            return eval(f'{my_rating} {sign} {value}')
        elif isinstance(value, ChessPlayer):
            return eval(f'{my_rating} {sign} {value.rating}')

        return 'Невозможно выполнить сравнение'

    def __eq__(self, other):
        return self.verify_value(self.rating, '==', other)

    def __gt__(self, other):
        return self.verify_value(self.rating, '>', other)

    def __lt__(self, other):
        return self.verify_value(self.rating, '<', other)

magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus > ian) # True
print(magnus < ian) # False
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"