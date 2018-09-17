'''Refazendo Progressão Aritmética com While'''
print('=-='*20)
print('Progressão Aritmética')
print('=-='*20)
primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão para a progressão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo),end='')
    termo += razao
    cont += 1
print('Fim')
