pesos = []

qtd = 0
qdt = int(input('Quantidade de produtos vendidos no dia: '))

for i in range(qtd):
  peso = print(float(input(f'Insira o peso do produto {i}')))
  pesos.append(peso)

# print(f'O peso médio das vendas é de {sum(pesos) / len(pesos)}')
# print(f'Peso minimos: {min(pesos)}')
# print(f'Peso minimos: {max(pesos)}')
