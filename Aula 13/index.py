valor = int(input('Digite o valor do seu produto: '))


while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'o valor final do seu produto será de R${valor}')
    break