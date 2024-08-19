# Crie uma função que duplica,triplica e/ou quadriplica o número recebido como parametro.

def potencia(base):
    def eleva(expoente):
        return base ** expoente
    return eleva


quadrado = potencia(2)

resultado = quadrado(3)
print(resultado)
