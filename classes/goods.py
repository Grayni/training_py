class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print('Print info out Goods')
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        print('init MixinLog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: product sold at 00:00:00')

    def print_info(self):
        print('Print info out MixinLog')


class Notebook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)  # Var1 overrided for MixinLog


n = Notebook('Acer', 1.5, 30000)
MixinLog.print_info(n)  # Var2

n.print_info()
n.save_sell_log()

print(Notebook.__mro__)