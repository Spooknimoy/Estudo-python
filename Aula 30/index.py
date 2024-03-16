# lists
   # Armazenar mais de uma informação em variáveis
   # Manter a sequencia dos dados em uma variável
   

# Criar uma lista de frutas a partit do input fornecido pelo usuário


# Solicita ao usuário que digite os nomes das frutas separados por vírgula
frutas_usuarios = input('Digite o nome das frutas separados por vírgula: ')

# A função split(',') é usada para dividir a string em uma lista, usando a vírgula como delimitador
# O argumento ', ' é utilizado para garantir que o espaço após a vírgula seja removido
frutas_lista = frutas_usuarios.split(', ')

# Imprime a lista de frutas
print(frutas_lista)
