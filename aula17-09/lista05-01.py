'''
Desenvolva um programa que possua um vetor de 10 números inteiros. Após o usuário inserir os valores, mostre quantos desses números são maiores, menores e iguais ao primeiro elemento do vetor.
'''

lista = []
maior = menor = igual = 0


for i in range(10):
  num = int(input(f'Insira o {i+1}º valor da lista: '))
  lista.append(num)

for x in lista[1::]:
  primeiro_elemento = lista[0]
  if primeiro_elemento > x:
    menor+=1
  elif primeiro_elemento < x:
    maior+=1

print(f'Primeiro elemento do vetor {primeiro_elemento} \nNúmeros maiores: {maior} \nNúmeros menores: {menor} \nNúmeros iguais: {lista.count(primeiro_elemento)}')



