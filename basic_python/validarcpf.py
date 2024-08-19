

cpf_enviado = '235.856.498-23' \
    .replace('.', '')\
    .replace('.', '')\
    .replace('-', '')


# Calculo do primero digito do CPF (2)
soma = sum(int(cpf_enviado[i]) * (10 - i) for i in range(9))
resto = (soma * 10) % 11

novo_digito = resto if resto <= 9 else 0


# Calculo do segundo digito do CPF (3)

soma2 = sum(int(cpf_enviado[i]) * (11 - i) for i in range(9))
soma2 += int(cpf_enviado[9]) * int(novo_digito)


resto2 = (soma2 * 10) % 11
novo_digito2 = resto2 if resto2 <= 9 else 0
cpf_gerado = f"{cpf_enviado[:9]}{novo_digito}{novo_digito2}"

# if cpf_gerado == cpf_enviado:
#     print("CPF válido.")
# else:
#     print("CPF inválido.")
