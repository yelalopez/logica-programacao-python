idades = []
for i in range(6):
  idade = int(input(f'Informe a {i+1}ª idade: '))
  idades.append(idade)

print(f'Idades lidas: {len(idades)}')
print(f'Maior idade: {max(idades)}')
print(f'Menor idade: {min(idades)}')
print(f'Media de idades: {sum(idades) / len(idades):.2f}')