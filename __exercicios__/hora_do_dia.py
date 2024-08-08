# Faça um programa que pergunte a hora ao usuário.

# Baseando-se na hora descrita exiba a saudação apropriada
# Ex: bom dia = 0-11, boa tarde = 12-17 e boa noite = 18-23
hora_do_dia = input("Olá, poderia me dizer que horas são agora? ")

try:
  
    hora_do_dia = int(hora_do_dia)
    if hora_do_dia >= 0 and hora_do_dia <= 11:
      print("bom dia")
    elif hora_do_dia >= 12 and hora_do_dia <= 17:
      print("boa tarde")
    elif hora_do_dia >= 18 and hora_do_dia <= 23:
      print("boa noite")
    else:
      print("Não conheço essa hora.")

except:
      print('Voçe não digitou um número!')
