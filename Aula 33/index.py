# set (listas)
    # Similçar a listas
    # Evita intens duplicados
    # Não utiliza index
    

# Definindo duas listas de números
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

# Convertendo as listas para conjuntos usando a função set()
num1 = set(list1)
num2 = set(list2)

# Imprimindo a união dos conjuntos num1 e num2 usando o operador |
print(num1 | num2)  # union

# Imprimindo a diferença entre os conjuntos num1 e num2 usando o operador -
print(num1 - num2)  # Difference

# Imprimindo a diferença simétrica dos conjuntos num1 e num2 usando o operador ^
print(num1 ^ num2)  # Symmetric Difference

# Imprimindo a interseção dos conjuntos num1 e num2 usando o operador &
print(num1 & num2)  # And

# Imprimindo o tamanho do conjunto num1 usando a função len()
print(len(num1))  # tamanho

# Tentativa de acesso ao índice 0 do conjunto num1, o que não é possível
# Set não é uma estrutura indexada, então num1[0] causará um erro.
# print(num1[0])  # Isso resultará em um TypeError: 'set' object is not subscriptable
