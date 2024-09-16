class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Dúcie', 'Maria')

p2 = Pessoa('José', 'Bezerra')

print(p1.nome)
print(p2.nome)
