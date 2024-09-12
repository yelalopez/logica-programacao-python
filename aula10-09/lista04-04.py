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


