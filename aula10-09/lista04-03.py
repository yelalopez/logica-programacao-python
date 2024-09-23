# def sequencia():
#   while True:
#     value = int(input('Digite um número inteiro ou 0 para sair: '))
#     if value == 0:
#       break
#     elif value > 0:
#       sequencia = ' '.join(str(value) for value in range(1, value + 1))
#       print(sequencia)
#     else:
#       print('Insira um inteiro positivo')


def sequencia(lista):
   for x in lista:
    i = 1
    while i<=x:
      print(i, end=' ')
      i+=1
    print()

lista = []

while True:
  value = int(input('Digite um número inteiro ou 0 para sair: '))
  if value == 0:
      break
  elif value < 0:
    print('Insira um inteiro positivo')
  else:
    lista.append(value)

sequencia(lista)