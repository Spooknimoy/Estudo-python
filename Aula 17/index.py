# Variável global
mensagem = "Olá, Mundo!"

# Função que usa a variável global 'mensagem'
def imprimir_mensagem_global():
    print("Dentro da função imprimir_mensagem_global:")
    print(mensagem)  # Imprime a variável global 'mensagem'

# Função que define uma variável local com o mesmo nome da variável global
def imprimir_mensagem_local():
    mensagem = "Olá, Brasil!"  # Variável local com o mesmo nome da variável global
    print("Dentro da função imprimir_mensagem_local:")
    print(mensagem)  # Imprime a variável local 'mensagem'

# Chamada da função imprimir_mensagem_global()
imprimir_mensagem_global()

# Chamada da função imprimir_mensagem_local()
imprimir_mensagem_local()

# Imprimindo novamente a variável global 'mensagem' fora das funções
print("Fora das funções:")
print(mensagem)  # Imprime a variável global 'mensagem'
