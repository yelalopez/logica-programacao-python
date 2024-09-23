'''
Precisa-se desenvolver um sistema para verificar se um aluno foi aprovado na disciplina. Pede-se que o professor insira as duas notas do aluno e a sua frequência em porcentagem.

Primeiro, verifica-se se o aluno teve 75% de frequência, caso seja verdadeiro, verifica-se se a média do aluno é maior ou igual a 7, mostrando a mensagem "Aprovado por média". Se não, mostra-se a mensagem "Reprovado por média"

Mas, se a frequência for abaixo de 75%, mostra a mensagem "Reprovado por falta"
'''

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