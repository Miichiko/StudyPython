# cpf: 235.856.498.23


# Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada
# um dos valores por uma contagem regressiva começando no 10.

cpf_enviado = '23585649823'
nove_digitos = cpf_enviado[:9]


# Calculo do primero digito do CPF (2)
soma = sum(int(nove_digitos[i]) * (10 - i) for i in range(9))
resto = (soma * 10) % 11

novo_digito = resto if resto <= 9 else 0
print(novo_digito)

# Calculo do segundo digito do CPF (3)

soma2 = sum(int(nove_digitos[i]) * (11 - i) for i in range(9))
soma2 += int(nove_digitos[9]) * int(novo_digito)
print(nove_digitos[9])

resto2 = (soma2 * 10) % 11
novo_digito2 = resto2 if resto2 <= 9 else 0
print(novo_digito2)
cpf_gerado = f"{nove_digitos}{novo_digito}{novo_digito2}"
print(cpf_gerado)

# if cpf_gerado == cpf_enviado:
#     print("CPF válido.")
# else:
#     print("CPF inválido.")
