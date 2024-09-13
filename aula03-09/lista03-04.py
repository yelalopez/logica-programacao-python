lista_real = []
lista_real_ao_quadrado = []

for i in range(10):
  lista_real.append(float(input('Escreva um numero real: ')))

for num in lista_real:
  quadrado = num**2
  lista_real_ao_quadrado.append(quadrado)

print(lista_real)
print(lista_real_ao_quadrado)