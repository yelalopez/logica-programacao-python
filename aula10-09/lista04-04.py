'''
Faça um programa que receba um valor em horas e dê duas opções ao usuário, converter em minutos ou em segundos. A partir da escolha do usuário, o programa deverá chamar a função específica de conversão.

- A função para converter horas em minutos deverá receber como parâmetro a hora e retornar o valor em minutos.
- A função para converter horas em segundos deverá receber como parâmetro a hora e retornar o valor em segundos.

No programa principal imprima o valor retornado pela função.
'''

def minutos(horas):
    return horas*60

def segundos(horas):
    return (minutos(horas)) * 60


horas = int(input('Digite el número de horas: '))
opcao = input('Convertir en minutos [M] ou segundo [S]: ').upper()

if opcao == 'M':
    print(f'{horas} horas são {minutos(horas)} minutos')
elif opcao == 'S':
    print(f'{horas} horas são {segundos(horas)} segundos')


