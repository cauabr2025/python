valores = []
numeros = valores
for cont in range(5):
    valores.append(input('Qual valor você deseja? '))
    if numeros == valores:
        valores.append(input('Qual valor voce deseja? '))
    else:
        break
print(valores)

