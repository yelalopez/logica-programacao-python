num = int(input('Insira a quantidade de pessoas do grupo: '))
soma = 0
acima_de_80 = 0

for i in range(0, num):
  peso = float(input('Insira o peso da pessoa: '))
  soma += peso

  if peso >= 80:
    acima_de_80+=1

print(f'A média dos pesos é de {soma/num:.2f}')
print(f'{acima_de_80} estão acima de 80kg')
