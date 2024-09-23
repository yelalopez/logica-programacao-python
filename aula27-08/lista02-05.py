'''
Desenvolva um programa utilizando o for que faça a tabuada de um número inteiro que será digitado pelo usuário.
Mas a tabuada não deve, necessariamente, iniciar em 1 e terminar em 10, o valor inicial deve ser informado pelo usuário.

Exemplo (mostrar a tabuada de 5):
- Começar por 4
- terminar em 7

Saída de dados:
- 5x4 = 20
- 5x5 = 25
- 5x6 = 30
- 5x7 = 35
'''

tabuada = int(input('Montar tabuada do: '))
comeca = int(input('Comecando em: '))
termina = int(input('Terminando em: '))

for i in range(comeca, termina + 1):
  print(f'{tabuada} x {i} = {tabuada * i}')