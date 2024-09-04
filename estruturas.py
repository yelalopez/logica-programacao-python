valores = []

for i in range(5):
  valores.append(int(input("Digite um valor: ")))

print(valores)

for c, i in enumerate(valores):
  print(f'{i} na posicao {c+1}')


