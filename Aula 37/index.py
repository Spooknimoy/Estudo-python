# Dicionários
    #  Utiliza index no fomato de keys e values
    # aCEITA STRING, INTERGER , FLOAT, BOOLEAN...
    
    
# Criando um dicionário chamado aluno com algumas informações
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# Tentativa de atualizar o nome e a nota final do aluno
# aluno.update({'nome': 'Jose', 'nota_final': 'B'})

# Tentativa de adicionar o endereço do aluno ao dicionário
# aluno.update({'endereço': 'Rua A'})

# Tentativa de deletar a chave 'idade' do dicionário aluno
# del aluno['idade']

# Obtendo o valor da chave 'endereço' do dicionário aluno
# Se a chave 'endereço' não existir, retorna 'Não existe'
print(aluno.get('endereço', 'Não existe'))
