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
