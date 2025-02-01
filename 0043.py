import random
x5 = 0
while True:
    x1 = int(input('Digite um valor: '))
    x2 = input('Par ou Impar [P/I] ')
    numero = random.randint(1, 11)
    soma = x1 + numero
    div = soma % 2
    if div == 0:
        resul = 'Par'
    else:
        resul = 'Impar'
    x3 = print(f'Você jogou {x1} e o computador {numero}. Total de {soma} deu {resul}')
    if x2 == 'P' and resul == 'Par' or x2 == 'I' and resul == 'Impar':
        print('Você Ganhou')
        x5 += 1
    else:
        print('Você Perdeu')
        break
print(f'Gamer over! Mas você ganhou {x5}')
