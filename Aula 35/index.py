# set (listas)
    # Similçar a listas
    # Evita intens duplicados
    # Não utiliza index
    
    
# Definindo três conjuntos: set1, set2 e set3
set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

# Criando um novo conjunto set4 que é a união de set1 e set2
set4 = set1.union(set2)

# Criando um novo conjunto set5 que é a diferença entre set1 e set2
set5 = set1.difference(set2)

# Criando um novo conjunto set6 que é a interseção entre set1 e set3
set6 = set1.intersection(set3)

# Criando um novo conjunto set7 que é a diferença simétrica entre set1 e set3
set7 = set1.symmetric_difference(set3)

# Imprimindo os conjuntos resultantes
print(set4)  # União de set1 e set2
print(set5)  # Diferença de set1 e set2
print(set6)  # Interseção de set1 e set3
print(set7)  # Diferença simétrica de set1 e set3

