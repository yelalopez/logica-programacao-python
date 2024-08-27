cont = 0

while cont < 5:
  filhos = int(input('Quantos filhos você tem?: '))
  
  if(filhos < 0) : 
    print('Insira um valor válido')
    continue

  if(filhos == 0):
    print('Voce não tem bônus')
    cont+=1
    continue
  
  bonus = filhos * 150.00
  print(f'Seu bônus é de R${bonus}')
  cont+=1
  