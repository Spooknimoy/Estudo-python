# Listas
# Armazenar mais de uma informação em variáveis
# Manter a sequência dos dados em uma variável

# Definição de variáveis individuais para cidades
cidade1 = 'RIO DE JANEIRO'
cidade2 = 'SÃO PAULO'
cidade3 = 'SALVADOR'

# Criando uma lista de cidades
cidades = ['RIO DE JANEIRO', 'SÃO PAULO', 'SALVADOR', 'Goiania']

# Adicionando 'Santa Catarina' à lista de cidades
cidades.append('Santa Catarina')

# Removendo 'SALVADOR' da lista de cidades
cidades.remove("SALVADOR")

# Inserindo 'BRASILIA' na posição 1 da lista de cidades
cidades.insert(1, 'BRASILIA')

# Removendo o primeiro elemento ('RIO DE JANEIRO') da lista de cidades
cidades.pop(0)

# Ordenando a lista de cidades em ordem alfabética
cidades.sort()

# Imprimindo a lista de cidades modificada
print(cidades)
