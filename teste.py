# fazer ma função pra cálcular o item por unidade
def calcular_custo_por_unidade(preco_por_kilo, quantidade_gramas):
    # Calcular o preço por grama
    # neste caso é 0,024 pq (R$ 24 / por 1000)
    preco_por_grama = preco_por_kilo / 1000
    # Calcular o custo total pela quantidade em gramas
    # aki custo total = R$ 4,80 (0,024 x 200g)
    custo_total = preco_por_grama * quantidade_gramas
    return custo_total, preco_por_grama


# Exemplo de uso
preco_alho = 24  # preço por quilo
quantidade_alho = 200  # quantidade em gramas

# custo_alho é 4.80 (200g) e preco por grama é 0.024 ( 1g = 24 centavos)

custo_alho, preco_por_grama_alho = calcular_custo_por_unidade(
    preco_alho, quantidade_alho)
#                            200g                           4.80
print(f"Custo total de {quantidade_alho}g de alho: R$ {custo_alho:.2f}")
print(f"Preço por grama de alho: R$ {preco_por_grama_alho:.3f}")  # 24 centavos
