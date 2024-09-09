lista = []
pares = []
impares = []

for i in range(10):
  lista.append(int(input(f'Informe o número {i+1} inteiro: ')))
  
for i in lista:
  if i % 2 == 0:
    pares.append(i)
  else:
    impares.append(i)

print(f'Lista: {lista}')
print(f'Lista pares: {pares}')
print(f'Lista impares: {impares}')
