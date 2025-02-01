primeiro_termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
dez_termos = 0
termos = 0
x2 = ''
x3 = ''
x5 = 'Sim'
while dez_termos < 10:
    dez_termos += 1
    primeiro_termo += razao
    print(primeiro_termo)
X2 = input('Quer mais termos? ')
if x2 != x5:
    x3 = int(input('Quantos termos vc quer? '))
    x6 = int(input('Qual a razão? '))
    x7 = int(input('Qual o primeiro termo? '))
    while termos < x3:
        termos += 1
        x7 += x6
        print(x7)
else:
    print('Acabado')




