casa = float(input('Qual o valor da casa? '))
sala = float(input('Qual o valor do seu salario? '))
anos = int(input('Quantos anos você deseja dividir? '))
meses = anos * 12
parcela = casa / meses
porcentagem = sala * (30/100)
if parcela > porcentagem:
    print ('Vai trabalhar mais, que com esse salario não dar certo não.')
else:
    print(f'O valor da parcela é de {parcela}')
print('o valor da parcela é {:.2f}'.format(parcela))
