# ENUNCIADO: quero que o nome Michiko fique assim *M*i*c*h*i*k*o*


# TAMANHO DO NOME : 7

# M I C H I K O
# 0 1 2 3 4 5 6
#-7-6-5-4-3-2-1

nome = "Michiko"
resultado = " "
i = 0

while i < len(nome):
    resultado += "*" + nome[i]  
    i += 1

    resultado += "*"  
    print(resultado)

