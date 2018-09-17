print('=-='*20)
print('Progressão Aritmética')
print('=-='*20)
termo1 = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão para a progressão: '))
decimo = termo1 + (10 - 1) * razao
for contador in range(termo1, decimo + razao, razao):
    print('{},'.format(contador), end='')


