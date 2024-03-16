# CRIAR A CLASSE
class funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        # O método __init__ é um método especial em Python que é chamado quando uma nova instância da classe é criada.
        # Ele inicializa os atributos da classe com os valores passados como argumentos.
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        # Aqui, estamos definindo os atributos da classe: nome, sobrenome e data de nascimento.

# Criar Objeto
usuario1 = funcionarios('Elena', 'Cabrabral', '12/02/2009')
# Aqui, criamos um objeto 'usuario1' da classe 'funcionarios' com os valores 'Elena', 'Cabrabral' e '12/02/2009' para nome, sobrenome e data de nascimento, respectivamente.

usuario2 = funcionarios('Carol', 'Pereira', '22/04/1999')
# Aqui, criamos um objeto 'usuario2' da classe 'funcionarios' com os valores 'Carol', 'Pereira' e '22/04/1999' para nome, sobrenome e data de nascimento, respectivamente.

usuario3 = funcionarios('Luan', 'Pablo', '22/05/2002')
# Aqui, criamos um objeto 'usuario3' da classe 'funcionarios' com os valores 'Luan', 'Pablo' e '22/05/2002' para nome, sobrenome e data de nascimento, respectivamente.

# # Criar os parametros (Estes estão comentados, pois não são necessários já que passamos os valores no momento da criação dos objetos)

# # usuario1.nome = 'Elena'
# # usuario1.sobrenome = 'Cabral'
# # usuario1.data_nascimento = '12/01/2009'

# # usuario2.nome = 'Carol'
# # usuario2.sobrenome = 'Pereira'
# # usuario2.data_nascimento = '22/04/2010'

# print
print(usuario1.nome)  # Imprime o nome do usuario1: Elena
print(usuario2.data_nascimento)  # Imprime a data de nascimento do usuario2: 22/04/1999
