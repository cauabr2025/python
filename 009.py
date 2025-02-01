velo = int(input('\033[4;32m Qual a velocidade km/h do carro? '))
if velo > 80:
    print ('\033[1;31m Você foi multado!')
    multa = (velo - 80)
    multa = (multa * 7)
    print (f'\033[1;31m Vai ter que pagar {multa} reais')
else:
    print ('\033[4;32m Voce estar regular\033[m')