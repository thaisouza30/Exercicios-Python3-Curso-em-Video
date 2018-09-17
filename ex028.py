import random
from time import sleep
n = (random.randrange(5))
print('-=-'*20)
print('Vou pensar em um número...tente adivinhar')
print('-=-'*20)
res = int(input('Descubra qual o número de 0 a 5 :'))
print('-=-'*20)
print('PROCESSANDO ...')
sleep(3)
if res == n:
    print('Parabéns você Venceu!')
else:
    print('Perdeu! O resultado é {}'.format(n))


    



