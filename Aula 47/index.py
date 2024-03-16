# Erros
   # Exelente para testes
   # Não realiza o 'stop' no progama
   # Mensaggens customizadas quando encontra um erro
   

# Utilizando try-except para capturar um IndexError

try:
    # Define uma lista de letras
    letras = ['a', 'b', 'c']
    
    # Tenta acessar o elemento no índice 3 da lista (que não existe)
    print(letras[3])
    
# Captura a exceção IndexError
except IndexError:
    # Imprime uma mensagem amigável
    print('Index não existe')
