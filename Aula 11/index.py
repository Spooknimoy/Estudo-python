# == while loops ===

# While = enquanto

# Excelente para loops dependentes de uma condição.

# Criar uma promoção para um prduto no valor de R$100




# Definição do valor inicial do produto
valor = 100

# Definição do dia inicial
dia = 0

# Loop enquanto o valor do produto for maior que R$ 20
while valor > 20:
    # Incremento do dia
    dia += 1
    
    # Impressão do dia e do valor do produto formatado
    print(f' No dia {dia} o produto vai ser vendido por R${valor}')
    
    # Redução do valor do produto em R$ 5
    valor -= 5
