palavras = []

for i in range(5):
  palavra = input(f'Insira a {i+1}º palavra: ')
  palavras.append(palavra)
  palavras.sort(reverse=True)

for i in palavras:
  print(i)