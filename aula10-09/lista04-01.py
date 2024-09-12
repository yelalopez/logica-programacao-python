def inverter(str):
  return str[::-1]


dd = input('Digite seu dia de nascimento: ')
mm = input('Digite seu mês de nascimento: ')
aaaa= input('Digite seu ano de nascimento: ')


print(f'Sua senha é {mm}${inverter(dd)}#{dd}!{inverter(mm)}*{aaaa}')