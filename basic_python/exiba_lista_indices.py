#  Exercicio: em uma lista exiba os indices das variaveis "Qualquer","coisa","aleatória".

lista = ["Qualquer","coisa","aleatória"]
indice = 0


while indice < len(lista):
    print(f'{indice}, {lista[indice]}')

    indice += 1

#  *variável serve pra guardar o resto de uma lista, por ex:

# nome1, *resto = ["Qualquer","coisa","aleatória"]

# print(nome1, resto)
