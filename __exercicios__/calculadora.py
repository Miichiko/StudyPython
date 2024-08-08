# peça ao usário dois números e um operador
# os números precisam ser válidos
# faça com que a calculadora execute +-*/
# faça uma opção de encerrar a seção
# use o try e except




# faça um if e elif pra cada situação 

try:
    numero1 = int(input("Escolha um número? "))
    operador = input("Escolha um operador (+-*/?)" )
    numero2 = int(input("Escolha um outro número? "))

    if operador == '+':
        resultado = numero1 + numero2
        print(f"Seu resultado é {resultado}.")

    elif operador == '-':
        resultado = numero1 - numero2
        print(f"Seu resultado é {resultado}.")

    elif operador == '*':
        resultado = numero1 * numero2
        print(f"Seu resultado é {resultado}.")

    elif operador == '/':
        resultado = numero1 / numero2
        print(f'Seu resultado é {resultado:.2f}.')
      
    else:
       pass
        
    
except ZeroDivisionError:
    print('Divisão por zero não é permitida!!!')
    
except ValueError:
    print("Por favor digite apenas números inteiros!")
    