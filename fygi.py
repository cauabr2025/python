nome=input('qual o seu nome? ')
idade=float(input('qual o ano que você nasceu? '))
peso=float(input('qual o seu peso? '))
altura=float(input('qual a sua altura '))

media=(peso)/(altura*altura)
ano=(2024-idade)

print('legal', nome, 'a media do seu peso e altura é ', media, ' e sua idade é', ano)

if media <18.5:
    print('voce estar abaixo do peso')
elif media ==18.5 or media<24.9:
    print ('peso normal')
else:
    print ('abaixo do peso')

