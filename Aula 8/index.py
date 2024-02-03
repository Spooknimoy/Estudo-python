# FOR COM IF, ELSE E ELIF

# Enviar um email com os detalhes da compra online (maximo 
# 3 tentivas) para compras confumadas.

compra_confirmada = False
dados_compra = 'compra no valor de 12.50 e entraga confirmada'

for enviar in range(3):
    if compra_confirmada:
       print(dados_compra)
       print('Detralhes enviado paera o seu email')
       break
else:
    print('Falha na compra')