arquivo = open('aula17-09/exemplo3.txt', 'r')
anterior = 1000
cont = 0

medicoes = arquivo.readlines()
arquivo.close()

for med in medicoes:
  med = int(med)
  if med > anterior:
    cont+=1
    print(f'{cont}: {med}')
  anterior = med

# for i in arquivo:
#   i = int(i)
#   if i > anterior:
#     cont+=1
#   anterior = i

print(f'Maiores medicões: {cont}')
# arquivo.close()