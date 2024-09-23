'''
Desenvolva uma função que permita receber uma variável inteira X inúmeras vezes (deve parar quando o valor digitado for igual a zero). Como retorno da função,
para cada valor lido deverá ser imprimido a sequência de 1 até X (o número digitado), com um espaço entre cada número e seu sucessor.
'''

def sequencia():
  while True:
    value = int(input('Digite um número inteiro ou 0 para sair: '))
    if value == 0:
      break
    elif value > 0:
      sequencia = ' '.join(str(value) for value in range(1, value + 1))
      print(sequencia)
    else:
      print('Insira um inteiro positivo')

   

  
sequencia()
