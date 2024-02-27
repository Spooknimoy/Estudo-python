# Functions (funções)
   # DRY - Don´t repeat yourself
   # Vários argumenstos (xargs)
   
# Criar uma função que soma Vários Números

def soma(*numeros):
    # Inicializa a variável 'resultado' como zero
    resultado = 0

    # Loop através de cada 'num' na tupla 'numeros'
    for num in numeros:
        # Adiciona o valor de 'num' ao 'resultado'
        resultado += num

    # Retorna o resultado da soma
    return resultado

# Chama a função 'soma' com os números 2, 3, 4, 7
x = soma(2, 3, 4, 7)

# Imprime o resultado da soma
print(x)
