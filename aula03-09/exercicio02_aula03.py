alturas = []

for i in range(5):
  alturas.append(float(input(f'Informe a altura do {i+1}º jogador: ')))
  media = sum(alturas) / len(alturas)

print(f'Media do grupo: {media:.2f}')

for i in alturas:
  if i <= media:
    print(f'Altura do jogador é menor a media do grupo, altura {i}')