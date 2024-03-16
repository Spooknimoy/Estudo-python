# Map Function
   # Muito utilizado com listar
   # A plica uma função a um iterable, por item. (list, tuple, dic etc.)
   
# Define uma lista chamada lista1 com os elementos [1, 2, 3, 4]
lista1 = [1, 2, 3, 4]

# Usa a função map com uma função lambda para multiplicar cada elemento da lista1 por 2
# A função lambda é uma função anônima que multiplica o argumento "x" por 2
# Isso cria um objeto de mapa que guarda os resultados da função lambda aplicada a cada elemento da lista1
resultado_map = map(lambda x: x * 2, lista1)

# Converte o objeto de mapa em uma lista e a imprime
print(list(resultado_map))
