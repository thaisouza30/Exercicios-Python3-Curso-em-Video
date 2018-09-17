print('=-'*20)
numero = int(input('Digite o número que deseja ver a tabuada: '))
print('=-'*20)
for c in range(1, 11):
    print('{} X {} = {}'.format(c, numero, numero * c))
