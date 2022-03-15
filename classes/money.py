class Money:
    total_cents = 0

    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, ds):
        if not type(ds) == int or ds < 0:
            print("Error dollars")
        else:
            self.total_cents = ds * 100 + self.total_cents % 100

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cs):
        if not type(cs) == int or cs < 0 or cs > 99:
            print("Error cents")
        else:
            self.total_cents = (self.total_cents // 100) * 100 + cs

    def __repr__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
