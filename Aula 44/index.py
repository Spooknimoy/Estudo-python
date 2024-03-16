# list comprehension
    # mais cimples de se escrever
    # Utilizado quando você precisa criar uma nova lista a pártir de uma exitente
    # [expressão for inten in intens]
    
    
# Define uma lista chamada frutas1 com os elementos ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# Utiliza uma compreensão de lista para criar uma nova lista frutas2
# A compreensão de lista verifica cada item na lista frutas1
# e adiciona à frutas2 somente os itens que contêm a letra 'b'
frutas2 = [item for item in frutas1 if 'b' in item]

# Imprime a lista resultante
print(frutas2)
