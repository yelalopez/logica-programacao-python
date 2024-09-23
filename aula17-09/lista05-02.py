'''
Escreva um programa que lê um arquivo .txt contendo endereços IPs, da seguinte forma:
200.135.80.9 192.268.1.1 8.35.67.74 257.32.4.5 85.345.1.2 1.2.3.4 9.8.234.5 192.168.0.256
O programa deve mostrar os IPs indicando os que são válidos e inválidos (um endereço IP válido não pode ter uma de suas partes maior que 255).
'''

nome_arquivo = 'aula17-09/ips.txt'

with open(nome_arquivo, 'r', encoding='utf-8') as file:
  ips = file.readlines()

for ip in ips:
  ip = ip.strip()
  partes_ip = ip.split('.')
  
  if len(partes_ip) == 4:
    situacao = ""

    for parte in partes_ip:
      if int(parte) < 0 or int(parte) > 255:
        situacao = "Inválido"
        break
      else:
        situacao = "Válido"
      
    print(f'{ip} - {situacao}')







