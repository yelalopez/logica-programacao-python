lista = []
num_negativos = 0
cont_positivos = 0

for i in range(10):
  numero = float(input('Escreva um numero real: '))
  if numero < 0:
    num_negativos += 1 
  else:
    lista.append(numero)

print(f'Número negativos: {num_negativos}')
print(f'Soma: {sum(lista):.2f}')