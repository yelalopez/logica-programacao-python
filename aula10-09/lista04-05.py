'''
Faça uma função que retorne o reverso de um número inteiro informado pelo usuário
'''

def reverso(str):
  return str[::-1]

num = input('Digite el número: ')

print(f'{num} -> {reverso(num)}')