# Functions (funções)
# DRY - Don´t repeat yourself
# Realizam uma tarefa
# Calcula e retorna um Valor

def cliente1(nome):
    print(f'olá {nome}')   # Realiza a tarefa de imprimir uma saudação para o nome fornecido
    

def cliente2(nome):
    return f'olá {nome}'   # Retorna uma saudação formatada para o nome fornecido, amarzenado


y = cliente1('Maria')
x = cliente2('José')

