# Functions (funções)
   # DRY - Don´t repeat yourself
   # Parametro --> Argumento
   # Default = Aquele que você define o valor no parametro
   # Non-Default = Aquele que você não define o valor no parametro
   
   
                 #nome = non-default, quantidade = default
def boas_vindas (nome, quantidade):
    print(f'olá {nome}.')
    print(f'temos {str(quantidade)} laptops em estoque')
    
boas_vindas('Marcos', 6)


