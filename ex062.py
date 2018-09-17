'''Refazendo Progressão Aritmética com While'''
print('=-='*20)
print('Progressão Aritmética')
print('=-='*20)
primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão para a progressão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo),end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
