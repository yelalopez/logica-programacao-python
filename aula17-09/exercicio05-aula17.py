nomes = []
sobrenomes = []
idades = []


qdt = int(input('Insira o número de pessoas: '))

for i in range(qdt):
  nome = input(f'Insira o {i+1}º nome: ')
  nomes.append(nome)
  sobrenome = input(f'Insira o {i+1}º sobrenome: ')
  sobrenomes.append(sobrenome)
  idade = int(input(f'Insira a {i+1}ª idade: '))
  idades.append(idade)

arquivo = open('aula17-09/cadastro.txt', 'w', encoding='utf8')
arquivo.write(f'Há {qdt} pessoas cadastradas.\n')

for i in range(qdt):
  arquivo.write(f'Nome: {nomes[i]} {sobrenomes[i]} Idade: {idades[i]}\n')

arquivo.close()


