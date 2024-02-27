'''
criar um retamgulo de 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''


# Definição do número de linhas do retângulo
linhas = 6

# Definição do número de colunas do retângulo
colunas = 6

# Definição do símbolo que será utilizado para desenhar o retângulo
simbolo = '@'

# Loop externo para percorrer as linhas do retângulo
for l in range(linhas):
    # Loop interno para percorrer as colunas do retângulo
    for c in range(colunas):
        # Impressão do símbolo na posição atual, sem pular linha
        print(simbolo, end='')
    # Impressão de uma nova linha após imprimir todos os símbolos da linha atual
    print()
