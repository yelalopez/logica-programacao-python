def soma(num1, num2):
  return num1 + num2

def substracao(num1, num2):
  return num1 - num2

def multiplicacao(num1, num2):
  return num1 * num2

def divisao(num1, num2):
  if num2 == 0:
    return 'Não é possivel dividir por 0'
  elif num2 > num1:
    return num2 / num1
  return num1 / num2

while True:
  valor1 = float(input('Digite o 1º valor: '))
  valor2 = float(input('Digite o 2º valor: '))
  print('--CALCULADORA-- \n1-Soma \n2-Substracao \n3-Multiplicacao \n4-Divisao \n5-Sair')
  operacao = int(input('Escolha a operacao: '))

  if operacao == 1:
    print(soma(valor1, valor2))
  elif operacao == 2:
    print(substracao(valor1, valor2))
  elif operacao == 3:
    print(multiplicacao(valor1, valor2))
  elif operacao == 4:
    print(divisao(valor1, valor2))
  elif operacao == 5:
    break
  else:
    print('Insira um valor válido')
  
  continua = input('Quer realizar outra operacão: [S]-Sim [N]-Não: ').lower()
  if continua == 'n':
    break



  

