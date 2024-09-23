'''
A funenária Sua Hora Chegou possui vários caixões. O algorítmo deverá cadastrar o código dos caixões até o usuário digitar -1 (quando digitar -1 ele encerra) e
sair do cadastro. Por fim, o algorítmo mostrará o número de caixões cadastrados. Utilize o while.
'''

numero_caixoes = 0
total = 0

while True:

  numero_caixoes = int(input('Insira o código do caixão: '))
  
  if numero_caixoes == -1:
    break
  
  total += 1
  
print(f'Numero de caixões cadastrados: {total}')