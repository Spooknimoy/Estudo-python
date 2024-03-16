# unpacking lists
   # Armazenar mais de uma informação em variáveis
   # Manter a sequencia dos dados em uma variável
   
# Definição da lista de produtos
produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]

# Desempacotamento de elementos da lista em variáveis individuais
# item1, item2, item3, item4 = produtos
# Neste caso, item1 recebe 'arroz', item2 recebe 'feijão', item3 recebe 'laranja' e item4 recebe 'banana'

# Desempacotamento com * (asterisco) para capturar os itens restantes em uma lista
# item1, item2, item3, *outros = produtos
# Neste caso, item1 recebe 'arroz', item2 recebe 'feijão', item3 recebe 'laranja' e todos os outros itens são capturados em 
# uma lista chamada 'outros'

# Desempacotamento com * (asterisco) no meio e no final
item1, item2, *outros, item8 = produtos
# Neste caso, item1 recebe 'arroz', item2 recebe 'feijão', todos os itens no meio são capturados na lista 'outros' e item8 recebe o 
# último valor da lista ('8')

# Imprimir os valores das variáveis
print(item1)   # 'arroz'
print(item2)   # 'feijão'
print(item8)   # '8'
print(outros)  # ['laranja', 'banana', 5, 6, 7]



    