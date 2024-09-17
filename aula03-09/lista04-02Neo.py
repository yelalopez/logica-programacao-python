a = []
b = []

for i in range(5):
  value = int(input(f'Insira o {i+1}º valor Lista A: '))
  a.append(value)

for x in range(5):
  value = int(input(f'Insira o {x+1}º valor Lista B: '))
  b.append(value)

c = a + b
pares = 0 
impares = []
for i in c:
  if i % 2 == 0:
    pares+=i
  else:
    impares.append(i)

print(f'Soma pares: {pares}')
print(f'Média impares: {sum(impares) / len(impares)}')
print(f'Menor numero: {min(c)}')

