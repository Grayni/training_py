class Women:
    title = 'Object of class for field "title"'
    photo = 'Object of class for field "photo"'
    ordering = 'Object of class for field "ordering"'

    def __init__(self, usr, pwd):
        self._user = usr
        self._password = pwd
        self.meta = self.Meta(usr + '@' + pwd)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access
            self._t = Women.title


print(Women.ordering)
print(Women.Meta.ordering)

w = Women('user_1', 'password_1')

print(w.ordering)
print(w.__dict__)
print(w.meta.__dict__)
