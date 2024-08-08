# 1 faça um jogo pro usuário descobrir a palavra secreta
# 2 vc vai propor o jogador digitar apenas uma letra por vez
# 3 e vai contar cada tentativa do jogador
# 4 se a letra tiver na palavra exiba a letra 
# 5 se não tiver exiba "*" em todas as letras

# o usuário tenta letra por letra advinhar a palavra 


# letra imaginaria = a
palavra_secreta = "samuel"
palavra_exibida = ["*" for elemento in palavra_secreta] 
tentativas = 0
max_tentativas = 10

while True:
    letra_digitada = input("digite uma letra. ")  
    
    tentativas += 1 
    if(letra_digitada in palavra_secreta):
        for elemento in palavra_secreta:
            if(elemento == letra_digitada):
                indice_acertado = palavra_secreta.find(letra_digitada)
                palavra_exibida[indice_acertado] = letra_digitada
                print(" ".join(palavra_exibida))
    else:
        print("Nao tem essa letra nao!")
        
    if "".join(palavra_exibida) == palavra_secreta:
                print(f"Parabéns voce descobriu a palavra secreta depois de {tentativas} tentativas!!! ")
                
                break
    if tentativas >= max_tentativas:
    
        print(f"Voce atingiu o limite máximo de {max_tentativas} tentativas. Fim de jogo! ")
        break           