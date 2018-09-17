from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for contador in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento: '.format(contador)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas Maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
