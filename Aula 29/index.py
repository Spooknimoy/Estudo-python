 # lists
   # Armazenar mais de uma informação em variáveis
   # Manter a sequencia dos dados em uma variável
   
   


# Lista de cores
cores = ['amarelo', 'verde', 'azul', 'vermelho']

# Lista de valores
valores = [10, 20, 30, 40]

# Combinando as duas listas usando a função zip()
# A função zip() cria um iterador que combina elementos de múltiplas listas em tuplas
# Neste caso, ela irá combinar os elementos de 'valores' com os elementos correspondentes de 'cores'
duas_listas = zip(valores, cores)

# Convertendo o iterador em uma lista e imprimindo
# A função list() é usada para converter o iterador em uma lista
# Isso nos permite ver o resultado, pois o iterador zip() é consumido após a primeira vez que é utilizado
print(list(duas_listas))
