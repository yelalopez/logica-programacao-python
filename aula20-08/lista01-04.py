'''
Uma loja de roupa está em promoção: Acima de 2 peças de roupas compradas e fazendo o pagamento à vista, o cliente tem 20% de desconto no valor total.

Faça um algorítmo que receba:

- A quantidade de peças compradas
- O valor total da compra
- O código referente a condição de pagamento

1. À vista
2. Crédito
3. Crédito parcelado

Por fim, o algorítmo deverá apresentar uma mensagem informando se o desconto foi aplicado, e em caso positivo, o novo valor da compra
'''

roupas = int(input('Insira a quantidade de roupas compradas: '))
valor_total_compra = float(input('Valor total da compra $'))
forma_pagamento = int(input('Forma de pagamento: \n[1] À vista \n[2] Crédito \n[3] Crédito parcelado \nInsira a opcão: '))

if forma_pagamento == 1:
    tipo_pagamento = 'À vista'
elif forma_pagamento == 2:
    tipo_pagamento = 'Crédito'
elif forma_pagamento == 3:
    tipo_pagamento = 'Crédito parcelado'
else:
    tipo_pagamento = 'Forma de pagamento inválida'

if roupas>= 2 and forma_pagamento == 1:
  desconto = valor_total_compra * 0.2
  total_com_desconto = valor_total_compra - desconto
  print('---------\nVocê ganhou desconto')
  print(f'---------\nDESCONTO: ${desconto} \nTOTAL: ${total_com_desconto}\nFORMA DE PAGAMENTO: {tipo_pagamento}')
else:
  print('---------\nVocê não ganhou desconto')
  print(f'---------\nTOTAL:{valor_total_compra}\nFORMA DE PAGAMENTO: {tipo_pagamento}')



