'''
Um corretor quer analisar como foi sua venda no dia. Desenvolva um programa que receba a quantidade de apartamentos vendidos no dia e na sequência:
a) Implemente um vetor de números reais chamado areas, correspondente a área de cada um dos apartamentos vendidos (adicione as áreas no vetor);
b) Calcule e mostre na tela a soma das áreas; c) O maior e o menor apartamento vendido.
'''

areas = []

ap_vendidos = int(input('Digite a quantidade de apartamentos vendidos: '))

for i in range(ap_vendidos):
  area = float(input(f'Digite a área do {i+1}º apartamento: '))
  areas.append(area)

print(f'Soma total das áreas dos apartamentos: {sum(areas)}')
print(f'Maior apartamento vendido: {max(areas)}')
print(f'Menor apartamento vendido: {min(areas)}')
