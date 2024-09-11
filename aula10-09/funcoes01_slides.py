def media(num1,num2):
  media = (num1*0.4) + (num2*0.6)
  return media

def status(nota):
  if nota > 6 :
    return 'Aprovado'
  elif nota > 4:
    return 'Verificacão suplementar'
  elif nota < 4:
    return 'Reprovado'
  else:
    return 'Digite um valor válido'
  
nota1 = float(input('Digite a nota: '))
nota2 = float(input('Digite a nota: '))

media_curso = media(nota1, nota2)
print(media_curso)
print(status(media_curso))