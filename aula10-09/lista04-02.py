def ranged_list(lista, min, max):
  lista_ordenada = []
  for i in lista:
    if min <= i <= max:
      lista_ordenada.append(i)
  return sorted(lista_ordenada)



lista = []

for i in range(10): 
  num = int(input(f'Informe o {i+1}º de 10 números inteiros: '))
  lista.append(num)

limite_inferior = int(input('Informe o limite inferior: '))
limite_superior = int(input('Informe o limite superior: '))

nova_lista = ranged_list(lista, limite_inferior, limite_superior)

print(f'Nova Lista: {nova_lista}')

