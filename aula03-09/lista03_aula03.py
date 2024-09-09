pesos = []
qtd = int(input('Quantidade de produtos vendidos no dia: '))

for i in range(qtd):
  peso = float(input(f'Insira o peso do produto {i+1}: '))
  pesos.append(peso)

print(f'O peso médio das vendas é de {sum(pesos) / qtd:.2f}')
print(f'Peso minimos: {min(pesos)}')
print(f'Peso máximo: {max(pesos)}')
