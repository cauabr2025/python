ano = int(input('\033[4;36mQual o ano que você estar se referindo?\033[m '))
n1 = bool(ano % 4)
n2 = bool(ano % 100)
n3 = bool(ano % 400)

if n1 == 0 and n3 == 0 or n1 == 0 and n2 != 0:
    print('\033[1;32mBissexto\033[m')
else :
    print('\033[1;31mNão é:\033[m')