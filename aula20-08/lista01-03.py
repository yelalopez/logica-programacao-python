'''
Desenvolva um programa que leia a área em m² de um terreno retangular. Ao final, o programa deverá mostrar a classificação deste terreno, de acordo com a lista abaixo:

- Abaixo de 100m²: TERRENO POPULAR
- Entre 100m² e 500m²: TERRENO MASTER
- Acima de 500m²: TERRENO VIP

Obs: Cálculo da área de um retângulo: Área = Base X Altura
'''
area = int(input('Insira a área do terrenoem m2: '))

if area < 0:
  print('Insira um valor válido')
elif area < 100:
  print('TERRENO POPULAR')
elif area < 500:
  print('TERRENO MASTER')
else:
  print('AREA VIP')
  