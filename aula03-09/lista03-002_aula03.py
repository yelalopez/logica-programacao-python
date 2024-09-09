numeros = []

while True:
  numero = int(input('Insira o número:'))
  if numero == -1 :
    break
  numeros.append(numero)

print(f'Quantidade de números: {len(numeros)}')
numeros.sort(reverse=True)
print(numeros)
print(f'O valor 5 está na lista {numeros.count(5)} vez(es)')

  


