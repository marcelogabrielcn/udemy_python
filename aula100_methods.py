"""
Veremos as diferenças entre os métodos, estáticos, e métodos de classe
"""


class Connection():
    def __init__(self, host='localhost'):
        self.host = host
        self.name = None
        self.password = None
    
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, name, password):
        connection2 = cls()
        connection2.name = name
        connection2.password = password
        return connection2
    
    @staticmethod
    def teste():
        ...
    

c1 = Connection()
c1.name = 'Gabriel'
c1.password = 'teste123'
print(c1.name)
print(c1.password)

c2 = Connection.create_with_auth('Gabriel', 'teste4321')
print(c2.name)
print(c2.password)
