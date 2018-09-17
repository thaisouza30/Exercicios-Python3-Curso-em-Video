from random import randint
'''jogo melhorado com while'''
acertou = False
palpites = 0
computador = randint(0, 10)
print('-=-'*20)
print('Vou pensar em um número...tente adivinhar')
print('-=-'*20)
print('Descubra qual o número de 0 a 10 :')
print('-=-'*20)
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns !'.format(palpites))