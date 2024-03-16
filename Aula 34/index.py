# set (listas)
    # Similçar a listas
    # Evita intens duplicados
    # Não utiliza index
    
    
# list1 = [1, 2, 3, 5, 6]
# s1 = {1, 2, 3, 5, 6}


# print(list1)
# print(s1)

# print(type(list1))
# print(type(s1))


########################################################################################################


# Criando um conjunto inicial s1 com os elementos 1, 2, 3, 5 e 6
s1 = {1, 2, 3, 5, 6}

# Adicionando elementos ao conjunto s1 utilizando o método update()
s1.update([5, 7, 8, 9, 10])

# Removendo o elemento 10 do conjunto s1 utilizando o método remove()
s1.remove(10)  # Aqui ocorrerá um erro se o elemento não existir no conjunto

# Descartando o elemento 9 do conjunto s1 utilizando o método discard()
s1.discard(9)  # Aqui não ocorrerá erro se o elemento não existir no conjunto

# Imprimindo o conjunto s1 após as operações
print(s1)
