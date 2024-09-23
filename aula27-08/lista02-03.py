'''
Faça um algorítmo que receba idade de 6 pessoas. Por fim, o algirítmo deve informar:

- Quantas idades foram lidas;
- maior idade;
- menor idade;
- média das idades 
'''

idades = []
for i in range(6):
  idade = int(input(f'Informe a {i+1}ª idade: '))
  idades.append(idade)

print(f'Idades lidas: {len(idades)}')
print(f'Maior idade: {max(idades)}')
print(f'Menor idade: {min(idades)}')
print(f'Media de idades: {sum(idades) / len(idades):.2f}')