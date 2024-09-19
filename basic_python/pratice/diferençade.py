# method - @classmethod - @staticmethod

# se precisa de self usa method de instância

# Method
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def password(self, password):
        self.password = password

    #  auth quer dizer os dados de autentificação

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    # def soma(x, y):    não recebe self e class
    #     return x + y
    def connection_log(msg):
        print('LOG:', msg)


c1 = Connection()
c1 = Connection.create_with_auth('Michiko', '2708')
print(c1.user)
print(c1.password)
