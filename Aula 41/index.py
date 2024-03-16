 # built-in functions 
 
# Map Function
   # Muito utilizado com listar
   # A plica uma função a um iterable, por item. (list, tuple, dic etc.)
   

# Define uma lista chamada lista1 com os elementos [1, 2, 3, 4]
lista1 = [1, 2, 3, 4]

# Define uma função chamada multi que multiplica um número x por 2
def multi(x):
    return x * 2

# Aplica a função multi a cada elemento da lista1 usando a função map
# Isso cria um objeto de mapa que guarda os resultados da função multi aplicada a cada elemento da lista1
lista2 = map(multi, lista1)

# Converte o objeto de mapa em uma lista e a imprime
print(list(lista2))
