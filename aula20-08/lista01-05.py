equipe1 = input('Nome do time 1: ')
gols_equipe1 = int(input('Gols marcados time 1: '))
equipe2 = input('Nome do time 2: ')
gols_equipe2 = int(input('Gols marcados time 2: '))

if gols_equipe1 < 0 or gols_equipe2 < 0:
  print('Insira um valor válido!')
elif gols_equipe1 > gols_equipe2:
  print(f'{equipe1} VENCEDOR!')
elif gols_equipe1 < gols_equipe2:
  print(f'{equipe2} VENCEDOR!')
elif gols_equipe1 == gols_equipe2:
  print('EMPATE!')
