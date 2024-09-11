frase = input('Digite a frase: ')
palavra = input('Digite a palavra a ser substituida: ')
substituto = input('Digite a palavra a substituir: ')

frase_atualizada = frase.replace(palavra, substituto).upper()

print(frase_atualizada)