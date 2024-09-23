import math
while True:
  try:
    value = int(input('Digite o valor: '))
    raiz = math.sqrt(value)
    print(f'Raiz de {value}: {raiz:.2f}')
    break

  except ValueError:
    print('Digite um valor válido!')