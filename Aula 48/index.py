# Erros
   # Exelente para testes
   # Não realiza o 'stop' no progama
   # Mensaggens customizadas quando encontra um erro
   
   
try:
    valor = int(input('digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print(input('favor digitar numero: '))
    
    
print('mais codigo abaixo')