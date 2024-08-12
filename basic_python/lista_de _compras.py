#  faça uma lista de compras

acao = input("Selecione uma opção...\n[i]nserir, [a]pagar, [l]istar.")
lista_de_compras = []
indice = 0

# 1- faça a lista onde o usuário vai inserir os itens.

while True:
    if acao == "i":
        valor = (input("Valor: "))
        lista_de_compras.append(valor)

    for item in enumerate(lista_de_compras):
        indice, valor = item
        print(item)

        indice += 1

    if acao == "a":
        valor = (input("Valor: "))
        lista_de_compras.pop(valor)
