# Python Object-Oriented Progamming


#classes
    # UTILIAZADAS para criar objetos ( intances)
    # Objetos são partes dentro de uma class (instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilziar
    # ====
    # Class : Fruatas
    # Objects: Abacate, banana...
    
# CRIAR A CLASSE
class funcionarios:
    pass

# Criar Objeto
usuario1 = funcionarios()
usuario2 = funcionarios()

# Criar os parametros
usuario1.nome = 'Elena'
usuario1.sobrnome = 'Cabral'
usuario1.data_nascimento = '12/01/2009'

# Criar os parametros
usuario2.nome = 'Carol'
usuario2.sobrnome = 'Pereira'
usuario2.data_nascimento = '22/04/2010'

# print
print(usuario1.nome)
print(usuario2.data_nascimento)