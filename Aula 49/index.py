# Erros
   # Exelente para testes
   # Não realiza o 'stop' no progama
   # Mensaggens customizadas quando encontra um erro
   
try:
    # Tenta obter um valor inteiro a partir da entrada do usuário
    valor = int(input('Digite o valor do seu produto: '))
    
    # Se o valor for um número inteiro, imprime-o
    print(valor)
    
# Captura uma exceção se o valor não for um número inteiro
except ValueError:
    # Imprime uma mensagem de erro
    print('Favor digitar um número.')

# O bloco "finally" é opcional e é sempre executado, independentemente de haver uma exceção ou não.
finally:
    # Aqui, deveria ser um print para mostrar que o código está "ok"
    print('Código ok')

# Este bloco seria executado se NÃO houvesse uma exceção
# else:
#     print('Usuário digitou um valor correto')
#     resultado = valor * 2
#     print(resultado)

# Aqui está fora do bloco "try-except", então será executado de qualquer maneira
print('Mais código abaixo')
