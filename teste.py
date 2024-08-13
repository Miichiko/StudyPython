# soma2 = sum(int(nove_digitos[i]) * (11 - i) for i in range(9))

cpf = [2, 3, 5, 8, 5, 6, 4, 9, 8]
nova_lista = []

# 2 x 11
# 3 x 10
# 5 x 9

for indice, numero in enumerate(range(11, 2, -1)):
    soma = numero * cpf[indice]
    nova_lista.append(soma)


print(sum(nova_lista))
