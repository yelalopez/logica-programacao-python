nome_atleta = True
cont = 1
saltos = []

while nome_atleta != "Sair":
  print('Atleta', cont)
  nome_atleta = input('Insira o nome do atleta: ').capitalize()
  if nome_atleta == "Sair":
    break
  else:
    for i in range(5):
      distancia = (float(input(f'{i+1}º salto -- Digite a distancia do salto em metros: ')))
      saltos.append(distancia)
  
  media = sum(saltos) / len(saltos)
  
  print('••••Resultado••••')
  print(f'Atleta: {nome_atleta}')
  
  for i in range(5):
    print(f'{i+1}º salto: {saltos[i]}m')

  print(f'Média dos saltos: {media:.2f}m\n')
  cont+=1
