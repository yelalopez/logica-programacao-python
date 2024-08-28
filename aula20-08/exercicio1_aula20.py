valor = float(input('Digite o valor do produto: '))
soma = 0

while valor!= 0:
  if valor< 0:
    print('Valor inválido!')
  else:
    soma = soma + valor

  valor = float(input('Digite o valor do produto: '))

if soma >1000:
  soma-=soma*0.1

print(f'Total a pagar: R${soma}')
