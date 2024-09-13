tabuada = int(input('Montar tabuada do: '))
comeca = int(input('Comecando em: '))
termina = int(input('Terminando em: '))

for i in range(comeca, termina + 1):
  print(f'{tabuada} x {i} = {tabuada * i}')