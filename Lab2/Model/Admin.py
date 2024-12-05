class Admin:
    def __init__(self, id, name, password, role = "Admin"):
        self._id = id
        self._name = name
        self._password = password
        self._role = role

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._password

    @property
    def role(self):
        return self._role
