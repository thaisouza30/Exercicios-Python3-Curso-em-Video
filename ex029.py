vel = float(input('Escreva qual a velocidade atual do carro:'))
if vel > 80:
    print('Você passou do limite de velocidade de 80km/h e foi multado')
    multa = (vel - 80)*7
    print('Você pagará uma multa de R${:.2f}'.format(multa))
else:print('Você esta na velocidade correta, Tenha um bom dia!')
