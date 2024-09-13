horas = int(input('Quantas horas de atividade física você teve no mês?: '))

if horas < 0:
    print('Insira um valor válido')
else:
    if horas <= 10:
        pontos = horas * 2
    elif horas <= 20:
        pontos = horas * 5
    else:
        pontos = horas * 10

    print(f'Pontos no mês: {pontos}')