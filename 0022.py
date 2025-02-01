import random
print('Vamos jogar!!')
x1 = input('O que você escolhe: Pedra, Papel ou Tesoura? ' )
opcoes = ['Pedra', 'Papel', 'Tesoura']
x2 = random.choice(opcoes)
if x1 == 'Pedra' and x2 == 'Papel':
    print('\033[31m Voce perdeu, já tinha escolhido papel, e papel embrulha pedra\033[m')
elif x1 == 'Papel' and x2 == 'Tesoura':
    print('\033[31m Voce perdeu, já tinha escolhido tesoura, a tesousa corta papel\033[m')
elif x1 == 'Tesoura' and x2 == 'Pedra':
    print('\033[31m Voce perdeu, já tinha escolhido pedra, e pedra quebra tesoura\033[m')
else:
    print('\033[32m Você ganhou!! \033[m')

