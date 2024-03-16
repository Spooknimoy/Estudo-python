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
    
   def __init__(self, nome, sobrenome, data_nascimento):
       self.nome = nome
       self.sobrenome = sobrenome
       self.data_nascimento = data_nascimento

# Criar Objeto
usuario1 = funcionarios('Elena', 'Cabrabral', '12/02/2009')
usuario2 = funcionarios('Carol', 'Pereira', '22/04/1999')
usuario3 = funcionarios('Luan', 'Pablo', '22/05/2002')

# # Criar os parametros
# usuario1.nome = 'Elena'
# usuario1.sobrnome = 'Cabral'
# usuario1.data_nascimento = '12/01/2009'

# # Criar os parametros
# usuario2.nome = 'Carol'
# usuario2.sobrnome = 'Pereira'
# usuario2.data_nascimento = '22/04/2010'

# print
print(usuario1.nome)
print(usuario2.data_nascimento)
