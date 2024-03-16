# Importando a função getsizeof do módulo sys
from sys import getsizeof

# Lista de Compreensão:
# Cria uma lista de um milhão de números, cada um multiplicado por 10
numeros = [x * 10 for x in range(1000000)]

# Imprime o tipo de dados (type) da variável numeros (deve ser uma lista)
print(type(numeros))

# Imprime o tamanho em bytes da lista numeros
print(getsizeof(numeros))

print('===============================================================================================')

# Gerador (Generator Expression):
# Cria um gerador que gera um milhão de números, cada um multiplicado por 10
numeros = (x * 10 for x in range(1000000))

# Imprime o tipo de dados (type) da variável numeros (deve ser um gerador)
print(type(numeros))

# Imprime o tamanho em bytes do gerador numeros
print(getsizeof(numeros))
