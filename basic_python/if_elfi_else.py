
# escolha = input("Voçe abre o baú nele tem... uma espada, um arco e um cajado. Escolha entre um dos itens. ")

# if escolha == "espada":
#     print("Voçe pega a espada!")
# elif escolha == "arco":
#     print("Voçe pega o arco!")
# elif escolha == "cajado":
#     print("Voçe pega o cajado!")    
# else:
#     print("skip.")



# ''' Faça um programa que peça ao usuário digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um
# número inteiro, informe que não é um número inteiro.'''

numero_str = input('Olá, por favor digite um valor inteiro.')
# print(type(numero_str))
if numero_str.isdigit():
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print('Seu número é par.')
    elif (numero_int) % 2 == 1:
        print('Seu número é ímpar') 
    else:
        pass
else:
    print("Voçe não digitou um número inteiro!")



# não consegui fazer 


