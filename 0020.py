
preco = float(input('Qual o valor a ser pago? '))
print ('dinheiro/ cheque/ cartão/ 2x no cartão/ 3x no cartão')
pagamento = input('Qual a forma de pagamento?')

if pagamento == 'Dinheiro' or pagamento == 'dinheiro' or pagamento == 'Cheque' or pagamento == 'cheque':
    porcento = preco * (10/100)
    preco = preco - porcento
    print(f'Como vai ser pelo dinheiro, você vai ´pagar: {preco}')

elif pagamento == 'cartão' or pagamento == 'Cartão':
    porcento = preco * (5/100)
    preco = preco - porcento
    print(f'Como vai ser pelo cartão a vista, o preço é: {preco}')
elif pagamento == '2x no cartão' or pagamento == '2x no Cartão':
    parcela = preco/2
    print (f'o valor da parcela é {parcela} e o valor final é: {preco}, sem nenhum acrescimento')
elif pagamento == '3x no cartão' or pagamento == '3x no Cartão':
    porcento = preco * (20/100)
    preco = preco + porcento
    parcela = preco / 3
    print (f'o valor da parcela é {parcela} e o valor final é: {preco}, com acrescimo de 20%')
else:
    print('Ta digitado errado a forma de pagamento!')