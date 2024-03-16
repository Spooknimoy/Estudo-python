class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome 

# Criar Objetos
usuario1 = Funcionarios('Elena', 'Cabrabral', '12/02/2009')
usuario2 = Funcionarios('Carol', 'Pereira', '22/04/1999')
usuario3 = Funcionarios('Luan', 'Pablo', '22/05/2002')

# Chamar método para imprimir nome completo
print(usuario1.nome_completo())
