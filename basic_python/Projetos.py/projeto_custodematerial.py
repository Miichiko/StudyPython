# Dados de material e mercado

material = [

    {'nome': 'farinha', 'gramas': 250},
    {'nome': 'margarina', 'gramas': 100},
    {'nome': 'acucar', 'gramas': 100},
    {'nome': 'ovo', 'gramas': 60},

]

mercado = [
    {'produto': 'farinha', 'preco':  3},  # preço de 1k de farinha
    {'produto': 'margarina', 'preco': 7},  # preço de 1k margarina
    {'produto': 'acucar', 'preco': 4},  # preço de 1k de açucar
    {'produto': 'ovo', 'produto': 15},  # cartela com 30 ovos

]


# Função para calcular o custo de um material
def calcular_custo(material, mercado):
    custo_total = 0

    for item in material:
        nome_material = item['nome']
        quantidade_gramas = item['gramas']

        # Encontrar o preço no mercado
        for produto in mercado:
            if produto['produto'] == nome_material:
                preco = produto['preco']

                # Se o material é vendido por peso (em kg)
                if nome_material != 'ovo':
                    # Preço por grama
                    preco_por_grama = preco / 1000
                    custo_item = quantidade_gramas * preco_por_grama

                # Se for ovo, calcular por unidade
                else:
                    preco_por_unidade = preco / 30  # Preço de 1 ovo
                    custo_item = (quantidade_gramas / 60) * \
                        preco_por_unidade  # 60g equivale a 1 ovo

                custo_total += custo_item

    return round(custo_total, 2)


# Cálculo do custo final do produto
custo_produto_final = calcular_custo(material, mercado)
print(f'Custo total para fazer o produto: R${custo_produto_final}')
