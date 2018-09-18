from random import randint
vitoria = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    num = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = num + comp
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você escolheu o número {num} e o computador {comp} a soma é {total} ', end=' ')
    print('Deu par' if total % 2 == 0 else 'Deu Ímpar')
    if total % 2 == 0:
        if opcao == 'P':
            print('Você ganhou!!!')
            vitoria += 1
        else:
            print('Você perdeu.')
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('Você ganhou!!!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Fim de jogo!!! Você venceu {vitoria} vezes.')







