sistema_operacional = []


while True:
  print('Qual o melhor sistema operacional para uso em servidores: ')
  print('1-Windows Server \n2-Linux \n3-Mac OS \n4-Outro \n0-Sair')
  
  voto = int(input('Insira seu voto: '))
  if voto >= 5:
    print('\n\nDigite un valor válido!\n\n')
  elif voto != 0:
    sistema_operacional.append(voto)
  elif voto == 0:
    print('--Votacão encerrada--')
    break
  

print(f'Quantidade Total de votos {len(sistema_operacional)}')
print(f'1-Windows Server = {sistema_operacional.count(1)}')
print(f'2-Linux = {sistema_operacional.count(2)}')
print(f'3-Mac OS = {sistema_operacional.count(3)}')
print(f'4-Outro = {sistema_operacional.count(4)}')