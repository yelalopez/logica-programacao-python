homens_cadastrados = 0
idade_mulher_mais_velha = 0
media_idade_grupo = 0
mulheres_acima_de_20 = 0

for i in range(5):
  idade = int(input("Insira a idade da pessoa: "))
  genero = input("Insira o genero da pessoa [F] / [M] ").upper()

  media_idade_grupo += idade

  if genero == 'M':
    homens_cadastrados+=1
  else:
    if idade > idade_mulher_mais_velha:
      idade_mulher_mais_velha = idade
    if idade > 20:
      mulheres_acima_de_20 += 1

print(f'Total de homens cadastrados:{homens_cadastrados}')
print(f'A idade da mulher mais velha é {idade_mulher_mais_velha}')
print(f'A media de idade do grupo é de: {media_idade_grupo}')
print(f'Total de mulheres cadastradas acima de 20 anos = {mulheres_acima_de_20}')