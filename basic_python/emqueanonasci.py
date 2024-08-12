# Faça um programa que o cliente pode digitar a idade dele e o programa fale em que ano ele nasceu
# já fiz para você a variável que captura a idade do cliente, agora entregue como print o ano que ele nasceu:

# 1- pega a idade do cliente.
idade_do_cliente = input("Qual sua idade?")
# como conferir se já fez aniversário - boolean.
aniversario = input('Você já fez aniversário?')
# 2- subtrair por 2024.
# se a pessoa fez aniversário se não -1 se sim deixe como está.
if aniversario == 'sim':
    resultado = (2024 - int(idade_do_cliente))
else:
    resultado = (2024 - int(idade_do_cliente)) -1
    
# 3- fazer o print do ano que ele nasceu.
print(resultado)


