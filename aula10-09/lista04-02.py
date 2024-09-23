'''
Faça uma função que receba uma lista de números e dois valores (limite inferior e limite superior). A função deverá retornar uma lista cujo os elementos
são maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.

No programa principal, informe 10 números inteiros, armazenando-os numa lista. Informe também o limite inferior e o limite superior.

Teste a função implementada e exiba o resultado.
'''

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

