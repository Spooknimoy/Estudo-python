from array import array

# Array (Matriz)
    # Similar a listas
    # Melhor perfomance
    
# Definindo uma lista de strings chamada letras com os elementos 'a', 'b', 'c' e 'd'
letras = ['a', 'b', 'c', 'd']

# Definindo uma lista de inteiros chamada numeros_i com os elementos 10, 20, 30 e 40
numeros_i = [10, 20, 30, 40]

# Definindo uma lista de floats chamada numeros_f com os elementos 1.2, 2.2, 3.2
numeros_f = [1.2, 2.2, 3.2]

# Imprimindo a lista letras
print(letras)

# Imprimindo a lista numeros_i
print(numeros_i)

# Imprimindo a lista numeros_f
print(numeros_f)

# Imprimindo uma linha em branco para separar as saídas
print()

# Agora vamos redefinir as variáveis usando a classe 'array' do módulo 'array'
# Aqui estamos usando 'u' para indicar que vamos criar um array de caracteres unicode (string)
letras = array('u', ['a', 'b', 'c', 'd'])

# Aqui estamos usando 'i' para indicar que vamos criar um array de inteiros
numeros_i = array('i', [10, 20, 30, 40])

# Aqui estamos usando 'f' para indicar que vamos criar um array de floats
numeros_f = array('f', [1.2, 2.2, 3.2])

# Imprimindo o array de letras
print(letras)

# Imprimindo o array de inteiros
print(numeros_i)

# Imprimindo o array de decimais
print(numeros_f)