'''
def boas_vindas_Marcos():
    print('olá Marcos!')
    print('temos 5 laptops no estoque') 
    
    
def boas_vindas_Ronaldo():
    print('olá Ronaldo!')
    print('temos 4 laptops no estoque') 
    
    
def boas_vindas_linda():
    print('olá linda!')
    print('temos 2 laptops no estoque') 
    
boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_linda()
'''
    
#otimizada a function


def boas_vindas(nome, quantidade):
    print(f'olá {nome}!')
    print(f'temos {str(quantidade)} laptops no estoque') 
    
boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 4)
boas_vindas('linda', 2)
       

    
