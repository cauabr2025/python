salario = float(input('Qual o seu salario? '))
if salario > 1250.00:
    porcentagem = 0.10 * salario
    salario = salario + porcentagem
    print (salario)
else :
    porcentagem = 0.15 * salario
    salario = salario + porcentagem
    print(salario)
