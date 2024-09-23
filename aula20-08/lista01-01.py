'''
Um programa de vida saudável quer dar pontos para atividades físicas, os quais poderão ser trocados por dinheiro. O sistema funciona assim:

- até 10 horas de atividades no mês: ganha 2 pontos por hora;
- de 11 até 20 horas de atividades por mês: ganha 5 pontos por hora
- acima de 20 horas de atividades por mês: ganha 10 pontos por hora.

Faça um programa que leia quantas horas de atividades uma pessoa teve por mês, calcule e mostre quantos pontos ela obteve.
'''

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