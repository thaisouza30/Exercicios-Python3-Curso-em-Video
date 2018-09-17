soma = 0
cont = 0
for contador in range(1,501, 2):
    if contador % 3 == 0:
        cont = cont + 1
        soma = soma + contador
print('A soma dos {} números ímpares múltiplos de 3 é {}'.format(cont, soma))



