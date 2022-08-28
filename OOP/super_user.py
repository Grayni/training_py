class User:
    count = 0

    def __init__(self, name, login, password):
        self.name = name
        self._login = login
        self.__password = password
        self.__class__.count += 1

    @property
    def login(self):
        return self._login

    def set_password(self, value):
        self.__password = value

    password = property(fset=set_password)

    def show_info(self):
        print(f'Hello, {self._login} ({self.name})')


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.role = role
        self.count += 1

    @property
    def param_role(self):
        return self.role

    @param_role.setter
    def param_role(self, value):
        self.role = value

    def show_info(self):
        print(f'Hello, {self._login} ({self.name}). Role: {self.param_role}')


user_1 = User('Paul McCartney', 'paul', '1234')
user_2 = User('George Harrison', 'george', '5678')
user_3 = User('Richard Starkey', 'ringo', '8523')
admin = SuperUser('John Lennon', 'john', '0000', 'admin')

user_1.show_info()
admin.show_info()

users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')  # 3
print(f'Всего супер-пользователей: {admins}')  # 1

user_3.name = 'Ringo Star'
print(user_3.name)  # Ringo Star

print(user_2.login)  # george

# user_2.login = 'geo'  # error

user_1.password = 'Pa$$w0rd'
# print(user_1.password)  # error

admin.param_role = 'mega-admin'
print(admin.role)
