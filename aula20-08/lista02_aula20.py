frequencia = int(input('Insira a frequencia do aluno em porcentagem: '))
num = 1
soma = 0
if frequencia > 75:
  while num <= 2:
    notas = int(input(f'Insira a nota {num}: '))
    soma+=notas
    num+=1

  media = soma / 2

  if media >= 7:
    print(f'Aprovado por media={media}')
  else:
    print(f'Reprovado por media={media}')

else:
  print('Reprovado por falta')