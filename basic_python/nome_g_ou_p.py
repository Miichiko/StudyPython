nome = input("Qual é se nome? ")

comprimento_nome = len(nome)

if len(nome) <= 4:
    print("Seu nome é curto.")
elif len(nome) <= 6: 
    print("Seu tem um tamanho normal.")   
elif len(nome) <= 8:
    print("Uau, nome seu nome é grande!")
else:
    print("Eita, seu nome é grande demais.")