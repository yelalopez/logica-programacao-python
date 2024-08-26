nome = input('Insira seu nome: ')
peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))
atividade = input('Você pratica alguma atividade física? ')
litros = float(input('Quanto litros de água você bebe por dia? '))

imc = peso/(altura**2)

print(f'{nome} de altura: {altura} e peso: {peso}kg, pratica atividade física? {atividade} e bebe {litros} litros de água por dia. \nO seu IMC é de {imc:.2f}')