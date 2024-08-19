
perguntas = [
    {
        'Pergunta': 'Quanto é 4+5?',
        'Opções': ['4', '7', '9', '8'],
        'Resposta': '9',
    },
    {
        'Pergunta': 'Quanto é 3*8?',
        'Opções': ['21', '24', '27', '30'],
        'Resposta': '24',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['5', '4', '6', '3'],
        'Resposta': '5',
    }
]

# Função pra rodar o quiz.


def rodar_quiz(perguntas):
    pontuação = 0
    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        for i, opção in enumerate(pergunta, start=1):
            print(f"Pergunta {i}: {pergunta['Pergunta']}")
        for j, opção in enumerate(pergunta['Opções'], start=1):
            print(f' {j}. {opção}')
        resposta_usuário = input("Escolha a opção correta (1-2-3-4): ")

# Verifica se a resposta está correta.
        if pergunta['Opções'][int(resposta_usuário) - 1] == pergunta['Resposta']:
            print('Correto!\n')
            pontuação += 1
        else:
            pass
    print(f'Voçe acertou {pontuação} de {len(perguntas)} perguntas.')


# Rodando o quiz.
rodar_quiz(perguntas)
