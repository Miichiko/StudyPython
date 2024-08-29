# yiedy transforma as funções em geradores
# permite armazenar conjuntos de valores,
# mas sem armazena-los na memória.

# aki estou criando um gerador, usando yield como pause e chamando o valor só quando é a vez dele
def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    # tem como importar uma funçao pra dentro de outra, mas aki: é yield from alguma_coisa().
    yield from gen1()
    yield 4
    yield 5
    yield 6


g = gen2()

for numero in g:
    print(numero)

# fazer um exemplo sem precisar digitar yield toda hora.


def contador(maximo):
    contador = 1
    while contador <= maximo:
        yield contador
        contador += 1


# usando o gerador
for numero in contador(10):
    print(numero)

# assim posso processar uma grande quantidade de informações.
