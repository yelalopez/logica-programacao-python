arquivo = open('aula17-09/exemplo.txt', 'r')
soma = 0
qdt = 0

for i in arquivo:
  i = float(i)
  soma+=i
  qdt+=1

arquivo.close()

media = soma / qdt
print(f'Média: {media}')
