x1 = 0
x2 = 0
x3 = 0
while x1 != 999:
    x1 = int(input('Digite o valor: '))
    if x1 != 999:
        x2 += 1
        x3 += x1
print(f'O tanto de numeros digitados é de {x2} e a soma de todos os valores é de {x3}')


