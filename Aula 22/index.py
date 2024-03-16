# Functions (funções)
   # DRY - Don´t repeat yourself
   # Vários Argumentos (xargs) indentificando o Parametros.
   
# Criar uma Função mque armazena numeros e strings (dados)


def agencia(**carro):
    return carro 


print(agencia(marca='gol', cor='branca', modelo=1.0, placa=1234))
print(agencia(marca='gol', cor='preto', modelo=1.0, placa=12233))
print(agencia(marca='gol', cor='azul', modelo=1.6, placa=2232))