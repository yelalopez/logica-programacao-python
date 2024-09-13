area = int(input('Insira a área do terrenoem m2: '))

if area < 0:
  print('Insira um valor válido')
elif area < 100:
  print('TERRENO POPULAR')
elif area < 500:
  print('TERRENO MASTER')
else:
  print('AREA VIP')
  