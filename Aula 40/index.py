# lambda Fuction
    # É uma função (pequena) sem nome
    # Pode ter va´rios argumentos mas somente 1 expressão
    # Muito utiulizada dentro de outras funções  !! ATENÇÃO !!
    # Código mais 'clean'

# Definição da função "somar" que recebe um argumento "x"
def somar(x):
    # Definição de uma função lambda "func2" que adiciona 10 ao argumento que recebe
    func2 = lambda x: x + 10
    # Retorna o resultado de chamar a "func2" com o argumento "x" e multiplicá-lo por 4
    return func2(x) * 4

# Chamando a função "somar" com o argumento 2 e imprimindo o resultado
print(somar(2))

