 # lists
   # Armazenar mais de uma informação em variáveis
   # Manter a sequencia dos dados em uma variável
   

# Solicita ao usuário que digite a cor desejada
cor_cliente = input('Digite a cor desejada:')

# Lista de cores disponíveis em estoque
cores = ['amarelo', 'verde', 'azul', 'vermelho']

# Verifica se a cor digitada pelo cliente (em letras minúsculas) está na lista de cores
# O método lower() é usado para converter a entrada do usuário em minúsculas
if cor_cliente.lower() in cores:
    # Se a cor estiver na lista, imprime 'Em estoque'
    print('Em estoque')
else:
    # Se a cor não estiver na lista, imprime 'Não temos esta cor em estoque'
    print('Não temos esta cor em estoque')
