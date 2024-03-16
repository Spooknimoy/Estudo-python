
# Dicionários
    #  Utiliza index no fomato de keys e values
    # aCEITA STRING, INTERGER , FLOAT, BOOLEAN...



# Criando um dicionário chamado aluno com algumas informações
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# Utilizando um loop for para percorrer o dicionário
# O método items() retorna uma lista de tuplas onde cada tupla contém uma chave e seu valor
# Na iteração, 'keys' recebe a chave e 'values' recebe o valor correspondente
for keys, values in aluno.items():
    # Imprimindo a chave e o valor em cada iteração
    print(keys, values)
