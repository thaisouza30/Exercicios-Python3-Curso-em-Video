while True:
    print('=*' * 20)
    numero = int(input('Digite um número para ver a sua tabuada: '))
    print('=*' * 20)
    if numero < 0:
        break
    for contador in range(1, 11):
        print(f'{numero} X {contador} = {contador * numero}')
print('Fim do programa')
