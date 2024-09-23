'''
Faça um programa que tenha duas funções. A primeira função irá receber como parâmetro o nome de um arquivo, e o abrirá em formato de escrita. Nesse arquivo deve ser armazenado o nome e sobrenome de 6 pessoas, 1 pessoa por linha.
A segunda função receberá o nome do arquivo criado na função anterior, apresentará um nome e sobrenome por vez e perguntará se o usuário deseja alterá-lo. Se o usuário digitar ‘Sim’, deverá alterar a linha com novas informações, senão, a linha permanece com o mesmo nome e sobrenome. As modificações devem ser salvas no mesmo arquivo.
'''

def open_file(doc):
  nomes = []
  sobrenomes = []
  for i in range(6):
    nome = input(f'Insira o {i+1}º nome: ')
    nomes.append(nome)
    sobrenome = input(f'Insira o {i+1}º sobrenome: ')
    sobrenomes.append(sobrenome)

  with open(doc, "w", encoding='utf8') as file:
    for i in range(6):
     file.write(f'Nome: {nomes[i]} {sobrenomes[i]}\n')

  
def modify_file(doc):
  with open(doc, 'r+', encoding='utf8') as file:
    linhas = file.readlines()
  
  nomes = []
  sobrenomes = []

  for i, linha in enumerate(linhas):
    print(f'Linha {i+1}: {linha.strip()}')
    option = input('Deseja alterar [S]-sim / [N]nao: ').upper()
    
    if option == 'S':
      nome = input(f'Insira o nome: ')
      sobrenome = input(f'Insira o sobrenome: ')
      linhas[i] = f'Nome: {nome} {sobrenome}\n'
  
  with open(doc, 'w', encoding='utf-8') as file:
    file.writelines(linhas)


arquivo = 'aula17-09/exemploLista05-04.txt'
open_file(arquivo)
modify_file(arquivo)