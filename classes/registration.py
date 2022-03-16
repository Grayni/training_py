import string

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not '@' in value:
            raise ValueError("Login must include at least one '@'")

        if not '.' in value:
            raise ValueError("Login must include at least one ' . '")

        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not type(value) == str:
            raise TypeError("Пароль должен быть строкой")

        if not 5 <= len(value) <= 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')

    @staticmethod
    def is_include_digit(digits):
        if not len([x for x in digits if x.isdigit()]):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

    @staticmethod
    def is_include_all_register(password):
        if len([x for x in password if x == x.upper()]) < 2:
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')

    @staticmethod
    def is_include_only_latin(st):
        for x in st:
            if x in string.punctuation:
                raise ValueError('Пароль должен содержать только латинский алфавит')

    @staticmethod
    def check_password_dictionary(st):
        with open('easy_password.txt', 'r', encoding='utf-8') as f:
            while True:
                x = f.readline()

                if not x:
                    break

                if st == x[:-1]:
                    raise ValueError('Ваш пароль содержится в списке самых легких')
