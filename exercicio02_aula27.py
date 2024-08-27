media = 0
cont = 0

while True:
  nota = float(input('Insira sua nota: '))
  
  if nota == -1:
    break
  
  media += nota
  cont+=1


print(f'Foram inseridas {cont} notas e a média foi de {media/cont:.2f}')



