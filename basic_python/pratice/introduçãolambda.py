#  a função lambda não tem nome, parenteses, return e é usada pra coisas pequenas e rápidas.

# Ex: o dobro de 2
# dobro = lambda x: x * 2      <= não sei pq o meu códico esta alterando
def dobro(x): return x * 2   # <= isso vai inprimir 4


print(dobro(2))

# agora uma forma errada e confusa de se fazer para quem vai ver meu códico.
#  é usar letras tipo...


def executa(funcao, *args):
    return funcao(*args)


duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(duplica(2))
