cont = 0
soma = 0
for c in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Você informou {} números pares e a soma deles é {}'.format(cont, soma))



