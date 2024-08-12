#  faça uma lista de compras

# 1- faça a lista onde o usuário vai inserir os itens.


lista_de_compras = []
indice = 0

while (len(lista_de_compras)) < 10:

    opcao = input("Selecione uma opção...\n[i]nserir, [a]pagar, [l]istar. ")

    if opcao == "i":
        valor = (input("Valor: "))
        lista_de_compras.append(valor)

        if opcao == "a":

            if (len(lista_de_compras)) > 0:
                apagar = input("Escolha o índice para apagar: ")
                elemento_removido = lista_de_compras.pop(int(apagar))
            else:
                print("Erro: Nada para apagar.")

        if opcao == "l":
            if (len(lista_de_compras)) > 0:
                for item in enumerate(lista_de_compras):
                    indice, valor = item
                    print(item)
                    indice += 1
            else:
                print("Erro: nada para listar")
    else:
        print("Por favor, digite: i, a ou l.")
