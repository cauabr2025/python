viagem = int(input('Qual a distancia da sua Viagem Km? '))
if viagem <= 200:
    preco = viagem * 0.50
    print (f'O preço é de: {preco}')
else:
    preco = viagem * 0.45
    print (f'O preço é de: {preco}')