reptil = []
mamifero = []
ave = []
outro = []

for i in range(10):
  animal = input('Nome do animal silvestre: ').lower()
  categoria = int(input('Em que categoria deseja cadastrarlo: \n1 - Réptil \n2 - Mamífero \n3 - Ave \n4 - Outro \nInsira a categoria: '))

  if categoria == 1:
    reptil.append(animal)
  elif categoria == 2:
    mamifero.append(animal)
  elif categoria == 3:
    ave.append(animal)
  elif categoria == 4:
    outro.append(animal)
  else:
    print('Digite um valor válido!')
print('\n\n------------------------------------------')
print(f'Réptiles: {reptil} Quantidade: {len(reptil)}')
print(f'Mamíferos: {mamifero} Quantidade: {len(mamifero)}')
print(f'Ave: {ave} Quantidade: {len(ave)}')
print(f'Outros: {outro} Quantidade: {len(outro)}')

